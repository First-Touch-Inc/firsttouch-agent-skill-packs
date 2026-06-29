# FirstTouch Revenue Skills — Customer Pack

> **Turn Claude, Cursor, Codex, and ChatGPT into HubSpot-native LinkedIn revenue operators.**

This pack gives your customers' coding/AI agents a structured set of **plays** — reusable skills that execute real LinkedIn-outreach workflows inside HubSpot, with attribution, approvals, and CRM logging baked in.

It is built to the open **Agent Skills** standard ([agentskills.io](https://agentskills.io)), so every skill works in Claude Code, Claude.ai, Cursor, Windsurf, and any MCP-compatible harness.

---

## Why this pack exists

Most "AI outreach" tools stop at generating copy. Customers can get an agent to *write* a message, but not to:

- act on a **HubSpot signal** (lifecycle change, deal stall, form fill)
- find the right person on **LinkedIn** and reach out safely
- **log** the touch to the contact timeline and attribute it to pipeline
- respect **ownership, approvals, and account-safety limits**

Each play here closes that loop. This is the difference between an agent that *sounds* like an SDR and one that *operates* like one.

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
    ├── firsttouch-messaging/               ← foundation: how to write outreach (every play builds on this)
    ├── warm-engager-followup/
    ├── hubspot-signal-to-linkedin-touch/
    ├── champion-mapper/
    ├── stalled-deal-reactivation/
    ├── owner-safe-outreach-operator/
    ├── pipeline-attribution-analyst/
    ├── workspace-audit/
    ├── sequence-qa-reviewer/
    └── founder-led-outbound/
```

**Two layers:**
1. **Foundation** (`references/` + skill `00`) — the shared grounding every play assumes. Read once, reused everywhere.
2. **Plays** (`01`–`10`) — each is a self-contained, revenue-tied workflow. Each play's `SKILL.md` is tight (<500 lines); heavy detail lives in its own `references/`.

---

## Install (for end customers)

1. Drop any skill folder into your agent's skills directory:
   - **Claude Code:** `~/.claude/skills/<skill-name>/` (or `.claude/skills/` per-project)
   - **Claude.ai:** Settings → Features → upload as zip
   - **Cursor / Windsurf / custom:** copy the folder anywhere the agent can read
2. Connect the MCPs your plays need — see [`references/mcp-setup.md`](references/mcp-setup.md). Most plays need **FirstTouch MCP** + **HubSpot MCP**.
3. Complete [`references/onboarding.md`](references/onboarding.md) before running the first play:
   - Ask whether the user has **Sales Navigator / Premium** or a **free/basic** LinkedIn account.
   - Ask whether they use **HubSpot** and can connect the HubSpot MCP or provide a HubSpot service key / private app token.
   - If HubSpot is unavailable, only run FirstTouch-only plays or ask them to create a HubSpot list FirstTouch can access.
4. Start with high-intent plays first; add outbound only after those are running and account limits are respected.

---

## First-run onboarding and recommended rollout

Every pack should ask three questions before running volume:

| Question | Why it matters |
|---|---|
| Do you have Sales Navigator / Premium, or a free/basic LinkedIn account? | Free/basic accounts are capped at **10** connection requests/day and cannot use connection notes; Sales Navigator / Premium can use notes and go up to **20**/day. |
| Do you use HubSpot, and can you connect the HubSpot MCP or provide a service key/private app token? | HubSpot-specific plays need internal CRM context. Without it, the user must create a HubSpot list FirstTouch can access. |
| Which plays do you want to run first? | Recommend high-intent plays first, then outbound once warm motions are running to keep the account healthy. |

**Recommended order:** inbound speed-to-lead, warm engager follow-up, website visitor follow-up, HubSpot signal touches, customer champion, and stalled-deal reactivation first; AI SDR / ICP outbound second, running daily approval batches of 10 free/basic or 15 Sales Navigator/Premium contacts.

---

## The plays that drive the most value

These are the highest-value motions customers repeatedly get ROI from:

1. **Founder-led sales** — strategic outbound in the founder's own voice
2. **Social post engagement follow-up** — if someone engages with content, check connection status, connect if needed, and start a light conversation
3. **Inbound speed-to-lead** — attach connection requests / social touches to inbound signups or trials
4. **Customer champion** — when a customer milestone is hit, reach out and deepen the relationship
5. **Website visitors** — act on website de-anon or HubSpot website-visitor signals
6. **ICP outbound** — pull target accounts/lists, qualify, find the right personas, and add them to flow

The rest of the skills support, safeguard, or measure these core motions.

---

## The 10 plays at a glance

| # | Play | Outcome | Needs |
|---|------|---------|-------|
| 00 | FirstTouch Messaging | Draft on-brand, high-converting LinkedIn outreach | — |
| 01 | Warm Engager Follow-Up | Turn post engagers into conversations | FirstTouch |
| 02 | HubSpot Signal → LinkedIn Touch | Act on CRM signals with social outreach | FirstTouch + HubSpot |
| 03 | Champion Mapper | Map likely champions across an account | FirstTouch + HubSpot |
| 04 | Stalled Deal Reactivation | Restart stuck opps with social proof | FirstTouch + HubSpot |
| 05 | Owner-Safe Outreach Operator | Route, gate, and log every send safely | FirstTouch + HubSpot |
| 07 | Pipeline Attribution Analyst | Show which social touches influenced pipeline | FirstTouch + HubSpot |
| 08 | Workspace Audit | Find setup gaps before launch | FirstTouch |
| 09 | Sequence QA Reviewer | Review campaigns for risk + quality | FirstTouch |
| 10 | Founder-Led Outbound | Run founder-style social outbound | FirstTouch + HubSpot |
| 11 | Inbound Speed-to-Lead | Attach LinkedIn connection + follow-up to inbound signups or trials | FirstTouch + HubSpot |
| 12 | Customer Champion | Reach out when a customer milestone is reached | FirstTouch + HubSpot |
| 13 | Website Visitor Follow-Up | Turn website visitor intent into social outreach | FirstTouch + HubSpot |
| 14 | ICP Outbound Builder | Pull target accounts, qualify, find personas, and add to flow | FirstTouch + HubSpot |

---

## Design principles (Anthropic Agent Skills standard)

- **Progressive disclosure** — only the relevant context loads. Metadata is always present; the body loads on trigger; references load on demand.
- **Passive, deliverable-oriented** — each skill defines a *deliverable*, not a goal. The agent produces an artifact; a human approves before anything sends.
- **Human-in-the-loop by default** — no play sends outbound autonomously. Every send goes through an approval gate (see [`references/safety-governance.md`](references/safety-governance.md)).
- **Attribution-aware** — plays that touch prospects also log to HubSpot and can report influenced pipeline.

---

*Built by FirstTouch. Distributed under the Agent Skills open standard.*

---

## Persona Packs

In addition to the flat `skills/` folder above, this repo ships **4 downloadable persona packs** — self-contained bundles that collect the right skills for a specific role.

| Pack | Persona | Skills included | Key plays |
|---|---|---|---|
| `founder-pack` | Founders doing their own sales | 9 | Founder-led outbound, connection mining, social engager, inbound follow-up |
| `ae-pack` | Account Executives | 9 | Stalled deal reactivation, champion mapping, meeting multi-thread, closed-lost re-engage |
| `bdr-pack` | Business Development Reps | 7 | Inbound speed-to-lead, social engager, target-list AI SDR, lead recovery |
| `revops-pack` | Revenue Operations | 11 | Workspace audit, sequence QA, pipeline attribution, HubSpot workflow build, team governance |

### Shared-core model

All 4 packs include the same 5 core plays, each with a persona-specific lens:

1. **Inbound speed-to-lead** — fast LinkedIn touch on signups, trials, demo requests
2. **Social engager flow** — act on post engagement (your posts or leadership's)
3. **Website visitor play** — turn high-intent page visits into outreach
4. **AI SDR build** — daily approval-ready outbound from a HubSpot contact/company list, or from a newly discovered ICP list when no HubSpot list exists
5. **Scoop-up slipped leads** — recover dormant MQLs, no-shows, and stale pipeline

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
│   └── references/        ← mcp-setup.md + safety-governance.md
├── founder-pack.zip       ← ready to upload to Claude.ai
├── ae-pack/  ...
└── revops-pack/  ...
```

Re-running the script syncs all packs to the current canonical state and rebuilds the zips. The `dist/` folder is gitignored; zips are the distributable artifact.

### Roadmap plays

Some plays are specced but not yet buildable — the FirstTouch MCP capability doesn't exist yet. These are documented in `roadmap/` (clearly marked "Not yet implemented") so they appear in the pack READMEs as honest "coming soon" items, never as broken stub skills.

| Roadmap play | Blocked on | Persona(s) |
|---|---|---|
| Customer referral / advocacy ask | Post-thank-you engagement logic | Founder, RevOps |
| Rep-led AI SDR | Rep-voice overlay (founder-voice exists today) | AE, BDR |
| Inbox triage + reply draft | FT MCP inbox read capability | BDR, AE |
| CS handoff / retention connector | CS-as-sender routing at milestone | RevOps |
