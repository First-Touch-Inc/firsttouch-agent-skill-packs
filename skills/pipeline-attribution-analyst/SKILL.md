---
name: pipeline-attribution-analyst
description: Measure and report which LinkedIn/social touches influenced HubSpot pipeline — meetings booked, deals created, revenue touched — by joining FirstTouch activity data with HubSpot deal/contact records. Produces attribution reports and identifies the plays and signals driving revenue. Use when the user wants to prove LinkedIn ROI, measure social selling impact, attribute pipeline to outreach, or report on what's working.
metadata:
  author: firsttouch
  version: "1.0"
  category: play
  requires: [firsttouch-mcp, hubspot-mcp]
---

# Play 07 — Pipeline Attribution Analyst

**Outcome:** Prove, with data, that LinkedIn outreach drove pipeline. Turn "social selling" from a vibe into a number.

## First-run onboarding gate
Before running this skill for the first time in a workspace, load `../../references/onboarding.md` and complete the onboarding questions. Do not proceed until you know: LinkedIn account type (free/basic = no connection notes and 10 connection requests/day max; Sales Navigator/Premium = connection notes available and up to 20/day), HubSpot access (MCP, service key/private app token, HubSpot list only, or none), and which play the user wants to run. Recommend high-intent plays before outbound to keep the LinkedIn account healthy. If HubSpot is unavailable, do not run HubSpot-specific steps unless the user provides a HubSpot list FirstTouch can access.

## When to use
- "Did LinkedIn actually drive pipeline this quarter?"
- "Show me the ROI of our social selling"
- Monthly/quarterly GTM review
- Justifying the FirstTouch seat spend to leadership
- Deciding which plays to double down on

## When NOT to use
- You only need raw activity counts (that's a FirstTouch dashboard, not attribution)
- Real-time send monitoring (that's play 05)

## Step-by-step

### 1. Define the window & pipeline scope (HubSpot MCP)
- Time range (e.g. last quarter)
- Pipeline stages in scope (e.g. everything from "Qualified" onward)
- Deal statuses (open + won; optionally lost for learning)

### 2. Pull LinkedIn activity (FirstTouch MCP)
All FirstTouch-logged touches in the window: connection requests, messages, replies, by contact/company/date, tagged by originating play + signal.

### 3. Join to HubSpot pipeline
For each deal in scope, check whether any associated contact received a FirstTouch touch **before** the deal's key milestones (created, stage advancement, close). Classify:
- **Directly influenced** — touch preceded the milestone within an influence window (default 30 days)
- **Touched, no clear influence** — touch logged but timing ambiguous
- **Untouched** — no FirstTouch activity on any associated contact

### 4. Compute the metrics
| Metric | Definition |
|--------|-----------|
| **Pipeline touched** | $ amount of deals with ≥1 influencing touch |
| **Meetings influenced** | Meetings whose booking contact was touched first |
| **Touch-to-meeting rate** | % of touched contacts who booked |
| **Revenue won (influenced)** | $ won where a touch preceded close |
| **Cost per influenced meeting** | FirstTouch seat cost ÷ influenced meetings |
| **By-play breakdown** | Which play (01–06,10) generated the influencing touches |
| **By-signal breakdown** | Which trigger signals (play 02) converted best |

### 5. Identify what's working / not
- Top-performing play by influenced pipeline
- Top-performing signal type
- Plays with high activity but low influence (candidates to cut)
- Segments (ICP tier, seniority) where social converts best

### 6. Produce the report
A clear written report + table:
```
Q3 LinkedIn Attribution Report
Pipeline touched by social: $1.2M (38% of total open pipeline)
Meetings influenced: 41
Top play: 02 (HubSpot Signal → Touch) — 14 influenced meetings
Top signal: "Form fill → connect" — 29% touch-to-meeting rate
Revenue won (influenced): $310k
Recommendation: double down on play 02 for SDR team; sunset high-volume play 01 T3 tier.
```

### 7. Recommend actions
Translate findings into next steps (which plays to scale, which signals to prioritize, where to add seats).

## Output
- Attribution report (metrics + by-play/by-signal breakdown)
- Ranked list of what's working
- Concrete recommendations

## Examples
**Question:** "Did our LinkedIn outreach matter last quarter?"
**Report finds:** 38% of open pipeline had an influencing FirstTouch touch; play 02 alone drove 14 meetings at $0.42 cost-per-meeting vs. $1.80 for paid ads. → Recommend expanding play 02 to the full SDR team.

## Why this play wins
This is the moat. Competitors help you *send* outreach; FirstTouch lets you **prove it drove revenue**, tied to the CRM system of record. That's what unlocks budget, seats, and enterprise deals.

## Methodology notes
- **Influence ≠ causation.** Be honest: a touch *preceding* a milestone is correlation. State the influence window and avoid overclaiming.
- **Attribution model:** default "first-touch-in-window influences subsequent milestones." Configurable.
- **Data hygiene dependency:** this play only works if plays 01–06 actually logged to HubSpot (Gate 5). Garbage in, garbage out.

## Pitfalls
- **Overclaiming causation** — "LinkedIn drove the deal" is rarely provable. Use "influenced."
- **Ignoring untouched won deals** — some revenue has zero social touch; report both sides.
- **Short windows** — 7-day influence windows undercount; 30+ is more realistic for B2B.

## Reference
- System model (the 3 layers): [`../../references/system-grounding.md`](../../references/system-grounding.md)
- The plays whose data this analyzes: skills 01–06, 10
