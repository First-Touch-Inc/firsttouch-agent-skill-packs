# Troubleshooting - When a Play Goes Wrong

Operational playbook for the failures customers actually hit. Load this when an MCP call fails, LinkedIn pushes back, sends stall, or something reached a contact it shouldn't have. For setup problems, start with `mcp-setup.md`; this doc covers what breaks *after* setup.

**Still stuck?** Ask in the FirstTouch Slack community (`firsttouch-workspace.slack.com`) or use chat support inside the FirstTouch app.

---

## MCP connection failures

| Symptom | Likely cause | What to do |
|---------|-------------|-----|
| Agent says it "can't send" or FirstTouch tools error | FirstTouch MCP not connected or OAuth expired | Re-authenticate in the agent's connector/workspace settings, then retry the failed step only - do not re-run the whole play (risk of duplicate queueing). |
| FirstTouch tools return permission errors | Connected user lacks workspace rights | Check `get_auth_scopes`; ask a FirstTouch workspace admin to grant the missing scope. |
| Agent ignores owner routing | HubSpot MCP missing or no owner read scope | Reconnect HubSpot MCP with owner read scope. Until then, treat every contact as "owner unknown" and require explicit approval before touching it. |
| Agent drafts but never logs to HubSpot | Logging not enabled / wrong HubSpot portal | Confirm the FirstTouch↔HubSpot sync is active and pointed at the right portal. |
| HubSpot task tools fail in the social task runner | Connected HubSpot MCP lacks task read/write | Verify task access per `mcp-setup.md`; until write access exists, output the completed-actions table and ask the user to mark tasks complete manually. |

**Rule for any MCP failure mid-play:** stop queueing new actions, report exactly which step failed and which contacts were already queued, and wait for the human. Never re-run enrichment or discovery blindly - it spends credits.

---

## LinkedIn warnings and restrictions

`safety-governance.md` says warnings are a **hard stop**. Here is what a hard stop means in practice:

1. **Stop all queued sends immediately** - pause the flow (`manage_flow_publication`) or hold the daily approval batch. Do not "finish today's batch."
2. **Tell the user what happened** and which motion was running when the warning appeared.
3. **Wait at least 24-48 hours** with zero connection requests before resuming anything.
4. **Resume at half volume**: if the account was at the recommended cap (10/day free-basic, 20/day Sales Navigator/Premium), restart at 5/day or 10/day respectively and hold there for a week.
5. **Escalate instead of resuming** if any of these are true: a second warning, an "action required" prompt from LinkedIn, or a restriction (not just a warning). The user should contact LinkedIn support before any further automation runs on that seat.

**Soft signals that deserve the same treatment before LinkedIn complains:** acceptance rate dropping below ~20%, reply quality falling off, or several "I don't know this person" responses. Lower the cap and slow down - cheaper than a restriction.

---

## Sends queued but nothing goes out

| Check | How |
|-------|-----|
| Is the flow actually published? | Publishing a flow does **not** enroll awaiting contacts - check enrollments (`list_enrollments`) and enroll approved items explicitly. |
| Are rows stuck awaiting approval? | Look for awaiting-approval status in the queue (`list_linkedin_outreach_queue`, `list_user_tasks`). Approval tasks route to the owner - is the right human seeing them? |
| Sending schedule / quiet hours? | FirstTouch sends inside the configured schedule. A row queued at 6pm may wait until tomorrow morning. This is correct behavior, not a bug. |
| Daily cap already consumed? | Other motions on the same sender share the daily budget. If AI SDR and a social campaign run on the same seat/day, one waits. |
| Account warning blocking the queue? | See the LinkedIn section above - check before force-retrying anything. |

---

## Credit spend problems

- **Before any bulk discovery or enrichment**, quote the cost: `get_feature_costs` for per-action pricing, `get_credits_usage` for the current balance. Preview with a small sample (10-25 contacts) before committing to hundreds.
- **Balance low mid-play:** stop enriching, report how many contacts are done vs remaining, and offer choices - reduce the list, enrich only missing-email contacts, or top up credits in the FirstTouch app.
- **Spend looks wrong:** `get_credits_usage` shows usage; compare against what the play actually ran. Duplicate enrichment of the same contacts is the usual culprit - check before re-running any discovery step.

---

## A contact was touched who shouldn't have been

Suppression, DNC, and cooldown misses usually trace to one of these:

1. **Stale HubSpot data** - the unsubscribe/DNC property changed after the batch was queued. Fix: re-check suppression at approval time, not just at list-build time, for any batch older than a day.
2. **The contact existed under a second record** - duplicate HubSpot contacts with different emails/LinkedIn URLs slip past the "already contacted" gate. Fix: report the duplicate pair to the user for a HubSpot merge; add the touched contact to the exclusion list now.
3. **Cooldown window mismatch** - the duplicate gate defaults to last-30-days contacted (configurable). If the team expected 90 days, the gate was working as configured, not broken. Fix: confirm the window with the user and restate it in every approval table.
4. **Two motions targeting the same list** - e.g. AI SDR and a social campaign both pulled the contact. Fix: before launching any new motion, check active enrollments for overlap (`list_enrollments`).

After any miss: add the contact to the exclusion/DNC list, note what happened in HubSpot if connected, and tell the user before continuing the batch.

---

## Recovering a broken play mid-run

When a play fails halfway (MCP died, user canceled, limits hit):

1. Establish state first: what was drafted, what was approved, what was queued, what actually sent. Use the queue and enrollment tools - don't reconstruct from chat memory.
2. Never re-queue anything already queued or sent. The duplicate gate is the last line of defense, not the plan.
3. Resume from the first unfinished step, and say explicitly which contacts are being resumed.
4. If state can't be established with confidence, stop and give the user the reconciliation table - human eyes beat a duplicate send.
