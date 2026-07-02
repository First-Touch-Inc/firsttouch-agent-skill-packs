---
name: post-demo-followup
description: Convert a completed demo or discovery call into same-day follow-up, stakeholder expansion, and momentum touches without sounding automated. Drafts the buyer follow-up, champion thank-you, stakeholder intro, and a 3-day momentum touch from real meeting context; includes a no-show recovery path. Use right after a demo or discovery call, when the user says "we just had the demo," wants to multi-thread after a meeting, or needs to recover a no-show.
metadata:
  author: firsttouch
  version: "1.0"
  category: play
  requires: [firsttouch-mcp]
---

# Post-Demo Follow-Up

**Outcome:** The meeting momentum survives contact with the calendar. Same-day follow-up to the attendees, expansion to the stakeholders who were not in the room, and a scheduled momentum touch - all drafted from what actually happened in the meeting, all approved before anything sends.

## First-run onboarding gate
Before running this skill for the first time in a workspace, load `../../references/onboarding.md` and complete the onboarding questions. Do not proceed until you know: LinkedIn account type (free/basic = no connection notes; recommend 10 connection requests/day and never exceed the FirstTouch max of 20/day; Sales Navigator/Premium = connection notes available; recommend 20 connection requests/day and never exceed the FirstTouch max of 30/day), HubSpot access (MCP, service key/private app token, HubSpot list only, or none), and which play the user wants to run. If HubSpot is unavailable, run from user-provided meeting details instead of CRM context.

## When to use
- "We just finished the demo with Acme"
- Multi-threading an account right after a meeting
- A demo no-show needs recovering without guilt-tripping
- Three days post-demo and the thread has gone quiet

## Step-by-step

### 1. Gather the meeting context
**With HubSpot connected:** pull the meeting record, attendees, deal stage, and recent notes for the contact/deal. **Without HubSpot:** ask the user for the essentials.

Either way, confirm these five inputs before drafting - and **never fabricate meeting details**; if something is missing, ask:
- Who attended (names/roles) and who was invited but absent
- The 1-2 pains that actually resonated
- What was promised (recap, pricing, security doc, intro)
- The agreed next step and its date, if one exists
- Known stakeholders NOT in the meeting (economic buyer, technical lead)

### 2. Draft the follow-up set
Draft all applicable pieces in one pass using `firsttouch-messaging` quality gates; the user picks which to send:

1. **Same-day buyer follow-up** (email or LinkedIn message to the main attendee): recap in one line, the promised item, the agreed next step with date. No new pitch.
2. **Champion thank-you** (LinkedIn message): short, human, references one specific moment from the call. Builds the relationship, asks for nothing.
3. **Stakeholder expansion** (connection request + opener to 1-2 people who were not in the room): references the live evaluation without leaking details - "We're working with {champion} on {topic}; wanted to connect since this touches your team." Never make the champion look bypassed - when in doubt, ask the champion first.
4. **3-day momentum touch** (queued, sends only if no reply): light value-add tied to the discussed pain - a relevant resource or a specific answer to an open question. Not "just checking in."

**No-show variant:** skip 1-3. Draft a zero-guilt recovery: assume good faith, offer two specific new times, add one line of value so the reschedule feels worth it.

### 3. Route and gate
- Run Gate 0-2 checks from `../../references/safety-governance.md` on every stakeholder-expansion target (suppression, duplicates, owner).
- Present the full set in one approval table: recipient, channel, piece, draft, timing. The user approves per row.
- Queue approved rows through FirstTouch (`get_dynamic_action_guide` then `add_dynamic_action` for LinkedIn pieces; the momentum touch goes on the appropriate delay).

### 4. Log
When HubSpot is connected, activity logs to the contact/deal timeline automatically via the FirstTouch integration. Note the promised-item and next-step date in the deal notes if the user wants it.

## Output
- Approval table: buyer follow-up, champion thank-you, 1-2 stakeholder expansions, 3-day momentum touch (or the no-show recovery)
- Queued rows for everything approved
- Open-items note: what was promised and when the next step lands

## Examples
**AE:** "Demo with Acme just ended - Sarah (VP Sales) loved the routing piece, her RevOps lead Marcus wasn't there, we owe them a security doc, next step is a technical review Thursday."
**Run:** same-day follow-up to Sarah with the security doc and Thursday confirmation; thank-you referencing her routing question; connection request to Marcus mentioning the eval with Sarah; momentum touch queued for Monday if Thursday's review does not get confirmed.

## Why this play wins
The 24 hours after a demo decide whether the deal has momentum or joins the stalled pile. Most AEs send one recap email and wait. This play turns the same hour into four touches across the buying committee - drafted from what really happened, so none of it smells automated.

## Pitfalls
- **Fabricating meeting detail** - one invented "as we discussed" destroys the credibility of every future touch. Missing input = ask, never guess.
- **Stakeholder expansion that bypasses the champion** - expansion should feel like diligence, not a flank. Reference the champion respectfully or clear it with them first.
- **Momentum touch that is just a bump** - "checking in" adds nothing; every touch carries a specific piece of value or it does not send.
- **Treating the no-show as an insult** - people miss meetings; the recovery that assumes good faith gets the reschedule.

## Reference
- Message quality gates: [`../../references/messaging-framework.md`](../../references/messaging-framework.md)
- Safety gates for expansion targets: [`../../references/safety-governance.md`](../../references/safety-governance.md)
