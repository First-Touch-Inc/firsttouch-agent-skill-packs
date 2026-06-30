# FirstTouch Revenue Skills — Customer Pack

> **Turn Claude, Cursor, Codex, and ChatGPT into FirstTouch-native LinkedIn revenue operators.**

This pack gives customers a structured set of **plays** — reusable skills that execute real LinkedIn-outreach workflows with FirstTouch, human approvals, account-safety limits, and HubSpot context when available.

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
│   └── safety-governance.md               ← approval gates, send safety, account limits
└── skills/
    ├── firsttouch-messaging/              ← foundation: how to write outreach
    ├── warm-engager-followup/             ← social engagement flow
    ├── icp-outbound-builder/              ← AI SDR
    ├── founder-led-outbound/              ← founder AI SDR
    ├── inbound-speed-to-lead/
    ├── hubspot-signal-to-linkedin-touch/
    ├── website-visitor-followup/
    ├── stalled-deal-reactivation/
    ├── customer-champion/
    ├── sequence-qa-reviewer/
    └── workspace-audit/
```

**Two layers:**
1. **Foundation** (`references/` + `firsttouch-messaging`) — shared grounding every play assumes.
2. **Customer plays** — self-contained, revenue-tied workflows. Governance and attribution rules live in shared references instead of separate customer-facing plays.

---

## Install (for end customers)

1. Drop any skill folder into your agent's skills directory:
   - **Claude Code:** `~/.claude/skills/<skill-name>/` (or `.claude/skills/` per-project)
   - **Claude.ai:** Settings → Features → upload as zip
   - **Cursor / Windsurf / custom:** copy the folder anywhere the agent can read
2. Connect the MCPs your plays need — see [`references/mcp-setup.md`](references/mcp-setup.md).
   - **FirstTouch MCP** is required for FirstTouch execution and approvals.
   - **HubSpot MCP or a service key/private app token** unlocks HubSpot-specific plays.
   - If HubSpot is unavailable, run FirstTouch-only plays such as social engagement, AI SDR from Discover Contacts, founder AI SDR, sequence QA, and workspace audit.
3. Complete [`references/onboarding.md`](references/onboarding.md) before running the first play.
4. Start with high-intent plays first; add outbound only after those are running and account limits are respected.

---

## First-run onboarding and recommended rollout

Every pack should ask three questions before running volume:

| Question | Why it matters |
|---|---|
| Do you have Sales Navigator / Premium, or a free/basic LinkedIn account? | Free/basic accounts are capped at **10** connection requests/day and cannot use connection notes; Sales Navigator / Premium can use notes and go up to **20**/day. |
| Do you use HubSpot, and can you connect the HubSpot MCP or provide a service key/private app token? | HubSpot-specific plays need internal CRM context. Without it, run FirstTouch-only plays or ask the user to create a HubSpot list/source FirstTouch can access. |
| Which plays do you want to run first? | Recommend high-intent plays first, then outbound once warm motions are running to keep the account healthy. |

**Recommended order:**
1. For founders, start with **Social Engagement Flow** first. It does not require HubSpot and uses the warmest signal available.
2. Run other high-intent plays next: inbound speed-to-lead, website visitor follow-up, HubSpot signal touches, customer champion, and stalled-deal reactivation when the required data exists.
3. Add AI SDR / Founder AI SDR only after warm motions are running, with daily approval batches of 10 free/basic or 20 Sales Navigator/Premium contacts.

---

## The plays that drive the most value

1. **Social Engagement Flow** — act on post/profile engagement first; for founders this is the number one starter play and does not require HubSpot.
2. **AI SDR / ICP Outbound** — build daily approval-ready batches from a HubSpot list or FirstTouch Discover Contacts.
3. **Founder AI SDR** — the AI SDR workflow in founder voice, with the same approval queue and 10/20 daily caps.
4. **Inbound Speed-to-Lead** — attach LinkedIn connection and follow-up to signups, trials, or demo requests.
5. **Website Visitor Follow-Up** — act on pricing/demo/product-page intent from HubSpot tracking or RB2B/list sources.
6. **HubSpot Signal Touches** — turn lifecycle, list, or deal events into timely social touches.
7. **Stalled Deal Reactivation** — trigger a contact-based HubSpot workflow for contacts associated to open deals not Closed Won/Lost with no engagement for 60+ days, then draft a fresh approved LinkedIn touch.
8. **Customer Champion** — reach out around customer milestones.
9. **Sequence QA / Workspace Audit** — make sure the setup and messaging are safe before scaling.

---

## Plays at a glance

| Play | Outcome | Needs / fallback |
|------|---------|-------|
| FirstTouch Messaging | Draft on-brand, high-converting LinkedIn outreach | No HubSpot required |
| Warm Engager Follow-Up | Turn post engagers into conversations | FirstTouch; HubSpot optional for qualification/routing |
| AI SDR / ICP Outbound Builder | Pull target accounts, qualify, find personas, and add to a daily approval queue | HubSpot list preferred; otherwise ICP brief + FirstTouch Discover Contacts |
| Founder-Led AI SDR | Run the AI SDR workflow in founder voice | HubSpot list preferred; otherwise ICP brief + FirstTouch Discover Contacts |
| Inbound Speed-to-Lead | Attach LinkedIn connection + follow-up to inbound signups or trials | HubSpot or FirstTouch-accessible inbound list/import |
| HubSpot Signal → LinkedIn Touch | Act on CRM lifecycle/list/deal signals with social outreach | HubSpot required |
| Website Visitor Follow-Up | Turn website visitor intent into social outreach | HubSpot tracking or RB2B/list source |
| Stalled Deal Reactivation | Contact-based HubSpot workflow for contacts associated to open deals not Closed Won/Lost with no engagement for 60+ days, then queue reactivation touches | HubSpot required |
| Customer Champion | Reach out when a customer milestone is reached | HubSpot required |
| Sequence QA Reviewer | Review campaigns for risk + quality | No HubSpot required |
| Workspace Audit | Find setup gaps before launch | No HubSpot required; HubSpot improves CRM checks |

---

## Design principles (Anthropic Agent Skills standard)

- **Progressive disclosure** — only the relevant context loads. Metadata is always present; the body loads on trigger; references load on demand.
- **Passive, deliverable-oriented** — each skill defines a deliverable, not a goal. The agent produces an artifact; a human approves before anything sends.
- **Human-in-the-loop by default** — no play sends outbound autonomously. Every send goes through an approval gate (see [`references/safety-governance.md`](references/safety-governance.md)).
- **HubSpot-aware, not HubSpot-blocked where possible** — HubSpot-specific plays say so clearly; AI SDR and founder AI SDR can run from FirstTouch Discover Contacts when no HubSpot list exists.

---

## Persona Packs

In addition to the flat `skills/` folder above, this repo ships **4 downloadable persona packs** — self-contained bundles that collect the right skills for a specific role.

| Pack | Persona | Skills included | Key plays |
|---|---|---:|---|
| `founder-pack` | Founders doing their own sales | 8 | Social engagement flow, founder AI SDR, inbound follow-up, stalled open-deal workflow, customer thank-you |
| `ae-pack` | Account Executives | 7 | Inbound speed-to-lead, stalled open-deal workflow, meeting-booked stakeholder follow-up, closed-lost re-engage |
| `bdr-pack` | Business Development Reps | 6 | Inbound speed-to-lead, social engagement flow, target-list AI SDR, lead recovery |
| `revops-pack` | Revenue Operations | 10 | Workspace audit, sequence QA, stalled open-deal workflow, HubSpot workflow build, team governance |

### Shared-core model

All 4 packs include the same 5 core plays, each with a persona-specific lens:

1. **Inbound speed-to-lead** — fast LinkedIn touch on signups, trials, demo requests
2. **Social engagement flow** — act on post engagement from your posts, leadership posts, or company content
3. **Website visitor play** — turn high-intent page visits into outreach
4. **AI SDR build** — daily approval-ready outbound from a HubSpot contact/company list, or from a newly discovered ICP list when no HubSpot list exists
5. **Scoop-up slipped leads** — recover dormant MQLs, no-shows, and stale pipeline when HubSpot/list data exists. Stalled-deal reactivation specifically means a contact-based HubSpot workflow enrolling contacts associated to open deals not Closed Won/Lost with no engagement for 60+ days.

Each pack then adds persona-unique plays on top of this shared core.

### How packs are built

Packs are **vendored copies** of canonical skills — no symlinks, no shared imports. This is required by the Agent Skills standard: every install path (Claude Code `~/.claude/skills/`, Claude.ai zip upload, Cursor folder copy) works with isolated skill folders. The build script handles sync so canonical `skills/` remains the single source of truth.

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

Re-running the script syncs all packs to the current canonical state, rebuilds the zips in `dist/`, and publishes the distributable zips to `packs/*-pack.zip`.
