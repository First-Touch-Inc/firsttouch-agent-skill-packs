---
name: hubspot-signal-to-linkedin-touch
description: Turn a HubSpot CRM event — lifecycle stage change, deal stage movement, form fill, list addition — into a timely, personalized LinkedIn touch. Reads the signal from HubSpot, qualifies the contact, drafts outreach via FirstTouch, gates for approval, and logs back to the timeline. Use when the user wants to act on HubSpot activity with LinkedIn outreach, trigger social touches from CRM events, or make outbound "event-driven."
metadata:
  author: firsttouch
  version: "1.0"
  category: play
  requires: [firsttouch-mcp, hubspot-mcp]
---

# HubSpot Signal → LinkedIn Touch

**Outcome:** Make LinkedIn outreach event-driven — every touch is triggered by a real CRM event, not a cadence timer.

## First-run onboarding gate
Before running this skill for the first time in a workspace, load `../../references/onboarding.md` and complete the onboarding questions. Do not proceed until you know: LinkedIn account type (free/basic = no connection notes and 10 connection requests/day max; Sales Navigator/Premium = connection notes available and up to 20/day), HubSpot access (MCP, service key/private app token, HubSpot list only, or none), and which play the user wants to run. Recommend high-intent plays before outbound to keep the LinkedIn account healthy. If HubSpot is unavailable, do not run HubSpot-specific steps unless the user provides a HubSpot list FirstTouch can access.

## When to use
- "When a contact hits MQL, reach out on LinkedIn"
- "If a deal moves to 'Decision Maker Buy-In,' send a social touch"
- "Anyone who filled out the pricing form this week, connect on LinkedIn"
- Building event-driven outbound from HubSpot lists, lifecycle fields, forms, or contact-based workflow outputs

## Inputs
- **Signal definition:** which HubSpot event triggers the play (lifecycle change / deal stage / form / list membership / inactivity)
- **Audience scope:** which contacts/companies the trigger applies to
- **Cooldown:** min days between touches for a contact (default: 14)

## Step-by-step

### 1. Define & query the signal (HubSpot MCP)
Pull contacts matching the trigger event within the window. For AE use, a manually filtered HubSpot contact list is enough for a one-time run today; RevOps/admin workflow setup is needed only for recurring automation. FirstTouch supports HubSpot workflow actions that trigger FirstTouch flows; if the desired trigger needs a HubSpot workflow, confirm the customer portal exposes the needed FirstTouch action card and permissions, then produce the contact-based workflow/list criteria for RevOps/admin. Do not claim the agent created a HubSpot workflow unless the connected portal confirms that capability. For each, capture: name, title, company, owner, lifecycle/deal stage, the triggering event + timestamp, and recent timeline activity.

### 2. Qualify
For each triggered contact:
- Run Gate 0 suppression/DNC check from `../../references/safety-governance.md`; if suppressed or unsubscribed → **skip**
- Has an owner? → if no, **route to assignment, do not send** (Gate 2)
- Within cooldown? → **skip**
- Already in active sequence / recently contacted? → **skip** (Gate 1)
- LinkedIn URL present? → if no, flag for enrichment

### 3. Map signal → message type
The HubSpot event determines the message:
| Signal | Message type | Why |
|--------|-------------|-----|
| New MQL / form fill | Connection request | Start relationship |
| Lifecycle up (SQL→Opportunity) | Opener to connected | Warm the opp |
| Meeting logged on an associated deal | Connection request to unconnected stakeholders, or opener/value touch to connected stakeholders | Multi-thread the account after a real meeting signal. Configure as a contact-based HubSpot list/workflow, for example: contacts at companies where an associated deal has a meeting logged in the last 7 days. |
| Deal moved forward | Value touch to stakeholders | Reinforce |
| Open deal not Closed Won/Lost and no engagement for 60+ days | Re-engage | Use a contact-based stalled-deal list/workflow-output pattern; if this pack does not include the stalled-deal skill, ask RevOps/admin to supply the qualifying HubSpot list or setup steps. Deal triggers are unsupported. |
| Closed Lost deal selected for win-back | Connection request or re-engage | Use a contact-based list of contacts associated to Closed Lost deals; keep this separate from stalled open-deal reactivation. |
| Re-engaged after silence | Opener | Context renewed |

### 4. Draft (load `firsttouch-messaging`)
The **signal is the HubSpot event itself** — e.g. "saw you just downloaded the outbound playbook." Draft accordingly. Run the quality gate.

### 5. Present for approval (Gate 4)
Table of: contact, triggering event, owner, message type, draft. All marked awaiting approval.

### 6. Execute + log (FirstTouch MCP)
On approval: send via FirstTouch, log to HubSpot timeline, tag with `signal_triggered_touch` + the signal type for attribution.

### 7. Track
Cohort tagged by signal type so the team can review which signals produce replies, meetings, and pipeline. When FirstTouch team metrics are available, pull metrics filtered by this flow/tag to report replies, meetings, and opportunities.

## Output
- Triggered-contact list with the HubSpot event per row
- Drafted, gated messages
- Send + log confirmation
- Signal-tagged cohort for attribution

## Examples
**Signal:** Contact filled "Request a demo" form, owner = AE, not yet connected on LinkedIn.
**Draft (connection request):** "Hi Devon, saw you're exploring FirstTouch after the demo request. Connecting so I can share setup tips as you evaluate."

**Closed Lost win-back signal:** Contact is associated to a Closed Lost deal selected for a fresh reengagement motion.
**Draft (re-engage opener):** "Hi Dana, noticed your team previously evaluated FirstTouch and wanted to share what changed since then. Worth comparing notes if social attribution is back on the roadmap."

## Why this play wins
Static sequences message on a timer. This play messages on a **real event** — dramatically higher relevance and reply rate, and fully attributable in HubSpot.

## Pitfalls
- **Triggering on too-broad events** — "any lifecycle change" floods the queue. Scope triggers tightly.
- **Ignoring owner** — messaging a contact another AE owns causes internal friction. Always check owner (Gate 2).
- **No cooldown** — a contact bouncing stages gets spammed. Enforce cooldown.

## Reference
- Messaging: [`../../references/messaging-framework.md`](../../references/messaging-framework.md)
- Safety gates: [`../../references/safety-governance.md`](../../references/safety-governance.md)
