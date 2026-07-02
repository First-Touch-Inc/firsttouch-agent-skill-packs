# BDR Seat Safety & Shared Queue Basics

One page, no drama. How your LinkedIn seat behaves inside FirstTouch and how shared inbound queues stay clean.

## What happens if I hit a limit?

Nothing bad. FirstTouch enforces your configured daily limits, so hitting one just means the seat goes on **cooldown** - sends pause and resume automatically in the next window.

- Cooldown is normal. Do not force-retry or re-queue anything; the queue picks itself back up.
- If you hit cooldown most days, lower your daily volume a little so sends flow evenly instead of bunching at the cap.
- You can see and adjust your limits in the FirstTouch app under Settings -> User Accounts -> Daily limits.

## Which statuses need action?

Your seat's status shows in FirstTouch Social settings:

| Status | Meaning | What you do |
|---|---|---|
| Available | Ready to send | Nothing - you're good |
| Cooldown | Daily limit reached | Nothing - resumes next window |
| 2FA / OTP / Confirm in app | Platform wants a verification step | Complete it in FirstTouch or the LinkedIn app |
| Action required | Platform asked for a manual check | Resolve it before more sends from your seat |
| Disconnected | Session expired | Reconnect in FirstTouch (automation pauses on its own meanwhile) |
| Restricted | Platform restricted the account | Pause the seat, resolve with the platform, restart at lower volume |

## How shared inbound queues avoid double touches

If several BDRs work one inbound list, the system keeps you out of each other's way:

- **The duplicate gate has your back:** before any draft, the agent checks FirstTouch history. If a teammate already touched or queued the contact, your row is skipped - that is correct behavior, not a bug.
- **Owner mismatch = flag, not send:** if the contact's HubSpot owner is someone else, the row is flagged for review instead of sending.
- **Your queue is your own:** FirstTouch queues actions per rep, first-come-first-serve within your own queue - a teammate's queued actions never slow yours down. For a time-sensitive row, set its priority to high to move it ahead of your other queued work.
- **Same-morning collisions:** if two BDRs pick up the same fresh lead, the duplicate gate catches it when the second row is drafted or queued - the second row is skipped and nothing double-sends.

## What good BDR hygiene looks like

- Smaller, warmer batches beat maxed-out cold ones - approve your best 10, not your first 10.
- Glance at your acceptance rate weekly; above ~40% is healthy. If it slides, tighten targeting and personalize harder before adding volume.
- Run only FirstTouch on your LinkedIn account - stacking a second automation tool on the same seat is the most common self-inflicted problem.
- Keep your approval queue current; rows older than a day get stale, and your manager can see the aged queue.
- Friday: run "Show your manager the numbers" so the week's work is visible.
