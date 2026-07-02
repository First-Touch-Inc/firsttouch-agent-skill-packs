# FirstTouch AE Pack

*Pack version 1.4.1*

> Booked meetings, signups, and warm deal signals go cold when LinkedIn follow-up and stakeholder expansion happen too late: these are the plays for the job you actually do.

## Who this is for
You carry a number. Your job depends on turning fresh meetings and inbound hand-raisers into active conversations fast, then keeping quiet open opportunities from becoming no-decisions. These plays tell you what to do first when a meeting books, how to multi-thread the account, how to work warm LinkedIn engagement, and how to reactivate genuinely stalled open deals from a HubSpot list or workflow.

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
1. **Meeting booked / signup source:** run **Auto-connect on meeting or signup** first for fresh booked meetings, signups, or a manually exported meeting-booked list.
2. **HubSpot + stakeholder expansion:** run **Meeting-booked stakeholder follow-up** when a booked-meeting source/list is available and the AE wants to multi-thread the account. It can run from the same booked-meeting source as auto-connect because it targets other stakeholders, not duplicate outreach to the booked contact.
3. **Warm LinkedIn engagers:** run **Social engager flow - leadership's audience** when prospects engage with leadership, competitor, or influencer personal-profile posts.
4. **No HubSpot/list access:** run **AE AI SDR** from ICP + Discover Contacts; this cannot touch existing pipeline without HubSpot or a FirstTouch-accessible contact list.
5. **HubSpot + quiet pipeline:** run **Stalled deal reactivation** from a manually filtered HubSpot list of open deals with no engagement for 60+ days. If a deal only went quiet this week, use HubSpot signal/meeting-trigger follow-up; sub-60-day quiet-deal detection is not a native FirstTouch query.
6. **HubSpot MCP + tasks already created for LinkedIn/social steps:** run **Automate due HubSpot social tasks** as a secondary task runner for tasks due today, not as a cadence/list creator.

## Your week
- **Every morning (10 min):** approve auto-connect drafts for yesterday's booked meetings and signups.
- **Midweek:** work warm engagers from leadership posts and multi-thread your active deals.
- **Friday:** review the stalled-deal queue and approve next week's reactivation touches.

## Quickstart play cards
| Situation | Run this | What happens |
|---|---|---|
| Meeting booked | Auto-connect on meeting/signup | Connect the booked contact same day |
| Demo just happened | Post-demo follow-up | Same-day recap, thank-you, stakeholder expansion, momentum touch |
| Champion changed jobs | Champion job change | Congrats now, reconnect later, protect the old account |
| Same account has other stakeholders | Meeting-booked stakeholder follow-up | Multi-thread the account without duplicating outreach |
| Warm LinkedIn engagement | Social engager flow - leadership's audience | Work engagers from leadership / competitor / influencer posts |
| Quiet open opp | Stalled deal reactivation | One-time HubSpot list or recurring workflow |
| No warm source/list | AE AI SDR | Discover, enrich, and draft approval rows |

## How to use this pack
- **Recipes** are the best starting point. They combine the right skills into the job you actually want done.
- **Skills** are the individual building blocks. Run a skill directly only when you know the exact motion you want.
- **Read once:** `references/system-grounding.md` explains how agents, FirstTouch, HubSpot, approvals, and measurement fit together.
- **FirstTouch terms:** a campaign/sequence/social campaign in this pack becomes a FirstTouch audience, flow plan, dynamic action, or enrollment depending on the play. "AI SDR" in this pack maps to `icp-outbound-builder`. The agent should use FirstTouch's available execution objects and state the exact object it created.
- **Approval locations:** before assuming approval tasks are enabled, ask the user or check available FirstTouch task/workspace settings. If approval tasks are enabled, route them to the owner in HubSpot or the FirstTouch app under **Tasks**. If that workflow is not enabled or cannot be confirmed, present the table in chat and wait for explicit approval.

## HubSpot reality check
- **What works without HubSpot:** Auto-connect on meeting or signup when a booked-meeting/signup source exists; social engager flow from leadership/executive personal profiles, competitor founder profiles, or influencer personal profiles; plus AE AI SDR from FirstTouch Discover Contacts. Most AE deal, customer, territory, and stalled-pipeline use cases need HubSpot.
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
| stalled-deal-reactivation | Build and govern a contact-based HubSpot workflow for contacts associated to open deals that are not Closed Won and not Closed Lost and have had no engagement for 60+ days. | HubSpot required; may need RevOps/admin for workflow setup | `stalled-deal-reactivation` |
| customer-referral | Auto-prepare LinkedIn connection requests and thank-you/referral messages for new customers after they choose the product. | HubSpot Closed Won/customer source or imported/FirstTouch-accessible customer list required; HubSpot improves owner/CSM routing and logging | `customer-referral` |
| campaign-pause-and-fix | Pause a live FirstTouch campaign/flow mid-send, diagnose what is wrong, cancel or hold the affected enrollments, fix the messaging or audience, and safely restart with re-enrollment - without duplicate sends. | No HubSpot required; works on any running FirstTouch flow | `campaign-pause-and-fix` |
| post-demo-followup | Convert a completed demo or discovery call into same-day follow-up, stakeholder expansion, and momentum touches without sounding automated. | HubSpot recommended for meeting/deal context; can run from user-provided meeting notes | `post-demo-followup` |
| champion-job-change | When a champion or strong contact changes jobs, run a warm reactivation into their new company and protect the old account relationship. | No HubSpot required for the outreach; HubSpot recommended for CRM updates and old-account context | `champion-job-change` |

### Support skills (called by plays)
| Skill | What it does | Needs / HubSpot status | Runs |
|---|---|---|---|
| firsttouch-messaging | Write on-brand, high-converting LinkedIn outreach messages - connection requests, openers, follow-ups, and meeting asks - calibrated to the prospect's seniority and a real signal. | No HubSpot required | `firsttouch-messaging` |

### Recipes (recommended starting points)
#### HubSpot-connected deal and inbound plays
| Play | What it does | Needs | Composes from |
|---|---|---|---|
| Auto-connect on meeting or signup | Draft a same-day LinkedIn touch for approval when prospects book or submit. An AE can run this once today from a HubSpot/exported inbound contact list; recurring automation needs a connected source or RevOps workflow. This can run alongside Meeting-booked stakeholder follow-up because it targets the booked contact. | HubSpot or FirstTouch-accessible inbound list/import required; AE can run once from a manual list; RevOps needed only for recurring automation | `inbound-speed-to-lead` + `firsttouch-messaging` |
| Social campaigns - territory and deal expansion | Build a narrow AE push for a territory, event, customer expansion, or stalled-pipeline segment. Default to row-level dynamic approvals like AI SDR; use static flow-level approval only when RevOps/founder approves the exact audience and templates. | No HubSpot required for pure ICP/imported/Discover segments; HubSpot required for territory/deal/customer CRM segments; row-level approval by default | `social-campaigns` + `firsttouch-messaging` |
| Stalled deal reactivation - 60-day open-deal workflow | From a HubSpot list/workflow of open deals that are not Closed Won/Lost and have had no engagement for 60+ days, build an owner-approved LinkedIn reactivation queue. Treat recurring workflow setup as a RevOps/admin step unless already configured; sub-60-day quiet-deal detection is not a native FirstTouch query. | HubSpot required; an AE with HubSpot access can run once from a manually built/filtered contact list; RevOps/admin needed only for recurring workflow setup | `stalled-deal-reactivation` + `firsttouch-messaging` |
| Meeting-booked stakeholder follow-up | Draft stakeholder LinkedIn touches from a meeting-booked contact list/source so the deal is not single-threaded. This can run from the same booked-meeting source as Auto-connect because it targets other stakeholders, not duplicate outreach to the booked contact. An AE can run this once today from a manually filtered HubSpot list; RevOps is needed only for recurring setup. | HubSpot required; AE can run once from a manually built meeting-booked contact list/source; RevOps needed only for recurring workflow setup | `hubspot-signal-to-linkedin-touch` + `firsttouch-messaging` |
| Closed-lost reengagement | Re-engage historical closed-lost accounts from a HubSpot Closed Lost contact list with a fresh, approved LinkedIn touch and a separate win-back angle; keep this separate from stalled open-deal reactivation. | HubSpot required; run from a Closed Lost contact list; separate from stalled open-deal workflow | `hubspot-signal-to-linkedin-touch` + `icp-outbound-builder` + `firsttouch-messaging` |
#### CRM social task automation: only if tasks already exist
| Play | What it does | Needs | Composes from |
|---|---|---|---|
| Automate due HubSpot social tasks | Find HubSpot tasks due today in the AE/user queue that already represent LinkedIn connect/message/social follow-up steps, execute eligible ones through FirstTouch, and mark the CRM tasks complete after queue/send confirmation. | HubSpot MCP required; use only if HubSpot tasks for social steps are already being created each day; not a cadence/list creator or prospecting engine | `hubspot-social-task-runner` |
#### No-HubSpot / self-serve starts
| Play | What it does | Needs | Composes from |
|---|---|---|---|
| Social engager flow - leadership's audience | Social Engagement can be enabled through FirstTouch MCP; Reach people engaging with leadership/executive personal-profile content before they go cold. | Social Engagement can be enabled through FirstTouch MCP; No HubSpot required; use leadership/executive personal-profile, competitor founder, or influencer personal-profile engagement; HubSpot optional for qualification/routing; profile views unavailable | `warm-engager-followup` + `firsttouch-messaging` |
| AE AI SDR - daily approval queue | View a HubSpot contact/company list or discover a new ICP list, enrich each prospect, and draft up to the recommended 10/day free/basic or 20/day Sales Nav/Premium AE-owned LinkedIn touches for approval. | No HubSpot required with ICP brief + FirstTouch Discover Contacts; HubSpot list optional | `icp-outbound-builder` + `firsttouch-messaging` |
| New-customer referral thank-you | After an AE-owned deal becomes a new customer, connect, thank them for choosing the product, ask what could be better, and add a light network-value/referral line after row-level approval. | HubSpot Closed Won/customer source or imported/FirstTouch-accessible customer list required; HubSpot improves owner/CSM routing and logging | `customer-referral` + `firsttouch-messaging` |
| Post-demo follow-up | Same-day buyer follow-up, champion thank-you, stakeholder expansion, and a 3-day momentum touch drafted from the real meeting | HubSpot recommended for meeting/deal context; works from your meeting notes without it | `post-demo-followup` + `firsttouch-messaging` |
| Champion job change | Turn a champion's move into a warm path at the new company and a protected relationship at the old account | No HubSpot required for outreach; HubSpot recommended for CRM updates. Reacts to a known move - FirstTouch does not monitor job changes | `champion-job-change` + `firsttouch-messaging` |
#### Intent source required: HubSpot tracking, RB2B, or list/import
| Play | What it does | Needs | Composes from |
|---|---|---|---|
| Website visitor play | Turn pricing/demo/product-page visits into LinkedIn touches while intent is active; if no visitor signal source exists, choose the AE AI SDR recipe as a separate prospecting motion instead. | HubSpot tracking or RB2B/list source required; if no visitor signal source exists, use the persona AI SDR recipe as a separate prospecting motion | `website-visitor-followup` |

### How to run each recipe

**Auto-connect on meeting or signup**
1. Pull the day's booked meetings/signups (HubSpot event or your inbound list) with `inbound-speed-to-lead`. 2. Load `firsttouch-messaging` and draft a blank connection request plus a short post-accept opener per contact. 3. Approve the table; the agent queues the requests and appends openers to the connection_accepted branch.

**Automate due HubSpot social tasks**
1. `hubspot-social-task-runner` pulls today's due LinkedIn/social tasks from HubSpot. 2. Review the approval table (task, contact, intended action, copy source). 3. Approve; the agent executes via FirstTouch and marks each task complete only after the action is queued or sent.

**Social engager flow - leadership's audience**
1. Confirm Social Engagement is enabled for the monitored profile (`warm-engager-followup`, step 1). 2. Pull the week's engagers and keep the ICP fits. 3. Draft signal-based openers with `firsttouch-messaging`, approve, queue.

**Website visitor play**
1. Confirm a visitor source exists (HubSpot tracking or an RB2B/list source); stop if none. 2. `website-visitor-followup` qualifies visitors and picks a contact-level or account-level motion. 3. Draft soft, non-creepy touches, approve, queue.

**AE AI SDR - daily approval queue**
1. Pick the source: a HubSpot list or your ICP + FirstTouch Discover Contacts. 2. `icp-outbound-builder` enriches each prospect and drafts the daily batch. 3. Approve rows each morning; the agent queues sends and logs touches.

**Social campaigns - territory and deal expansion**
1. Define the narrow segment (25-100 people) and pick the mode: dynamic rows (rep-run) or a one-time static flow. 2. `social-campaigns` builds the audience and drafts with `firsttouch-messaging`. 3. Approve (row-level or flow-level), enroll explicitly, monitor.

**Stalled deal reactivation - 60-day open-deal workflow**
1. Get or self-build the HubSpot list of open-deal contacts quiet for 60+ days (the skill includes the exact filter recipe). 2. `stalled-deal-reactivation` qualifies and drafts value-first touches - never 'just checking in'. 3. Owner approves, queue, log to the deal.

**New-customer referral thank-you**
1. Pull the Closed Won/customer list. 2. `customer-referral` checks connection state and drafts a thank-you plus light referral ask (both connected and unconnected paths). 3. The account owner approves, then queue.

**Meeting-booked stakeholder follow-up**
1. Trigger on the booked-meeting event via `hubspot-signal-to-linkedin-touch`. 2. Identify 1-2 additional stakeholders at the account - not the person who booked. 3. Draft intro touches with `firsttouch-messaging`, approve, queue.

**Closed-lost reengagement**
1. Pull the HubSpot Closed Lost contact list (keep it separate from stalled open deals). 2. Use `hubspot-signal-to-linkedin-touch` for known contacts and `icp-outbound-builder` to find new stakeholders at those accounts. 3. Draft a win-back angle that references what changed since the loss, approve, queue.

**Post-demo follow-up**
1. Right after the demo, give the agent the meeting context (or let it pull from HubSpot): attendees, resonant pains, promises, next step. 2. Review the drafted set - recap, thank-you, 1-2 stakeholder intros, momentum touch. 3. Approve per row; the momentum touch only sends if the thread goes quiet.

**Champion job change**
1. Confirm the move (enrich_contact if unsure). 2. Approve the no-pitch congratulations now and the reconnect note queued 3-4 weeks out. 3. Send the continuity touch to the old account's remaining stakeholders and update HubSpot.

## Example prompts
- "A meeting was just booked at Acme. Auto-connect with the booked contact on LinkedIn today and draft the same-day follow-up for my approval."
- "I just booked a meeting at Acme. Draft LinkedIn touches to the other stakeholders so the deal is not single-threaded."
- "From this HubSpot list of open deals with no engagement in 60+ days, draft owner-approved LinkedIn reactivations; do not try to infer the cohort without the list."
- "If HubSpot already creates LinkedIn/social tasks daily, find today's due tasks and run the eligible ones through FirstTouch."
- "A new customer just closed from my territory. Connect with the champion on LinkedIn and draft a thank-you, product-feedback, and light referral note for my approval."

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
