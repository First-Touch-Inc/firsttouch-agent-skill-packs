# Safety & Governance — The Non-Negotiable Rules

*Every play in this pack enforces these. If you fork or adapt a play, keep these intact.*

LinkedIn account safety and CRM trust are the two things you cannot afford to break. These rules protect both.

---

## The Golden Rule

> **No play sends outbound autonomously. Every LinkedIn action goes through a human approval gate before it executes.**

Agents **draft**. Humans **approve**. FirstTouch **executes**. This sequence is hardcoded into every play.

**Default recommendation:** if AI-generated messaging is new for the customer, keep approvals **ON for at least the first few weeks** until the team trusts the quality and safety of the drafts.

---

## The 5 safety gates (enforce all 5 before any send)

### Gate 1 — Duplicate check
Before messaging anyone, confirm they are **not** already in an active sequence or recently contacted.
- Query FirstTouch campaign history for the contact.
- If contacted in the last 30 days (configurable), **skip** and log the skip.

### Gate 2 — Owner routing
Confirm the contact has an **owner** in HubSpot and that the authorized user is allowed to message on their behalf.
- If no owner → route to enrichment/assignment, **do not send**.
- If owner mismatch → flag for human review, **do not send**.

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
Every executed action is logged to the HubSpot contact timeline via FirstTouch, within minutes.
- If logging fails → surface an alert; do not consider the play complete.

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

**Play-specific stricter cap:** AI SDR uses a tighter recurring outbound cap: **10 contacts/day** for free/basic accounts and **15 contacts/day** for Sales Navigator/Premium.

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

1. Owner is missing or disputed
2. Contact is already being actively worked by another sequence
3. Account is near or over safety limits
4. A safety/verification prompt appeared on the LinkedIn account
5. The prospect asked to stop / marked not interested → **permanently suppress** and log
6. Logging to HubSpot failed after a send
7. Anything that "feels off" — ambiguous intent, missing context, conflicting data

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

This trail is what makes the **Pipeline Attribution Analyst** (play 07) possible — and what gives enterprise buyers confidence.
