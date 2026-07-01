# Changelog

All notable changes to the FirstTouch Agent Skill Packs.

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
