---
name: champion-mapper
description: Map the likely internal champions and decision-makers across a target account by combining HubSpot company/contact data with LinkedIn relationships and enrichment. Produces a stakeholder map with roles, influence, relationship status, and a recommended engagement order. Use when the user wants to map an account, find champions, do account-based outreach, or figure out "who else should I talk to at this account."
metadata:
  author: firsttouch
  version: "1.0"
  category: play
  requires: [firsttouch-mcp, hubspot-mcp]
---

# Play 03 — Champion Mapper

**Outcome:** For a target account, produce a stakeholder map showing who the likely champions are, their influence, current relationship status, and the order to engage them.

## First-run onboarding gate
Before running this skill for the first time in a workspace, load `../../references/onboarding.md` and complete the onboarding questions. Do not proceed until you know: LinkedIn account type (free/basic = no connection notes and 10 connection requests/day max; Sales Navigator/Premium = connection notes available and up to 20/day), HubSpot access (MCP, service key/private app token, HubSpot list only, or none), and which play the user wants to run. Recommend high-intent plays before outbound to keep the LinkedIn account healthy. If HubSpot is unavailable, do not run HubSpot-specific steps unless the user provides a HubSpot list FirstTouch can access.

## When to use
- "Map the buying committee at Acme"
- "Who else should I be talking to at this account?"
- ABM account planning before outreach
- A deal is stuck with one contact and you need multi-thread

## Inputs
- **Target account(s):** company name or HubSpot company ID
- **Goal:** new logo / expand / unstick a deal
- **Known contacts:** any existing relationships to anchor the map

## Step-by-step

### 1. Pull account context (HubSpot MCP)
Get the company record: industry, size, tech stack, lifecycle stage, associated contacts, open deals, owner, recent activity. Note who's already in HubSpot.

### 2. Enumerate stakeholders (HubSpot + enrichment)
Find people at the account across the buying motion:
- **Economic buyer** (VP/C-level who owns the budget)
- **Champion** ( practitioner who feels the pain, will advocate internally)
- **Influencers** (peers whose opinion matters)
- **Blockers / end-users** (who must not be ignored)

Use HubSpot contacts first, then enrichment (Clay/Surfe MCP) to fill gaps — LinkedIn URLs, titles, tenure.

### 3. Assess relationship status (FirstTouch MCP)
For each stakeholder:
- Connected on LinkedIn? (yes/no)
- Prior DMs / engagement history?
- In any active sequence?
- Owner in HubSpot?

### 4. Score influence + accessibility
Rate each stakeholder:
- **Influence** (High/Med/Low) — do they sway the decision?
- **Accessibility** (High/Med/Low) — can you realistically reach them?
- **Warmth** (Cold/Warm/Hot) — existing relationship strength

Champions = high accessibility + practitioner-level + feels the pain.

### 5. Produce the stakeholder map
A table + recommended sequence:
| Stakeholder | Title | Role | Influence | Accessibility | Warmth | Owner | Next action |

Recommend an **engagement order**: typically Champion first (to gain intel + internal advocate) → Influencers → Economic buyer (with champion's help).

### 6. Draft initial outreach (load `firsttouch-messaging`)
For the top 1–3 stakeholders, draft connection requests/openers gated for approval. Defer the rest until the champion engages.

### 7. Log the map to HubSpot
Write the stakeholder map as a note on the company record (or a custom "account map" property) so it persists.

## Output
- **Account stakeholder map** (table + engagement order)
- Drafted outreach for top stakeholders (gated)
- Map logged to the HubSpot company record

## Examples
**Account:** Acme (300 employees, SaaS, expanding sales team)
**Map output:** Champion = Dana (Dir Sales Ops, accessible, feels the attribution pain) → engage first. Economic buyer = VP Sales (high influence, low accessibility) → engage via Dana after she's warm.

## Why this play wins
Most outreach single-threads one contact and stalls. This play systematizes **multi-threading** — the single biggest lever on enterprise win rate.

## Pitfalls
- **Skipping the champion** — going straight to the VP cold almost never works. Start where the pain is.
- **Stale enrichment** — titles change. Verify tenure/role before drafting.
- **Not logging the map** — if it lives only in chat, the next rep starts over. Always write it to HubSpot.

## Reference
- Messaging: [`../../references/messaging-framework.md`](../../references/messaging-framework.md)
- System model: [`../../references/system-grounding.md`](../../references/system-grounding.md)
