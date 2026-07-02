# FirstTouch BDR Pack

*Pack version 1.4.1*

> Inbox busywork and slow follow-up make you miss the inbound window and look bad to your AE: these are the plays for the job you actually do.

## Who this is for
Your job is meetings. You live in the gap between marketing handing over a lead and sales getting a discovery call on the calendar. Every delay in follow-up, every manual step, every no-show not chased: that's a meeting you didn't book. These plays close that gap: fast inbound response, warm-signal conversion, and lead recovery without the grind.

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
Use this source-based chooser:

| What you have today | Run first | Why |
|---|---|---|
| No source/list yet | **BDR AI SDR** (`icp-outbound-builder`) | Daily approval engine from ICP + Discover Contacts |
| No-show, event, old-MQL, or HubSpot list | **Scoop-up slipped leads** | Lead recovery from a provided source |
| Connected inbound feed or imported signup/demo list | **Auto-connect on meeting or signup** | Same-day inbound follow-up |
| Leadership/competitor post engagement | **Social engager flow** | Work warm engagers before they go cold |
| RB2B/HubSpot visitor source | **Website visitor play** | Conditional; most BDRs skip if no visitor source exists |
| HubSpot MCP + tasks already created for LinkedIn/social steps | **Automate due HubSpot social tasks** | Secondary task runner for tasks due today in the user/owner queue; not a prospecting engine |

**Daily engine means approval queue, not autosend:** the agent discovers, enriches, drafts, and queues rows; every first-touch row still requires individual BDR approval before sending. Use **Social campaigns** only for manager-approved special pushes, not normal daily work.

## Your week
- **Every morning (15 min):** approve your BDR AI SDR batch - that is the daily engine.
- **Midweek:** work warm engagers from leadership or competitor posts.
- **Friday:** sweep no-shows and slipped inbound leads, queue recovery touches, and run "Show your manager the numbers" (`team-performance-report`) so your manager sees the week.

## Quickstart play cards
Use the source-based chooser above as the quickstart. The recipe table below has execution details; Social campaigns are only the manager-approved special-push mode, not daily prospecting.

## How to use this pack
- **Recipes** are the best starting point. They combine the right skills into the job you actually want done.
- **Skills** are the individual building blocks. Run a skill directly only when you know the exact motion you want.
- **Read once:** `references/system-grounding.md` explains how agents, FirstTouch, HubSpot, approvals, and measurement fit together.
- **FirstTouch terms:** a campaign/sequence/social campaign in this pack becomes a FirstTouch audience, flow plan, dynamic action, or enrollment depending on the play. "AI SDR" in this pack maps to `icp-outbound-builder`. The agent should use FirstTouch's available execution objects and state the exact object it created.
- **Approval locations:** before assuming approval tasks are enabled, ask the user or check available FirstTouch task/workspace settings. If approval tasks are enabled, route them to the owner in HubSpot or the FirstTouch app under **Tasks**. If that workflow is not enabled or cannot be confirmed, present the table in chat and wait for explicit approval.

## HubSpot reality check
- **What works without HubSpot:** BDR AI SDR from FirstTouch Discover Contacts, social engager flow from leadership/competitor/influencer profiles, and special social campaigns from imported/Discover lists. Inbound speed-to-lead needs HubSpot or a FirstTouch-accessible inbound source.
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
| hubspot-social-task-runner | Find HubSpot CRM tasks due today in the user/owner queue that already represent LinkedIn/social steps, such as connect, message, or follow-up, then execute the approved social action through FirstTouch and mark the HubSpot task complete only after the action is queued or sent. | HubSpot MCP required; use only when LinkedIn/social tasks already exist daily | `hubspot-social-task-runner` |
| social-campaigns | "Build a ONE-TIME (not recurring) LinkedIn social campaign for a very narrow ICP segment: define precise audience criteria, source/enrich contacts from FirstTouch and optional HubSpot lists, then choose either row-level dynamic actions for rep/BDR one-at-a-time execution or static flow templates for RevOps/founder-approved one-time campaigns. | No HubSpot for pure ICP/imported/connection-list campaigns; HubSpot required for CRM/deal/customer segments | `social-campaigns` |
| campaign-pause-and-fix | Pause a live FirstTouch campaign/flow mid-send, diagnose what is wrong, cancel or hold the affected enrollments, fix the messaging or audience, and safely restart with re-enrollment - without duplicate sends. | No HubSpot required; works on any running FirstTouch flow | `campaign-pause-and-fix` |
| team-performance-report | Pull FirstTouch team metrics for a selected date range, flow, sender, or campaign cohort, then summarize sends, replies, reply sentiment where available, meetings booked, opportunities, and HubSpot logging coverage. | No HubSpot required for FirstTouch team metrics; HubSpot improves opportunity/pipeline reconciliation | `team-performance-report` |

### Support skills (called by plays)
| Skill | What it does | Needs / HubSpot status | Runs |
|---|---|---|---|
| firsttouch-messaging | Write on-brand, high-converting LinkedIn outreach messages - connection requests, openers, follow-ups, and meeting asks - calibrated to the prospect's seniority and a real signal. | No HubSpot required | `firsttouch-messaging` |

### Recipes (recommended starting points)
#### Inbound / source-gated plays
| Play | What it does | Needs | Composes from |
|---|---|---|---|
| Auto-connect on meeting or signup | Inbound only: when a meeting/signup source is already connected or imported, prepare same-day LinkedIn drafts for approval. If no inbound source exists, use BDR AI SDR instead. | HubSpot or FirstTouch-accessible inbound list/import required | `inbound-speed-to-lead` + `firsttouch-messaging` |
| Website visitor play | Conditional, most BDRs skip unless RB2B/HubSpot tracking or a visitor list exists: turn pricing/demo/product-page visits into LinkedIn touches while intent is active. | Conditional; HubSpot tracking, RB2B/list source, or visitor export required; most BDRs skip if no source exists | `website-visitor-followup` |
#### CRM social task automation: only if tasks already exist
| Play | What it does | Needs | Composes from |
|---|---|---|---|
| Automate due HubSpot social tasks | Work today's existing HubSpot LinkedIn/social tasks in the BDR/user queue: connect, message, or follow up through FirstTouch, then mark tasks complete only after queue/send confirmation. | HubSpot MCP required; use only if HubSpot tasks for social steps are already being created each day; not a cadence/list creator or prospecting engine | `hubspot-social-task-runner` |
#### Daily engine
| Play | What it does | Needs | Composes from |
|---|---|---|---|
| BDR AI SDR - daily approval queue | Daily engine: discover or load ICP-fit prospects, enrich each prospect, and draft connection-request rows up to the recommended 10/day free/basic or 20/day Sales Nav/Premium connection-request cap for approval. Already-connected message rows use the separate message cap. | No HubSpot required with ICP brief + FirstTouch Discover Contacts; HubSpot list optional | `icp-outbound-builder` + `firsttouch-messaging` |
#### Warm social signals
| Play | What it does | Needs | Composes from |
|---|---|---|---|
| Social engager flow - leadership posts | Social Engagement can be enabled through FirstTouch MCP; Convert engagement on CEO/exec/leadership posts into booked meetings before interest fades. | Social Engagement can be enabled through FirstTouch MCP; No HubSpot required; use leadership, competitor founder, or influencer profile engagement; HubSpot optional for qualification/routing; profile views unavailable | `warm-engager-followup` + `firsttouch-messaging` |
#### Manager-approved special pushes
| Play | What it does | Needs | Composes from |
|---|---|---|---|
| Social campaigns - special row-level push | Build a manager-approved narrow BDR push such as tradeshow-city buyers, no-shows from a provided event/HubSpot list, or connected leadership titles. Default to AI-SDR-like row-level dynamic approvals, not self-serve flow building. | No HubSpot required for Discover Contacts or imported/event lists; HubSpot required for no-show or CRM-history segments; row-level approval by default; manager/RevOps approval recommended | `social-campaigns` + `firsttouch-messaging` |
#### Lead recovery
| Play | What it does | Needs | Composes from |
|---|---|---|---|
| Scoop-up slipped leads - HubSpot no-shows and old MQLs | Lead recovery: work no-shows and old MQLs from a HubSpot/event list or RevOps-supplied HubSpot property. If no HubSpot/event source exists, use the imported recovery-list recipe or BDR AI SDR instead. | HubSpot/event list or RevOps-supplied HubSpot property required | `hubspot-signal-to-linkedin-touch` + `firsttouch-messaging` |
| Scoop-up slipped leads - imported recovery list | Lead recovery from an imported no-show, event, old-MQL, or dormant-lead CSV/list: enrich the provided people, draft recovery touches, and gate each row for approval. If no recovery source exists, use BDR AI SDR instead. | Imported event/no-show/recovery list required; no HubSpot required when source rows include enough identity data | `icp-outbound-builder` + `firsttouch-messaging` |
#### Requires inbound, HubSpot, or external source
| Play | What it does | Needs | Composes from |
|---|---|---|---|
| Show your manager the numbers | Weekly one-pager for your manager: connection requests sent, accepts, replies, meetings booked, by day | FirstTouch only; HubSpot improves meeting/opportunity reconciliation | `team-performance-report` |

### How to run each recipe

**Auto-connect on meeting or signup**
1. Pull the day's booked meetings/signups (HubSpot event or your inbound list) with `inbound-speed-to-lead`. 2. Load `firsttouch-messaging` and draft a blank connection request plus a short post-accept opener per contact. 3. Approve the table; the agent queues the requests and appends openers to the connection_accepted branch.

**Automate due HubSpot social tasks**
1. `hubspot-social-task-runner` pulls today's due LinkedIn/social tasks from HubSpot. 2. Review the approval table (task, contact, intended action, copy source). 3. Approve; the agent executes via FirstTouch and marks each task complete only after the action is queued or sent.

**BDR AI SDR - daily approval queue**
1. Pick the source: a HubSpot list or your ICP + FirstTouch Discover Contacts. 2. `icp-outbound-builder` enriches each prospect and drafts the daily batch. 3. Approve rows each morning; the agent queues sends and logs touches.

**Social engager flow - leadership posts**
1. Confirm Social Engagement is enabled for the monitored profile (`warm-engager-followup`, step 1). 2. Pull the week's engagers and keep the ICP fits. 3. Draft signal-based openers with `firsttouch-messaging`, approve, queue.

**Website visitor play**
1. Confirm a visitor source exists (HubSpot tracking or an RB2B/list source); stop if none. 2. `website-visitor-followup` qualifies visitors and picks a contact-level or account-level motion. 3. Draft soft, non-creepy touches, approve, queue.

**Social campaigns - special row-level push**
1. Define the narrow segment (25-100 people); manager approves the push. 2. `social-campaigns` builds the audience and drafts row-level actions. 3. Approve each row, queue inside your daily cap.

**Scoop-up slipped leads - HubSpot no-shows and old MQLs**
1. Build or request the recovery list (no-shows, old MQLs) in HubSpot. 2. `hubspot-signal-to-linkedin-touch` qualifies and drafts low-pressure re-openers. 3. Approve, queue, and put non-responders on cooldown.

**Scoop-up slipped leads - imported recovery list**
1. Import the recovery list so FirstTouch can read it. 2. `icp-outbound-builder` enriches and drafts low-pressure re-openers. 3. Approve, queue, and put non-responders on cooldown.

**Show your manager the numbers**
1. Friday: run `team-performance-report` scoped to your sender seat for the trailing 7 days. 2. Keep it honest: sends, accepts, replies, meetings booked; mark anything unverifiable as unverified. 3. Paste the summary table to your manager - same format every week so trends show.

## Example prompts
- "Run the FirstTouch AI SDR play for today: discover ICP-fit prospects, enrich them, and show me an approval table up to my daily connection cap. Do not send until I approve."
- "Build today's LinkedIn outbound batch from this ICP and gate every row for approval."
- "Find people who engaged with our leadership profile this week and draft connection requests for my approval."
- "Build a manager-approved LinkedIn push for no-shows from this event list and gate every row for approval."
- "If HubSpot already creates LinkedIn/social tasks daily, find today's due tasks and run the eligible ones through FirstTouch."

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
