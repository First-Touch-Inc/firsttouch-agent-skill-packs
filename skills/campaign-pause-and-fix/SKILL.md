---
name: campaign-pause-and-fix
description: Pause a live FirstTouch campaign/flow mid-send, diagnose what is wrong, cancel or hold the affected enrollments, fix the messaging or audience, and safely restart with re-enrollment — without duplicate sends. Use when the user says "pause this campaign," "stop sending," replies or acceptance rates look bad mid-run, a mistake shipped in live copy, LinkedIn issued a warning, or a running flow needs its message or audience changed.
metadata:
  author: firsttouch
  version: "1.0"
  category: play
  requires: [firsttouch-mcp]
---

# Campaign Pause & Fix

**Outcome:** A running campaign stops cleanly, the problem gets fixed, and the motion restarts without double-touching anyone. This is the mid-send escape hatch for every other play.

## First-run onboarding gate
Before running this skill for the first time in a workspace, load `../../references/onboarding.md` and complete the onboarding questions. Do not proceed until you know: LinkedIn account type (free/basic = no connection notes; recommend 10 connection requests/day and never exceed the FirstTouch max of 20/day; Sales Navigator/Premium = connection notes available; recommend 20 connection requests/day and never exceed the FirstTouch max of 30/day), HubSpot access (MCP, service key/private app token, HubSpot list only, or none), and which play the user wants to run. Recommend high-intent plays before outbound to keep the LinkedIn account healthy. If HubSpot is unavailable, do not run HubSpot-specific steps unless the user provides a HubSpot list FirstTouch can access.

## When to use
- "Pause the campaign" / "stop sending right now"
- Bad copy, wrong audience, or a broken variable shipped in a live flow
- Acceptance or reply rates dropped mid-run, or replies are negative
- LinkedIn warning or restriction appeared (see `../../references/troubleshooting.md` — that protocol takes precedence)
- The user wants to change the message or audience of a flow that is already running

## Step-by-step

### 1. Identify the running motion
Find the flow the user means — do not guess from chat memory:
- `list_flow_plans` to list flows; confirm the exact flow plan with the user by name.
- `list_flow_plan_enrollments` (or `list_enrollments`) to see who is in it and in what state: awaiting, in-progress, completed, failed, canceled.
- `list_linkedin_outreach_queue` for what is queued to send next.

Present a status snapshot before touching anything: total enrolled, sent so far, queued next 24h, awaiting approval.

### 2. Stop the bleeding
- Unpublish/pause the flow with `manage_flow_publication`. This stops new sends; it does not undo anything already sent.
- Confirm to the user what is now frozen and what already went out. Anything already sent is a fact to work with, not something to hide.
- If the trigger was a LinkedIn warning, stop here and follow the hard-stop protocol in `../../references/troubleshooting.md` before any fix-and-restart.

### 3. Diagnose
Establish which of these is the actual problem — the fix differs:
- **Copy problem** (wrong message, broken `{{variable}}`, off-brand tone) → fix templates; audience can stay.
- **Audience problem** (wrong segment, suppressed contacts included, duplicates with another motion) → fix the list; re-run Gate 0/Gate 1 from `../../references/safety-governance.md` on whatever remains.
- **Volume/health problem** (caps too aggressive, acceptance dropping) → keep copy and audience, lower the daily cap and restart slower.
- **Wrong motion entirely** → cancel and route the user to the right play instead of patching this one.

### 4. Cancel or hold the affected enrollments
- Cancel enrollments that must not continue with `cancel_flow_enrollments` — scope the cancellation to affected contacts, not blindly to everyone (completed contacts are done either way; untouched awaiting rows may only need the fix, not cancellation).
- Record exactly who was canceled at which step. This list drives safe re-enrollment.

### 5. Apply the fix
- Copy fix: update the flow's templates (draft through `firsttouch-messaging` quality gates; `replace_flow_root` / `update_flow_plan` where the connected MCP supports flow edits — otherwise the user edits in the FirstTouch app and confirms).
- Audience fix: rebuild or prune the audience; re-run suppression, duplicate, and owner checks on the corrected list.
- Volume fix: restate the new daily cap in the approval table (never above the FirstTouch max: 20/day free/basic, 30/day Sales Navigator/Premium).

### 6. Gate the restart
The restart is a new send decision, not a resumption of old approval. Present a restart approval table: who re-enters, at which step, with which (new) copy, at what daily cap. Wait for explicit approval.

### 7. Re-enroll safely
- Run `validate_flow_reenroll` first for contacts being re-enrolled — never skip the validation step.
- Re-enroll approved contacts with `reenroll_flow_enrollments`; enroll net-new approved contacts with `enroll_awaiting_flow_items`.
- Republish the flow with `manage_flow_publication`.
- Confirm with `list_enrollments` that re-enrolled contacts moved from awaiting to in-progress, and report the restart state to the user.

**Duplicate-send rule:** anyone who already received a step's message must never receive that step again. If FirstTouch cannot confirm where a contact stopped, leave that contact out and list them for manual review — skipping a prospect is recoverable; double-messaging them is not.

## Output
- Pre-pause snapshot (enrolled / sent / queued / awaiting)
- Diagnosis: copy, audience, volume, or wrong-motion
- Canceled-enrollment list with steps reached
- Restart approval table and post-restart confirmation

## Examples
**User:** "The AI SDR batch is getting bad replies — stop it."
**Play:** pause via `manage_flow_publication` → snapshot shows 34 sent, 61 queued → diagnosis: opener has a meeting ask (iron-rule violation) → cancel the 61 queued enrollments, fix copy through the messaging quality gate → restart approval at 10/day → `validate_flow_reenroll` + `reenroll_flow_enrollments` → confirm in-progress. The 34 already-sent contacts are excluded from the restart.

## Why this play wins
Every outbound motion eventually needs a mid-flight correction. Without a clean pause-and-fix path, users either let a broken campaign keep sending or nuke everything and double-touch people on the redo. This play is the difference between a five-minute correction and a burned account.

## Pitfalls
- **Pausing without snapshotting first** — you can't restart safely if you don't know who got what.
- **Canceling everyone by default** — completed contacts don't need cancellation; untouched rows may only need the fix.
- **Treating the restart as pre-approved** — the original approval covered the original copy/audience/caps. Fixed motion = fresh gate.
- **Re-enrolling without `validate_flow_reenroll`** — the validation exists to catch exactly the duplicate-send cases humans miss.

## Reference
- Safety gates for the restart: [`../../references/safety-governance.md`](../../references/safety-governance.md)
- LinkedIn warning hard-stop protocol: [`../../references/troubleshooting.md`](../../references/troubleshooting.md)
- Messaging quality gates for fixed copy: [`../../references/messaging-framework.md`](../../references/messaging-framework.md)
