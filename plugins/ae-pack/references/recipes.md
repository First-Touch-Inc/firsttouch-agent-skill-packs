# Recipe Catalog - AE Pack

Use this file when the agent installed `skills/` and `references/` without loading the root README. These recipes are the recommended starting points for the ae persona.

## Recommended start point
1. **Meeting booked / signup source:** run **Auto-connect on meeting or signup** first for fresh booked meetings, signups, or a manually exported meeting-booked list.
2. **HubSpot + stakeholder expansion:** run **Meeting-booked stakeholder follow-up** when a booked-meeting source/list is available and the AE wants to multi-thread the account. It can run from the same booked-meeting source as auto-connect because it targets other stakeholders, not duplicate outreach to the booked contact.
3. **Warm LinkedIn engagers:** run **Social engager flow - leadership's audience** when prospects engage with leadership, competitor, or influencer personal-profile posts.
4. **No HubSpot/list access:** run **AE AI SDR** from ICP + Discover Contacts; this cannot touch existing pipeline without HubSpot or a FirstTouch-accessible contact list.
5. **HubSpot + quiet pipeline:** run **Stalled deal reactivation** from a manually filtered HubSpot list of open deals with no engagement for 60+ days. If a deal only went quiet this week, use HubSpot signal/meeting-trigger follow-up; sub-60-day quiet-deal detection is not a native FirstTouch query.
6. **HubSpot MCP + tasks already created for LinkedIn/social steps:** run **Automate due HubSpot social tasks** as a secondary task runner for tasks due today, not as a cadence/list creator.

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

## Recipes
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

## Approval reminder
Dynamic/AI SDR rows require row-level approval. Static social-campaign flows can use flow-level approval only after the exact audience, static templates, sender/routing rule, launch window, and daily cap are approved.
