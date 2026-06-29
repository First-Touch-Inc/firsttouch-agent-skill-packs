---
name: workspace-audit
description: Audit a FirstTouch + HubSpot workspace for readiness before launching outreach — checks MCP connections, owner coverage, LinkedIn account health, safety limits, logging setup, and data hygiene. Produces a readiness scorecard with prioritized fixes. Use when onboarding a new customer, before launching a campaign, or when outreach "isn't working" and you suspect setup issues.
metadata:
  author: firsttouch
  version: "1.0"
  category: play
  requires: [firsttouch-mcp]
---

# Workspace Audit

**Outcome:** Catch setup problems *before* they burn an account or waste sends. Produce a readiness scorecard so a customer knows exactly what to fix before going live.

## First-run onboarding gate
Before running this skill for the first time in a workspace, load `../../references/onboarding.md` and complete the onboarding questions. Do not proceed until you know: LinkedIn account type (free/basic = no connection notes and 10 connection requests/day max; Sales Navigator/Premium = connection notes available and up to 20/day), HubSpot access (MCP, service key/private app token, HubSpot list only, or none), and which play the user wants to run. Recommend high-intent plays before outbound to keep the LinkedIn account healthy. If HubSpot is unavailable, do not run HubSpot-specific steps unless the user provides a HubSpot list FirstTouch can access.

## When to use
- New customer onboarding ("are we ready to launch?")
- Before a big campaign push
- Outreach is underperforming and you suspect configuration, not copy
- Quarterly health check

## Step-by-step

### 1. Check MCP connectivity
- FirstTouch MCP reachable + returns campaign/seat data? ✅/❌
- HubSpot MCP reachable + returns contacts/owners? ✅/❌ (if a play needs it)
- Enrichment MCP connected (if AI SDR, founder AI SDR, or customer-champion plays will run)? ✅/❌/n/a

### 2. LinkedIn account health (FirstTouch)
- Seat connected and authenticated? ✅/❌
- Current usage vs. daily limits (connection requests, messages, views)
- Any active warnings/restrictions on the account? 🚩 (hard stop if yes)
- SSI / account age / warmup status

### 3. Owner coverage (HubSpot)
- % of target contacts with an assigned owner
- Orphaned contacts (no owner) → routing risk for HubSpot signal, inbound, stalled-deal, and customer-champion plays
- Owner-to-seat alignment (does the authorized LinkedIn user map to the right owners?)

### 4. Safety configuration
- Duplicate-check enabled? ✅/❌
- Cooldown windows set? ✅/❌
- Daily limit caps configured? ✅/❌
- Approval workflow defined (who approves, where)? ✅/❌

### 5. Logging & attribution readiness
- FirstTouch→HubSpot timeline logging active? ✅/❌
- Attribution tags/properties created (e.g. `linkedin_intent`, play tags)? ✅/❌
- Deals associated with contacts that have timeline activity? ✅/❌

### 6. Data hygiene
- LinkedIn URL coverage on target contacts (%)
- Duplicate contacts in HubSpot
- Stale contacts (no activity > 180 days) in active lists

### 7. Produce the readiness scorecard
```
WORKSPACE READINESS — {customer} — {date}
Overall: 72/100 — READY WITH FIXES

Connections:       ✅ 100 — FirstTouch + HubSpot connected
Account health:    ⚠  60 — Seat at 22/25 daily connects; no warnings
Owner coverage:    ❌ 40 — 38% of target contacts have no owner
Safety config:     ✅  95 — all gates configured
Logging:           ✅ 100 — timeline logging active
Data hygiene:      ⚠  55 — LinkedIn URL coverage at 61%

PRIORITY FIXES (do before launch):
1. Assign owners to 253 orphaned contacts (blocks owner-routed HubSpot plays)
2. Enrich LinkedIn URLs to >90% coverage (enables all plays)
3. Pause — seat near daily limit; resume tomorrow
```

## Output
- Readiness scorecard (score + per-area status)
- Prioritized fix list (what blocks launch, what's nice-to-have)
- Go/no-go recommendation

## Examples
**Customer:** new onboarding, eager to launch.
**Audit finds:** 38% no-owner contacts + 61% LinkedIn URL coverage → **not ready**.
**Recommendation:** fix owners + enrich URLs first (blocks owner-routed HubSpot plays). Safe to pilot warm-engager follow-up immediately if HubSpot owner routing is not required.

## Why this play wins
Most outreach failures are setup failures dressed up as copy failures. This play surfaces the real blocker in 10 minutes instead of 3 weeks of "why aren't we getting replies?"

## Pitfalls
- **Auditing once** — workspaces drift. Run quarterly + before any major push.
- **Ignoring the "no owner" red flag** — it's the #1 cause of misrouted outreach.
- **Launching with account warnings** — never. A restricted account is a hard stop.

## Reference
- MCP setup requirements: [`../../references/mcp-setup.md`](../../references/mcp-setup.md)
- Safety config the audit checks: [`../../references/safety-governance.md`](../../references/safety-governance.md)
