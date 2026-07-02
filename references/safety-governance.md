# Safety & Governance - The Non-Negotiable Rules

*Every play in this pack enforces these. If you fork or adapt a play, keep these intact.*

LinkedIn account safety and CRM trust are the two things you cannot afford to break. These rules protect both.

---

## The Golden Rule

> **The agent never sends a message or publishes a flow without showing it to a human first. Approval happens in the chat: the agent presents the exact draft (or the exact flow) and waits for an explicit yes.**

Agents **draft**. Humans **approve**. FirstTouch **executes**. These skills require that sequence in every play.

There are two approval layers, and they are different things:

1. **Chat approval (always - required by these skills).** Before queueing any send or publishing any flow, the agent shows the human exactly what will go out and waits for approval in the conversation. This is agent behavior the plays require, not a product setting.
2. **FirstTouch human-in-the-loop (optional product layer - off by default).** FirstTouch can additionally require an in-product approval on individual flow actions. When enabled, the send pauses as an approval task in the FirstTouch app under **Tasks** (or as an approval task in HubSpot when the action runs through a HubSpot workflow) until a human completes it.

**The consequence that matters:** a published flow keeps running after the chat ends. Chat approval covers what the human saw at build time - it does not cover sends the flow generates later from new signals or new enrollees. For any flow that keeps enrolling contacts over time (social engagement, signal-triggered, recurring), either enable FirstTouch human-in-the-loop on the send actions, or get the human's explicit acknowledgment in chat that future sends from this flow are autonomous and limited to the exact static templates they approved.

**Default recommendation:** if AI-generated messaging is new for the customer, keep FirstTouch human-in-the-loop approvals **ON for at least the first two weeks** until the team trusts the quality and safety of the drafts.

---

## The safety gates (enforce all before any send)

### Gate 0 - Suppression / DNC check
Before messaging anyone, confirm they are **not** suppressed, unsubscribed, opted out, bounced, marked do-not-contact, or blocked by compliance policy.
- In FirstTouch, check Exclusion Lists / suppression and campaign history when those settings are available in the connected workspace.
- When HubSpot is connected, also check unsubscribe/marketing status, do-not-contact fields, bounced email status, suppression lists, and any customer-defined exclusion lists.
- When HubSpot is not connected, check FirstTouch suppression/campaign history and any user-provided exclusion list.
- If suppressed or opted out → **skip permanently**, log the reason, and do not draft.

### Gate 1 - Duplicate check
Before messaging anyone, confirm they are **not** already in an active sequence or recently contacted.
- Query FirstTouch campaign history for the contact.
- If contacted in the last 30 days (configurable), **skip** and log the skip.

### Gate 2 - Owner routing
When HubSpot is connected, confirm the contact has an **owner** in HubSpot and that the authorized user is allowed to message on their behalf.

- If HubSpot is connected and no owner exists → stop, report the no-owner record, ask the user/RevOps to assign it in HubSpot, and **do not send**.
- If owner mismatch → flag for human review, **do not send**.
- If HubSpot is not connected and the user is running a single-seat FirstTouch-only play, state that CRM owner routing is unavailable and require explicit human approval before any send.

### Gate 3 - Account-safety limits
Never exceed the authorized account's safe daily/weekly limits.
- Before queueing sends, confirm the FirstTouch Sending Schedule/quiet-hours setting when available, then pull FirstTouch LinkedIn outreach queue/status data for the sender, including `active`, `in_queue`, blocked/review-required, and today's completed/pending connection-request rows. Count today's connection requests against the recommended sender cap (10/day free/basic or 20/day Sales Nav/Premium) before adding more rows; if the user explicitly approves higher volume, never exceed the FirstTouch max (20/day free/basic or 30/day Sales Nav/Premium). If queue data is unavailable, say the cap check is estimated and use the recommended safe batch size.
- If near limit → **stop and report**, do not push volume.
- AI SDR and all other plays share the same daily **connection-request** budget for rows that send connection requests. First messages to already-connected contacts draw from the separate LinkedIn message cap. If multiple plays run in one day, keep the combined connection-request total under the recommended 10/day for free/basic or 20/day for Sales Navigator/Premium unless the user explicitly approves more; never exceed the FirstTouch max of 20/day free/basic or 30/day Sales Navigator/Premium.
- When a social campaign and AI SDR run on the same sender/day, either pause/reduce AI SDR during the campaign window or split the daily cap explicitly (for example, 6 AI SDR + 4 campaign against the recommended 10/day free/basic cap). Recompute campaign sending-day estimates against the reduced allocation, not the full daily cap.
- Queues are per sender: each rep's actions process first-come-first-serve within their own queue, and another rep's queued actions never delay yours. For a time-sensitive send, set the enrollment's priority to high so it moves ahead of that sender's other queued work - do not try to beat the queue by adding volume.

### Gate 3a - Credit/spend governance
Discovery and enrichment can consume FirstTouch credits.
- Before any bulk Discover Contacts, contact enrichment, email enrichment, phone enrichment, or company enrichment, preview a small sample first.
- State the estimated **maximum** credits before bulk work. Use the connected FirstTouch credit/cost tools when available, such as `get_credits_usage` and `get_feature_costs`; otherwise state that the estimate could not be verified.
- Require explicit human approval for the bulk credit spend before importing/enriching the full audience.
- If credit balance or feature costs are unavailable, report that uncertainty and ask before proceeding.

### Gate 4 - Human approval
Present the **exact** draft (recipient, message, intended action) to a human in chat.
- Approve → execute via FirstTouch
- Edit → re-queue with edits
- Deny → log and stop
- When FirstTouch human-in-the-loop is enabled on the action, the send also pauses as an approval task assigned to the owner - in the FirstTouch app under **Tasks**, or as an approval task in HubSpot when the action runs through a HubSpot workflow. There is **no automatic escalation or SLA** on approval tasks: if an approval sits unactioned, following up is manual. Recurring plays should include checking the pending-approval queue (`list_user_tasks`) as part of the routine.
- Slack/email approval delivery requires external workspace configuration and is not assumed FirstTouch-native. If no in-product approval workflow is configured, use in-agent approval: show the approval table in chat and wait for the human response before executing anything.

> **Approval must be per-send for dynamic first-touch outbound.** Batch approval is acceptable only for follow-ups in an already-approved sequence, or for a one-time `social-campaigns` flow where the human approves the exact segment, sender/routing rule, static templates, launch window, and daily cap before the flow launches. Do not treat social-campaign flow approval as permission for future dynamic or AI-generated campaigns.

### Gate 5 - Log after send
When HubSpot is connected, every executed action is logged to the HubSpot contact timeline via FirstTouch, within minutes.
- If HubSpot logging fails → surface an alert; do not consider the HubSpot-specific play complete.
- If HubSpot is not connected, log the execution record in FirstTouch and clearly state that CRM timeline logging was skipped.

---

## Account-safety reference (LinkedIn norms)

Capture account type during first-run onboarding. FirstTouch enforces these limits automatically - you can adjust your volume anytime in the FirstTouch app, and you can never go over the peak limits. Tune down for new accounts:

| Account / action | Recommended safe daily cap | FirstTouch max | Source of limit |
|---|---:|---:|---|
| Free/basic LinkedIn - connection requests | 10/day | 20/day | FirstTouch-supported max; pack recommends lower for safety |
| Sales Navigator / Premium - connection requests | 20/day | 30/day | FirstTouch-supported max; pack recommends lower for safety |
| LinkedIn messages - free/basic | 20/day | 20/day | FirstTouch-supported max |
| LinkedIn messages - Sales Navigator/Premium | 30/day | 30/day | FirstTouch-supported max |

**General LinkedIn hygiene:** post engagement activity is a LinkedIn behavior norm, not a FirstTouch-sourced or FirstTouch-enforced cap. If a user asks about liking/commenting volume, keep it conservative and separate from the FirstTouch connection/message caps above.

**Connection-note rule:** use connection notes only when the sender has Sales Navigator / Premium and the message is approved. For free/basic accounts, send blank connection requests and use the approved opener after the prospect accepts.

**Play-specific AI SDR cap:** AI SDR uses the recommended recurring outbound cap of **10 connection-request rows/day** for free/basic accounts and **20 connection-request rows/day** for Sales Navigator/Premium. Already-connected message rows still require approval and should respect the separate message cap: 20/day free/basic and 30/day Sales Navigator/Premium.

**Volume signals - when to dial down:**
- **Account on cooldown:** normal. The seat hit its daily limit; FirstTouch enforced it and sends resume in the next window. If cooldowns happen often, lower daily volume so the queue flows evenly.
- **Acceptance rate dropping:** a targeting/messaging signal AND an account-health signal. FirstTouch Trust & Safety guidance: above ~40% acceptance is healthy; below ~25% is the danger zone. Lower volume and tighten targeting before scaling back up.
- **Seat status not Available** (Action required / Disconnected / Restricted in FirstTouch Social settings): pause that seat until the status is resolved - see `troubleshooting.md`.

FirstTouch enforces your configured send limits and prevents over-volume inside FirstTouch. Account health also depends on things FirstTouch cannot control: list quality, acceptance rate, copy quality, and whether other automation tools run on the same account. Send warm, targeted, approved outreach to help keep the account healthy.

---

## Data handling

- The agent should use **only** data from connected MCPs (HubSpot, FirstTouch, enrichment). No fabricating contacts, names, or company facts.
- Never paste API keys or OAuth tokens into chat. Authenticate in the tool, reference the connection by name.
- Drafts may contain prospect data; treat them as sensitive. Don't echo full contact lists into shared channels unnecessarily.

---

## Exclusion lists
Connect FirstTouch **Exclusion Lists** to keep outreach away from people you should not touch - current customers, deals in pipeline, partners, or anyone who opted out. Gate 0 checks them before any draft. Manage the lists in the FirstTouch app; when a prospect asks to stop or marks not interested, add them and they are excluded from every future motion.

## When the agent should STOP and ask

Pause-and-ask conditions (agent stops and checks with a human):

1. Prospect is suppressed, unsubscribed, opted out, bounced, marked do-not-contact, or appears on a suppression list
2. Owner is missing or disputed
3. Contact is already being actively worked by another sequence
4. Account is near or over safety limits
5. The LinkedIn seat is on cooldown and the user is asking to push more volume anyway
6. The prospect asked to stop / marked not interested → **permanently suppress** and log
7. Logging to HubSpot failed after a send
8. Anything that "feels off" - ambiguous intent, missing context, conflicting data

A cautious agent that stops early is worth far more than a fast one that burns an account.

---

## Audit trail

Every completed play produces a record:
- **Who** was targeted (contact + company)
- **What** signal triggered it
- **What** was drafted and approved
- **Who** approved and when
- **Whether** it sent + logged successfully
- **Outcome** tracked over time (reply, meeting, influenced deal)

This trail is what lets the team audit outcomes later and gives enterprise buyers confidence.
