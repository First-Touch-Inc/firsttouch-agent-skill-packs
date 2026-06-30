---
name: team-performance-report
description: Pull FirstTouch team metrics for a selected date range, flow, sender, or campaign cohort, then summarize sends, replies, reply sentiment where available, meetings booked, opportunities, and HubSpot logging coverage. Use when RevOps asks what is working, needs a monthly attribution report, or wants performance by flow/sender/date after launch.
metadata:
  author: firsttouch
  version: "1.1"
  category: play
  requires: [firsttouch-mcp]
---

# Team Performance Report

**Outcome:** Give RevOps a recurring performance report, not just a setup audit: what ran, who sent it, how prospects engaged, and whether the results are attributable.

## First-run onboarding gate
Run the first-run gate in `../../references/onboarding.md` before first use, unless onboarding has already been completed in this session. Confirm reporting date range, flows/campaigns to include, and whether HubSpot is connected for opportunity/pipeline reconciliation.

## When to use
- "Show me FirstTouch performance for the last 30 days"
- "Which flows are driving replies or meetings?"
- "Report by sender for this month"
- "Prove whether the rollout is working"
- Monthly or quarterly RevOps attribution reviews

## Inputs
- **Date range:** default trailing 30 days
- **Scope:** all team, selected flow plans, selected senders, or selected cohort/tag when available
- **Breakdown:** by flow, sender, day/week/month, or source
- **HubSpot status:** connected or not connected for opportunity/pipeline reconciliation

## Step-by-step

### 1. Define report scope
Capture the requested date range, flow/campaign names, sender/team members, and whether the user wants totals, trends, or per-sender rankings. If scope is missing, default to trailing 30 days and all accessible FirstTouch team activity.

### 2. Pull FirstTouch team metrics
Use the FirstTouch team metrics capability for the selected date range and filters. Include, when available:
- actions sent
- email and LinkedIn engagement
- replies
- reply sentiment
- meetings booked
- opportunities
- flow/source and sender breakdowns
- chart/trend buckets only when the user asks for a trend

If metrics are unavailable or permissions are missing, mark the report `unverified` and state the missing access rather than inventing numbers.

### 3. Reconcile attribution coverage
If HubSpot is connected, compare performance reporting against HubSpot logging coverage and opportunity visibility. If HubSpot is not connected, report FirstTouch outcomes only and state that CRM opportunity/pipeline reconciliation is unavailable.

### 4. Produce the RevOps report
Use this structure:

```markdown
# FirstTouch Team Performance — {date_range}
Scope: {flows/senders/team}
HubSpot reconciliation: connected / not connected / unverified

## Executive summary
- Sends:
- Replies:
- Positive replies / sentiment:
- Meetings booked:
- Opportunities:
- Best-performing flow/sender:
- Biggest blocker or data gap:

## Breakdown
| Flow/source | Sender | Sends | Replies | Positive | Meetings | Opportunities | Notes |
|---|---|---:|---:|---:|---:|---:|---|

## Attribution coverage
- FirstTouch metrics available: yes/no
- HubSpot logging coverage: yes/no/n/a
- Missing data:

## Recommended RevOps actions
1. Keep / scale:
2. Fix / pause:
3. Next review date:
```

## Pitfalls
- Do not report invented metrics. If FirstTouch team metrics or HubSpot opportunity data is unavailable, say so.
- Do not claim arbitrary inbox access. Use FirstTouch-managed outreach metrics only.
- Do not mix setup readiness with outcome performance. For setup checks, run `workspace-audit`; for outcomes, run this skill.

## Reference
- MCP setup requirements: [`../../references/mcp-setup.md`](../../references/mcp-setup.md)
- Safety gates: [`../../references/safety-governance.md`](../../references/safety-governance.md)
