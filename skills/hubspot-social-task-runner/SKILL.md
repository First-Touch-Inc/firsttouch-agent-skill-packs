---
name: hubspot-social-task-runner
description: Find HubSpot CRM tasks due today in the user/owner queue that already represent LinkedIn/social steps, such as connect, message, or follow-up, then execute the approved social action through FirstTouch and mark the HubSpot task complete only after the action is queued or sent. Use only when a HubSpot task read/write connector is available and the team already creates these social-step tasks every day.
metadata:
  author: firsttouch
  version: "1.1"
  category: play
  requires: [firsttouch-mcp, hubspot-mcp]
---

# HubSpot Social Task Runner

**Outcome:** Turn an existing HubSpot task queue into completed LinkedIn/social actions for the tasks due today. This play does **not** create a new cadence, infer missing task logic, or replace RevOps setup. It only works when HubSpot already has daily social-step tasks such as LinkedIn connect, LinkedIn message, or social follow-up.

## First-run onboarding gate
Before running this skill for the first time in a workspace, load `../../references/onboarding.md` and complete the onboarding questions. Do not proceed until you know: LinkedIn account type, HubSpot task read/write connector status, FirstTouch sender/account readiness, and whether HubSpot tasks are already being created daily for social steps. If the HubSpot connector cannot read and complete tasks, or if no task queue exists, stop and recommend setting up the task source first.

## When to use
- "Work my HubSpot LinkedIn tasks due today"
- "Automate the manual social tasks my team already creates"
- "Find all due HubSpot tasks that say connect on LinkedIn or send LinkedIn message, then run them"
- AE/BDR teams that already get daily CRM tasks for social touches but waste time manually clicking through them

## When NOT to use
- There are no HubSpot/CRM tasks already being created for social steps
- The CRM connector is not connected or cannot expose tasks
- The user wants a new cadence/list/flow created. Use `hubspot-signal-to-linkedin-touch`, `social-campaigns`, or `icp-outbound-builder` instead.
- The task is ambiguous, missing a contact, missing a LinkedIn URL, missing sender/owner, or not clearly a LinkedIn/social action
- The task is an email/call/manual research task rather than a LinkedIn connect/message/social follow-up

## Inputs
- **Date scope:** default = tasks due today in the workspace timezone and inside the approved same-day send window, not overdue backlog unless the user asks. If the same-day send window has passed, preview the rows and ask before sending.
- **Task filters:** user/owner queue, task status open/not started, due date today, task title/body/type containing LinkedIn/social/connect/message/follow-up cues such as `LinkedIn`, `LI`, `connect`, `connection request`, `message on LinkedIn`, or `social touch`
- **Allowed social actions:** LinkedIn connection request, LinkedIn message to existing connection, post-accept follow-up when already modeled by the task
- **Approval mode:** treat a task from an explicitly approved CRM workflow or approved daily task process as prior approval to execute exactly that task. If that prior approval is unclear, or if new copy is drafted, preview and ask before execution.

## Step-by-step

### 1. Confirm this is task automation, not cadence creation
State the constraint back to the user:
> "I will only process HubSpot tasks already due today that clearly represent LinkedIn/social steps. I will not create new tasks, new cadence logic, or infer missing workflow rules."

If daily tasks are not already being created, stop and recommend the appropriate setup play.

### 2. Pull due social tasks from HubSpot
Using the CRM connector, query HubSpot tasks that are:
- assigned to the requested user/owner/sender, or the current user if unspecified
- due today in the workspace timezone and inside the approved same-day send window
- open / not completed
- associated to a contact or company/contact record
- clearly labeled as a social step, for example task title/body contains `LinkedIn`, `LI`, `connect`, `connection request`, `message on LinkedIn`, or `social touch`

Do not include calls, emails, generic follow-ups, research tasks, or tasks with no contact association.

### 3. Normalize each task into an execution row
For each candidate task, capture:

| Field | Required? |
|---|---|
| HubSpot task id | yes |
| Due date | yes |
| Contact name + HubSpot contact id | yes |
| Company | recommended |
| Contact owner / sender | yes |
| LinkedIn URL | required for LinkedIn actions; enrich or skip if unavailable |
| Intended social action | connect / message / follow-up |
| Task source/workflow name | recommended |
| Existing task notes or approved copy | required for message actions unless FirstTouch drafts and user approves |

### 4. Run safety gates before execution
For every row:
- Gate 0 suppression/DNC from `../../references/safety-governance.md`
- Gate 1 duplicate/recent FirstTouch outreach check
- Gate 2 owner/sender routing
- Gate 3 LinkedIn daily cap check, including today's active, in-queue, blocked/review-required, and completed/pending connection requests for the sender
- Confirm the task is actually due today and not already completed

Skip and report any row that fails a gate. Do not mark skipped HubSpot tasks complete unless the user explicitly asks.

### 5. Map task type to FirstTouch action
Use this mapping:

| HubSpot task signal | FirstTouch action |
|---|---|
| connect / connection request / add on LinkedIn | LinkedIn connection request. Free/basic accounts use blank connection requests with no note. Use a note only when Sales Navigator/Premium is available and the task includes approved note copy or the user approves it. |
| LinkedIn message / social message / follow-up and contact is already connected | LinkedIn message using task-approved copy or user-approved drafted copy. |
| LinkedIn follow-up after accepted connection | LinkedIn message only if connection status or FirstTouch state confirms the contact is connected/accepted. |
| unclear task | skip and report for manual review |

Before creating any one-contact LinkedIn action, run `get_dynamic_action_guide`, then call `add_dynamic_action` in the supported order. Do not bypass the FirstTouch dynamic-action preflight.

### 6. Execute only approved/eligible rows
A HubSpot task from an explicitly approved CRM workflow or approved daily task process counts as prior approval to execute exactly that task, as long as it contains enough information to act safely. If the task was ad hoc, ambiguous, outside the same-day send window, or requires freshly generated copy, show the approval table first and wait.

Approval/execution table:

| # | HubSpot task | Contact | Owner/sender | Due | Intended action | Copy/source | Gate result | Execution status |
|---|---|---|---|---|---|---|---|---|

### 7. Mark HubSpot task complete after FirstTouch queues/sends
After FirstTouch confirms the LinkedIn action is queued or sent:
- mark the corresponding HubSpot task complete through the CRM connector when supported
- add a completion note such as `Executed via FirstTouch: LinkedIn connection request queued` or `LinkedIn message queued/sent`
- if FirstTouch action fails, leave the HubSpot task open and add/report the failure reason

### 8. Report results
Return:
- tasks scanned
- eligible LinkedIn/social tasks due today
- sent/queued count by action type
- skipped count with reasons
- remaining daily cap for each sender
- HubSpot tasks completed
- HubSpot tasks left open for manual review

## Output
```markdown
## HubSpot social tasks processed today
- Owner/sender:
- Tasks scanned:
- Eligible social tasks due today:
- LinkedIn connection requests queued/sent:
- LinkedIn messages queued/sent:
- HubSpot tasks marked complete:
- Skipped/manual review:
- Remaining connection-request cap:

| Task | Contact | Action | Status | Reason/details |
|---|---|---|---|---|
```

## Pitfalls
- Treating this as a prospecting engine. It is only a task runner for existing CRM tasks.
- Running overdue/backlog tasks without an explicit user ask; default is due today only.
- Sending ambiguous tasks that do not clearly specify a LinkedIn/social action.
- Marking HubSpot tasks complete before FirstTouch confirms queue/send success.
- Ignoring shared daily LinkedIn caps when AI SDR or social campaigns are also running.
- Drafting new message copy and sending it automatically. If the task does not already contain approved copy, ask for approval.

## Reference
- Onboarding: [`../../references/onboarding.md`](../../references/onboarding.md)
- HubSpot setup: [`../../references/hubspot-setup.md`](../../references/hubspot-setup.md)
- Safety gates: [`../../references/safety-governance.md`](../../references/safety-governance.md)
- System model: [`../../references/system-grounding.md`](../../references/system-grounding.md)
