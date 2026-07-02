# Recipe Catalog - RevOps Pack

Use this file when the agent installed `skills/` and `references/` without loading the root README. These recipes are the recommended starting points for the revops persona.

## Recommended start point
Start with **Pre-launch rollout audit** before any rep launches volume. Then govern the core rollout: HubSpot list triggers, **Team-wide AI SDR**, social campaigns, stalled-deal workflows, and **Attribution & team performance review** as the recurring reporting cadence. **Ad hoc queue diagnostics:** if a rep asks why a LinkedIn/email action has not sent, ask the agent a direct queue/status question first; you do not need to run the full workspace audit. Keep situational plays such as events, new-customer referral thank-you, website visitors, and closed-lost reengagement for after the core governance path is stable. **Rolling out to 2 or more reps? Read and apply section D (readiness by rollout size) in `references/revops-admin-appendix.md` first - pick your tier and run that tier's checklist.**

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

## Recipes
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

## Approval reminder
Dynamic/AI SDR rows require row-level approval. Static social-campaign flows can use flow-level approval only after the exact audience, static templates, sender/routing rule, launch window, and daily cap are approved.
