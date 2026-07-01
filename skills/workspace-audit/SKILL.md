---
name: workspace-audit
description: Audit a FirstTouch + HubSpot workspace for readiness before launching outreach - checks MCP connections, owner coverage, LinkedIn account health, safety limits, logging setup, and data hygiene. Produces a readiness scorecard with prioritized fixes. Use when onboarding a new customer, before launching a campaign, or when outreach "isn't working" and you suspect setup issues.
metadata:
  author: firsttouch
  version: "1.1"
  category: play
  requires: [firsttouch-mcp]
---

# Workspace Audit

**Outcome:** Catch setup problems *before* they burn an account or waste sends. Produce a readiness scorecard so a customer knows exactly what to fix before going live.

## First-run onboarding gate
Before running this skill for the first time in a workspace, load `../../references/onboarding.md` and complete the onboarding questions. Do not proceed until you know: LinkedIn account type (free/basic = no connection notes; recommend 10 connection requests/day and never exceed the FirstTouch max of 20/day; Sales Navigator/Premium = connection notes available; recommend 20 connection requests/day and never exceed the FirstTouch max of 30/day), HubSpot access (MCP, service key/private app token, HubSpot list only, or none), and which play the user wants to run. Recommend high-intent plays before outbound to keep the LinkedIn account healthy. If HubSpot is unavailable, do not run HubSpot-specific steps unless the user provides a HubSpot list FirstTouch can access.

## When to use
- New customer onboarding ("are we ready to launch?")
- Before a big campaign push
- Outreach is underperforming and you suspect configuration, not copy
- Quarterly health check

## Step-by-step

Every check below is one of two kinds, and the scorecard must keep them separate so a "ready" score can never hide unverified areas:

- **[AUTO]** - verifiable through the connected MCPs. Mark ✅/❌ from live data only.
- **[MANUAL]** - needs the user or the FirstTouch/HubSpot dashboard. Mark `manual check required`; never guess, and never count an unchecked item toward the readiness score.

### 1. Check MCP connectivity [AUTO]
- FirstTouch MCP reachable + returns campaign/seat data? ✅/❌
- HubSpot MCP reachable + returns contacts/owners? ✅/❌ (if a play needs it)
- FirstTouch enrichment available and credits understood for AI SDR? ✅/❌/n/a; external Clay/Surfe enrichment MCP is optional, not required

### 2. LinkedIn account health (FirstTouch) [AUTO + MANUAL]
- Seat connected and authenticated? ✅/❌
- Current usage vs. daily limits (connection requests, messages, views) when available from FirstTouch
- Any active warnings/restrictions on the account? 🚩 (hard stop if yes)
- SSI / account age / warmup status - manual/dashboard check unless FirstTouch exposes it directly
- If FirstTouch cannot return a metric, ask the user to check the FirstTouch dashboard and mark that metric `manual check required`

### 3. Owner coverage (HubSpot) [AUTO when HubSpot connected, else MANUAL]
- % of target contacts with an assigned owner when HubSpot is connected
- Orphaned contacts (no owner) → routing risk for HubSpot signal, inbound, stalled-deal, and other owner-routed plays
- Owner-to-seat alignment (does the authorized LinkedIn user map to the right owners?)
- If HubSpot or owner reports are unavailable, ask the user/RevOps to provide an owner export and mark this area `manual check required`, not failed

### 4. Safety configuration [AUTO]
- Duplicate-check enabled? ✅/❌
- Cooldown windows set? ✅/❌
- Daily limit caps configured? ✅/❌
- Approval workflow defined (who approves, where)? ✅/❌

### 5. Logging, replies & attribution readiness [AUTO + MANUAL test round-trip]
- FirstTouch→HubSpot timeline logging active? ✅/❌
- HubSpot write scope for timeline tags/properties confirmed? ✅/❌
- Test action round-trip completed: create/approve one safe test action to a contact/record explicitly designated by the user as a test recipient, or to the operator's own profile. Never use a live prospect just to verify logging. Then verify the HubSpot timeline/logging record and FirstTouch reply/status visibility came back as expected. If the team will not run a test action, mark attribution/logging `unverified`, not `ready`.
- Attribution tags/properties created or writable (e.g. `linkedin_intent`, play tags)? ✅/❌/manual HubSpot check
- FirstTouch reply tracking visible for outreach actions? ✅/❌ - the agent cannot read arbitrary inbox history, but FirstTouch-tracked outreach can surface reply/engagement status for actions it manages.
- Deals associated with contacts that have timeline activity? ✅/❌

### 6. Queue/status hygiene [AUTO]
- Current outreach queues: pending, blocked, review-required, failed, canceled, completed counts when available
- Stuck approval rows or actions older than the team's SLA? list them as queue hygiene issues, not automated alerts unless an alerting workflow is explicitly configured
- Email/LinkedIn queue blockers: missing account, missing recipient/profile, approval required, account readiness, scheduler/limit delay

### 7. Data hygiene [AUTO when HubSpot connected, else MANUAL]
- LinkedIn URL coverage on target contacts (%)
- Duplicate contacts in HubSpot
- Stale contacts (no activity > 180 days) in active lists

### 8. Produce the two-part readiness scorecard
Present verified and unverified areas separately. Replace every number with live workspace data before presenting; never score an unverified area.

```
WORKSPACE READINESS - {customer} - {date}
Verified score: {x}/100 across {n} MCP-verified areas - {READY / READY WITH FIXES / NOT READY}

VERIFIED (live MCP data)
  Connections:     ✅ - FirstTouch + HubSpot connected
  Owner coverage:  ❌ - 38% of target contacts have no owner
  Safety config:   ✅ - all gates configured
  Queue hygiene:   ⚠ - 14 rows pending approval >2 days

MANUAL CHECK REQUIRED (not counted in score)
  Account warnings/SSI: user must confirm in FirstTouch dashboard
  Logging round-trip:   pending user-designated test contact

PRIORITY FIXES (do before launch):
1. Assign owners to orphaned contacts (blocks owner-routed plays)
2. Confirm no LinkedIn account warnings before any volume
```

If HubSpot is not connected, mark CRM-only rows `N/A - HubSpot not connected` rather than failing the workspace, and recommend piloting FirstTouch-only plays (warm engagers, social campaigns from Discover/imported lists, AI SDR via Discover Contacts) while HubSpot gets connected.

### 9. Outcome metrics handoff
For recurring attribution reporting, run `team-performance-report`. In this readiness audit, only verify whether FirstTouch team metrics access and HubSpot logging coverage are available; do not treat a setup audit as the recurring report itself.

## Output
- Readiness scorecard (score + per-area status)
- Prioritized fix list (what blocks launch, what's nice-to-have)
- Go/no-go recommendation
- Outcome metrics snapshot: sends, replies, sentiment, meetings, opportunities by flow/sender/date when available

## Examples
**Customer:** new onboarding, eager to launch.
**Audit finds:** 38% no-owner contacts + 61% LinkedIn URL coverage → **not ready**.
**Recommendation:** fix owners + enrich URLs first (blocks owner-routed HubSpot plays). Safe to pilot warm-engager follow-up immediately if HubSpot owner routing is not required.

## Why this play wins
Most outreach failures are setup failures dressed up as copy failures. This play surfaces the real blocker in 10 minutes instead of 3 weeks of "why aren't we getting replies?"

## Pitfalls
- **Auditing once** - workspaces drift. Run quarterly + before any major push.
- **Ignoring the "no owner" red flag** - it's the #1 cause of misrouted outreach.
- **Launching with account warnings** - never. A restricted account is a hard stop.

## Reference
- MCP setup requirements: [`../../references/mcp-setup.md`](../../references/mcp-setup.md)
- Safety config the audit checks: [`../../references/safety-governance.md`](../../references/safety-governance.md)
