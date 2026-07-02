---
name: champion-job-change
description: When a champion or strong contact changes jobs, run a warm reactivation into their new company and protect the old account relationship. Drafts the congratulations note, the reconnect-when-settled follow-up, and the old-account stakeholder handoff; updates HubSpot when connected. Use when the user learns a champion moved - via a LinkedIn notification, a bounced email, an enrichment refresh, or a HubSpot update. This skill reacts to a known job change; FirstTouch does not monitor for job changes automatically.
metadata:
  author: firsttouch
  version: "1.0"
  category: play
  requires: [firsttouch-mcp]
---

# Champion Job Change

**Outcome:** A champion's move becomes two relationships instead of zero: a warm path into the new company on their timeline, and a protected relationship at the old account before the deal or renewal drifts.

## First-run onboarding gate
Before running this skill for the first time in a workspace, load `../../references/onboarding.md` and complete the onboarding questions. Do not proceed until you know: LinkedIn account type (free/basic = no connection notes; recommend 10 connection requests/day and never exceed the FirstTouch max of 20/day; Sales Navigator/Premium = connection notes available; recommend 20 connection requests/day and never exceed the FirstTouch max of 30/day), HubSpot access (MCP, service key/private app token, HubSpot list only, or none), and which play the user wants to run. If HubSpot is unavailable, run the outreach steps and skip the CRM updates.

## How you find out (this skill reacts, it does not monitor)
FirstTouch does not watch for job changes. The trigger is the user learning about the move:
- A LinkedIn "started a new position" notification
- A bounced email or an out-of-office naming a departure
- An enrichment refresh showing a new company (`enrich_contact` can confirm a suspected move)
- A HubSpot update from another team member

When the user suspects but is not sure, confirm with `enrich_contact` before acting - congratulating someone on a job they did not take is worse than silence.

## When to use
- "Sarah just left Acme for Initech"
- A champion's email bounced mid-deal
- Quarterly book review turns up moved contacts
- The user wants a standard motion for every champion move

## Step-by-step

### 1. Confirm the move and assess both sides
- Verify the new company/title (enrichment or the user's direct knowledge).
- **Safety rule: a job change is not buying intent.** New-role executives are flooded with "congrats + pitch" messages; this play's edge is explicitly NOT doing that.
- Old account: what is live there - open deal, renewal, active relationship? Who else do we know?
- New company: is it even ICP? If not, the congratulations still sends (relationships compound); the reactivation path just stays personal, not commercial.

### 2. The new-company path (two touches, spaced)
1. **Congratulations note** (day 0, LinkedIn message if connected - usually they are): genuinely about them. One line of history, one line of well-wishing. **No pitch, no ask, no "would love to show you."**
2. **Reconnect-when-settled note** (queued for 3-4 weeks later, approval before send): "Now that you're settled in - worth a catch-up on how you're thinking about {problem space} at {new company}?" Low pressure; their timeline. If they replied warmly to the congratulations, the user may pull this forward manually.

### 3. The old-account path
- Identify who inherits the relationship: the champion's likely successor plus the stakeholders already known from the deal.
- Draft the stakeholder continuity note: acknowledge the transition without gossiping, reaffirm whatever is in flight, offer continuity - "Want to make sure {project/renewal} keeps moving; who is picking this up on your side?"
- If nobody at the old account is connected yet, queue a connection request to the most relevant known stakeholder with a context-rich opener.

### 4. Gate, queue, and update the CRM
- All touches pass Gate 0-2 from `../../references/safety-governance.md` and go through the standard approval table.
- Queue approved LinkedIn actions via `get_dynamic_action_guide` then `add_dynamic_action` (the reconnect note is a delayed follow-up; the congratulations goes now).
- **HubSpot updates when connected:** note the job change on the contact, associate or create the new-company record per the team's convention, create a task for the reconnect date, and flag the old account's open deal/renewal so the owner sees the relationship risk. Ask before creating records - portals have different conventions.

## Output
- Confirmed move summary (old account exposure + new company fit)
- Approval table: congratulations note, delayed reconnect note, old-account continuity touch(es)
- HubSpot update list (what was noted, tasked, and flagged)

## Examples
**AE:** "My champion at Acme just posted she's joining Initech as VP Ops - we have an open renewal at Acme."
**Run:** congratulations to Sarah today (no pitch); reconnect note queued for 4 weeks; continuity note to Acme's known ops manager asking who inherits the renewal; HubSpot - Sarah's record updated, renewal flagged, reconnect task created for the owner.

## Why this play wins
A champion move is simultaneously the warmest possible door into a new account and the biggest silent risk to an existing one. Most teams notice the move on LinkedIn, think "should do something about that," and do neither. This play makes both sides a 10-minute motion.

## Pitfalls
- **Pitching inside the congratulations** - the single most common way to burn the warmest intro you will ever have. The pitch waits 3-4 weeks minimum.
- **Assuming intent from the move** - new-role energy is not budget. The reconnect note asks about their thinking, not their calendar.
- **Forgetting the old account** - the deal risk materializes in weeks, not quarters. The continuity touch is the urgent half of this play.
- **Acting on an unconfirmed move** - verify first; enrichment is one call.

## Reference
- Message quality: [`../../references/messaging-framework.md`](../../references/messaging-framework.md)
- Safety gates: [`../../references/safety-governance.md`](../../references/safety-governance.md)
