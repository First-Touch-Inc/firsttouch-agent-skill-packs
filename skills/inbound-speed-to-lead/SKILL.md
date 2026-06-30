---
name: inbound-speed-to-lead
description: Attach LinkedIn connection requests and lightweight follow-up to inbound signups, trial starts, demo requests, or other high-intent inbound lists. Can start from HubSpot events when connected or a FirstTouch-accessible inbound list/import when HubSpot is unavailable. Checks connection status, drafts the smallest possible conversation-starting message, gates for approval, and logs to HubSpot when connected. Use when the user wants to improve speed-to-lead for inbound, connect on LinkedIn after a signup/trial, or add a social touch to inbound conversion.
metadata:
  author: firsttouch
  version: "1.0"
  category: play
  requires: [firsttouch-mcp]
---

# Inbound Speed-to-Lead

**Team-governance note:** For team-wide rollouts, run this with owner-based routing, per-seat cap sharing, approval review, and FirstTouch/HubSpot logging checks — not as an ungoverned single-rep send.


**Outcome:** Add a fast, light LinkedIn touch to high-intent inbound moments — signups, trials, demo requests — when the agent runs or on a configured schedule. True live speed-to-lead requires a connected source that continuously feeds FirstTouch.

## First-run onboarding gate
Before running this skill for the first time in a workspace, load `../../references/onboarding.md` and complete the onboarding questions. Do not proceed until you know: LinkedIn account type (free/basic = no connection notes and 10 connection requests/day max; Sales Navigator/Premium = connection notes available and up to 20/day), HubSpot access (MCP, service key/private app token, HubSpot list only, or none), and which play the user wants to run. Recommend high-intent plays before outbound to keep the LinkedIn account healthy. If HubSpot is unavailable, do not run HubSpot-specific steps unless the user provides a HubSpot list FirstTouch can access.

## When to use
- New signup or trial starts in HubSpot
- Demo request submitted
- Inbound contact reaches a high-intent lifecycle state
- The user says "attach LinkedIn to inbound" or "improve speed to lead"

## Inputs
- **Trigger event:** signup / trial / demo / hand-raise form / list membership
- **Window:** how soon after trigger to act (default: same day)
- **Connection-note policy:** use note only if sender has Premium/Sales Nav and the motion is warm enough

## Step-by-step

### 1. Pull inbound contacts
**Path A — HubSpot connected:** query the trigger event and return contacts created or updated in the window. Capture: name, title, company, owner, event type, timestamp, lifecycle stage, LinkedIn URL.

**Path B — no HubSpot access:** ask for a FirstTouch-accessible inbound list, CSV import, audience, or other connected source list containing the hand-raisers. A FirstTouch-accessible list means FirstTouch can read the contacts from an imported CSV/audience or connected source. State clearly: this is list/import-based unless a source continuously feeds FirstTouch; true speed-to-lead automation requires HubSpot or another connected inbound source. Capture the same fields when available. State that HubSpot owner routing and CRM timeline logging are unavailable until HubSpot is connected.

### 2. Check readiness
For each contact:
- Run Gate 0 suppression/DNC check from `../../references/safety-governance.md`; if suppressed or unsubscribed → skip
- Has owner? if HubSpot is connected and no owner exists → stop, report the no-owner contact, and ask the user/RevOps to assign it before drafting
- Has LinkedIn URL / can be matched? if no → enrichment queue
- Already connected? yes/no
- Recently contacted? if yes → skip

### 3. Choose the action
- **Not connected** → connection request
- **Already connected** → light opener / follow-up

### 4. Draft the message (load `firsttouch-messaging`)
Use the inbound event as the signal.

Rules:
- conversational, usually **2 sentences max**
- smallest possible ask
- do **not** force a meeting immediately unless the inbound event explicitly warrants it
- if Premium/Sales Nav is available, a short connection note is allowed

Example directions:
- Demo request → "Saw you just requested a demo. Wanted to connect here too in case helpful as you evaluate."
- Trial signup → "Saw you started a trial. Happy to be useful if anything jumps out as you get into it."

### 5. Present for approval
Show per contact:
| Contact | Trigger | Connected? | Message type | Draft |
Awaiting approval only.

### 6. Execute + log
On approval: send via FirstTouch. If HubSpot is connected, log to the HubSpot timeline and tag as `inbound_speed_to_lead`; if not, log the execution record in FirstTouch and state that CRM logging was skipped.

### 7. Track
Measure touch-to-meeting rate and reply rate for inbound contacts who received the LinkedIn touch versus those who did not.

## Output
- prioritized inbound queue
- drafted social touches, gated for approval
- send + log confirmation
- tagged cohort for attribution when HubSpot/list metadata is available

## Pitfalls
- treating all inbound equally — prioritize hand-raisers over lightweight ebook downloads
- asking for too much too fast — keep it conversational
- missing the same-day window — this play depends on running the agent quickly or scheduling it against a connected inbound source

## Reference
- Messaging: [`../../references/messaging-framework.md`](../../references/messaging-framework.md)
- Safety: [`../../references/safety-governance.md`](../../references/safety-governance.md)
