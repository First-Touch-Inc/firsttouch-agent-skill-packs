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
- If HubSpot is connected and no owner exists → route to enrichment/assignment, **do not send**.
- If owner mismatch → flag for human review, **do not send**.
- If HubSpot is not connected and the user is running a single-seat FirstTouch-only play, state that CRM owner routing is unavailable and require explicit human approval before any send.

### Gate 3 — Account-safety limits
Never exceed the authorized account's safe daily/weekly limits.
- Check seat usage before queueing sends.
- If near limit → **stop and report**, do not push volume.

### Gate 4 — Human approval
Present the **exact** draft (recipient, message, intended action) to a human.
- Approve → execute via FirstTouch
- Edit → re-queue with edits
- Deny → log and stop

> **Approval must be per-send for first-touch outbound.** Batch approval is acceptable only for follow-ups in an already-approved sequence.

### Gate 5 — Log after send
When HubSpot is connected, every executed action is logged to the HubSpot contact timeline via FirstTouch, within minutes.
- If HubSpot logging fails → surface an alert; do not consider the HubSpot-specific play complete.
- If HubSpot is not connected, log the execution record in FirstTouch and clearly state that CRM timeline logging was skipped.

---

## Account-safety reference (LinkedIn norms)

Capture account type during first-run onboarding, then use the stricter cap. Tune down for new/warned accounts; never exceed:

| Account / action | Suggested daily cap |
|--------|---------------------|
| Free/basic LinkedIn — connection requests | 10 |
| Sales Navigator / Premium — connection requests | up to 20 |
| Messages / InMail | ~30–40 |
| Profile views | ~80 |
| Post engagements | ~50 |

**Connection-note rule:** use connection notes only when the sender has Sales Navigator / Premium and the message is approved. For free/basic accounts, send blank connection requests and use the approved opener after the prospect accepts.

**Play-specific AI SDR cap:** AI SDR uses a recurring outbound cap of **10 contacts/day** for free/basic accounts and **20 contacts/day** for Sales Navigator/Premium.

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
