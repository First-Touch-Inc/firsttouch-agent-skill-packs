# Team Governance - Rolling Out to Multiple Reps

For RevOps / the workspace admin. How to run FirstTouch skills across a team.

## Limits are handled for you

FirstTouch enforces each seat's configured sending limits automatically. Reps can adjust their volume in the FirstTouch web app (Settings -> User Accounts -> Daily limits), and FirstTouch will not push a seat past its peak limits (20/day free-basic, 30/day Sales Navigator/Premium connection requests). If a seat hits its daily limit, it goes on **cooldown** - sends resume in the next window. Frequent cooldowns just mean that seat should run a lower daily volume so the queue flows evenly.

Account health still depends on quality, not just volume: keep acceptance rates healthy (above ~40% per FirstTouch Trust & Safety guidance; below ~25% is the danger zone), keep copy personal, and make sure no other automation tool runs on the same LinkedIn account. If a seat shows Action required, Disconnected, or Restricted in Social settings, pause it until resolved (see `troubleshooting.md`).

Planning guidance: recommend 10/day (free/basic) or 20/day (Sales Navigator/Premium) per rep, and plan team volume as reps x recommended cap. New reps can start at half volume for their first two weeks while they calibrate messaging.

## Keeping outreach clean across the team

- **Exclusion Lists:** connect FirstTouch Exclusion Lists so no motion touches current customers, deals in pipeline, or opted-out contacts. Gate 0 checks them on every play.
- **Duplicate checks:** FirstTouch campaign history backs the Gate 1 duplicate/recent-contact check, so reps working the same accounts do not double-touch prospects.
- **Auto-tagging:** FirstTouch auto-tags every enrollment - no custom tag schema needed. When the HubSpot integration is connected and engagement tracking (a FirstTouch setting, configured in FirstTouch, not HubSpot) is enabled, it writes activity back automatically (contact properties, app events for connect request / accept / message sent / reply received, and timeline entries).

## Approval SLA (team policy, not product enforcement)

- **Set the expectation: same business day.** Rows queued in the morning are approved or rejected by end of day.
- Escalation is manual - FirstTouch does not auto-reassign or escalate a stale approval task. Make it team policy that anything still awaiting approval the next morning goes to the rep's manager or a designated backup approver; an unapproved speed-to-lead row from yesterday is already late.

## Rollout path

A phased rollout keeps things easy to coach:

1. **Start with 1-2 reps** running the daily AI SDR queue plus one warm motion. Optional: run `workspace-audit` first if you want to verify MCP connections and HubSpot logging before scaling.
2. **Add the next group** once the first reps have a smooth weekly rhythm - approvals moving same-day, replies coming in, logging visible in HubSpot.
3. **Full team** once the signal plays (inbound, stalled-deal) are routing to the right owners.

## Weekly check (Monday, ~10 min)

1. Queue hygiene: pending / blocked counts per seat (`list_enrollments`, `list_linkedin_outreach_queue`); nudge any approval rows older than a business day.
2. Volume and health: seats on frequent cooldown should lower daily volume; seats with strong acceptance (>40%) can step up toward the recommended cap; any seat showing Action required / Disconnected / Restricted pauses until resolved.
3. Results: replies and meetings by seat - coach messaging where acceptance is fine but replies lag.

## Attribution for the CRO

`team-performance-report` pulls sends, accepts, replies, and meetings by flow, sender, and date. Because FirstTouch auto-tags every enrollment and logs to HubSpot, you can compare touched vs untouched contacts in the same segment and track time from first touch to meeting. Report influenced pipeline as influenced - the honest framing is also the durable one.
