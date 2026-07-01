---
name: social-campaigns
description: Build a focused LinkedIn social campaign for a very narrow ICP segment: define precise audience criteria, source/enrich contacts from FirstTouch and optional HubSpot lists, then choose either row-level dynamic actions for rep/BDR one-at-a-time execution or static flow templates for RevOps/founder-approved one-time campaigns. Use for product updates, event invites, territory pushes, reengagement lists, or team-routed social motions.
metadata:
  author: firsttouch
  version: "1.1"
  category: play
  requires: [firsttouch-mcp]
---

# Social Campaigns

**Founder/RevOps use:** one-time narrow pushes such as feature-feedback, product-update, travel-week, or team-routed campaigns. **AE/BDR use:** row-level dynamic mode for manager-approved special pushes, not normal daily prospecting.

**Outcome:** Create a focused FirstTouch social campaign for a narrow, explicitly defined ICP segment. For reps and BDRs, this should often feel like AI SDR: a curated list of rows with one-at-a-time approval, not a flow-building exercise. For founders and RevOps, it can also become a one-time static-template flow with bulk approval after the exact audience and templates are approved.

## First-run onboarding gate
Before running this skill for the first time in a workspace, load `../../references/onboarding.md` and complete the onboarding questions. Do not proceed until you know: LinkedIn account type (free/basic = no connection notes and 10 connection requests/day max; Sales Navigator/Premium = connection notes available and up to 20/day), HubSpot access (MCP, service key/private app token, HubSpot list only, or none), and which campaign the user wants to run. If the requested audience depends on HubSpot data such as no-shows, closed-won customers, deal amount, deal age, territory, owner, or lifecycle status, require HubSpot access or a HubSpot list/source FirstTouch can access.

## When to use
- A founder wants a one-time feature-feedback, product-update, or travel-week outreach campaign
- An AE wants a targeted territory, event, customer expansion, or stalled-pipeline push, usually as row-level dynamic actions unless RevOps approves a static flow
- RevOps wants to build a governed team-routed campaign with static templates and audit trail
- A BDR or manager wants a special push such as event invite/no-show follow-up, usually executed as approved one-at-a-time rows
- The user wants a product update, event invite, reactivation list, or team-connection push

## When NOT to use
- Daily fresh prospecting or recurring AI SDR queues. Use this pack's persona AI SDR play instead.
- A BDR's normal daily queue unless the campaign is explicitly a narrow special push. For daily prospecting, use `inbound-speed-to-lead`, `warm-engager-followup`, or the persona AI SDR play included in this pack.
- Highly personalized one-off account strategy. Use the relevant signal, stalled-deal, or founder play.
- A broad audience like "all VPs of Sales" without a narrow filter. Narrow it first.
- Any campaign where the user expects unreviewed AI-generated copy for every recipient. If copy is dynamic per recipient, use row-level approval like AI SDR.

## How narrow is narrow enough
Default to **25-100 people** for a first social campaign. Warn and ask for confirmation above **100**, require a stronger reason above **200**, and split anything larger into smaller waves by segment, sender, or launch window. Pull the daily-cap math into the sizing step. If AI SDR is also running for the same sender, either pause/reduce AI SDR during the campaign window or split the daily cap explicitly, for example 6 AI SDR + 4 campaign on a free/basic seat. Recompute campaign sending-day estimates against the campaign allocation: a 100-person campaign takes roughly 10 sending days only if the full 10/day free/basic cap is allocated to it, or 5 sending days only if the full 20/day Sales Navigator/Premium cap is allocated to it, before safety throttling. Never queue more connection requests than the sender's allocated daily cap allows.

## Examples by role

**Founder-first examples:**
- Leadership-role connections for feature feedback after a product launch
- VPs of Sales at software companies in a city during the founder's travel week

**AE examples:**
- VPs of Sales in a territory, using Discover Contacts when territory is market-defined or HubSpot when territory is CRM-defined
- Open deals from last year that have not closed, using HubSpot open-deal criteria

**BDR examples, use as special campaigns rather than daily work:**
- ICP buyers in a tradeshow city for a booth or meeting invite
- Last-year no-shows who never converted to opportunity, only if HubSpot or a provided event/no-show list exists
- Connected leadership titles who match ICP and should hear a specific product update

**RevOps examples:**
- Inbound signups enriched to the likely decision-maker and routed from the contact/company owner
- Deals over $50k stuck for 30+ days where the CEO should send a social touch
- First-degree team connections at target accounts for product-update messaging

## Inputs
- **Campaign goal:** product update, event invite, reactivation, expansion/upgrade, territory intro, feedback ask
- **Narrow segment criteria:** title/seniority, geography, industry, company size, customer/deal status, event attendance/no-show status, connection status, owner/sender, target accounts, date window
- **Source:** HubSpot list/workflow, FirstTouch audience/list, FirstTouch Discover Contacts, CSV/imported list, Sales Navigator source, or user-provided account/contact list
- **Sender strategy:** contact/company owner, CEO/founder, BDR, AE, or specific team member connected to the prospect
- **LinkedIn account type:** free/basic or Sales Navigator/Premium
- **Campaign messaging:** static connection request note when allowed, static first message template, optional one follow-up template

## Campaign approval model

Social campaigns have **two execution modes**. Choose the mode before building anything:

| Mode | Best for | Approval | Messaging |
|---|---|---|---|
| **Rep/BDR dynamic-row mode** | AE/BDR special pushes, event follow-up, territory bursts, small manager-approved lists | Row-level approval, like AI SDR. Each first-touch row must be approved individually. | Dynamic per-recipient copy is allowed only if each row is reviewed. |
| **Static campaign-flow mode** | Founder/RevOps governed one-time campaigns, product updates, reengagement motions, team-routed pushes | Flow-level approval after exact audience, sender/routing rule, static templates, launch window, daily cap, and suppression results are approved. | Static templates with approved factual variables only. |

Do not make AE/BDR users learn flow-building when they just need a targeted push. Default them to dynamic-row mode unless they explicitly ask for a reusable/static campaign flow or RevOps is coordinating it.

**Recommended copy mode:** static templates for flow-level campaigns; row-level dynamic drafts for rep/BDR mode. Variables must be factual fields from HubSpot, FirstTouch, enrichment, or the user's supplied data.

## Step-by-step

### 1. Define the narrow segment
Turn the user's idea into precise inclusion and exclusion criteria. If the segment is too broad, stop and narrow it.

Capture:
- who qualifies
- who is excluded
- source of truth for each criterion
- expected audience size
- whether HubSpot is required for the criteria

### 2. Choose the source path
Use this decision tree:

| If the segment depends on... | Use this path | HubSpot needed? |
|---|---|---|
| CRM fields: customer status, closed-won date, deal amount/stage/age, owner, territory field, no-show status stored in CRM | **HubSpot/list-driven**: read HubSpot MCP or a HubSpot list FirstTouch can access | Yes |
| Market/ICP filters: title, geography, industry, company size, software company, event city | **FirstTouch Discover**: build and preview a small audience from Discover Contacts; state estimated max credits before bulk import | No |
| User-provided contacts, event attendees, target accounts, or connection export | **Imported/list-driven**: use the CSV/list/audience, then enrich and check connection status | No, unless CRM fields are part of the criteria |
| Existing sender/team connections at target accounts | **Team-connection**: start from FirstTouch Team LinkedIn Connections data or a user-provided connection export; if neither exists, ask for one before claiming a team-connection campaign | No, unless CRM fields are part of routing |

Do not call this a team-connection campaign unless FirstTouch or the user provides connection data. If connection data is unavailable, run an imported/list or Discover campaign and mark connection status as unknown until checked prospect by prospect.

### 3. Enrich and qualify the audience
Before bulk discovery or enrichment, run Gate 3a from `../../references/safety-governance.md`: preview a small sample, state estimated maximum credits, and get approval for bulk credit spend.

For each candidate, enrich and verify:
- LinkedIn URL and current title
- company domain, size, industry, location
- ICP fit and exclusion rules
- owner/sender routing
- connection status or team-connected sender when relevant
- HubSpot customer/deal/event fields when the campaign depends on CRM criteria

Run Gate 0 suppression/DNC and Gate 1 duplicate checks from `../../references/safety-governance.md`. Exclude anyone suppressed, opted out, already in an active sequence, recently contacted, outside ICP, missing a usable LinkedIn profile, or owned by another sender without explicit routing approval.

### 4. Choose the execution object
Create the FirstTouch execution object that matches the chosen mode and connected MCP support. State the exact object created.

- **Rep/BDR dynamic-row mode:** build an audience and queue dynamic actions/manual approval rows, one prospect at a time; before adding per-contact dynamic actions, run `get_dynamic_action_guide`, then call `add_dynamic_action` in the supported order.
- **Static campaign-flow mode:** build an audience plus flow plan/campaign with approved static templates.

Recommended sequence:
- If already connected: send the approved static first-message template, then optionally one approved static follow-up.
- If not connected: send a connection request. Use a note only when the account has Sales Navigator/Premium and the user approves a strong reason for the note; otherwise send a blank connection request and use the approved message after accept.

Daily cap:
- free/basic: 10 connection requests/day
- Sales Navigator/Premium: up to 20 connection requests/day
- lower the cap if the account is new, under warning, or close to limits

### 5. Draft messages or static templates
Load `firsttouch-messaging` for tone and quality rules. In rep/BDR dynamic-row mode, draft one row at a time for approval. In static campaign-flow mode, produce static campaign templates rather than unique AI-generated messages per recipient.

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
- Reengagement: "Hi {first_name}, we did not get to connect after {prior_event}. Sharing a quick update in case this is still relevant for {company}."

### 6. Present campaign for approval
Do **not** launch automatically. Present a campaign approval summary:

```markdown
## Social campaign approval
- Campaign name:
- Goal:
- Segment criteria:
- Source path:
- Final audience count:
- Suppression/DNC skipped:
- Duplicate/recent-contact skipped:
- Sender/routing rule:
- Daily cap:
- Launch window: start date/time and end date or max run length
- FirstTouch object to create/use:
- Approval mode: row-level dynamic rows / static campaign flow
- Connection request draft or static template:
- First-message draft or static template:
- Follow-up draft or static template:
- Variables used:
- Logging / attribution tag:

Audience preview, first 20 rows max:
| # | Name | Company | Title | Source | Sender | Connection status | Status |
|---|---|---|---|---|---|---|---|

Approve this campaign? Row-level mode approves only the listed rows. Flow-level mode approves only this exact one-time audience and static templates, not future dynamic campaigns.
```

If the user approves, launch only the approved rows or approved flow. If they edit copy, update the rows/templates and re-present before launch.

### 7. Launch and log
After approval:
- before queuing per-contact dynamic actions, run `get_dynamic_action_guide`, then call `add_dynamic_action` in the supported order
- publish or queue the FirstTouch dynamic actions, flow, campaign, or audience enrollment supported by the connected MCP
- remember: publishing a flow activates it but does **not** enroll awaiting contacts; explicitly enroll approved contacts/items, then confirm they moved from awaiting to in-progress
- enroll or queue only the approved audience/rows according to daily caps
- log the campaign and attribution tag in FirstTouch and HubSpot when HubSpot is connected
- report queued, sent, blocked, failed, and completed counts
- do not convert this into an evergreen recurring campaign without a fresh approval cycle

## Output
- final segment definition and count
- source path and dependency status
- enriched/qualified audience summary
- approved row drafts or static templates
- row-level or flow-level approval summary
- launch/log confirmation
- blocked/skipped contacts summary

## Pitfalls
- letting the user start from a broad segment; narrow before building
- treating this like AI SDR with generated one-off copy per recipient
- making reps/BDRs learn flow-building when row-level dynamic actions would fit better
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
