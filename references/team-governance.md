# Team Governance - Rolling Out to Multiple Reps

For RevOps / the workspace admin. How to run FirstTouch skills across a team without burning accounts, double-touching prospects, or losing the attribution story.

## Daily cap budget across seats

Caps are **per seat** (per rep's LinkedIn account), and FirstTouch enforces the hard max platform-side - a seat cannot exceed 20/day (free/basic) or 30/day (Sales Navigator/Premium) connection requests. Your job is managing the *recommended* level, not policing the ceiling:

- **Team budget formula:** reps x recommended cap (10 free/basic, 20 Sales Nav/Premium) = the volume you plan around.
- **Per-seat discipline:** each rep's motions share their seat's daily budget. If a rep runs AI SDR and a social campaign the same day, the combined requests should stay within their recommended cap - the agent checks the queue before approving more rows.
- **New/warming seats:** start new reps at half the recommended cap for the first two weeks.
- **Health check:** any seat with falling acceptance rates drops to half volume until it recovers. One rep's restricted account is a week of lost pipeline; volume is never worth it.

## Preventing cross-rep collisions

- One shared FirstTouch workspace gives all seats one campaign history, so the Gate 1 duplicate check sees everyone's touches. This is the recommended setup.
- If reps run **separate FirstTouch workspaces**, the duplicate check cannot see across them - the shared HubSpot `first_touch_*` properties become the only common record. Require every motion to check `first_touch_latest_linkedin_connection_request_date` / `first_touch_number_of_linkedin_messages_sent` before drafting, and keep the central DNC property authoritative (see `safety-governance.md`).
- Account-level rule: when two reps work the same company, split by persona or department *before* launching, not after the prospect gets two connection requests in one week.

## Approval SLA

- **SLA: same business day.** Rows queued in the morning are approved or rejected by end of day.
- **Escalation:** anything still awaiting approval the next morning escalates to the rep's manager or a designated backup approver. An unapproved speed-to-lead row from yesterday is already late.
- **Monday hygiene:** the weekly governance check (below) lists all approval rows older than one business day. A growing aged-approval queue means an owner is on vacation or the routing is broken - fix routing, don't let rows rot.

## Pilot-to-scale runbook

Do not roll out to the full team on day 1. The gate between each phase is evidence, not enthusiasm.

**Phase 1 - 2 reps, 2 weeks**
- Run `workspace-audit` first, including the approval-routing live test and the logging round-trip. Readiness must be READY, not "unverified."
- Reps run the daily AI SDR queue plus one warm motion, at recommended caps.
- Exit gates: zero LinkedIn warnings; 100% of sends went through approval; timeline logging and `first_touch_*` properties updating on touched contacts; reply quality sane.

**Phase 2 - add 3 more reps (5 total), 2 weeks**
- Add the signal plays (inbound, stalled-deal) with owner routing under real multi-owner conditions.
- Exit gates: no cross-rep double-touches (spot-check 20 contacts); aged-approval queue stays near zero under SLA; DNC list growing and being respected.

**Phase 3 - full team**
- Add remaining motions (social campaigns, referral, website visitor where sources exist).
- Standing cadence: weekly governance check + monthly `team-performance-report` review.

**Rollback rule:** any LinkedIn warning during pilot = that seat pauses 24-48h and restarts at half volume (see `troubleshooting.md`); two warnings across the team = pause expansion and re-audit before adding reps.

## Weekly governance check (Monday, ~15 min)

1. Queue hygiene: pending / blocked / failed counts per seat (`list_enrollments`, `list_linkedin_outreach_queue`); flag approval rows older than one business day.
2. Cap usage: any seat that hit its recommended cap 4+ days last week gets reviewed - either raise deliberately or investigate queue stacking.
3. Duplicate/suppression: check Gate 1 skip counts and DNC list growth; zero skips + zero growth usually means the checks aren't running, not that everything is clean.
4. Account health: any warnings, acceptance-rate drops, or "action required" prompts across seats - hard stop rules apply.
5. Output one line per seat: green / yellow (one issue, owned) / red (stop sends, debug now).

## Attribution for the CRO

`team-performance-report` proves the sequence (touch -> reply -> meeting -> opportunity) via the `first_touch_*` properties and timeline entries - that is influence, not causation. To make the story stronger over a quarter:

- Build HubSpot lists/reports keyed on `first_touch_latest_linkedin_reply_date` and compare meeting rates for touched vs untouched contacts in the same segment.
- Track velocity: days from `first_touch_first_linkedin_connection_request_date` to meeting booked, per flow.
- Be honest in the report: influenced pipeline, stated as influenced. Overclaiming causation is how attribution reports die in CRO meetings.
