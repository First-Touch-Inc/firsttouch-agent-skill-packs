# First-Run Onboarding - RevOps Pack

This onboarding is scoped to the skills and recipes actually included in this installed pack.

## Ask before running anything
1. **LinkedIn account type:** free/basic or Sales Navigator/Premium.
   - Free/basic: no connection notes; recommend 10 connection requests/day; FirstTouch max 20/day.
   - Sales Navigator/Premium: connection notes available for approved warm signals; recommend 20 connection requests/day; FirstTouch max 30/day.
   - AI SDR and all other connection-request plays share the same daily budget.
   - If AI SDR and a social campaign run on the same sender/day, pause/reduce one motion or split the recommended daily cap explicitly before queueing sends; never exceed the FirstTouch max.
   - Already-connected LinkedIn message rows use a separate FirstTouch-supported message cap: 20/day on free/basic LinkedIn and 30/day on Sales Navigator/Premium. Reduce volume if acceptance or reply quality drops.
   - FirstTouch enforces these limits automatically - you can adjust volume anytime in the FirstTouch app, and you can never go over the peak limits. If a seat hits its daily limit it simply goes on cooldown until the next window.
2. **HubSpot access:** MCP connected by an admin, service key/private app token from an admin, HubSpot list only, or none. Getting access is easy: ask an admin to approve HubSpot MCP access (a quick approval) or to issue a **read-only service key** that lets the agent read deals, contacts, and companies with no write risk. Do not ask a rep/BDR to mint credentials they do not own.
3. **ICP/list/source data:** if HubSpot is absent, ask for ICP criteria or an imported/FirstTouch-accessible list before qualifying prospects.
4. **Persona start point:** recommend the persona-specific start point below, not a generic catalog dump.

## Persona start point
Start with **Pre-launch rollout audit** before any rep launches volume. Then govern the core rollout: HubSpot list triggers, **Team-wide AI SDR**, social campaigns, stalled-deal workflows, and **Attribution & team performance review** as the recurring reporting cadence. **Ad hoc queue diagnostics:** if a rep asks why a LinkedIn/email action has not sent, ask the agent a direct queue/status question first; you do not need to run the full workspace audit. Keep situational plays such as events, new-customer referral thank-you, website visitors, and closed-lost reengagement for after the core governance path is stable. **Rolling out to 2 or more reps? Read and apply section D (readiness by rollout size) in `references/revops-admin-appendix.md` first - pick your tier and run that tier's checklist.**

- Social engagement / warm engager flows are delivered by `warm-engager-followup`. They use LinkedIn post likes and comments from Social Engagement monitoring; if Social Engagement is not enabled, enable it through FirstTouch MCP for the monitored profile when permissions allow, or use a user-provided/exported engager list. Profile-view capture is not treated as MCP-native.

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

## Available recipes in this pack
#### Core governance
| Recipe | What it does | Needs |
|---|---|---|
| Pre-launch rollout audit | Run once before first launch or major rollout: MCP connections, approval workflow, suppression checks, sequence quality, logging round-trip, and per-seat safety limits. | No HubSpot required; HubSpot improves CRM/owner checks |
| Attribution & team performance review | Run the recurring RevOps reporting cadence as its own report: pull FirstTouch team metrics for the trailing 30 days by flow, sender, and date, then reconcile sends, replies, sentiment, meetings, and opportunities against HubSpot logging coverage. | No HubSpot required for FirstTouch team metrics; HubSpot improves opportunity/pipeline reconciliation |
| HubSpot list trigger - team-wide LinkedIn flows | Use HubSpot lists or contact-based workflow outputs as the trigger source for FirstTouch LinkedIn outreach across your team. Confirm FirstTouch action cards using references/hubspot-setup.md; if cards are not present, use the documented HubSpot list/source fallback. | HubSpot required |
| Team-wide AI SDR - daily approval queues | Action AI SDR across the whole team, not just one user: define the ICP, choose senders/owners, discover or load prospects, enrich each prospect, apply per-sender recommended 10/20 connection caps, FirstTouch 20/30 connection max, and 20/30 message caps, then produce team-wide approval queues. | No HubSpot required with ICP brief + FirstTouch Discover Contacts; HubSpot/list optional for owner routing and account context |
| Social campaigns - team-routed operational campaigns | Build governed campaigns such as inbound-signup decision-maker enrichment, CEO touches to stuck $50k+ deals, or product-update messaging to first-degree team connections at target accounts. RevOps chooses row-level dynamic approvals or a static flow-level campaign based on risk. | No HubSpot required for imported target-account/connection lists; HubSpot required for inbound owner routing, deal amount, deal age, or customer/deal segments |
| Stalled deal reactivation spec - team-wide | Produce the contact-based stalled-deal qualification spec, qualifying HubSpot list/workflow setup steps, and owner-approved LinkedIn reactivation queue. Automation is only claimed after RevOps confirms the portal/source can feed FirstTouch. | HubSpot required; RevOps/admin may be needed only for recurring workflow setup |
#### Situational rollout plays
| Recipe | What it does | Needs |
|---|---|---|
| Social engager setup for team | Configure warm-engager signal capture and flows so the whole team benefits from personal-profile content engagement; use Team-wide AI SDR as the separate prospecting fallback when Social Engagement is unavailable or thin. | No HubSpot required; enable Social Engagement through FirstTouch MCP to monitor owned leadership personal profiles or relevant competitor/influencer personal profiles; HubSpot optional for qualification/routing; profile views and company-page engagement unavailable |
| Website visitor play | Turn pricing/demo/product-page visits into LinkedIn touches while intent is active; if no visitor signal source exists, choose Team-wide AI SDR as a separate prospecting motion instead. | HubSpot tracking or RB2B/list source required; if no visitor signal source exists, use Team-wide AI SDR as a separate prospecting motion |
| Closed-lost reengagement - team-wide | Re-engage historical closed-lost accounts across all reps when RevOps explicitly chooses a win-back motion; keep this separate from stalled open-deal reactivation. | HubSpot required; separate from stalled open-deal workflow |
| New-customer referral thank-you | After a new customer is created or Closed Won, RevOps confirms sender routing and caps, then the right owner connects, thanks them for choosing the product, collects feedback, and asks whether anyone in their network would also find value. | HubSpot Closed Won/customer source or imported/FirstTouch-accessible customer list required; HubSpot improves owner/CSM routing and logging |
| HubSpot setup guide for FirstTouch-triggered actions | Coach RevOps/admin through references/hubspot-setup.md: confirm whether FirstTouch action cards exist in HubSpot workflows, or use the supported fallback of a HubSpot list/source that FirstTouch reads before enrolling/queueing actions. | HubSpot required; confirm action cards exist in the customer portal before promising UI steps |
| Event plays - pre-invite and post-follow-up | Build audience and invite flow before an event, then run follow-up flows to attendees and no-shows. | HubSpot or imported attendee/source list required |

## Included skills and dependency status
| Skill | Needs |
|---|---|
| `firsttouch-messaging` | No HubSpot required |
| `inbound-speed-to-lead` | HubSpot or FirstTouch-accessible inbound list/import required; true automation needs a connected source |
| `warm-engager-followup` | No HubSpot required; enable Social Engagement through FirstTouch MCP for monitored profiles; user-provided/exported engager lists also work |
| `website-visitor-followup` | HubSpot tracking or RB2B/list source required |
| `icp-outbound-builder` | No HubSpot required with ICP brief + FirstTouch Discover Contacts; HubSpot list optional |
| `hubspot-signal-to-linkedin-touch` | HubSpot required |
| `social-campaigns` | No HubSpot for pure ICP/imported/connection-list campaigns; HubSpot required for CRM/deal/customer segments |
| `stalled-deal-reactivation` | HubSpot required; may need RevOps/admin for workflow setup |
| `customer-referral` | HubSpot Closed Won/customer source or imported/FirstTouch-accessible customer list required; HubSpot improves owner/CSM routing and logging |
| `sequence-qa-reviewer` | No HubSpot for FirstTouch QA; HubSpot improves duplicate/owner checks |
| `workspace-audit` | No HubSpot for FirstTouch-only audit; HubSpot needed for owner/logging coverage |
| `team-performance-report` | No HubSpot required for FirstTouch team metrics; HubSpot improves opportunity/pipeline reconciliation |
| `campaign-pause-and-fix` | No HubSpot required; works on any running FirstTouch flow |

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
- Persona: revops
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
