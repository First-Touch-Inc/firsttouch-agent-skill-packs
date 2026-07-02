# First-Run Onboarding - BDR Pack

This onboarding is scoped to the skills and recipes actually included in this installed pack.

## Ask before running anything
1. **LinkedIn account type:** free/basic or Sales Navigator/Premium.
   - Free/basic: no connection notes; recommend 10 connection requests/day; FirstTouch max 20/day.
   - Sales Navigator/Premium: connection notes available for approved warm signals; recommend 20 connection requests/day; FirstTouch max 30/day.
   - AI SDR and all other connection-request plays share the same daily budget.
   - If AI SDR and a social campaign run on the same sender/day, pause/reduce one motion or split the recommended daily cap explicitly before queueing sends; never exceed the FirstTouch max.
   - Already-connected LinkedIn message rows use a separate FirstTouch-supported message cap: 20/day on free/basic LinkedIn and 30/day on Sales Navigator/Premium. Reduce volume if acceptance or reply quality drops.
   - FirstTouch enforces these limits automatically - you can adjust volume anytime in the FirstTouch app, and you can never go over the peak limits. If a seat hits its daily limit it simply goes on cooldown until the next window.
2. **HubSpot access:** MCP connected by an admin, service key/private app token from an admin, HubSpot list only, or none. Getting access is easy: ask an admin to approve HubSpot MCP access (a quick approval - the preferred path) or, as a fallback, to issue a **read-only service key** that lets the agent read deals, contacts, and companies with no write risk. Do not ask a rep/BDR to mint credentials they do not own.
3. **ICP/list/source data:** if HubSpot is absent, ask for ICP criteria or an imported/FirstTouch-accessible list before qualifying prospects.
4. **Persona start point:** recommend the persona-specific start point below, not a generic catalog dump.

## Persona start point
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

- Social engagement / warm engager flows are delivered by `warm-engager-followup`. They use LinkedIn post likes and comments from Social Engagement monitoring; if Social Engagement is not enabled, enable it through FirstTouch MCP for the monitored profile when permissions allow, or use a user-provided/exported engager list. Profile-view capture is not treated as MCP-native.

## Quickstart play cards
Use the source-based chooser above as the quickstart. The recipe table below has execution details; Social campaigns are only the manager-approved special-push mode, not daily prospecting.

## Available recipes in this pack
#### Inbound / source-gated plays
| Recipe | What it does | Needs |
|---|---|---|
| Auto-connect on meeting or signup | Inbound only: when a meeting/signup source is already connected or imported, prepare same-day LinkedIn drafts for approval. If no inbound source exists, use BDR AI SDR instead. | HubSpot or FirstTouch-accessible inbound list/import required |
| Website visitor play | Conditional, most BDRs skip unless RB2B/HubSpot tracking or a visitor list exists: turn pricing/demo/product-page visits into LinkedIn touches while intent is active. | Conditional; HubSpot tracking, RB2B/list source, or visitor export required; most BDRs skip if no source exists |
#### CRM social task automation: only if tasks already exist
| Recipe | What it does | Needs |
|---|---|---|
| Automate due HubSpot social tasks | Work today's existing HubSpot LinkedIn/social tasks in the BDR/user queue: connect, message, or follow up through FirstTouch, then mark tasks complete only after queue/send confirmation. | HubSpot MCP required; use only if HubSpot tasks for social steps are already being created each day; not a cadence/list creator or prospecting engine |
#### Daily engine
| Recipe | What it does | Needs |
|---|---|---|
| BDR AI SDR - daily approval queue | Daily engine: discover or load ICP-fit prospects, enrich each prospect, and draft connection-request rows up to the recommended 10/day free/basic or 20/day Sales Nav/Premium connection-request cap for approval. Already-connected message rows use the separate message cap. | No HubSpot required with ICP brief + FirstTouch Discover Contacts; HubSpot list optional |
#### Warm social signals
| Recipe | What it does | Needs |
|---|---|---|
| Social engager flow - leadership posts | Social Engagement can be enabled through FirstTouch MCP; Convert engagement on CEO/exec/leadership posts into booked meetings before interest fades. | Social Engagement can be enabled through FirstTouch MCP; No HubSpot required; use leadership, competitor founder, or influencer profile engagement; HubSpot optional for qualification/routing; profile views unavailable |
#### Manager-approved special pushes
| Recipe | What it does | Needs |
|---|---|---|
| Social campaigns - special row-level push | Build a manager-approved narrow BDR push such as tradeshow-city buyers, no-shows from a provided event/HubSpot list, or connected leadership titles. Default to AI-SDR-like row-level dynamic approvals, not self-serve flow building. | No HubSpot required for Discover Contacts or imported/event lists; HubSpot required for no-show or CRM-history segments; row-level approval by default; manager/RevOps approval recommended |
#### Lead recovery
| Recipe | What it does | Needs |
|---|---|---|
| Scoop-up slipped leads - HubSpot no-shows and old MQLs | Lead recovery: work no-shows and old MQLs from a HubSpot/event list or RevOps-supplied HubSpot property. If no HubSpot/event source exists, use the imported recovery-list recipe or BDR AI SDR instead. | HubSpot/event list or RevOps-supplied HubSpot property required |
| Scoop-up slipped leads - imported recovery list | Lead recovery from an imported no-show, event, old-MQL, or dormant-lead CSV/list: enrich the provided people, draft recovery touches, and gate each row for approval. If no recovery source exists, use BDR AI SDR instead. | Imported event/no-show/recovery list required; no HubSpot required when source rows include enough identity data |
#### Requires inbound, HubSpot, or external source
| Recipe | What it does | Needs |
|---|---|---|
| Show your manager the numbers | Weekly one-pager for your manager: connection requests sent, accepts, replies, meetings booked, by day | FirstTouch only; HubSpot improves meeting/opportunity reconciliation |

## Included skills and dependency status
| Skill | Needs |
|---|---|
| `firsttouch-messaging` | No HubSpot required |
| `inbound-speed-to-lead` | HubSpot or FirstTouch-accessible inbound list/import required; true automation needs a connected source |
| `warm-engager-followup` | No HubSpot required; enable Social Engagement through FirstTouch MCP for monitored profiles; user-provided/exported engager lists also work |
| `website-visitor-followup` | HubSpot tracking or RB2B/list source required |
| `icp-outbound-builder` | No HubSpot required with ICP brief + FirstTouch Discover Contacts; HubSpot list optional |
| `hubspot-signal-to-linkedin-touch` | HubSpot required |
| `hubspot-social-task-runner` | HubSpot MCP required; use only when LinkedIn/social tasks already exist daily |
| `social-campaigns` | No HubSpot for pure ICP/imported/connection-list campaigns; HubSpot required for CRM/deal/customer segments |
| `campaign-pause-and-fix` | No HubSpot required; works on any running FirstTouch flow |
| `team-performance-report` | No HubSpot required for FirstTouch team metrics; HubSpot improves opportunity/pipeline reconciliation |

## HubSpot access rules for this pack
- If HubSpot is connected, HubSpot-specific recipes can read CRM context, owner, lifecycle/deal/list data, and log back where the connected FirstTouch-HubSpot integration supports it.
- If HubSpot is used but no MCP/key is connected, ask for a HubSpot list or other FirstTouch-accessible source before running HubSpot-dependent motions.
- If HubSpot is not used, run only the recipes above whose Needs column says no HubSpot or imported/Discover/list source is enough.

## Social Engagement source options
Social Engagement can be enabled through FirstTouch MCP and can monitor relevant LinkedIn profiles for post likes and comments. Prefer the user's own founder/leadership personal profile when available; if they do not have enough owned engagement yet, monitor a relevant competitor founder, category influencer, or executive profile and work the ICP-fit people engaging there. Profile views are not an available signal.

## Approval model
Approval always happens in chat first: the agent shows the exact draft and waits for a yes. FirstTouch's optional in-product human-in-the-loop layer (off by default) additionally pauses sends as approval tasks in the FirstTouch app under **Tasks** or in HubSpot. Approval tasks have **no automatic escalation or SLA** - if one sits unactioned, following up is manual, so recurring plays should check the pending-approval queue as part of the routine.

Publishing a flow activates it but does **not** enroll awaiting contacts. After approval, explicitly enroll the approved contacts/items, then confirm they moved from awaiting to in-progress.

| Motion | Approval style |
|---|---|
| AI SDR / dynamic actions | Row-level approval. Each first-touch row must be approved individually; if approval tasks are confirmed enabled, route them to the owner in HubSpot or the FirstTouch app under **Tasks**. |
| Warm engager, inbound, website visitor, HubSpot signal, customer/stalled deal | Row-level approval unless FirstTouch records an equivalent per-contact approval; approval tasks route to the owner in HubSpot or app **Tasks** when enabled. |
| Social campaigns | Two modes: rep/BDR dynamic rows use row-level approval like AI SDR; RevOps/founder one-time static campaigns can use flow-level approval after exact audience, templates, sender/routing rule, launch window, and daily cap are approved. |

## Trial-window expectation
FirstTouch trials run **two weeks**. Sequence the rollout so the user sees real results inside that window: high-intent plays in the first days (they convert fastest), outbound added once warm motions are running. Do not quote benchmark accept/reply/meeting rates - FirstTouch does not publish them. Instead, measure the user's own numbers with the team-metrics tools and compare week 1 to week 2.

## Onboarding output format
```markdown
## FirstTouch onboarding summary
- Persona: bdr
- LinkedIn account: Free/basic or Sales Navigator/Premium
- Daily connection cap: recommended 10/day free/basic or 20/day Sales Nav/Premium; FirstTouch max 20/day free/basic or 30/day Sales Nav/Premium
- Daily message cap: 20/day free/basic or 30/day Sales Nav/Premium
- HubSpot access: MCP / service key / list only / none
- Social Engagement enabled: yes/no/unknown
- ICP/list available if no HubSpot: yes/no + source
- Plays available now from this pack: ...
- Plays blocked until HubSpot access/list or source data exists: ...
- Recommended first play: ...
- Approval workflow: row-level for dynamic plays; confirm whether approval tasks are enabled before routing to the owner in HubSpot or FirstTouch app Tasks; flow-level only for approved one-time social campaigns
```
