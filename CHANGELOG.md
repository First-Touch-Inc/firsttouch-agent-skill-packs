# Changelog

All notable changes to the FirstTouch Agent Skill Packs.

## 1.4.1 - 2026-07-02

Grader-verified polish (persona scores: founder 92, BDR 91, RevOps 92, AE 87 -> fixes below):

### Changed
- post-demo-followup: promised item + next-step date are now captured explicitly - shown as a Promise/next-step column in the approval table, written to HubSpot deal notes when connected (restated in output when not), and the 3-day momentum touch is drafted against the stored promise
- founder-post-generator: voice profile is a saved, reusable artifact - restated in the first run's output and reused on later runs instead of re-asking the founder
- RevOps start-here: rolling out to 2+ reps now points explicitly at admin appendix section D (readiness by rollout size)
- Generated READMEs: explicit "Next:" hand-off from first-run onboarding to Start here

## 1.4.0 - 2026-07-01

Depth without clutter: persona-specific growth plays plus optional admin depth. The default install stays self-serve.

### Added
- New skill `founder-post-generator` (founder pack): 5 post types, CTA rules (no hard demo CTA), and the 24-72h bridge into warm-engager-followup - fixes the top-of-funnel gap where founders have no engagement to harvest
- New skill `post-demo-followup` (AE pack): same-day buyer follow-up, champion thank-you, stakeholder expansion, 3-day momentum touch, and a no-show recovery path; never fabricates meeting details
- New skill `champion-job-change` (AE pack): no-pitch congratulations, delayed reconnect, old-account continuity, HubSpot updates; explicitly reactive - FirstTouch does not monitor job changes
- references/bdr-seat-and-queue.md (BDR pack): reassuring one-pager - cooldowns are normal, which statuses need action, how shared queues avoid double touches, weekly hygiene
- references/revops-admin-appendix.md (RevOps pack): HubSpot read/write surface (first_touch_* properties, app events, timeline), read-only-by-default access model, lightweight exclusion governance, and readiness tiers by rollout size (solo -> pilot -> team -> enterprise review)
- Founder start-here and weekly rhythm now route thin-engagement founders through the post generator first

## 1.3.1 - 2026-07-01

### Changed
- Safety reframed around how FirstTouch actually works, grounded in docs.firsttouch.com: configured limits are enforced automatically per seat (adjustable in the web app, never above peak); cooldowns are normal, account-action statuses (Action required / Disconnected / Restricted) are the thing to resolve; acceptance rate is both a targeting and account-health signal (>40% healthy, <25% danger zone). Fear-based warning language removed; accurate status guidance kept.
- Exclusion Lists positioned as the way to protect customers and pipeline (replaces the DNC-governance process docs)
- Attribution documented as automatic once the HubSpot integration is connected and engagement tracking is enabled; no custom tag schema needed - FirstTouch auto-tags every enrollment and writes properties, app events, and timeline entries
- workspace-audit is explicitly optional; approval-routing and logging round-trip tests are optional confidence checks, not launch gates (skipped tests are still marked unverified)
- External-profile monitoring note shortened to clarify it uses public likes/comments only
- team-governance slimmed to match: enforced limits, exclusion lists, auto-tagging, same-business-day approval SLA, simple rollout path

### Removed
- "It is YOUR account on the line" section in safety-governance
- BDR shared-queue onboarding section
- references/hubspot-properties.md and the HubSpot scope-lockdown guidance

## 1.3.0 - 2026-07-01

### Added
- references/hubspot-properties.md: the real first_touch_* property schema FirstTouch writes to HubSpot, app events, timeline objects, and a minimum-scope lockdown table (agent key = read-only)
- references/team-governance.md (RevOps pack): per-seat cap budgets (platform enforces the hard max), cross-rep collision rules, same-business-day approval SLA, pilot-to-scale runbook, weekly governance check, CRO attribution guidance
- Run guides on every recipe in all four packs - each "composes X + Y" row now ships 3-step instructions
- BDR pack: team-performance-report skill + "Show your manager the numbers" weekly recipe
- BDR onboarding: shared inbound queue rules (duplicate gate, owner mismatch, same-morning collisions)
- workspace-audit: live approval-routing test - untested routing now means NOT READY
- stalled-deal-reactivation: AE self-serve HubSpot list walkthrough (exact filters, no admin needed)
- warm-engager-followup: plain-language note on what monitoring external profiles actually does (public likes/comments only)
- safety-governance: "It is YOUR account on the line" stakes section and central DNC ownership rules

### Changed
- Generated pack READMEs reordered: first-run onboarding (with easy-access and credits notes) now comes before Start here
- Claude Code install docs: Windows paths and an "ask the agent to install it" easiest path

## 1.2.1 - 2026-07-01

### Changed
- Persona onboarding fixes: plain-English "What is MCP?" explainer with per-platform naming (Connector vs MCP server) in every pack README and mcp-setup.md; "Your week" rhythm section per persona; HubSpot access reframed as easy (admin approval or read-only service key); 100-starting-credits reassurance in onboarding and both AI SDR skills
- Style: em dashes replaced with hyphens repo-wide

## 1.2.0 - 2026-07-01

### Added
- New skill: `campaign-pause-and-fix` - pause a live campaign mid-send, diagnose (copy/audience/volume), cancel affected enrollments, fix, and restart with validated re-enrollment and no duplicate sends. Included in all four persona packs.

### Changed
- Skill quality pass: exact FirstTouch MCP tool names at previously vague steps across 8 skills; trigger descriptions de-collided (one-time vs daily-recurring, founder-voice vs team AI SDR, inbound-only vs any-CRM-event); workspace-audit scorecard split into MCP-verified vs manual-check-required
- New references/troubleshooting.md shipped in every pack; reply-handling protocol and expanded glossary in system-grounding.md

## 1.1.0 - 2026-07-01

### Added
- MIT LICENSE (bundled into every pack and skill zip)
- Per-skill zips at `packs/skills/<skill-name>.zip` - self-contained (skill + its linked references + license) for Claude.ai single-skill upload
- `version` field in pack manifests, stamped into generated pack READMEs
- CI validation (`scripts/validate.py` + GitHub Actions): SKILL.md frontmatter, manifest integrity, and pack-zip freshness checked on every push/PR
- Post-install verification steps in all install docs

### Changed
- Build script now hard-fails on missing skills/references and reports friendly errors for malformed manifest JSON (previously warned and shipped incomplete packs)
- `install/claude-ai.md` rewritten around per-skill zips (multi-skill pack zips register only one skill on Claude.ai)
- README: two-tier cap phrasing (recommend 10/20, max 20/30); folder tree and plays table now list all 14 skills

### Removed
- `embed/ftmcp-landing.js` (marketing widget, not part of skills distribution)

## 1.0.0 - 2026-06-30

Initial public release: 14 skills, 4 persona packs (founder, AE, BDR, RevOps), shared references, install guides.
