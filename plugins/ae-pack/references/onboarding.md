# First-Run Onboarding - AE Pack

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
1. **Meeting booked / signup source:** run **Auto-connect on meeting or signup** first for fresh booked meetings, signups, or a manually exported meeting-booked list.
2. **HubSpot + stakeholder expansion:** run **Meeting-booked stakeholder follow-up** when a booked-meeting source/list is available and the AE wants to multi-thread the account. It can run from the same booked-meeting source as auto-connect because it targets other stakeholders, not duplicate outreach to the booked contact.
3. **Warm LinkedIn engagers:** run **Social engager flow - leadership's audience** when prospects engage with leadership, competitor, or influencer personal-profile posts.
4. **No HubSpot/list access:** run **AE AI SDR** from ICP + Discover Contacts; this cannot touch existing pipeline without HubSpot or a FirstTouch-accessible contact list.
5. **HubSpot + quiet pipeline:** run **Stalled deal reactivation** from a manually filtered HubSpot list of open deals with no engagement for 60+ days. If a deal only went quiet this week, use HubSpot signal/meeting-trigger follow-up; sub-60-day quiet-deal detection is not a native FirstTouch query.
6. **HubSpot MCP + tasks already created for LinkedIn/social steps:** run **Automate due HubSpot social tasks** as a secondary task runner for tasks due today, not as a cadence/list creator.

- Social engagement / warm engager flows are delivered by `warm-engager-followup`. They use LinkedIn post likes and comments from Social Engagement monitoring; if Social Engagement is not enabled, enable it through FirstTouch MCP for the monitored profile when permissions allow, or use a user-provided/exported engager list. Profile-view capture is not treated as MCP-native.

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

## Available recipes in this pack
#### HubSpot-connected deal and inbound plays
| Recipe | What it does | Needs |
|---|---|---|
| Auto-connect on meeting or signup | Draft a same-day LinkedIn touch for approval when prospects book or submit. An AE can run this once today from a HubSpot/exported inbound contact list; recurring automation needs a connected source or RevOps workflow. This can run alongside Meeting-booked stakeholder follow-up because it targets the booked contact. | HubSpot or FirstTouch-accessible inbound list/import required; AE can run once from a manual list; RevOps needed only for recurring automation |
| Social campaigns - territory and deal expansion | Build a narrow AE push for a territory, event, customer expansion, or stalled-pipeline segment. Default to row-level dynamic approvals like AI SDR; use static flow-level approval only when RevOps/founder approves the exact audience and templates. | No HubSpot required for pure ICP/imported/Discover segments; HubSpot required for territory/deal/customer CRM segments; row-level approval by default |
| Stalled deal reactivation - 60-day open-deal workflow | From a HubSpot list/workflow of open deals that are not Closed Won/Lost and have had no engagement for 60+ days, build an owner-approved LinkedIn reactivation queue. Treat recurring workflow setup as a RevOps/admin step unless already configured; sub-60-day quiet-deal detection is not a native FirstTouch query. | HubSpot required; an AE with HubSpot access can run once from a manually built/filtered contact list; RevOps/admin needed only for recurring workflow setup |
| Meeting-booked stakeholder follow-up | Draft stakeholder LinkedIn touches from a meeting-booked contact list/source so the deal is not single-threaded. This can run from the same booked-meeting source as Auto-connect because it targets other stakeholders, not duplicate outreach to the booked contact. An AE can run this once today from a manually filtered HubSpot list; RevOps is needed only for recurring setup. | HubSpot required; AE can run once from a manually built meeting-booked contact list/source; RevOps needed only for recurring workflow setup |
| Closed-lost reengagement | Re-engage historical closed-lost accounts from a HubSpot Closed Lost contact list with a fresh, approved LinkedIn touch and a separate win-back angle; keep this separate from stalled open-deal reactivation. | HubSpot required; run from a Closed Lost contact list; separate from stalled open-deal workflow |
#### CRM social task automation: only if tasks already exist
| Recipe | What it does | Needs |
|---|---|---|
| Automate due HubSpot social tasks | Find HubSpot tasks due today in the AE/user queue that already represent LinkedIn connect/message/social follow-up steps, execute eligible ones through FirstTouch, and mark the CRM tasks complete after queue/send confirmation. | HubSpot MCP required; use only if HubSpot tasks for social steps are already being created each day; not a cadence/list creator or prospecting engine |
#### No-HubSpot / self-serve starts
| Recipe | What it does | Needs |
|---|---|---|
| Social engager flow - leadership's audience | Social Engagement can be enabled through FirstTouch MCP; Reach people engaging with leadership/executive personal-profile content before they go cold. | Social Engagement can be enabled through FirstTouch MCP; No HubSpot required; use leadership/executive personal-profile, competitor founder, or influencer personal-profile engagement; HubSpot optional for qualification/routing; profile views unavailable |
| AE AI SDR - daily approval queue | View a HubSpot contact/company list or discover a new ICP list, enrich each prospect, and draft up to the recommended 10/day free/basic or 20/day Sales Nav/Premium AE-owned LinkedIn touches for approval. | No HubSpot required with ICP brief + FirstTouch Discover Contacts; HubSpot list optional |
| New-customer referral thank-you | After an AE-owned deal becomes a new customer, connect, thank them for choosing the product, ask what could be better, and add a light network-value/referral line after row-level approval. | HubSpot Closed Won/customer source or imported/FirstTouch-accessible customer list required; HubSpot improves owner/CSM routing and logging |
| Post-demo follow-up | Same-day buyer follow-up, champion thank-you, stakeholder expansion, and a 3-day momentum touch drafted from the real meeting | HubSpot recommended for meeting/deal context; works from your meeting notes without it |
| Champion job change | Turn a champion's move into a warm path at the new company and a protected relationship at the old account | No HubSpot required for outreach; HubSpot recommended for CRM updates. Reacts to a known move - FirstTouch does not monitor job changes |
#### Intent source required: HubSpot tracking, RB2B, or list/import
| Recipe | What it does | Needs |
|---|---|---|
| Website visitor play | Turn pricing/demo/product-page visits into LinkedIn touches while intent is active; if no visitor signal source exists, choose the AE AI SDR recipe as a separate prospecting motion instead. | HubSpot tracking or RB2B/list source required; if no visitor signal source exists, use the persona AI SDR recipe as a separate prospecting motion |

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
| `stalled-deal-reactivation` | HubSpot required; may need RevOps/admin for workflow setup |
| `customer-referral` | HubSpot Closed Won/customer source or imported/FirstTouch-accessible customer list required; HubSpot improves owner/CSM routing and logging |
| `campaign-pause-and-fix` | No HubSpot required; works on any running FirstTouch flow |
| `post-demo-followup` | HubSpot recommended for meeting/deal context; can run from user-provided meeting notes |
| `champion-job-change` | No HubSpot required for the outreach; HubSpot recommended for CRM updates and old-account context |

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
- Persona: ae
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
