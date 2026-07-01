# HubSpot Properties & Scopes - What FirstTouch Reads and Writes

For the HubSpot admin connecting FirstTouch. This is the exact data surface: what FirstTouch pushes into your portal, what the agent reads, and the minimum scopes to grant.

## What FirstTouch writes to HubSpot

FirstTouch pushes three kinds of data when the FirstTouch-HubSpot integration is connected:

1. **Contact properties** (the `first_touch_*` property group - created automatically by the integration)
2. **App events** - unique events for: connection request sent, connection accepted, message sent, reply received
3. **Timeline entries** - LinkedIn messages logged as the default LinkedIn message communication object on the contact timeline

### FirstTouch contact properties

| Property | What it tracks |
|---|---|
| `first_touch_enrollment` | Which FirstTouch flow/enrollment the contact is in |
| `first_touch_source` | Where FirstTouch sourced the contact |
| `first_touch_score` | FirstTouch fit/engagement score |
| `first_touch_score_evidence` | Why the score is what it is |
| `first_touch_action_plan_signal` | The signal that triggered the action plan |
| `first_touch_is_linkedin_connected` | Whether the contact is connected to a team seat |
| `first_touch_first_linkedin_connection_request_date` | First connection request sent |
| `first_touch_latest_linkedin_connection_request_date` | Most recent connection request sent |
| `first_touch_first_linkedin_connection_accepted_date` | First accept |
| `first_touch_latest_linkedin_connection_accepted_date` | Most recent accept |
| `first_touch_number_of_linkedin_connection_requests` | Total connection requests to this contact |
| `first_touch_number_of_linkedin_messages_sent` | Total LinkedIn messages sent |
| `first_touch_first_linkedin_reply_date` | First reply received |
| `first_touch_latest_linkedin_reply_date` | Most recent reply received |
| `first_touch_first_linkedin_connection_user` | Which team member first connected |
| `first_touch_latest_linkedin_connection_user` | Most recent connecting team member |
| `first_touch_linkedin_connected_hubspot_users` | All HubSpot users connected to this contact |
| `first_touch_linkedin_connected_accounts` | All connected LinkedIn seats |
| `first_touch_enriched_date` | When FirstTouch last enriched the contact |
| `first_touch_initial_activity_date` | First FirstTouch activity on the contact |
| `firsttouch_plan` | FirstTouch plan/tier context |

These properties are the **attribution backbone**: reports, list triggers, and duplicate checks should key off them rather than inventing custom tags. Example: a "replied to LinkedIn outreach" active list is simply `first_touch_latest_linkedin_reply_date` is known.

## What the agent reads (and the properties plays depend on)

| Property | Needed for | Native or setup |
|---|---|---|
| LinkedIn URL (`hs_linkedin_url` or your custom equivalent) | Every outreach play - contacts without one are skipped | Native/varies; enrichment fills gaps |
| Contact owner (`hubspot_owner_id`) | Owner routing (Gate 2) | Native |
| Lifecycle stage, deal stage, last activity date | Signal plays, stalled-deal lists | Native |
| `do_not_contact` (or your DNC field) | Gate 0 suppression | **Create if missing** - see the DNC section in `safety-governance.md` |
| The `first_touch_*` properties above | Duplicate checks, attribution, reply-based lists | Created by the FirstTouch integration |

## Minimum HubSpot scopes to grant

For the HubSpot MCP or a service key used by the agent:

| Scope | Level | Why |
|---|---|---|
| Contacts, companies, deals, owners, lists | **Read** | Signal plays, routing, list sources |
| Timeline/engagements | **Read** | Duplicate and recent-touch checks |
| Tasks | Read (+ write only if using `hubspot-social-task-runner`) | Task runner marks tasks complete |
| Property edits, deal-stage changes, owner changes | **Do not grant** | No play needs them; the FirstTouch integration handles its own property writes through its app connection, not through the agent's key |

**Rule of thumb:** the agent's HubSpot access is read-only; FirstTouch's own app integration does the writing. A read-only service key is enough for every play except the task runner.

## Verifying the write path

Before trusting attribution, run the round-trip test in `workspace-audit`: one approved test action to a designated test contact, then confirm the timeline entry and the `first_touch_*` date properties updated. If they did not, the FirstTouch-HubSpot integration is not fully connected - fix that before running volume, or reports will undercount everything.
