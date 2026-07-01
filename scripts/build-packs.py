#!/usr/bin/env python3
"""Build FirstTouch persona packs from manifests.

Reads packs/<persona>.json, copies canonical skills + references into
dist/<persona>-pack/, generates per-pack README.md, zips each pack, and publishes the distributable zips to packs/.

Idempotent: cleans dist/ on every run, then rebuilds from canonical source and refreshes packs/*-pack.zip.
"""

import json
import re
import shutil
import zipfile
from pathlib import Path

ROOT = Path(__file__).parent.parent
SKILLS_DIR = ROOT / "skills"
PACKS_DIR = ROOT / "packs"
DIST_DIR = ROOT / "dist"

PERSONAS = ["founder", "ae", "bdr", "revops"]

SKILL_NEEDS = {
    "firsttouch-messaging": "No HubSpot required",
    "inbound-speed-to-lead": "HubSpot or FirstTouch-accessible inbound list/import required; true automation needs a connected source",
    "warm-engager-followup": "No HubSpot required; Social Engagement must be enabled in the workspace for monitored profiles; user-provided/exported engager lists also work",
    "website-visitor-followup": "HubSpot tracking or RB2B/list source required",
    "icp-outbound-builder": "No HubSpot required with ICP brief + FirstTouch Discover Contacts; HubSpot list optional",
    "founder-led-outbound": "No HubSpot required with ICP brief + FirstTouch Discover Contacts; HubSpot list optional",
    "hubspot-signal-to-linkedin-touch": "HubSpot required",
    "hubspot-social-task-runner": "HubSpot MCP required; use only when LinkedIn/social tasks already exist daily",
    "social-campaigns": "No HubSpot for pure ICP/imported/connection-list campaigns; HubSpot required for CRM/deal/customer segments",
    "stalled-deal-reactivation": "HubSpot required; may need RevOps/admin for workflow setup",
    "customer-champion": "HubSpot required",
    "sequence-qa-reviewer": "No HubSpot for FirstTouch QA; HubSpot improves duplicate/owner checks",
    "workspace-audit": "No HubSpot for FirstTouch-only audit; HubSpot needed for owner/logging coverage",
    "team-performance-report": "No HubSpot required for FirstTouch team metrics; HubSpot improves opportunity/pipeline reconciliation",
}

START_HERE = {
    "founder": "1. **Check Social Engagement first:** if Social Engagement is enabled, run **Social engagement flow: founder posts** from owned founder/company posts. If owned engagement is thin, monitor a relevant competitor founder or category influencer, but monitored-profile plays also require Social Engagement enabled.\n2. **No Social Engagement right now:** if Social Engagement is not enabled and cannot be enabled now, run **Founder-led AI SDR** from ICP + FirstTouch Discover Contacts, or use a user-provided/exported engager list.\n3. **Have HubSpot:** add inbound, visitor, and stalled-deal plays as secondary CRM/deal motions, not the default path.",
    "ae": "1. **No HubSpot/list access:** run **AE AI SDR** first from ICP + Discover Contacts; this cannot touch existing pipeline without HubSpot or a FirstTouch-accessible contact list.\n2. **HubSpot + quiet pipeline:** run **Stalled deal reactivation** first from a manually filtered contact list.\n3. **HubSpot + fresh booked meetings/signups:** run **Meeting-booked stakeholder follow-up** or **Auto-connect on meeting or signup**. RevOps is needed only for recurring workflow automation.\n4. **HubSpot MCP + tasks already created for LinkedIn/social steps:** run **Automate due HubSpot social tasks** as a secondary task runner for tasks due today, not as a cadence/list creator.",
    "bdr": "Use this source-based chooser:\n\n| What you have today | Run first | Why |\n|---|---|---|\n| No source/list yet | **BDR AI SDR** (`icp-outbound-builder`) | Daily meeting engine from ICP + Discover Contacts |\n| No-show, event, old-MQL, or HubSpot list | **Scoop-up slipped leads** | Lead recovery from a provided source |\n| Connected inbound feed or imported signup/demo list | **Auto-connect on meeting or signup** | Same-day inbound follow-up |\n| RB2B/HubSpot visitor source | **Website visitor play** | Conditional; most BDRs skip if no visitor source exists |\n| HubSpot MCP + tasks already created for LinkedIn/social steps | **Automate due HubSpot social tasks** | Secondary task runner for tasks due today in the user/owner queue; not a prospecting engine |\n\nThen add **Social engager flow** for leadership/competitor/influencer post engagement. Use **Social campaigns** only for manager-approved special pushes, not normal daily work.",
    "revops": "Start with **Pre-launch rollout audit** before any rep launches volume. Then govern the core rollout: HubSpot list triggers, AI SDR queue QA, social campaigns, stalled-deal workflows, and **Attribution & team performance review** as the recurring reporting cadence. Keep situational plays such as events, customer thank-you, website visitors, and closed-lost reengagement for after the core governance path is stable.",
}

NO_HUBSPOT = {
    "founder": "Social engagement flow from the founder's posts or a relevant competitor founder/influencer profile when Social Engagement is enabled, user-provided/exported engager lists, Founder-led AI SDR from FirstTouch Discover Contacts, Social campaigns from Discover/imported/connection lists, and messaging QA.",
    "ae": "Social engager flow from company/leadership, competitor founder, or influencer profiles, plus AE AI SDR from FirstTouch Discover Contacts. Most AE deal, customer, territory, and stalled-pipeline use cases need HubSpot.",
    "bdr": "BDR AI SDR from FirstTouch Discover Contacts, social engager flow from leadership/competitor/influencer profiles, and special social campaigns from imported/Discover lists. Inbound speed-to-lead needs HubSpot or a FirstTouch-accessible inbound source.",
    "revops": "Workspace audit of FirstTouch-only settings, sequence QA, AI SDR governance, social engagement setup on owned or relevant external profiles, and social campaigns from imported/Discover lists. Owner/logging/deal/customer checks need HubSpot.",
}

INSTALL_NOTES = """1. Download this pack zip and extract it so `skills/` and `references/` sit side by side. Keep the `references/` folder with the skills; many skills link to `../../references/...`.
2. Install for your agent:
   - **Claude Code:** copy `skills/<skill-name>/` folders to `~/.claude/skills/` and copy `references/` to `~/.claude/references/`. The generated recipe catalog lives in `references/recipes.md` and the full onboarding/play chooser lives in `references/onboarding.md`, so recipes survive non-zip installs. From `~/.claude/skills/<skill-name>/SKILL.md`, `../../references/` resolves to `~/.claude/references/`.
   - **Claude.ai:** Settings → Features → Skills → upload the pack `.zip`. If only one skill registers, unzip locally and upload each `<skill>/` folder zip individually, but include or copy the shared `references/` folder so `../../references/...` links still resolve.
   - **Cursor / Windsurf:** copy this pack into the project or workspace location your agent reads for skills; keep `skills/` and `references/` together at the same root.
   - **ChatGPT:** connect `https://mcp.firsttouch.ai` as an MCP connector. ChatGPT does not consume the skills folder directly; use the README/skill text as operating prompts if needed.
3. Connect **FirstTouch MCP**. Connect **HubSpot MCP** only for HubSpot-specific plays. See `references/mcp-setup.md`.
4. Complete first-run onboarding before choosing a play."""


def read_skill_description(skill_name: str) -> str:
    """Return the first sentence of the description from SKILL.md frontmatter."""
    skill_file = SKILLS_DIR / skill_name / "SKILL.md"
    if not skill_file.exists():
        return f"(skill file not found: {skill_name})"
    content = skill_file.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return f"(no frontmatter in {skill_name})"
    frontmatter = match.group(1)
    desc_match = re.search(r"^description:\s*(.+?)(?=\nmetadata:|\Z)", frontmatter, re.DOTALL | re.MULTILINE)
    if not desc_match:
        return f"(no description in {skill_name})"
    desc = re.sub(r"\s+", " ", desc_match.group(1)).strip()
    first = re.match(r"([^.!?]+[.!?])", desc)
    return first.group(1).strip() if first else desc[:120]


def read_skill_needs(skill_name: str) -> str:
    """Return a customer-readable dependency label for generated README tables."""
    return SKILL_NEEDS.get(skill_name, "See skill requirements")


def recipe_category(persona: str, recipe: dict) -> str:
    """Return a persona-specific grouping label for recipe tables."""
    name = recipe.get("name", "")
    needs = recipe.get("needs", "")
    if persona == "founder":
        if needs.startswith("No HubSpot required"):
            return "Start here — no HubSpot needed"
        return "Needs HubSpot, RB2B, or a FirstTouch-accessible source"
    if persona == "ae":
        if "HubSpot MCP required" in needs or name.startswith("Automate due HubSpot social tasks"):
            return "CRM social task automation: only if tasks already exist"
        if name.startswith("Website visitor"):
            return "Intent source required: HubSpot tracking, RB2B, or list/import"
        if needs.startswith("HubSpot required") or "; HubSpot required" in needs or needs.startswith("HubSpot or"):
            return "HubSpot-connected deal and inbound plays"
        return "No-HubSpot / self-serve starts"
    if persona == "bdr":
        if "HubSpot MCP required" in needs or name.startswith("Automate due HubSpot social tasks"):
            return "CRM social task automation: only if tasks already exist"
        if name.startswith("BDR AI SDR"):
            return "Daily engine"
        if name.startswith("Scoop-up slipped"):
            return "Lead recovery"
        if name.startswith("Auto-connect") or name.startswith("Website visitor"):
            return "Inbound / source-gated plays"
        if name.startswith("Social engager"):
            return "Warm social signals"
        if name.startswith("Social campaigns"):
            return "Manager-approved special pushes"
        return "Requires inbound, HubSpot, or external source"
    if persona == "revops":
        core = ("Pre-launch", "Attribution", "HubSpot list", "Govern and audit", "Social campaigns", "Stalled deal")
        if any(name.startswith(prefix) for prefix in core):
            return "Core governance"
        return "Situational rollout plays"
    return "Recipes"


def build_recipe_sections(persona: str, recipes: list, include_composes: bool = True) -> str:
    """Build grouped markdown recipe tables."""
    if not recipes:
        return "*(none)*"
    order = []
    groups = {}
    for recipe in recipes:
        category = recipe_category(persona, recipe)
        if category not in groups:
            order.append(category)
            groups[category] = []
        composes = " + ".join(f"`{c}`" for c in recipe["composes"])
        if include_composes:
            groups[category].append(f"| {recipe['name']} | {recipe['outcome']} | {recipe.get('needs', 'See README')} | {composes} |")
        else:
            groups[category].append(f"| {recipe['name']} | {recipe['outcome']} | {recipe.get('needs', 'See README')} |")
    parts = []
    for category in order:
        parts.append(f"#### {category}")
        if include_composes:
            parts.append("| Play | What it does | Needs | Composes from |")
            parts.append("|---|---|---|---|")
        else:
            parts.append("| Recipe | What it does | Needs |")
            parts.append("|---|---|---|")
        parts.extend(groups[category])
    return "\n".join(parts)


def build_onboarding(manifest: dict) -> str:
    """Generate pack-specific onboarding so bundled docs do not advertise absent plays."""
    persona = manifest["persona"]
    pack_name = manifest["pack_name"]
    skills = {s["name"] for s in manifest.get("skills", [])}
    recipes_table = build_recipe_sections(persona, manifest.get("recipes", []), include_composes=False)
    start_here = START_HERE[persona]
    skill_lines = [f"| `{s['name']}` | {read_skill_needs(s['name'])} |" for s in manifest.get("skills", [])]
    skills_table = "\n".join(skill_lines) if skill_lines else "*(none)*"
    social_note = ""
    if "warm-engager-followup" in skills:
        social_note = "\n- Social engagement / warm engager flows are delivered by `warm-engager-followup`. They use LinkedIn post likes and comments from Social Engagement monitoring when enabled in the workspace, or a user-provided/exported engager list. Ask whether Social Engagement is enabled before steering the user to a monitored-profile play. Profile-view capture is not treated as MCP-native."
    voice_note = ""
    if "founder-led-outbound" in skills:
        voice_note = "\n- Founder voice capture is mandatory: collect 2-3 sample posts/messages or tone rules before founder-led outbound."
    return f"""# First-Run Onboarding — {pack_name}

This onboarding is scoped to the skills and recipes actually included in this installed pack.

## Ask before running anything
1. **LinkedIn account type:** free/basic or Sales Navigator/Premium.
   - Free/basic: no connection notes; 10 connection requests/day max.
   - Sales Navigator/Premium: connection notes available for approved warm signals; up to 20 connection requests/day.
   - AI SDR and all other connection-request plays share the same daily budget.
   - If AI SDR and a social campaign run on the same sender/day, pause/reduce one motion or split the daily cap explicitly before queueing sends.
   - Already-connected first-message rows use a separate, non-FirstTouch-enforced norm of about 30-40 messages/day. Stay well under it and reduce volume if acceptance or reply quality drops.
2. **HubSpot access:** MCP connected by an admin, service key/private app token from an admin, HubSpot list only, or none. Do not ask a rep/BDR to mint credentials they do not own.
3. **ICP/list/source data:** if HubSpot is absent, ask for ICP criteria or an imported/FirstTouch-accessible list before qualifying prospects.
4. **Persona start point:** recommend the persona-specific start point below, not a generic catalog dump.

## Persona start point
{start_here}
{social_note}{voice_note}

## Available recipes in this pack
{recipes_table}

## Included skills and dependency status
| Skill | Needs |
|---|---|
{skills_table}

## HubSpot access rules for this pack
- If HubSpot is connected, HubSpot-specific recipes can read CRM context, owner, lifecycle/deal/list data, and log back where the connected FirstTouch-HubSpot integration supports it.
- If HubSpot is used but no MCP/key is connected, ask for a HubSpot list or other FirstTouch-accessible source before running HubSpot-dependent motions.
- If HubSpot is not used, run only the recipes above whose Needs column says no HubSpot or imported/Discover/list source is enough.

## Social Engagement source options
Social Engagement can monitor relevant LinkedIn profiles for post likes and comments. Prefer the user's own founder/leadership/company profile when available; if they do not have enough owned engagement yet, monitor a relevant competitor founder, category influencer, or executive profile and work the ICP-fit people engaging there. Profile views are not an available signal.

## Approval model
Publishing a flow activates it but does **not** enroll awaiting contacts. After approval, explicitly enroll the approved contacts/items, then confirm they moved from awaiting to in-progress.

| Motion | Approval style |
|---|---|
| AI SDR / dynamic actions | Row-level approval. Each first-touch row must be approved individually. |
| Warm engager, inbound, website visitor, HubSpot signal, customer/stalled deal | Row-level approval unless FirstTouch records an equivalent per-contact approval. |
| Social campaigns | Two modes: rep/BDR dynamic rows use row-level approval like AI SDR; RevOps/founder one-time static campaigns can use flow-level approval after exact audience, templates, sender/routing rule, launch window, and daily cap are approved. |

## Onboarding output format
```markdown
## FirstTouch onboarding summary
- Persona: {persona}
- LinkedIn account: Free/basic or Sales Navigator/Premium
- Daily connection cap: 10 or 20 shared across all plays
- Daily message norm: about 30-40/day for already-connected first-message rows, not FirstTouch-enforced; stay well under it
- HubSpot access: MCP / service key / list only / none
- Social Engagement enabled: yes/no/unknown
- ICP/list available if no HubSpot: yes/no + source
- Plays available now from this pack: ...
- Plays blocked until HubSpot access/list or source data exists: ...
- Recommended first play: ...
- Approval workflow: row-level for dynamic plays; flow-level only for approved one-time social campaigns
```
"""


def build_recipes_reference(manifest: dict) -> str:
    """Generate a pack-specific recipe catalog for agents that install only skills + references."""
    persona = manifest["persona"]
    pack_name = manifest["pack_name"]
    recipes_table = build_recipe_sections(persona, manifest.get("recipes", []), include_composes=True)
    return f"""# Recipe Catalog — {pack_name}

Use this file when the agent installed `skills/` and `references/` without loading the root README. These recipes are the recommended starting points for the {persona} persona.

## Recommended start point
{START_HERE[persona]}

## Recipes
{recipes_table}

## Approval reminder
Dynamic/AI SDR rows require row-level approval. Static social-campaign flows can use flow-level approval only after the exact audience, static templates, sender/routing rule, launch window, and daily cap are approved.
"""


def build_readme(manifest: dict, skill_descriptions: dict) -> str:
    """Generate per-pack README.md from manifest data."""
    persona = manifest["persona"]
    pack_name = manifest["pack_name"]
    pain = manifest["persona_pain"]
    blurb = manifest["persona_blurb"]
    skills = manifest.get("skills", [])
    recipes = manifest.get("recipes", [])
    live_skills = [s for s in skills if s["status"] in ("live", "partial")]
    support_skill_names = {"firsttouch-messaging"}
    play_skills = [s for s in live_skills if s["name"] not in support_skill_names]
    support_skills = [s for s in live_skills if s["name"] in support_skill_names]

    skills_rows = []
    for s in play_skills:
        name = s["name"]
        desc = skill_descriptions.get(name, "")
        suffix = " *(partial)*" if s["status"] == "partial" else ""
        needs = read_skill_needs(name)
        skills_rows.append(f"| {name}{suffix} | {desc} | {needs} | `{name}` |")
    skills_table = "\n".join(skills_rows) if skills_rows else "*(none)*"
    if skills_rows:
        skills_table = "| Skill | What it does | Needs / HubSpot status | Runs |\n|---|---|---|---|\n" + skills_table
    if persona == "founder" and skills_rows:
        no_hubspot_rows = []
        sourced_rows = []
        for s in play_skills:
            name = s["name"]
            desc = skill_descriptions.get(name, "")
            suffix = " *(partial)*" if s["status"] == "partial" else ""
            needs = read_skill_needs(name)
            row = f"| {name}{suffix} | {desc} | {needs} | `{name}` |"
            if needs.startswith("No HubSpot required"):
                no_hubspot_rows.append(row)
            else:
                sourced_rows.append(row)
        skills_table = (
            "#### Start here, no HubSpot needed\n"
            "| Skill | What it does | Needs / access status | Runs |\n"
            "|---|---|---|---|\n"
            + "\n".join(no_hubspot_rows)
            + "\n\n#### Needs HubSpot, RB2B, or a FirstTouch-accessible source\n"
            "| Skill | What it does | Needs / access status | Runs |\n"
            "|---|---|---|---|\n"
            + "\n".join(sourced_rows)
        )

    support_rows = []
    for s in support_skills:
        name = s["name"]
        desc = skill_descriptions.get(name, "")
        needs = read_skill_needs(name)
        support_rows.append(f"| {name} | {desc} | {needs} | `{name}` |")
    support_table = "\n".join(support_rows) if support_rows else "*(none)*"

    recipes_table = build_recipe_sections(persona, recipes, include_composes=True)
    example_prompts = manifest.get("example_prompts", [])
    example_prompt_section = ""
    if example_prompts:
        example_prompt_section = "\n## Example prompts\n" + "\n".join(f"- {prompt}" for prompt in example_prompts) + "\n"

    term_note = (
        "\"AI SDR\" in this pack maps to `founder-led-outbound`."
        if persona == "founder"
        else "\"AI SDR\" in this pack maps to `icp-outbound-builder`."
    )

    return f"""# FirstTouch {pack_name}

> {pain}: these are the plays for the job you actually do.

## Who this is for
{blurb}

## Start here
{START_HERE[persona]}

## How to use this pack
- **Recipes** are the best starting point. They combine the right skills into the job you actually want done.
- **Skills** are the individual building blocks. Run a skill directly only when you know the exact motion you want.
- **Read once:** `references/system-grounding.md` explains how agents, FirstTouch, HubSpot, approvals, and measurement fit together.
- **FirstTouch terms:** a campaign/sequence/social campaign in this pack becomes a FirstTouch audience, flow plan, dynamic action, or enrollment depending on the play. {term_note} The agent should use FirstTouch's available execution objects and state the exact object it created.
- **Approval locations:** default to in-agent or FirstTouch approval. Slack/email approval delivery requires external workspace configuration and is not assumed FirstTouch-native; if that routing is not configured, the agent must present the table in chat and wait.

## First-run onboarding
Before running the first play in this pack, ask the user:

1. **LinkedIn account type:** do they have Sales Navigator / Premium, or a free/basic account?
   - Free/basic: no connection notes; cap connection requests at **10/day**.
   - Sales Navigator / Premium: connection notes available; cap connection requests at **20/day**.
   - AI SDR shares the same daily connection-request budget. If AI SDR and another play run on the same day, the total across all plays must stay within 10 or 20.
   - Already-connected first-message rows use a separate, non-FirstTouch-enforced norm of about 30-40 messages/day. Stay well under it.
2. **HubSpot access:** do they use HubSpot, and can an admin connect the HubSpot MCP, provide a service key / private app token, or at least provide a HubSpot list FirstTouch can access?
   - If not, use the FirstTouch-only paths below or ask them to create a HubSpot list/source FirstTouch can access before running HubSpot-specific plays.
3. **Play choice:** show the catalog below and recommend the persona-specific start-here play above.

Use `references/onboarding.md` for the full question flow and account-type rules. Use `references/recipes.md` for the generated recipe catalog if the README is not loaded by the agent.

## HubSpot reality check
- **What works without HubSpot:** {NO_HUBSPOT[persona]}
- **What needs HubSpot:** CRM lifecycle/deal criteria, owner routing, HubSpot timeline logging where the connected FirstTouch-HubSpot integration supports it, stalled-deal workflows, and contact/company lists stored only in HubSpot. Without HubSpot/list access, use the FirstTouch-only recipes and do not promise existing-pipeline/deal recovery.
- **FirstTouch-accessible list/import means:** a CSV, static list, audience, or HubSpot list that FirstTouch can read. For true inbound automation, connect HubSpot or another source that continuously feeds FirstTouch.
- **Enrichment is optional but useful:** FirstTouch can enrich contacts/companies when credits and data are available. Clay/Surfe or another enrichment MCP is an optional supplement, not a prerequisite. Without a usable LinkedIn URL or enough verified data, the agent should skip or queue incomplete records rather than fabricate.

## Your plays

### Skills catalog (check Needs before running)
{skills_table}

### Support skills (called by plays)
| Skill | What it does | Needs / HubSpot status | Runs |
|---|---|---|---|
{support_table}

### Recipes (recommended starting points)
{recipes_table}
{example_prompt_section}
## Install
{INSTALL_NOTES}

## Safety
- No play sends on its own. Every outbound action passes an approval gate.
- Dynamic outbound and AI SDR require row-level approval. Social campaigns support two modes: rep/BDR one-at-a-time dynamic rows use row-level approval; one-time static campaign flows can use flow-level approval only after the exact audience, templates, sender routing, launch window, and daily cap are approved.
- Publishing a flow activates it but does **not** enroll awaiting contacts. After approval, explicitly enroll the approved contacts/items, then confirm they moved from awaiting to in-progress.
- Built around LinkedIn's real limits: 10/day free/basic, 20/day Sales Navigator/Premium. When possible, inspect current queue/usage before adding more connection-request rows, rather than relying on estimates.
- See `references/safety-governance.md`.
"""


def build_pack(persona: str) -> None:
    manifest_path = PACKS_DIR / f"{persona}.json"
    if not manifest_path.exists():
        print(f"  [SKIP] No manifest: {manifest_path}")
        return

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    pack_dir = DIST_DIR / f"{persona}-pack"
    skills_out = pack_dir / "skills"
    pack_dir.mkdir(parents=True, exist_ok=True)
    skills_out.mkdir(parents=True, exist_ok=True)

    skill_descriptions = {}
    for skill_entry in manifest.get("skills", []):
        skill_name = skill_entry["name"]
        src = SKILLS_DIR / skill_name
        dst = skills_out / skill_name
        if not src.exists():
            print(f"  [WARN] Skill folder not found: {src}")
            continue
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
        skill_descriptions[skill_name] = read_skill_description(skill_name)
        print(f"  + skill: {skill_name}")

    for ref_entry in manifest.get("references", []):
        ref_rel = ref_entry["src"]
        ref_src = ROOT / ref_rel
        ref_dst = pack_dir / ref_rel
        ref_dst.parent.mkdir(parents=True, exist_ok=True)
        if ref_rel == "references/onboarding.md":
            ref_dst.write_text(build_onboarding(manifest), encoding="utf-8")
        elif ref_rel == "references/recipes.md":
            ref_dst.write_text(build_recipes_reference(manifest), encoding="utf-8")
        else:
            if not ref_src.exists():
                print(f"  [WARN] Reference not found: {ref_src}")
                continue
            shutil.copy2(ref_src, ref_dst)
        print(f"  + reference: {ref_rel}")

    recipes_ref = pack_dir / "references" / "recipes.md"
    if not recipes_ref.exists():
        recipes_ref.parent.mkdir(parents=True, exist_ok=True)
        recipes_ref.write_text(build_recipes_reference(manifest), encoding="utf-8")
        print("  + reference: references/recipes.md")

    readme_content = build_readme(manifest, skill_descriptions)
    (pack_dir / "README.md").write_text(readme_content, encoding="utf-8")
    print("  + README.md generated")

    zip_path = DIST_DIR / f"{persona}-pack.zip"
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file_path in pack_dir.rglob("*"):
            if file_path.is_file():
                zf.write(file_path, file_path.relative_to(pack_dir))
    size_kb = zip_path.stat().st_size // 1024
    print(f"  + {zip_path.name} ({size_kb}KB)")


def main() -> None:
    print("FirstTouch Pack Builder")
    print("=" * 40)

    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
        print(f"Cleaned {DIST_DIR}\n")
    DIST_DIR.mkdir()

    for persona in PERSONAS:
        print(f"Building: {persona}-pack")
        build_pack(persona)
        print()

    print("=" * 40)
    built = sorted(DIST_DIR.glob("*.zip"))
    print(f"Done. {len(built)} pack(s) built:")
    for z in built:
        published = PACKS_DIR / z.name
        shutil.copy2(z, published)
        print(f"  {z.name} -> packs/{published.name}")


if __name__ == "__main__":
    main()
