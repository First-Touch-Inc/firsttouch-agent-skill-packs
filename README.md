# FirstTouch Revenue Skills - Customer Pack

> **Turn Claude, Cursor, Codex, and ChatGPT into FirstTouch-native LinkedIn revenue operators.**

This pack gives customers a structured set of **plays** - reusable skills that execute real LinkedIn-outreach workflows with FirstTouch, human approvals, account-safety limits, and HubSpot context when available.

It is built to the open **Agent Skills** standard ([agentskills.io](https://agentskills.io)), so every skill works in Claude Code, Claude.ai, Cursor, Windsurf, and any MCP-compatible harness.

---

## Why this pack exists

Most "AI outreach" tools stop at generating copy. Customers can get an agent to *write* a message, but not to:

- act on a warm signal like post engagement, a form fill, a deal stall, or a website visit
- find the right person on LinkedIn and reach out safely
- prepare approval-ready FirstTouch queues instead of autonomous sends
- log and route through HubSpot when CRM access is connected
- respect account-safety limits and human approval gates

Each play closes that loop. This is the difference between an agent that *sounds* like an SDR and one that *operates* like one.

---

## How the pack is organized

```
firsttouch-skills/
├── README.md                              ← you are here
├── references/
│   ├── onboarding.md                      ← first-run questions, play catalog, account limits
│   ├── system-grounding.md                ← how FirstTouch + HubSpot + agents fit together
│   ├── mcp-setup.md                       ← connect HubSpot MCP, FirstTouch MCP, enrichment MCPs
│   ├── messaging-framework.md             ← FirstTouch LinkedIn messaging methodology
│   ├── safety-governance.md               ← approval gates, send safety, account limits
│   └── troubleshooting.md                 ← MCP failures, LinkedIn warnings, recovery
└── skills/
    ├── firsttouch-messaging/              ← foundation: how to write outreach
    ├── warm-engager-followup/             ← social engagement flow
    ├── social-campaigns/                  ← one-time static-template campaigns
    ├── icp-outbound-builder/              ← AI SDR
    ├── founder-led-outbound/              ← founder AI SDR
    ├── inbound-speed-to-lead/
    ├── hubspot-signal-to-linkedin-touch/
    ├── website-visitor-followup/
    ├── stalled-deal-reactivation/
    ├── customer-referral/
    ├── hubspot-social-task-runner/        ← execute due HubSpot social tasks
    ├── team-performance-report/           ← FirstTouch team metrics + attribution
    ├── sequence-qa-reviewer/
    ├── workspace-audit/
    └── campaign-pause-and-fix/            ← mid-send escape hatch: pause, fix, restart
```

**Two layers:**
1. **Foundation** (`references/` + `firsttouch-messaging`) - shared grounding every play assumes.
2. **Customer plays** - self-contained, revenue-tied workflows. Governance and attribution rules live in shared references instead of separate customer-facing plays.

---

## Get started in 5 steps

1. **Download your pack** (below) - or grab individual skills from [`packs/skills/`](packs/skills/).
2. **Install it** for your agent - platform guides in [`install/`](install/): [Claude Code](install/claude-code.md) · [Claude.ai](install/claude-ai.md) · [Cursor/Windsurf](install/cursor-windsurf.md) · [ChatGPT](install/chatgpt.md).
3. **Connect the FirstTouch MCP** (`https://mcp.firsttouch.ai`) - required by every play. HubSpot MCP is optional but unlocks the CRM plays. See [`references/mcp-setup.md`](references/mcp-setup.md).
4. **Answer the 3 onboarding questions** in [`references/onboarding.md`](references/onboarding.md) - LinkedIn account type, HubSpot access, which play to run first.
5. **Run your first play and approve the drafts** - nothing sends without your approval.

### Download your pack

| Pack | For | Download |
|---|---|---|
| Founder Pack | Founders doing their own sales | [`packs/founder-pack.zip`](packs/founder-pack.zip) |
| AE Pack | Account Executives | [`packs/ae-pack.zip`](packs/ae-pack.zip) |
| BDR Pack | Business Development Reps | [`packs/bdr-pack.zip`](packs/bdr-pack.zip) |
| RevOps Pack | Revenue Operations | [`packs/revops-pack.zip`](packs/revops-pack.zip) |

Single skills for Claude.ai (one skill per zip, references bundled): [`packs/skills/`](packs/skills/)

---

## Install (for end customers)

1. Drop any skill folder into your agent's skills directory:
   - **Claude Code:** `~/.claude/skills/<skill-name>/` (or `.claude/skills/` per-project)
   - **Claude.ai:** Settings → Features → upload a single-skill zip from [`packs/skills/`](packs/skills/)
   - **Cursor / Windsurf / custom:** copy the folder anywhere the agent can read
2. Connect the MCPs your plays need - see [`references/mcp-setup.md`](references/mcp-setup.md).
   - **FirstTouch MCP** is required for FirstTouch execution and approvals.
   - **HubSpot MCP or a service key/private app token** unlocks HubSpot-specific plays.
   - If HubSpot is unavailable, run FirstTouch-only plays such as social engagement, social campaigns from Discover Contacts or imported lists, AI SDR from Discover Contacts, founder AI SDR, sequence QA, and workspace audit.
3. Complete [`references/onboarding.md`](references/onboarding.md) before running the first play.
4. Start with high-intent plays first; add outbound only after those are running and account limits are respected.

---

## First-run onboarding and recommended rollout

Every pack should ask three questions before running volume:

| Question | Why it matters |
|---|---|
| Do you have Sales Navigator / Premium, or a free/basic LinkedIn account? | Free/basic accounts cannot use connection notes; recommend **10** connection requests/day (FirstTouch max 20/day). Sales Navigator / Premium can use notes; recommend **20**/day (FirstTouch max 30/day). |
| Do you use HubSpot, and can you connect the HubSpot MCP or provide a service key/private app token? | HubSpot-specific plays need internal CRM context. Without it, run FirstTouch-only plays or ask the user to create a HubSpot list/source FirstTouch can access. |
| Which plays do you want to run first? | Recommend high-intent plays first, then outbound once warm motions are running to keep the account healthy. |

**Recommended order:**
1. For founders, start with **Social Engagement Flow** first. It does not require HubSpot and uses the warmest signal available.
2. Run other high-intent plays next: inbound speed-to-lead, website visitor follow-up, HubSpot signal touches, customer referral thank-you, and stalled-deal reactivation when the required data exists.
3. Add one-time social campaigns when the audience is narrow and the user can approve static flow templates.
4. Add AI SDR / Founder AI SDR only after warm motions are running, with daily approval batches of 10 free/basic or 20 Sales Navigator/Premium contacts.

---

## The plays that drive the most value

1. **Social Engagement Flow** - act on post likes/comments first; for founders this is the number one starter play and can use owned posts or a relevant competitor founder/influencer profile.
2. **Social Campaigns** - build a narrow campaign using either row-level dynamic approvals for rep/BDR pushes or static templates with flow-level approval for governed one-time campaigns.
3. **AI SDR / ICP Outbound** - build daily approval-ready batches from a HubSpot list or FirstTouch Discover Contacts.
4. **Founder AI SDR** - the AI SDR workflow in founder voice, with the same approval queue and recommended 10/20 daily connection caps.
5. **Inbound Speed-to-Lead** - attach LinkedIn connection and follow-up to signups, trials, or demo requests.
6. **Website Visitor Follow-Up** - act on pricing/demo/product-page intent from HubSpot tracking or RB2B/list sources.
7. **HubSpot Signal Touches** - turn lifecycle, list, or deal events into timely social touches.
8. **Stalled Deal Reactivation** - trigger a contact-based HubSpot workflow for contacts associated to open deals not Closed Won/Lost with no engagement for 60+ days, then draft a fresh approved LinkedIn touch.
9. **Customer Referral Thank-You** - connect with new customers, thank them, ask for feedback, and invite light referrals.
10. **Sequence QA / Workspace Audit** - make sure the setup and messaging are safe before scaling.

---

## Plays at a glance

| Play | Outcome | Needs / fallback |
|------|---------|-------|
| FirstTouch Messaging | Draft on-brand, high-converting LinkedIn outreach | No HubSpot required |
| Warm Engager Follow-Up | Turn post engagers into conversations | FirstTouch; HubSpot optional for qualification/routing |
| Social Campaigns | Build one-time LinkedIn campaigns for narrow ICP segments with static templates and flow-level approval | No HubSpot required for Discover Contacts/imported lists; HubSpot required for CRM/deal/customer segments |
| AI SDR / ICP Outbound Builder | Pull target accounts, qualify, find personas, and add to a daily approval queue | HubSpot list preferred; otherwise ICP brief + FirstTouch Discover Contacts |
| Founder-Led AI SDR | Run the AI SDR workflow in founder voice | HubSpot list preferred; otherwise ICP brief + FirstTouch Discover Contacts |
| Inbound Speed-to-Lead | Attach LinkedIn connection + follow-up to inbound signups or trials | HubSpot or FirstTouch-accessible inbound list/import |
| HubSpot Signal → LinkedIn Touch | Act on CRM lifecycle/list/deal signals with social outreach | HubSpot required |
| Website Visitor Follow-Up | Turn website visitor intent into social outreach | HubSpot tracking or RB2B/list source |
| Stalled Deal Reactivation | Contact-based HubSpot workflow for contacts associated to open deals not Closed Won/Lost with no engagement for 60+ days, then queue reactivation touches | HubSpot required |
| Customer Referral Thank-You | Connect with new customers, thank them, ask for feedback, and invite light referrals | HubSpot Closed Won/customer source or imported customer list required |
| HubSpot Social Task Runner | Execute due HubSpot LinkedIn/social tasks through FirstTouch and mark them complete after queueing | HubSpot MCP with task read/write required |
| Team Performance Report | Summarize sends, replies, meetings, opportunities, and HubSpot logging coverage by flow/sender/date | FirstTouch; HubSpot improves logging coverage checks |
| Sequence QA Reviewer | Review campaigns for risk + quality | No HubSpot required |
| Campaign Pause & Fix | Pause a live flow mid-send, diagnose, fix copy/audience/volume, and restart with safe re-enrollment | No HubSpot required |
| Workspace Audit | Find setup gaps before launch | No HubSpot required; HubSpot improves CRM checks |

---

## Design principles (Anthropic Agent Skills standard)

- **Progressive disclosure** - only the relevant context loads. Metadata is always present; the body loads on trigger; references load on demand.
- **Passive, deliverable-oriented** - each skill defines a deliverable, not a goal. The agent produces an artifact; a human approves before anything sends.
- **Human-in-the-loop by default** - no play sends outbound autonomously. Dynamic plays require per-send approval; one-time social campaigns can use flow-level approval for the exact audience and static templates (see [`references/safety-governance.md`](references/safety-governance.md)).
- **HubSpot-aware, not HubSpot-blocked where possible** - HubSpot-specific plays say so clearly; AI SDR and founder AI SDR can run from FirstTouch Discover Contacts when no HubSpot list exists.

---

## Persona Packs

In addition to the flat `skills/` folder above, this repo ships **4 downloadable persona packs** - self-contained bundles that collect the right skills for a specific role.

| Pack | Persona | Skills included | Key plays |
|---|---|---:|---|
| `founder-pack` | Founders doing their own sales | 10 | Social engagement flow, social campaigns, founder AI SDR, inbound follow-up, customer referral thank-you, stalled open-deal workflow |
| `ae-pack` | Account Executives | 11 | Inbound speed-to-lead, social campaigns, customer referral thank-you, stalled open-deal workflow, meeting-booked stakeholder follow-up, closed-lost re-engage |
| `bdr-pack` | Business Development Reps | 9 | Inbound speed-to-lead, social engagement flow, social campaigns, target-list AI SDR, lead recovery |
| `revops-pack` | Revenue Operations | 13 | Workspace audit, sequence QA, customer referral thank-you, social campaigns, stalled open-deal workflow, HubSpot workflow build, team governance |

### Shared-core model

All 4 packs include the same 6 core plays, each with a persona-specific lens:

1. **Inbound speed-to-lead** - fast LinkedIn touch on signups, trials, demo requests
2. **Social engagement flow** - act on post engagement from your posts, leadership posts, or company content
3. **Social campaigns** - one-time campaigns for narrow ICP segments with static flow templates and flow-level approval
4. **Website visitor play** - turn high-intent page visits into outreach
5. **AI SDR build** - daily approval-ready outbound from a HubSpot contact/company list, or from a newly discovered ICP list when no HubSpot list exists
6. **Scoop-up slipped leads** - recover dormant MQLs, no-shows, and stale pipeline when HubSpot/list data exists. Stalled-deal reactivation specifically means a contact-based HubSpot workflow enrolling contacts associated to open deals not Closed Won/Lost with no engagement for 60+ days.

Each pack then adds persona-unique plays on top of this shared core.

### How packs are built

Packs are **vendored copies** of canonical skills - no symlinks, no shared imports. This is required by the Agent Skills standard: every install path (Claude Code `~/.claude/skills/`, Claude.ai zip upload, Cursor folder copy) works with isolated skill folders. The build script handles sync so canonical `skills/` remains the single source of truth.

```bash
python scripts/build-packs.py
```

This reads each `packs/<persona>.json` manifest and materializes:

```
dist/
├── founder-pack/
│   ├── README.md          ← persona-framed plays + install guide
│   ├── skills/            ← copies of this persona's skills
│   └── references/        ← onboarding, MCP setup, safety, messaging
├── founder-pack.zip       ← ready to upload to Claude.ai
├── ae-pack/  ...
└── revops-pack/  ...
```

Re-running the script syncs all packs to the current canonical state, rebuilds the zips in `dist/`, and publishes the distributable zips to `packs/*-pack.zip` plus self-contained single-skill zips to `packs/skills/`. CI validates frontmatter, manifests, and zip freshness on every push.

---

## Support

- **Slack community** - [firsttouch-workspace.slack.com](https://firsttouch-workspace.slack.com): the best place to ask questions, share plays, and get help from the FirstTouch team.
- **In-app chat** - chat support inside the FirstTouch app for account-specific issues.
- **Something broke mid-play?** - [`references/troubleshooting.md`](references/troubleshooting.md) covers MCP failures, LinkedIn warnings, stalled queues, and credit issues.

*Pack version 1.2.1 - last updated 2026-07-01. See [CHANGELOG.md](CHANGELOG.md).*
