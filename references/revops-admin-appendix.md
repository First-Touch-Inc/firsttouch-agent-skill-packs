# RevOps / Admin Appendix

Optional depth for admins and security reviewers. Nothing here is required to run the plays - it is the evidence layer for teams that want it before scaling.

## A. HubSpot data surface

**What FirstTouch writes (via its own app integration, once HubSpot is connected and engagement tracking is enabled):**

- **Contact properties** - the `first_touch_*` property group, created automatically by the integration. Highlights: `first_touch_enrollment`, `first_touch_source`, `first_touch_score`, `first_touch_is_linkedin_connected`, first/latest connection request dates, first/latest connection accepted dates, first/latest reply dates, `first_touch_number_of_linkedin_connection_requests`, `first_touch_number_of_linkedin_messages_sent`, connecting-user fields, `first_touch_enriched_date`.
- **App events** - unique events for connection request sent, connection accepted, message sent, and reply received.
- **Timeline entries** - LinkedIn messages logged as the LinkedIn message communication object on the contact timeline.

These are the attribution backbone. Build lists and reports on them (for example, an active list where `first_touch_latest_linkedin_reply_date` is known = "replied to LinkedIn outreach"). No custom properties or tag schema needed.

**What the agent reads:** contacts, companies, deals, owners, lists, and timeline activity - for signal plays, owner routing, and duplicate checks.

## B. Minimum access model

- **Agent key: read-only by default.** The agent's HubSpot MCP connection or service key needs read access to contacts, companies, deals, owners, lists, and engagements. It does not need property-edit, deal-stage, or owner-change scopes for any play.
- **Writes happen through FirstTouch's own app integration**, not through the agent's key. The properties, events, and timeline entries in section A come from the integration.
- **One named exception:** `hubspot-social-task-runner` needs task read/write on the connected HubSpot MCP to mark tasks complete. Grant it only if the team runs that play.

## C. Exclusion governance (lightweight)

- **Owner:** RevOps or the workspace admin.
- **Source of truth:** FirstTouch Exclusion Lists - covering customers, deals in pipeline, partners, and opt-outs. Optionally mirrored from a synced HubSpot list.
- **Opt-out SLA:** same business day. A "not interested" or opt-out goes on the list before the next day's batches queue.
- **Audit:** glance monthly, and before any major rollout expansion.
- **Multiple workspaces:** if reps run separate FirstTouch workspaces, verify each one points at a consistent exclusion source before scaling.

## D. Readiness by rollout size

Readiness is proportional to blast radius - a solo founder does not need a team audit, and a 10-rep rollout should not skip one. Nothing below is enforced by the pack; it is the checklist a careful admin runs.

| Rollout | Before launch |
|---|---|
| Solo founder / 1 rep | FirstTouch MCP connected; sender seat Available; approval path understood. Start sending. |
| 2-5 rep pilot | `workspace-audit` recommended; seat statuses checked; anything skipped (approval routing, logging round-trip) marked `unverified` in the scorecard rather than assumed |
| Team rollout | Approval-routing live test (one test action arrives at the owner/Tasks); HubSpot logging round-trip verified; Exclusion Lists confirmed connected; owner-routing spot-check on a handful of shared-account contacts |
| Enterprise / security review | This appendix + section A/B as the data-flow evidence; scopes reviewed; `team-governance.md` for the operating cadence; audit evidence exported from FirstTouch/HubSpot as needed |

## E. Related references

- Operating cadence, caps, approval SLA: [`team-governance.md`](team-governance.md)
- Cooldowns, seat statuses, recovery: [`troubleshooting.md`](troubleshooting.md)
- Gates and exclusion behavior: [`safety-governance.md`](safety-governance.md)
