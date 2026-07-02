# FirstTouch RevOps Pack

*Pack version 1.4.1*

> Data chaos and untracked touches make it impossible to prove what's working or govern the team: these are the plays for the job you actually do.

## Who this is for
You own the stack and the data. Every untracked touch is attribution you'll never recover. You care about owner routing, approval workflows, HubSpot data hygiene, and whether this creates compliance risk or solves it. These plays give you the governance layer, the attribution readiness checks, reply visibility, and the team-wide setup plays that turn individual reps' outreach into a measurable, auditable revenue motion.

## What is MCP?
MCP is the plug that lets your AI agent use FirstTouch. In **ChatGPT** and **Claude.ai** it shows up in settings as a **Connector**; in **Claude Code**, **Cursor**, **Windsurf**, and **Codex** it's called an **MCP server**. Same thing, different label. You set it up once (see `references/mcp-setup.md`), and it never sees your LinkedIn password - it only performs actions you approve.

## First-run onboarding (do this before any play)
Answer these once; every play depends on them:

1. **LinkedIn account type:** do you have Sales Navigator / Premium, or a free/basic account?
   - Free/basic: no connection notes; recommend **10/day** connection requests; FirstTouch max **20/day**.
   - Sales Navigator / Premium: connection notes available; recommend **20/day** connection requests; FirstTouch max **30/day**.
   - AI SDR shares the same daily connection-request budget. If AI SDR and another play run on the same day, the total across all plays should stay within the recommended 10 or 20 unless the user explicitly approves higher volume; never exceed the FirstTouch max of 20/day free/basic or 30/day Sales Navigator/Premium.
   - Already-connected LinkedIn message rows use a separate FirstTouch-supported message cap: 20/day on free/basic LinkedIn and 30/day on Sales Navigator/Premium.
   - FirstTouch enforces these limits automatically - adjust volume anytime in the FirstTouch app; you can never go over the peak limits. Hitting a limit just puts the seat on cooldown until the next window.
2. **HubSpot access:** getting access is easy - ask your admin to approve HubSpot MCP access (a quick approval), or request a **read-only service key** that lets the agent read deals, contacts, and companies with no write risk. If neither is available yet, plenty of plays below run without HubSpot; you can also ask an admin for a HubSpot list FirstTouch can access.
3. **Credits:** new FirstTouch workspaces start with **100 credits** - plenty for your first discoveries and enrichments. The agent checks the balance before any bulk run and asks before spending.
4. **Play choice:** pick from the persona start point below.

Use `references/onboarding.md` for the full question flow and account-type rules. Use `references/recipes.md` for the generated recipe catalog if the README is not loaded by the agent.

**Next:** answer the questions above once, then go straight to **Start here** below and pick your first play - that is the whole setup.

## Start here
Start with **Pre-launch rollout audit** before any rep launches volume. Then govern the core rollout: HubSpot list triggers, **Team-wide AI SDR**, social campaigns, stalled-deal workflows, and **Attribution & team performance review** as the recurring reporting cadence. **Ad hoc queue diagnostics:** if a rep asks why a LinkedIn/email action has not sent, ask the agent a direct queue/status question first; you do not need to run the full workspace audit. Keep situational plays such as events, new-customer referral thank-you, website visitors, and closed-lost reengagement for after the core governance path is stable. **Rolling out to 2 or more reps? Read and apply section D (readiness by rollout size) in `references/revops-admin-appendix.md` first - pick your tier and run that tier's checklist.**

## Your week
- **Monday:** check queue hygiene - stuck approvals, blocked rows, and cap usage across senders.
- **Midweek:** spot-check any new campaign with sequence QA before it launches.
- **Monthly:** run the team performance report and review caps, suppression lists, and logging coverage.

## Quickstart play cards
| Situation | Run this | What happens |
|---|---|---|
| Before launch | Pre-launch rollout audit | Validate seats, caps, approvals, and logging |
| Team prospecting | Team-wide AI SDR | Configure senders, owners, caps, and approval queues |
| HubSpot-driven outreach | HubSpot list trigger | Launch FirstTouch from approved CRM source |
| Governance / QA | Sequence QA reviewer | Catch risk before reps send |
| Reporting | Attribution & team performance review | Pull team metrics and reconcile CRM logging |
| New customers | Referral thank-you | Connect, thank, collect feedback, and ask for light network referrals |
| Rep asks why an action has not sent | Direct queue/status question | Inspect outreach queue blockers without running a full audit |

## How to use this pack
- **Recipes** are the best starting point. They combine the right skills into the job you actually want done.
- **Skills** are the individual building blocks. Run a skill directly only when you know the exact motion you want.
- **Read once:** `references/system-grounding.md` explains how agents, FirstTouch, HubSpot, approvals, and measurement fit together.
- **FirstTouch terms:** a campaign/sequence/social campaign in this pack becomes a FirstTouch audience, flow plan, dynamic action, or enrollment depending on the play. "AI SDR" in this pack maps to `icp-outbound-builder`. The agent should use FirstTouch's available execution objects and state the exact object it created.
- **Approval locations:** before assuming approval tasks are enabled, ask the user or check available FirstTouch task/workspace settings. If approval tasks are enabled, route them to the owner in HubSpot or the FirstTouch app under **Tasks**. If that workflow is not enabled or cannot be confirmed, present the table in chat and wait for explicit approval.

## HubSpot reality check
- **What works without HubSpot:** Workspace audit of FirstTouch-only settings, sequence QA, team-wide AI SDR from Discover Contacts, social engagement setup via FirstTouch MCP on owned or relevant external personal profiles, and social campaigns from imported/Discover lists. Owner/logging/deal/customer checks need HubSpot.
- **What needs HubSpot:** CRM lifecycle/deal criteria, owner routing, HubSpot timeline logging where the connected FirstTouch-HubSpot integration supports it, stalled-deal workflows, and contact/company lists stored only in HubSpot. Without HubSpot/list access, use the FirstTouch-only recipes and do not promise existing-pipeline/deal recovery.
- **FirstTouch-accessible list/import means:** a CSV, static list, audience, or HubSpot list that FirstTouch can read. For true inbound automation, connect HubSpot or another source that continuously feeds FirstTouch.
- **Enrichment is optional but useful:** FirstTouch can enrich contacts/companies when credits and data are available. Clay/Surfe or another enrichment MCP is an optional supplement, not a prerequisite. Without a usable LinkedIn URL or enough verified data, the agent should skip or queue incomplete records rather than fabricate.

## Your plays

### Skills catalog (check Needs before running)
| Skill | What it does | Needs / HubSpot status | Runs |
|---|---|---|---|
| inbound-speed-to-lead | "Attach LinkedIn connection requests and lightweight follow-up to booked meetings, inbound signups, trial starts, demo requests, or other high-intent inbound lists. | HubSpot or FirstTouch-accessible inbound list/import required; true automation needs a connected source | `inbound-speed-to-lead` |
| warm-engager-followup | Turn people who recently liked or commented on the sender's posts, an executive's posts, leadership/executive personal-profile content, or a relevant competitor founder/influencer profile into conversations and pipeline. | No HubSpot required; enable Social Engagement through FirstTouch MCP for monitored profiles; user-provided/exported engager lists also work | `warm-engager-followup` |
| website-visitor-followup | Turn website-visitor intent into LinkedIn outreach by using identified-visitor data or HubSpot website-visitor signals, checking connection status, drafting a lightweight message, and gating execution for approval. | HubSpot tracking or RB2B/list source required | `website-visitor-followup` |
| icp-outbound-builder | "Run the daily recurring team AI SDR motion (for SDRs, BDRs, and AEs): start from a HubSpot contact/company list or build a new ICP list via FirstTouch Discover Contacts, enrich each prospect, generate customized LinkedIn-first outreach, and queue a daily batch for human approval. | No HubSpot required with ICP brief + FirstTouch Discover Contacts; HubSpot list optional | `icp-outbound-builder` |
| hubspot-signal-to-linkedin-touch | Turn a HubSpot CRM event - lifecycle stage change, deal stage movement, form fill, list addition - into a timely, personalized LinkedIn touch. | HubSpot required | `hubspot-signal-to-linkedin-touch` |
| social-campaigns | "Build a ONE-TIME (not recurring) LinkedIn social campaign for a very narrow ICP segment: define precise audience criteria, source/enrich contacts from FirstTouch and optional HubSpot lists, then choose either row-level dynamic actions for rep/BDR one-at-a-time execution or static flow templates for RevOps/founder-approved one-time campaigns. | No HubSpot for pure ICP/imported/connection-list campaigns; HubSpot required for CRM/deal/customer segments | `social-campaigns` |
| stalled-deal-reactivation | Build and govern a contact-based HubSpot workflow for contacts associated to open deals that are not Closed Won and not Closed Lost and have had no engagement for 60+ days. | HubSpot required; may need RevOps/admin for workflow setup | `stalled-deal-reactivation` |
| customer-referral | Auto-prepare LinkedIn connection requests and thank-you/referral messages for new customers after they choose the product. | HubSpot Closed Won/customer source or imported/FirstTouch-accessible customer list required; HubSpot improves owner/CSM routing and logging | `customer-referral` |
| sequence-qa-reviewer | Review a FirstTouch LinkedIn campaign/sequence for risk and quality before it launches - checking send safety, messaging quality, personalization depth, duplicate risk, and compliance with the FirstTouch messaging framework. | No HubSpot for FirstTouch QA; HubSpot improves duplicate/owner checks | `sequence-qa-reviewer` |
| workspace-audit | Audit a FirstTouch + HubSpot workspace for readiness before launching outreach - checks MCP connections, owner coverage, LinkedIn account health, safety limits, logging setup, and data hygiene. | No HubSpot for FirstTouch-only audit; HubSpot needed for owner/logging coverage | `workspace-audit` |
| team-performance-report | Pull FirstTouch team metrics for a selected date range, flow, sender, or campaign cohort, then summarize sends, replies, reply sentiment where available, meetings booked, opportunities, and HubSpot logging coverage. | No HubSpot required for FirstTouch team metrics; HubSpot improves opportunity/pipeline reconciliation | `team-performance-report` |
| campaign-pause-and-fix | Pause a live FirstTouch campaign/flow mid-send, diagnose what is wrong, cancel or hold the affected enrollments, fix the messaging or audience, and safely restart with re-enrollment - without duplicate sends. | No HubSpot required; works on any running FirstTouch flow | `campaign-pause-and-fix` |

### Support skills (called by plays)
| Skill | What it does | Needs / HubSpot status | Runs |
|---|---|---|---|
| firsttouch-messaging | Write on-brand, high-converting LinkedIn outreach messages - connection requests, openers, follow-ups, and meeting asks - calibrated to the prospect's seniority and a real signal. | No HubSpot required | `firsttouch-messaging` |

### Recipes (recommended starting points)
#### Core governance
| Play | What it does | Needs | Composes from |
|---|---|---|---|
| Pre-launch rollout audit | Run once before first launch or major rollout: MCP connections, approval workflow, suppression checks, sequence quality, logging round-trip, and per-seat safety limits. | No HubSpot required; HubSpot improves CRM/owner checks | `workspace-audit` + `sequence-qa-reviewer` |
| Attribution & team performance review | Run the recurring RevOps reporting cadence as its own report: pull FirstTouch team metrics for the trailing 30 days by flow, sender, and date, then reconcile sends, replies, sentiment, meetings, and opportunities against HubSpot logging coverage. | No HubSpot required for FirstTouch team metrics; HubSpot improves opportunity/pipeline reconciliation | `team-performance-report` |
| HubSpot list trigger - team-wide LinkedIn flows | Use HubSpot lists or contact-based workflow outputs as the trigger source for FirstTouch LinkedIn outreach across your team. Confirm FirstTouch action cards using references/hubspot-setup.md; if cards are not present, use the documented HubSpot list/source fallback. | HubSpot required | `hubspot-signal-to-linkedin-touch` + `inbound-speed-to-lead` |
| Team-wide AI SDR - daily approval queues | Action AI SDR across the whole team, not just one user: define the ICP, choose senders/owners, discover or load prospects, enrich each prospect, apply per-sender recommended 10/20 connection caps, FirstTouch 20/30 connection max, and 20/30 message caps, then produce team-wide approval queues. | No HubSpot required with ICP brief + FirstTouch Discover Contacts; HubSpot/list optional for owner routing and account context | `icp-outbound-builder` + `firsttouch-messaging` + `workspace-audit` |
| Social campaigns - team-routed operational campaigns | Build governed campaigns such as inbound-signup decision-maker enrichment, CEO touches to stuck $50k+ deals, or product-update messaging to first-degree team connections at target accounts. RevOps chooses row-level dynamic approvals or a static flow-level campaign based on risk. | No HubSpot required for imported target-account/connection lists; HubSpot required for inbound owner routing, deal amount, deal age, or customer/deal segments | `social-campaigns` + `firsttouch-messaging` + `workspace-audit` |
| Stalled deal reactivation spec - team-wide | Produce the contact-based stalled-deal qualification spec, qualifying HubSpot list/workflow setup steps, and owner-approved LinkedIn reactivation queue. Automation is only claimed after RevOps confirms the portal/source can feed FirstTouch. | HubSpot required; RevOps/admin may be needed only for recurring workflow setup | `stalled-deal-reactivation` + `firsttouch-messaging` |
#### Situational rollout plays
| Play | What it does | Needs | Composes from |
|---|---|---|---|
| Social engager setup for team | Configure warm-engager signal capture and flows so the whole team benefits from personal-profile content engagement; use Team-wide AI SDR as the separate prospecting fallback when Social Engagement is unavailable or thin. | No HubSpot required; enable Social Engagement through FirstTouch MCP to monitor owned leadership personal profiles or relevant competitor/influencer personal profiles; HubSpot optional for qualification/routing; profile views and company-page engagement unavailable | `warm-engager-followup` + `icp-outbound-builder` |
| Website visitor play | Turn pricing/demo/product-page visits into LinkedIn touches while intent is active; if no visitor signal source exists, choose Team-wide AI SDR as a separate prospecting motion instead. | HubSpot tracking or RB2B/list source required; if no visitor signal source exists, use Team-wide AI SDR as a separate prospecting motion | `website-visitor-followup` |
| Closed-lost reengagement - team-wide | Re-engage historical closed-lost accounts across all reps when RevOps explicitly chooses a win-back motion; keep this separate from stalled open-deal reactivation. | HubSpot required; separate from stalled open-deal workflow | `hubspot-signal-to-linkedin-touch` + `icp-outbound-builder` + `firsttouch-messaging` |
| New-customer referral thank-you | After a new customer is created or Closed Won, RevOps confirms sender routing and caps, then the right owner connects, thanks them for choosing the product, collects feedback, and asks whether anyone in their network would also find value. | HubSpot Closed Won/customer source or imported/FirstTouch-accessible customer list required; HubSpot improves owner/CSM routing and logging | `customer-referral` + `firsttouch-messaging` |
| HubSpot setup guide for FirstTouch-triggered actions | Coach RevOps/admin through references/hubspot-setup.md: confirm whether FirstTouch action cards exist in HubSpot workflows, or use the supported fallback of a HubSpot list/source that FirstTouch reads before enrolling/queueing actions. | HubSpot required; confirm action cards exist in the customer portal before promising UI steps | `hubspot-signal-to-linkedin-touch` |
| Event plays - pre-invite and post-follow-up | Build audience and invite flow before an event, then run follow-up flows to attendees and no-shows. | HubSpot or imported attendee/source list required | `icp-outbound-builder` + `hubspot-signal-to-linkedin-touch` + `firsttouch-messaging` |

### How to run each recipe

**Pre-launch rollout audit**
1. Run `workspace-audit` for the readiness scorecard (verified vs manual-check areas). 2. Run `sequence-qa-reviewer` on any campaign prepared for launch. 3. Fix the priority items; do not launch with unverified logging or an account warning.

**Attribution & team performance review**
1. `team-performance-report` pulls the trailing 30 days by flow, sender, and date. 2. Reconcile with HubSpot logging coverage; mark unverifiable metrics as unverified. 3. Share the summary and adjust caps, plays, and coaching.

**HubSpot list trigger - team-wide LinkedIn flows**
1. An admin builds the contact-based workflow or list (see `references/hubspot-setup.md`). 2. `hubspot-signal-to-linkedin-touch` / `inbound-speed-to-lead` consume the events. 3. Approvals route to owners; approve, then queue.

**Social engager setup for team**
1. Enable Social Engagement monitoring on the chosen executive/competitor profiles. 2. Pull weekly engagers and route them to reps by owner. 3. Reps qualify against ICP criteria and run the warm-engager approval flow.

**Website visitor play**
1. Confirm a visitor source exists (HubSpot tracking or an RB2B/list source); stop if none. 2. `website-visitor-followup` qualifies visitors and picks a contact-level or account-level motion. 3. Draft soft, non-creepy touches, approve, queue.

**Team-wide AI SDR - daily approval queues**
1. Run `workspace-audit` before launch. 2. Each rep runs their own daily `icp-outbound-builder` queue inside per-seat caps. 3. RevOps reviews cap usage and draft quality weekly.

**Social campaigns - team-routed operational campaigns**
1. RevOps defines the segment and static templates; run `workspace-audit` if it is the first campaign. 2. QA the templates, then flow-level approval for the exact audience + templates + caps. 3. Enroll and monitor by sender.

**Stalled deal reactivation spec - team-wide**
1. RevOps builds the contact-based 60-day workflow (see `references/hubspot-setup.md`). 2. Reps approve their own owner-routed queues. 3. Track reactivation outcomes in the monthly performance review.

**Closed-lost reengagement - team-wide**
1. Pull the HubSpot Closed Lost contact list (keep it separate from stalled open deals). 2. Use `hubspot-signal-to-linkedin-touch` for known contacts and `icp-outbound-builder` to find new stakeholders at those accounts. 3. Draft a win-back angle that references what changed since the loss; owners approve their own rows.

**New-customer referral thank-you**
1. Pull the Closed Won/customer list. 2. `customer-referral` checks connection state and drafts a thank-you plus light referral ask (both connected and unconnected paths). 3. The account owner approves, then queue.

**HubSpot setup guide for FirstTouch-triggered actions**
1. Follow `references/hubspot-setup.md` to build the contact-based workflow. 2. Verify the FirstTouch action card is available, or fall back to a static list handoff. 3. Test with one designated test contact before any volume.

**Event plays - pre-invite and post-follow-up**
1. Build the invite segment from a HubSpot list or Discover Contacts. 2. Pre-event: personalized invites through the approval queue. 3. Post-event: follow up attendees and no-shows separately with different angles.

## Example prompts
- "Run the pre-launch rollout audit: check FirstTouch and HubSpot connections, approval workflow, owner coverage, LinkedIn caps, logging, and queue hygiene before reps send."
- "Set up Team-wide AI SDR for this ICP: choose senders, apply per-sender caps, create approval queues, and keep owner routing/logging auditable."
- "A new-customer list is ready. Build the governed referral thank-you motion: route owners, connect/message through FirstTouch, ask for feedback, and ask for light network referrals after approval."
- "Pull the last 30 days of FirstTouch team performance by sender and flow, then reconcile sends, replies, positive sentiment, meetings, and HubSpot logging gaps."

## Install
1. Download this pack zip and extract it so `skills/` and `references/` sit side by side. Keep the `references/` folder with the skills; many skills link to `../../references/...`.
2. Install for your agent:
   - **Claude Code (easiest path):** open Claude Code in the unzipped pack folder and say: *"Install these skills and references into my skills directory."* The agent does the copying for you.
   - **Claude Code (manual):** copy `skills/<skill-name>/` folders into your skills directory and `references/` next to them. On Windows that is `C:\Users\<you>\.claude\skills\` and `C:\Users\<you>\.claude\references\`; on Mac/Linux it is `~/.claude/skills/` and `~/.claude/references/`. The generated recipe catalog lives in `references/recipes.md` and the onboarding/play chooser in `references/onboarding.md`, so recipes survive non-zip installs.
   - **Claude.ai:** Settings → Features → Skills → upload the full persona pack `.zip` first. If uploading a single skill manually, include the specific referenced markdown files inside that skill folder before zipping, because `../../references/` paths may not resolve in single-skill Claude.ai uploads.
   - **Cursor / Windsurf:** copy this pack into the project or workspace location your agent reads for skills; keep `skills/` and `references/` together at the same root.
   - **ChatGPT:** connect `https://mcp.firsttouch.ai` as an MCP connector. ChatGPT does not consume the skills folder directly; use the README/skill text as operating prompts if needed.
3. Connect **FirstTouch MCP**. Connect **HubSpot MCP** only for HubSpot-specific plays. See `references/mcp-setup.md`.
4. Complete first-run onboarding before choosing a play.

## Safety
- The agent never sends a message or publishes a flow without showing it in chat and getting an explicit yes. FirstTouch also offers an optional in-product human-in-the-loop layer (off by default) that pauses sends as approval tasks in the FirstTouch app under Tasks or in HubSpot - enable it on send actions for any flow that keeps enrolling contacts after the chat ends.
- Dynamic outbound and AI SDR require row-level approval. Approval tasks have no automatic escalation or SLA; checking the pending-approval queue is part of the routine. Social campaigns support two modes: rep/BDR one-at-a-time dynamic rows use row-level approval; one-time static campaign flows can use flow-level approval only after the exact audience, templates, sender routing, launch window, and daily cap are approved.
- Publishing a flow activates it but does **not** enroll awaiting contacts. After approval, explicitly enroll the approved contacts/items, then confirm they moved from awaiting to in-progress.
- Built around FirstTouch-supported limits and safer recommendations: recommend 10/day free/basic or 20/day Sales Navigator/Premium connection requests; never exceed 20/day free/basic or 30/day Sales Navigator/Premium. When possible, inspect current queue/usage before adding more connection-request rows, rather than relying on estimates.
- See `references/safety-governance.md`.
