# Recipe Catalog - BDR Pack

Use this file when the agent installed `skills/` and `references/` without loading the root README. These recipes are the recommended starting points for the bdr persona.

## Recommended start point
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

## Quickstart play cards
Use the source-based chooser above as the quickstart. The recipe table below has execution details; Social campaigns are only the manager-approved special-push mode, not daily prospecting.

## Recipes
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

## Approval reminder
Dynamic/AI SDR rows require row-level approval. Static social-campaign flows can use flow-level approval only after the exact audience, static templates, sender/routing rule, launch window, and daily cap are approved.
