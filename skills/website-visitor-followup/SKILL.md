---
name: website-visitor-followup
description: Turn website-visitor intent into LinkedIn outreach by using de-anonymized visitor data or HubSpot website-visitor signals, checking connection status, drafting a lightweight message, and gating execution for approval. Use when the user wants to act on website visitors, use de-anon tools with FirstTouch, or add social touches to pricing-page and high-intent web activity.
metadata:
  author: firsttouch
  version: "1.0"
  category: play
  requires: [firsttouch-mcp, hubspot-mcp]
---

# Play 13 — Website Visitor Follow-Up

**Outcome:** Convert high-intent website visits into social touches while the account is actively researching.

## First-run onboarding gate
Before running this skill for the first time in a workspace, load `../../references/onboarding.md` and complete the onboarding questions. Do not proceed until you know: LinkedIn account type (free/basic = no connection notes and 10 connection requests/day max; Sales Navigator/Premium = connection notes available and up to 20/day), HubSpot access (MCP, service key/private app token, HubSpot list only, or none), and which play the user wants to run. Recommend high-intent plays before outbound to keep the LinkedIn account healthy. If HubSpot is unavailable, do not run HubSpot-specific steps unless the user provides a HubSpot list FirstTouch can access.

## When to use
- a de-anon tool identifies a target account/contact on key pages
- HubSpot website activity shows pricing / demo / product-page interest
- the user says "work website visitors"

## Inputs
- **signal source:** HubSpot's native website tracking (default) OR a de-anon platform like RB2B (recommended if native HubSpot web-visit volume is too low to be useful)
- **page threshold:** which pages count (pricing, demo, product, integrations, etc.)
- **identity confidence:** known contact vs likely account only

## Step-by-step

### 1. Pull visitor signals
Get recent high-intent visits with page path, timestamp, company/contact match confidence, and any associated HubSpot owner. **Two paths to the data:**
- **HubSpot native tracking pixel** (default) — HubSpot logs known-contact page activity automatically. Sufficient for most accounts with steady inbound.
- **RB2B (or similar de-anon tool)** — recommended when HubSpot-native web-visit volume is low or you need company-level identification for anonymous visitors. RB2B pushes identified visitors to a HubSpot list (or Slack), which FirstTouch then picks up. Wire RB2B → HubSpot list → FirstTouch picks up from the list.
- **Either way:** the play then runs identically — check connection status, draft, gate for approval.

### 2. Decide contact-level vs account-level motion
- **Known contact identified** → work contact directly
- **Only company known** → identify likely personas at the account (load `champion-mapper` if needed)

### 3. Check connection status + routing
- connected? yes/no
- owner assigned? yes/no
- recently contacted? yes/no

### 4. Draft the touch (load `firsttouch-messaging`)
Use the website visit as a soft signal — never sound creepy.

Do **not** say: "I saw you were on our pricing page at 2:14pm."

Instead, abstract the signal:
- "Looks like {company} may be evaluating options around {category}."
- "Seems like this might be live on your side right now."

Keep it light, conversational, and 2 sentences max.

### 5. Present for approval
Show the visitor signal, confidence level, target contact, and draft.

### 6. Execute + log
On approval: send via FirstTouch, log to HubSpot, tag `website_visitor_followup`.

### 7. Track
Measure reply and meeting rate by page type and signal confidence.

## Output
- high-intent visitor queue
- drafted messages, gated for approval
- send + log confirmation
- visitor tags for attribution

## Pitfalls
- being too explicit about the visit (comes off creepy)
- acting on low-confidence identity matches as if they are certain
- hitting visitors too late after the signal cools down

## Reference
- Messaging: [`../../references/messaging-framework.md`](../../references/messaging-framework.md)
- Mapping if only company known: load `champion-mapper`
