# Safety & Governance — The Non-Negotiable Rules

*Every play in this pack enforces these. If you fork or adapt a play, keep these intact.*

LinkedIn account safety and CRM trust are the two things you cannot afford to break. These rules protect both.

---

## The Golden Rule

> **No play sends outbound autonomously. Every LinkedIn action goes through a human approval gate before it executes.**

Agents **draft**. Humans **approve**. FirstTouch **executes**. This sequence is hardcoded into every play.

**Default recommendation:** if AI-generated messaging is new for the customer, keep approvals **ON for at least the first few weeks** until the team trusts the quality and safety of the drafts.

---

## The safety gates (enforce all before any send)

### Gate 0 — Suppression / DNC check
Before messaging anyone, confirm they are **not** suppressed, unsubscribed, opted out, bounced, marked do-not-contact, or blocked by compliance policy.
- When HubSpot is connected, check unsubscribe/marketing status, do-not-contact fields, bounced email status, suppression lists, and any customer-defined exclusion lists.
- When HubSpot is not connected, check FirstTouch suppression/campaign history and any user-provided exclusion list.
- If suppressed or opted out → **skip permanently**, log the reason, and do not draft.

### Gate 1 — Duplicate check
Before messaging anyone, confirm they are **not** already in an active sequence or recently contacted.
- Query FirstTouch campaign history for the contact.
- If contacted in the last 30 days (configurable), **skip** and log the skip.

### Gate 2 — Owner routing
When HubSpot is connected, confirm the contact has an **owner** in HubSpot and that the authorized user is allowed to message on their behalf.

- If HubSpot is connected and no owner exists → stop, report the no-owner record, ask the user/RevOps to assign it in HubSpot, and **do not send**.
- If owner mismatch → flag for human review, **do not send**.
- If HubSpot is not connected and the user is running a single-seat FirstTouch-only play, state that CRM owner routing is unavailable and require explicit human approval before any send.

### Gate 3 — Account-safety limits
Never exceed the authorized account's safe daily/weekly limits.
- Before queueing sends, pull FirstTouch LinkedIn outreach queue/status data for the sender, including `active`, `in_queue`, blocked/review-required, and today's completed/pending connection-request rows. Count today's connection requests against the sender's 10/day free/basic or 20/day Sales Nav/Premium cap before adding more rows; if queue data is unavailable, say the cap check is estimated and use the safer lower batch size.
- If near limit → **stop and report**, do not push volume.
- AI SDR and all other plays share the same daily **connection-request** budget for rows that send connection requests. First messages to already-connected contacts draw from the separate LinkedIn message cap. If multiple plays run in one day, keep the combined connection-request total under 10/day for free/basic or 20/day for Sales Navigator/Premium.
- When a social campaign and AI SDR run on the same sender/day, either pause/reduce AI SDR during the campaign window or split the daily cap explicitly (for example, 6 AI SDR + 4 campaign on a free/basic seat). Recompute campaign sending-day estimates against the reduced allocation, not the full daily cap.

### Gate 3a — Credit/spend governance
Discovery and enrichment can consume FirstTouch credits.
- Before any bulk Discover Contacts, contact enrichment, email enrichment, phone enrichment, or company enrichment, preview a small sample first.
- State the estimated **maximum** credits before bulk work.
- Require explicit human approval for the bulk credit spend before importing/enriching the full audience.
- If credit balance or feature costs are unavailable, report that uncertainty and ask before proceeding.

### Gate 4 — Human approval
Present the **exact** draft (recipient, message, intended action) to a human.
- Approve → execute via FirstTouch
- Edit → re-queue with edits
- Deny → log and stop
- Slack/email approval delivery requires external workspace configuration and is not assumed FirstTouch-native. If Slack/email/FirstTouch approval workflow is not configured, use in-agent approval: show the approval table in chat and wait for the human response before executing anything.

> **Approval must be per-send for dynamic first-touch outbound.** Batch approval is acceptable only for follow-ups in an already-approved sequence, or for a one-time `social-campaigns` flow where the human approves the exact segment, sender/routing rule, static templates, launch window, and daily cap before the flow launches. Do not treat social-campaign flow approval as permission for future dynamic or AI-generated campaigns.

### Gate 5 — Log after send
When HubSpot is connected, every executed action is logged to the HubSpot contact timeline via FirstTouch, within minutes.
- If HubSpot logging fails → surface an alert; do not consider the HubSpot-specific play complete.
- If HubSpot is not connected, log the execution record in FirstTouch and clearly state that CRM timeline logging was skipped.

---

## Account-safety reference (LinkedIn norms)

Capture account type during first-run onboarding, then use the stricter cap. Tune down for new/warned accounts; never exceed:

| Account / action | Suggested daily cap | Source of limit |
|--------|---------------------|---|
| Free/basic LinkedIn — connection requests | 10 | FirstTouch pack rule / product-backed cap |
| Sales Navigator / Premium — connection requests | up to 20 | FirstTouch pack rule / product-backed cap |
| LinkedIn messages — free/basic | 20/day | FirstTouch-supported cap |
| LinkedIn messages — Sales Navigator/Premium | up to 40/day | FirstTouch-supported cap |
| Post engagements | ~50 | General LinkedIn safety norm, not FirstTouch-enforced |

**Connection-note rule:** use connection notes only when the sender has Sales Navigator / Premium and the message is approved. For free/basic accounts, send blank connection requests and use the approved opener after the prospect accepts.

**Play-specific AI SDR cap:** AI SDR uses a recurring outbound cap of **10 connection-request rows/day** for free/basic accounts and **20 connection-request rows/day** for Sales Navigator/Premium. Already-connected message rows still require approval and should respect the separate message cap.

**Escalation cues — if any appear, pause the account:**
- Warnings or restrictions from LinkedIn
- Sudden drop in acceptance/reply rate
- "Action required" / verification prompts

The agent should treat these as **hard stops**, not warnings.

---

## Data handling

- The agent should use **only** data from connected MCPs (HubSpot, FirstTouch, enrichment). No fabricating contacts, names, or company facts.
- Never paste API keys or OAuth tokens into chat. Authenticate in the tool, reference the connection by name.
- Drafts may contain prospect data; treat them as sensitive. Don't echo full contact lists into shared channels unnecessarily.

---

## When the agent should STOP and ask

Hard-stop conditions (agent must pause and ask a human):

1. Prospect is suppressed, unsubscribed, opted out, bounced, marked do-not-contact, or appears on a suppression list
2. Owner is missing or disputed
3. Contact is already being actively worked by another sequence
4. Account is near or over safety limits
5. A safety/verification prompt appeared on the LinkedIn account
6. The prospect asked to stop / marked not interested → **permanently suppress** and log
7. Logging to HubSpot failed after a send
8. Anything that "feels off" — ambiguous intent, missing context, conflicting data

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
