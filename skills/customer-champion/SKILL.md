---
name: customer-champion
description: Reach out to customers when a meaningful milestone is hit — onboarding completed, usage threshold reached, expansion motion started, renewal window opened, or a champion moment appears. Uses HubSpot/customer milestones as signals, drafts a lightweight LinkedIn touch to deepen the relationship, and logs the action. Use when the user wants to strengthen customer champions, build advocates, or attach social touches to customer-success milestones.
metadata:
  author: firsttouch
  version: "1.1"
  category: play
  requires: [firsttouch-mcp, hubspot-mcp]
---

# Customer Champion

**Outcome:** Turn customer milestones into relationship-building moments on LinkedIn so champions feel seen before you need a favor, referral, quote, or renewal conversation.

## First-run onboarding gate
Before running this skill for the first time in a workspace, load `../../references/onboarding.md` and complete the onboarding questions. Do not proceed until you know: LinkedIn account type (free/basic = no connection notes and 10 connection requests/day max; Sales Navigator/Premium = connection notes available and up to 20/day), HubSpot access (MCP, service key/private app token, HubSpot list only, or none), and which play the user wants to run. Recommend high-intent plays before outbound to keep the LinkedIn account healthy. If HubSpot is unavailable, do not run HubSpot-specific steps unless the user provides a HubSpot list FirstTouch can access.

## When to use
- onboarding completed
- first value milestone reached
- product adoption / usage milestone
- renewal / expansion window opening
- customer gets promoted, posts a win, or shares a result

## Inputs
- **milestone definition** (the customer signal)
- **target role** (champion / admin / exec sponsor)
- **goal** (relationship deepen / advocacy / expansion groundwork)

## Step-by-step

Before drafting or queueing any contact, run the standard safety gates from `../../references/safety-governance.md`: Gate 0 suppression/DNC, Gate 1 duplicate/recent-contact check, Gate 2 owner/CSM routing, Gate 3 daily cap sharing, and Gate 4 human approval. Suppressed, unsubscribed, opted-out, do-not-contact, duplicate, recently contacted, or misrouted records are skipped and logged.


### 1. Pull milestone hits (HubSpot MCP)
Find customer contacts/accounts matching the milestone. Capture: contact, company, owner/CSM, milestone hit, date, renewal/expansion context.

### 2. Check relationship state
- connected on LinkedIn? yes/no
- recently messaged? yes/no (Gate 1)
- owner/CSM alignment? yes/no (Gate 2)
- sender has capacity under the shared 10/day free/basic or 20/day Sales Nav/Premium connection cap? yes/no (Gate 3)

### 3. Choose the touch
- **Not connected** → connect (warm, milestone-led)
- **Connected** → short congratulatory / curiosity-driven note

### 4. Draft the message (load `firsttouch-messaging`)
Use the customer milestone as the signal.

Rules:
- keep it warm and human, not salesy
- usually **2 sentences max**
- the ask should be tiny or nonexistent
- if later used for advocacy, first deepen the relationship before asking for a case study / intro

Example direction:
> "Saw your team hit {milestone}. Love seeing that land. Anything been especially useful so far?"

### 5. Present for approval
Show an approval table: contact, company, owner/CSM, milestone, relationship state, message type, draft, gate status. Each row must be marked awaiting approval and must not send until approved.

### 6. Execute + log
On approval: send via FirstTouch, log to HubSpot timeline, tag as `customer_champion`.

### 7. Hand off if needed
If the reply indicates expansion interest, route to AE/CSM. If advocacy interest, route to marketing/CS.

## Output
- milestone-based customer touch queue
- approved drafts
- send + log confirmation
- routed follow-ups if applicable

## Pitfalls
- making it feel like a hidden upsell pitch
- asking for too much too early (referral, review, intro)
- ignoring the CSM/owner relationship

## Reference
- Messaging: [`../../references/messaging-framework.md`](../../references/messaging-framework.md)
- Safety/owner routing: [`../../references/safety-governance.md`](../../references/safety-governance.md)
