---
name: social-campaigns
description: Build a one-time LinkedIn social campaign for a very narrow ICP segment: define precise audience criteria, source/enrich contacts from FirstTouch and optional HubSpot lists, build static flow messaging templates, get bulk approval for the flow/campaign, then launch through FirstTouch. Use when the user wants a focused campaign for a product update, event invite, customer note, territory push, reengagement list, or team-routed social motion.
metadata:
  author: firsttouch
  version: "1.0"
  category: play
  requires: [firsttouch-mcp]
---

# Social Campaigns

**Outcome:** Create a one-time FirstTouch social campaign for a narrow, explicitly defined ICP segment. Unlike AI SDR, this is **not** a recurring dynamic-action play. Build the audience, approve the static flow messaging, launch once, and track results.

## First-run onboarding gate
Before running this skill for the first time in a workspace, load `../../references/onboarding.md` and complete the onboarding questions. Do not proceed until you know: LinkedIn account type (free/basic = no connection notes and 10 connection requests/day max; Sales Navigator/Premium = connection notes available and up to 20/day), HubSpot access (MCP, service key/private app token, HubSpot list only, or none), and which campaign the user wants to run. If the requested audience depends on HubSpot data such as no-shows, closed-won customers, deal amount, deal age, territory, owner, or lifecycle status, require HubSpot access or a HubSpot list/source FirstTouch can access.

## When to use
- "Run a one-time LinkedIn campaign to this narrow segment"
- "Invite buyers in this city to our booth next week"
- "Tell my customers about a new product update"
- "Message no-shows from last year"
- "Reach out to first-degree connections across the team at these target accounts"
- "Have the CEO send a connect and message to stuck high-value deals"

## When NOT to use
- Daily fresh prospecting or recurring AI SDR queues. Use `icp-outbound-builder` or `founder-led-outbound`.
- Highly personalized one-off account strategy. Use the relevant signal, stalled-deal, or founder play.
- A broad audience like "all VPs of Sales" without a narrow filter. Narrow it first.
- Any campaign where the user expects AI-generated unique copy for every recipient. Social campaigns should default to static templates with approved variables.

## Inputs
- **Campaign goal:** product update, event invite, reactivation, customer thank-you, expansion/upgrade, territory intro, feedback ask
- **Narrow segment criteria:** title/seniority, geography, industry, company size, customer/deal status, event attendance/no-show status, connection status, owner/sender, target accounts, date window
- **Source:** HubSpot list/workflow, FirstTouch audience/list, FirstTouch Discover Contacts, CSV/imported list, Sales Navigator source, or user-provided account/contact list
- **Sender strategy:** contact/company owner, CEO/founder, BDR, AE, or specific team member connected to the prospect
- **LinkedIn account type:** free/basic or Sales Navigator/Premium
- **Campaign messaging:** static connection request note when allowed, static first message template, optional one follow-up template

## Campaign approval model

Social campaigns use **flow-level bulk approval**, not per-row dynamic approval.

The human approves:
1. the exact segment definition and final audience count
2. the sender/owner routing rule
3. the static flow templates and variables
4. the launch window and daily cap
5. suppression / DNC / duplicate-check results

After this approval, FirstTouch can launch the one-time campaign according to the approved flow. Do not use this approval model for AI SDR or dynamic actions that generate unique messages per recipient; those still require row-level approval.

**Recommended copy mode:** use static templates with approved variables, not AI-generated templates. Variables must be factual fields from HubSpot, FirstTouch, enrichment, or the user's supplied data.

## Step-by-step

### 1. Define the narrow segment
Turn the user's idea into precise inclusion and exclusion criteria. If the segment is too broad, stop and narrow it.

Examples:
- BDR: connected contacts with leadership titles who match ICP and should hear about a product update
- BDR: no-shows from last year who never converted to opportunity
- BDR: ICP buyers in Las Vegas for a tradeshow invite next week
- AE: VPs of Sales in my territory
- AE: closed-won customers eligible for a feature-upgrade message
- AE: open deals from last year that have not closed
- RevOps: inbound signups enriched to the likely decision-maker and routed from the contact/company owner
- RevOps: deals over $50k stuck for 30+ days where the CEO should send a social touch
- RevOps: first-degree team connections at target accounts for product-update messaging
- Founder: leadership-role connections for feature feedback
- Founder: customers in HubSpot for over a year for a thank-you note
- Founder: VPs of Sales at software companies in a city during the founder's travel week

### 2. Choose the source path

**Path A - HubSpot/list-driven campaign:**
Use this when the criteria depend on CRM data such as no-show status, closed-won date, renewal age, deal amount, deal stage, owner, territory, inbound signup, or customer tenure. Pull the qualifying list from HubSpot MCP, a HubSpot service key/private app token, or a HubSpot list that FirstTouch can access.

**Path B - FirstTouch Discover campaign:**
Use this when the criteria are market/ICP filters such as title, industry, geography, company size, software company, funding/stage, or location. Use FirstTouch Discover Contacts and preview a small sample before importing because discovery/enrichment can consume FirstTouch credits.

**Path C - Connection/team-connection campaign:**
Use this when the user wants to prioritize people already connected to the sender or team. Start from a user-provided connection list, FirstTouch/team connection data, or a target-account/prospect list, then check connection status and team connections before routing. If no connection inventory is available, say so and build the audience from HubSpot/FirstTouch first, then check connection status prospect by prospect.

### 3. Enrich and qualify the audience
For each candidate, enrich and verify:
- LinkedIn URL and current title
- company domain, size, industry, location
- ICP fit and exclusion rules
- owner/sender routing
- connection status or team-connected sender when relevant
- HubSpot customer/deal/event fields when the campaign depends on CRM criteria

Run Gate 0 suppression/DNC and Gate 1 duplicate checks from `../../references/safety-governance.md`. Exclude anyone suppressed, opted out, already in an active sequence, recently contacted, outside ICP, missing a usable LinkedIn profile, or owned by another sender without explicit routing approval.

### 4. Build the one-time FirstTouch flow
Create a FirstTouch audience or flow draft for the final campaign audience.

Recommended sequence:
- If already connected: send the approved static first-message template, then optionally one approved static follow-up.
- If not connected: send a connection request. Use a note only when the account has Sales Navigator/Premium and the approved template has a strong reason for the note; otherwise send a blank connection request and use the approved message after accept.

Daily cap:
- free/basic: 10 connection requests/day
- Sales Navigator/Premium: up to 20 connection requests/day
- lower the cap if the account is new, under warning, or close to limits

### 5. Draft static templates
Load `firsttouch-messaging` for tone and quality rules, but produce **static campaign templates** rather than unique AI-generated messages per recipient.

Template rules:
- 2 sentences max per LinkedIn message
- no em dashes
- one lightweight ask
- no fabricated personalization
- variables only from approved fields such as `{first_name}`, `{company}`, `{event_name}`, `{city}`, `{product_update}`, `{owner_name}`, `{customer_tenure}`, `{deal_context}`
- no meeting ask unless the campaign is explicitly event/travel invitation and the ask is low-friction

Example template shapes:
- Product update: "Hi {first_name}, we just shipped {product_update} for teams working on {relevant_problem}. Thought it might be useful given your role at {company}."
- Event invite: "Hi {first_name}, I will be in {city} for {event_name} next week and noticed {company} fits the teams we usually help. Open to coffee while I am there?"
- Customer thank-you: "Hi {first_name}, appreciate {company} sticking with us for over a year. Wanted to say thank you and share a small update that may be useful."
- Reengagement: "Hi {first_name}, we did not get to connect after {prior_event}. Sharing a quick update in case this is still relevant for {company}."

### 6. Present campaign for bulk approval
Do **not** launch automatically. Present a campaign approval summary:

```markdown
## Social campaign approval
- Campaign name:
- Goal:
- Segment criteria:
- Source path:
- Final audience count:
- Sender/routing rule:
- Daily cap:
- Suppression / duplicate checks:
- Static connection request template:
- Static first-message template:
- Static follow-up template:
- Variables used:
- Launch window:
- Logging / attribution tag:

Approve this one-time flow? Approval applies to the flow messaging and audience definition, not to future dynamic campaigns.
```

If the user approves, launch only this approved flow. If they edit copy, update the templates and re-present before launch.

### 7. Launch and log
After approval:
- publish the FirstTouch flow/campaign
- enroll the approved audience according to daily caps
- log the campaign and attribution tag in FirstTouch and HubSpot when HubSpot is connected
- report queued, sent, blocked, failed, and completed counts
- do not convert this into an evergreen recurring campaign unless the user explicitly asks for a new approval cycle

## Output
- final segment definition and count
- source path and dependency status
- enriched/qualified audience summary
- static approved templates
- one-time flow approval summary
- launch/log confirmation
- blocked/skipped contacts summary

## Pitfalls
- letting the user start from a broad segment; narrow before building
- treating this like AI SDR with generated one-off copy per recipient
- launching without flow-level human approval
- using connection notes on free/basic accounts
- exceeding the 10/20 daily connection cap
- using HubSpot-dependent criteria without HubSpot access or a FirstTouch-accessible HubSpot list
- claiming FirstTouch can natively de-anonymize website visitors; use RB2B/HubSpot/list sources instead
- turning a one-time campaign into recurring automation without a fresh approval cycle

## Reference
- Onboarding: [`../../references/onboarding.md`](../../references/onboarding.md)
- Messaging: [`../../references/messaging-framework.md`](../../references/messaging-framework.md)
- Safety and approval gates: [`../../references/safety-governance.md`](../../references/safety-governance.md)
