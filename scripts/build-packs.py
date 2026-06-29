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
    desc_match = re.search(
        r"^description:\s*(.+?)(?=\nmetadata:|\Z)",
        frontmatter,
        re.DOTALL | re.MULTILINE,
    )
    if not desc_match:
        return f"(no description in {skill_name})"

    desc = re.sub(r"\s+", " ", desc_match.group(1)).strip()
    first = re.match(r"([^.!?]+[.!?])", desc)
    return first.group(1).strip() if first else desc[:120]


def read_skill_needs(skill_name: str) -> str:
    """Return a concise dependency label from SKILL.md frontmatter."""
    skill_file = SKILLS_DIR / skill_name / "SKILL.md"
    if not skill_file.exists():
        return "See skill requirements"

    content = skill_file.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return "See skill requirements"

    req_match = re.search(r"requires:\s*\[(.*?)\]", match.group(1), re.DOTALL)
    if not req_match:
        return "See skill requirements"

    requires = {item.strip().strip("'\"") for item in req_match.group(1).split(",")}
    if "hubspot-mcp" in requires:
        return "HubSpot required"
    if "firsttouch-mcp" in requires:
        return "No HubSpot required unless recipe says so"
    return "See skill requirements"


def build_readme(manifest: dict, skill_descriptions: dict) -> str:
    """Generate per-pack README.md from manifest data."""
    pack_name = manifest["pack_name"]
    pain = manifest["persona_pain"]
    blurb = manifest["persona_blurb"]
    skills = manifest.get("skills", [])
    recipes = manifest.get("recipes", [])
    live_skills = [s for s in skills if s["status"] in ("live", "partial")]

    skills_rows = []
    for s in live_skills:
        name = s["name"]
        desc = skill_descriptions.get(name, "")
        suffix = " *(partial)*" if s["status"] == "partial" else ""
        needs = read_skill_needs(name)
        skills_rows.append(f"| {name}{suffix} | {desc} | {needs} | `{name}` |")
    skills_table = "\n".join(skills_rows) if skills_rows else "*(none)*"

    recipe_rows = []
    for r in recipes:
        composes_str = " + ".join(f"`{c}`" for c in r["composes"])
        needs = r.get("needs", "See skill requirements")
        recipe_rows.append(f"| {r['name']} | {r['outcome']} | {needs} | {composes_str} |")
    recipes_table = "\n".join(recipe_rows) if recipe_rows else "*(none)*"

    founder_hint = (
        "\n   - For founders, recommend **Social engagement flow** first. It does not require HubSpot."
        if manifest.get("persona") == "founder"
        else ""
    )

    return f"""# FirstTouch {pack_name}

> {pain} — these are the plays for the job you actually do.

## Who this is for
{blurb}

## First-run onboarding
Before running the first play in this pack, ask the user:

1. **LinkedIn account type:** do they have Sales Navigator / Premium, or a free/basic account?
   - Free/basic: no connection notes; cap connection requests at **10/day**.
   - Sales Navigator / Premium: connection notes available; cap connection requests at **20/day**.
   - For AI SDR daily queues specifically, use the stricter cap: **10/day** on free/basic or **15/day** on Sales Navigator / Premium.
2. **HubSpot access:** do they use HubSpot, and can they connect the HubSpot MCP or provide a HubSpot service key / private app token?
   - If not, run FirstTouch-only plays or ask them to create a HubSpot list/source FirstTouch can access before running HubSpot-specific plays.
3. **Play choice:** show the catalog below and recommend **high-intent plays first**, then outbound once those are running to keep the LinkedIn account healthy.{founder_hint}

Use `references/onboarding.md` for the full question flow, account-type rules, and play catalog.

## Your plays

### ✅ Ready now (skills)
| Play | What it does | Needs / HubSpot status | Runs |
|---|---|---|---|
{skills_table}

### ⚠️ Recipes (composable, run with guidance)
| Play | What it does | Needs / HubSpot status | Composes from |
|---|---|---|---|
{recipes_table}

## Install
1. Download this pack (or clone the repo).
2. Drop the `skills/` folder **and the shared `references/` folder** into your agent. Skills use `../../references/...`, so references must sit two levels above each `SKILL.md`:
   - **Claude Code:** copy each skill folder to `~/.claude/skills/<skill-name>/` and copy `references/` to `~/.claude/references/` (or use `.claude/skills/` plus `.claude/references/` per-project)
   - **Claude.ai:** Settings → Features → Skills → upload the pack `.zip`. *(If claude.ai only registers the first skill, unzip locally and upload each `<skill>/` folder's zip individually.)*
   - **Cursor / Windsurf:** copy the `skills/` and `references/` folders anywhere the agent reads
   - **ChatGPT:** MCP connector only — no skills folder. Connect `https://mcp.firsttouch.ai` via Settings → Connectors.
3. Connect MCPs: **FirstTouch MCP** for FirstTouch execution and approvals. Connect **HubSpot MCP** only for HubSpot-specific plays. See `references/mcp-setup.md`.
4. Complete the first-run onboarding in `references/onboarding.md` before choosing a play.

## Safety
- No play sends on its own. Every outbound action passes an approval gate.
- Built around LinkedIn's real limits. Owner/territory-safe routing.
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
        if not ref_src.exists():
            print(f"  [WARN] Reference not found: {ref_src}")
            continue
        ref_dst = pack_dir / ref_rel
        ref_dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ref_src, ref_dst)
        print(f"  + reference: {ref_rel}")

    readme_content = build_readme(manifest, skill_descriptions)
    (pack_dir / "README.md").write_text(readme_content, encoding="utf-8")
    print(f"  + README.md generated")

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
