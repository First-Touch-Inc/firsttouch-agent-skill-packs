---
name: customer-referral
description: Auto-prepare LinkedIn connection requests and thank-you/referral messages for new customers after they choose the product. Uses a HubSpot Closed Won/customer source or a FirstTouch-accessible customer list, checks owner/CSM routing and account-safety gates, drafts a warm thank-you that asks how the product can be better and whether anyone in their network would also find value, then queues approved FirstTouch Dynamic Actions. Use when the user wants a new-customer thank-you, feedback, or light referral motion.
metadata:
  author: firsttouch
  version: "1.0"
  category: play
  requires: [firsttouch-mcp]
---

# Customer Referral Thank-You

**Outcome:** When someone becomes a customer, connect with them on LinkedIn and send a warm thank-you that invites product feedback and a low-pressure referral signal, without making the first customer touch feel like a sales ask.

## First-run onboarding gate
Before running this skill for the first time in a workspace, load `../../references/onboarding.md` and complete the onboarding questions. Do not proceed until you know: LinkedIn account type (free/basic = no connection notes; recommend 10 connection requests/day and never exceed the FirstTouch max of 20/day; Sales Navigator/Premium = connection notes available; recommend 20 connection requests/day and never exceed the FirstTouch max of 30/day), HubSpot access (MCP, service key/private app token, HubSpot list only, or none), and which play the user wants to run. Recommend high-intent plays before broader outbound to keep the LinkedIn account healthy.

## When to use
- a deal moves to Closed Won
- a new customer starts onboarding
- a user/admin completes setup or hits first value
- the founder, AE, CSM, or account owner wants to thank the customer personally
- the team wants to ask for feedback and light referrals without launching a bulk campaign

## Inputs
- **Customer source:** HubSpot Closed Won/customer list, HubSpot workflow/list output, CSV/imported customer list, or FirstTouch-accessible customer source
- **Sender/routing rule:** founder, account owner, AE, CSM, or named executive sender
- **Relationship context:** product purchased, use case, onboarding status, first-value milestone, or why they chose the product
- **Referral ask style:** soft network ask, partner/customer intro ask, or feedback-only if the relationship is too early

HubSpot is preferred for Closed Won/customer routing and CRM logging. It is not mandatory when the user provides a customer CSV, imported list, or FirstTouch-accessible customer source with explicit customer status.

## Step-by-step

Before drafting or queueing any contact, run the standard safety gates from `../../references/safety-governance.md`: Gate 0 suppression/DNC, Gate 1 duplicate/recent-contact check, Gate 2 owner/CSM routing, Gate 3 daily cap sharing, and Gate 4 human approval. Suppressed, opted-out, duplicate, recently contacted, or misrouted records are skipped and logged.

### 1. Build the new-customer cohort
Use the safest available source:
- **HubSpot connected:** query or use a list/workflow of contacts associated to Closed Won deals, new customer lifecycle stage, onboarding-start events, or first-value milestones.
- **HubSpot list only:** use the provided HubSpot list/source FirstTouch can access; do not ask a rep to mint HubSpot credentials they do not own.
- **No HubSpot:** use a customer CSV/imported list or FirstTouch-accessible customer source with explicit customer status.

Capture: contact, company, role, owner/CSM, customer start date or milestone, product/use case, LinkedIn URL/status if available, and any suppression/recent-touch signals.

### 2. Pick the right sender
Default sender priority:
1. relationship owner / AE / CSM if the customer knows them
2. founder/executive if this is a founder-led thank-you motion
3. assigned team member if routing is defined by HubSpot owner or FirstTouch assignment

If owner routing is missing or ambiguous, stop and ask. Do not send a customer thank-you from a random sender.

### 3. Check LinkedIn relationship state
For each customer contact:
- **Already connected** → draft a LinkedIn message.
- **Not connected** → queue a connection request first; after the connection is accepted, queue the thank-you/referral message on the accepted branch.
- **Unknown connection state** → inspect FirstTouch/LinkedIn relationship data where available; if still unknown, present the row for review and do not assume connected.

Connection-note behavior:
- Free/basic LinkedIn: connection request must be blank/no note.
- Sales Navigator/Premium: a short warm note is allowed, but default to a blank request if the sender wants a lower-friction account-health posture.

### 4. Draft the message
Load `firsttouch-messaging` before drafting. Keep it warm, specific, and usually 2 sentences max. The message should:
- thank them for choosing the product
- ask one lightweight feedback question about how the product could be better
- include a soft network-value line only when it feels natural
- never make the customer feel immediately monetized

Default pattern:
> "Thanks again for choosing {product/company}. As you get into it, I would genuinely love to know what we could make better. If someone in your network would get value from this too, happy to be useful."

Founder-led variant:
> "Really appreciate you choosing {product/company}. If anything could be sharper as you get started, I would love to hear it. If another founder/operator in your network is dealing with the same problem, I am always happy to help."

CSM/owner variant:
> "Excited to have your team onboard. As you get into {product/company}, what is one thing we could make easier? If anyone in your network is trying to solve this too, I am happy to point them in the right direction."

Feedback-only variant:
> "Thanks for choosing {product/company}. As you get into it, I would genuinely love to know what we could make sharper. No ask, just want to hear it."

### 5. Present for approval
Show an approval table:

| Contact | Company | Owner/sender | Customer signal | Connected? | Action path | Draft | Gate status |
|---|---|---|---|---|---|---|---|

Every row must be marked `awaiting approval — will not send` until the assigned human approves that row. Do not treat one table-level approval as approval to send the whole batch unless the user explicitly approves every listed row.

### 6. Queue FirstTouch Dynamic Actions
After approval per row:
- before creating any one-contact LinkedIn action, run `get_dynamic_action_guide`, then call `add_dynamic_action` in the supported order
- if not connected, create a `linkedin_connect` action first; if a thank-you message should follow only after acceptance, append the `linkedin_message` to the `connection_accepted` branch
- if already connected, create the `linkedin_message` action directly
- enforce duplicate checks, account-safety limits, and approval status from `../../references/safety-governance.md`
- log execution and outcomes back to HubSpot when HubSpot is connected and the integration supports timeline logging
- if HubSpot is not connected, keep the execution record in FirstTouch and clearly state CRM owner routing/logging was unavailable

### 7. Route replies
- Product feedback → route to founder/product/CS owner.
- Referral or intro offer → route to owner/AE/CSM with context.
- Negative feedback → route to CSM/support and do not ask for referrals.
- No reply → do not chase with an aggressive referral follow-up; this is a customer relationship motion, not a cold sequence.

## Output
- new-customer cohort with routing and suppression status
- approved connection/message plan per contact
- thank-you/referral drafts
- FirstTouch Dynamic Actions queued only after approval
- HubSpot/FirstTouch logging summary
- routed follow-up tasks for feedback, support issues, or referrals

## Pitfalls
- **Sounding transactional:** thanking a new customer and immediately asking for referrals can feel extractive. Lead with gratitude and feedback.
- **Skipping owner routing:** customer relationships are sensitive; route through the person they know or the agreed founder/executive sender.
- **Using a connection note on free/basic LinkedIn:** free/basic requests should be blank/no note.
- **Messaging before connection acceptance:** if they are not connected, queue the thank-you message on the `connection_accepted` branch, not as an immediate message.
- **Autosending without approval:** never. This skill prepares and queues approved FirstTouch actions; it does not bypass human approval.

## Reference
- Messaging: [`../../references/messaging-framework.md`](../../references/messaging-framework.md)
- Safety/owner routing: [`../../references/safety-governance.md`](../../references/safety-governance.md)
- System model: [`../../references/system-grounding.md`](../../references/system-grounding.md)
