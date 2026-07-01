---
name: icp-outbound-builder
description: Run the AI SDR motion: start from a HubSpot contact/company list or build a new ICP list via FirstTouch Discover Contacts, enrich each prospect, generate customized LinkedIn-first outreach, and queue a daily batch for human approval. Use when the user wants AI SDR, outbound against a HubSpot list, fresh daily leads, ICP prospecting, or customized outreach for contacts/companies.
metadata:
  author: firsttouch
  version: "1.1"
  category: play
  requires: [firsttouch-mcp]
---

# AI SDR / ICP Outbound Builder

**Outcome:** Produce a daily approval-ready outbound batch from either an existing HubSpot contact/company list or a newly discovered ICP list.

## First-run onboarding gate
Before running this skill for the first time in a workspace, load `../../references/onboarding.md` and complete the onboarding questions. Do not proceed until you know: LinkedIn account type (free/basic = no connection notes; recommend 10 connection requests/day and never exceed the FirstTouch max of 20/day; Sales Navigator/Premium = connection notes available; recommend 20 connection requests/day and never exceed the FirstTouch max of 30/day), HubSpot access (MCP, service key/private app token, HubSpot list only, or none), and which play the user wants to run. Recommend high-intent plays before outbound to keep the LinkedIn account healthy. If HubSpot is unavailable, this AI SDR play can still run by building a new ICP list with FirstTouch Discover Contacts.

## When to use
- "Run AI SDR"
- "Run outbound against this HubSpot list"
- "Build a daily LinkedIn outbound motion"
- "Find prospects that match this ICP and draft outreach"
- "Generate customized outreach for these contacts/companies"
- account-based outbound planning after higher-intent queues are running

## Inputs
- **Source:** existing HubSpot contact list, HubSpot company list, FirstTouch target-account set, CSV imported into FirstTouch, or a new ICP brief
- **ICP criteria:** industry, company size, geography, funding/stage, tech stack, role, seniority, exclusions
- **Persona targets:** champion / manager / VP / founder / economic buyer
- **LinkedIn account type:** free/basic or Sales Navigator/Premium
- **Automation preference:** optional agent-harness schedule/reminder such as daily Claude automation or daily ChatGPT agent; this is not a FirstTouch autonomous-send feature

## Daily volume rules for AI SDR

| LinkedIn account | Daily AI SDR connection-request row cap | Connection request note |
|---|---:|---|
| Free/basic | Recommend 10 connection-request rows/day; FirstTouch max 20/day | No note |
| Sales Navigator / Premium | Recommend 20 connection-request rows/day; FirstTouch max 30/day | No note by default for cold AI SDR; notes are allowed only when the user explicitly approves a strong reason |

These caps apply to rows that send connection requests and are intentionally conservative for a recurring outbound motion. Already-connected first-message rows draw from the separate message cap and still require approval. If AI SDR and another play run on the same day, the combined connection requests should stay within the recommended 10 or 20 daily connection-request cap unless the user explicitly approves going higher; never exceed the FirstTouch max of 20/day free/basic or 30/day Sales Navigator/Premium. Before adding rows, inspect the sender's LinkedIn outreach queue/status for active, in-queue, blocked/review-required, and today's completed/pending connection requests. If the account is new, warned, or acceptance/reply rates drop, lower the cap and pause for human review.

## Default outreach plan

For every approved AI SDR prospect, first check LinkedIn connection status:

| Connection status | Sequence |
|---|---|
| Already connected | Send the first message, wait 2 days, then send one follow-up message if there is no reply. |
| Not connected | Send a blank connection request with no note. After the prospect accepts, send the first message, wait 2 days, then send one follow-up message if there is no reply. |

**Message rules for AI SDR:**
- First message and follow-up are each **2 sentences max**.
- Reference one real signal that might point to the prospect needing the user's solution.
- Use a lightweight ask CTA. Do **not** ask for a meeting in the connection request, first message, or first follow-up.
- Do **not** use em dashes in any drafted outreach copy.
- Do not fabricate personalization. Use only HubSpot, FirstTouch, enrichment, or user-provided data.

## Step-by-step

### 1. Choose the source path

**Path A — HubSpot list exists:**
- Open the HubSpot contact or company list the user provides.
- If it is a company list, select the best contacts at each company using the target personas.
- Capture contact/company fields, owner, lifecycle/deal context, prior activity, and LinkedIn URL if present.

**Path B — no HubSpot access or no existing list:**
- Ask the user for their ideal ICP: target industries, company size, geography, titles/seniority, exclusions, and any must-have signals.
- Use **FirstTouch Discover Contacts** to build a prospect list from that ICP.
- Run Gate 3a from `../../references/safety-governance.md`: preview a small sample, state estimated maximum discovery/enrichment credits, and get approval before larger imports because discovery/enrichment can consume FirstTouch credits.
- Save the discovered contacts into a FirstTouch audience or list for future daily runs.

### 2. Enrich every candidate
For each contact/company, enrich missing fields before drafting. If no enrichment MCP is connected, use HubSpot, FirstTouch, CSV, or user-provided fields; skip or queue records missing a usable LinkedIn URL rather than fabricating data:
- LinkedIn URL and current title
- company domain, size, industry, location
- relevant company/person signal when available
- work email/phone only if needed for routing or downstream systems

### 3. Filter and prioritize
Exclude anyone who is:
- suppressed, opted out, unsubscribed, on a DNC list, or blocked by Gate 0 in `../../references/safety-governance.md`
- already in an active sequence or recently contacted
- missing a usable LinkedIn profile after enrichment
- outside ICP
- owned by someone else without approval to route through that owner

Rank the remaining candidates by ICP fit, signal strength, seniority, and account priority.

### 4. Generate customized outreach
For the top daily batch only, load `firsttouch-messaging` and generate customized LinkedIn-first outreach for each prospect:
- check whether the prospect is already connected on LinkedIn
- if already connected: draft the first message and a 2-day follow-up
- if not connected: queue a blank connection request with **no note** by default for cold AI SDR, then append the first message to the `connection_accepted` branch and draft the 2-day follow-up
- keep every message to 2 sentences max
- reference a real signal that might point to the prospect needing the user's solution
- use a lightweight ask CTA, not a meeting ask
- never use em dashes in drafted outreach copy
- never fabricate a personalization fact; use only HubSpot, FirstTouch, enrichment, or user-provided data

### 5. Present the daily batch for approval
Do **not** send automatically. Output an approval table:

| # | Prospect | Company | Source | Why them | Connection status | Enriched signal | First message | 2-day follow-up | Action | Owner | Status |
|---|---|---|---|---|---|---|---|---|---|---|---|

Every row should be marked `awaiting approval`. Each first-touch outbound row requires individual approval; do not treat one table-level approval as approval to send the whole batch.

### 6. After approval → queue execution
After human approval:
- before queuing per-contact dynamic actions, run `get_dynamic_action_guide`, then call `add_dynamic_action` in the supported order
- if a LinkedIn message should only send after a connection request is accepted, append it to the `connection_accepted` branch rather than queueing it as an immediate message
- add approved contacts to the right FirstTouch flow/campaign, or queue dynamic actions
- enforce duplicate checks, account-safety limits, and approval status from `../../references/safety-governance.md`
- log execution and outcomes back to HubSpot when HubSpot is connected
- keep rejected contacts out of the next daily batch unless the user asks to revisit them

### 7. Recommend daily automation
Recommend that the user run this as a daily recurring motion:
- **Claude:** set up a daily automation that pulls the next list slice / discovers fresh ICP contacts, enriches, drafts, and presents the approval table.
- **ChatGPT:** set up a daily agent with the same job: refresh leads, enrich, draft, and prepare approvals.

For unattended daily runs, define an approval owner, where the approval queue is delivered, when aged approvals alert RevOps/manager, and where the audit trail is stored before enabling the schedule.

Default daily automation prompt:
> "Run the FirstTouch AI SDR play for today. Use my saved ICP/list, enrich fresh contacts, prepare up to my daily cap, and show me the approval table. Do not send anything until I approve."

## Output
- source summary: HubSpot list or newly discovered ICP list
- enriched account/contact table
- daily AI SDR batch capped at 10 free/basic or 20 Sales Navigator/Premium contacts
- customized first message and 2-day follow-up for each prospect
- approval table ready for human review
- optional daily automation/agent setup prompt

## Pitfalls
- treating AI SDR as a one-time bulk blast instead of a daily approval queue
- exceeding the recommended 10/20 daily AI SDR connection-request caps, or the FirstTouch hard max of 20/30
- drafting for un-enriched contacts with weak or fabricated personalization
- requiring HubSpot when the user has no HubSpot list; use Discover Contacts from their ICP instead
- skipping duplicate checks before adding contacts to a flow
- sending without approval

## Reference
- Onboarding: [`../../references/onboarding.md`](../../references/onboarding.md)
- Messaging: [`../../references/messaging-framework.md`](../../references/messaging-framework.md)
- Safety and approval gates: [`../../references/safety-governance.md`](../../references/safety-governance.md)
- If only a company/account is known, use the target personas and available FirstTouch/HubSpot contact data to select likely stakeholders.
