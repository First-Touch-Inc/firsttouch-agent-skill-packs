---
name: warm-engager-followup
description: Turn people who recently liked, commented on, or viewed the sender's posts/profile, an executive's posts/profile, or company/leadership content into conversations and pipeline. Identifies warm engagers via FirstTouch, optionally monitors a CEO/exec profile, qualifies engagers when HubSpot is connected, drafts a personalized connection request or opener, and gates the send for human approval. Use when the user wants to follow up on LinkedIn engagement, monitor leadership posts, convert post likers/commenters, or work "warm" social engagement.
metadata:
  author: firsttouch
  version: "1.0"
  category: play
  requires: [firsttouch-mcp]
---

# Warm Engager Follow-Up

**Outcome:** Convert recent LinkedIn engagement (likes, comments, profile views) into booked conversations, logged to HubSpot.

## First-run onboarding gate
Before running this skill for the first time in a workspace, load `../../references/onboarding.md` and complete the onboarding questions. Do not proceed until you know: LinkedIn account type (free/basic = no connection notes and 10 connection requests/day max; Sales Navigator/Premium = connection notes available and up to 20/day), HubSpot access (MCP, service key/private app token, HubSpot list only, or none), and which play the user wants to run. Recommend high-intent plays before outbound to keep the LinkedIn account healthy. If HubSpot is unavailable, do not run HubSpot-specific steps unless the user provides a HubSpot list FirstTouch can access.

## When to use
- The user says "follow up on people engaging with my posts," "who liked my last post," "work my warm leads"
- A BDR/AE/RevOps user wants to monitor a CEO, founder, exec, or company thought-leader profile and route engagers to reps
- A post or campaign just got engagement and you want to turn it into pipeline
- Weekly/biweekly warm-lead follow-up motion

## Inputs
- **Window:** how far back to pull engagement (default: 7 days)
- **Post scope:** specific post, all recent activity, or a monitored CEO/exec/leadership profile (default: all)
- **Tier filter:** which engagers to prioritize (default: ICP match + seniority)

## Step-by-step

### 1. Pull engagement (FirstTouch MCP)
Get recent engagers — likes, comments, profile views — within the window. Record for each: name, title, company, engagement type, what they engaged with, timestamp.

### 1a. If monitoring a leader's or executive's profile
Use the FirstTouch social engagement monitored-profile flow before pulling engagement:
- add or confirm the CEO/founder/exec profile as a monitored profile, for example `manage_social_engagement_monitored_profile` with `action=add` and `enableSocialEngagement=true` when that tool is available in the connected harness
- confirm the monitored profile is authorized by the customer and relevant to the sender/team
- pull engagers from that monitored profile's posts, then route drafts through the appropriate sender/owner for approval
- if the monitored-profile tool is unavailable, ask the user to provide a FirstTouch-accessible engager list exported from the leadership post

### 2. Qualify against HubSpot (if HubSpot MCP connected)
For each engager, run Gate 0 suppression/DNC first, then check:
- Are they in HubSpot? → existing contact context, owner, lifecycle stage
- Suppressed, unsubscribed, opted out, or DNC? → **skip** and log the reason
- Already in an active sequence or recently contacted? → **skip** (Gate 1: duplicate check)
- Do they match ICP? → tier them (T1 strategic / T2 mid / T3 volume)

### 3. Score and prioritize
Rank by: ICP fit + seniority + engagement depth (commented > liked > viewed). Produce a prioritized list.

### 4. Draft per engager (load `firsttouch-messaging` skill)
For each T1/T2 engager, draft the appropriate message type:
- Not yet connected → **connection request**
  - If the sender has **Premium / Sales Navigator** and this is a warm engagement signal, use a short connection note referencing the engagement.
  - If they do **not** have Premium / Sales Navigator, send the connection without a note.
- Already connected, no recent DM → **opener** referencing the engagement

Preferred opener pattern after engagement:
> "Thanks for engaging with some of my content. Anything stick out?"

Keep drafts conversational, usually **2 sentences max**, and optimize for the smallest next step. Run the messaging quality gate on each.

### 5. Present batch for approval
Output a review table:
| # | Prospect | Engagement | Signal | Owner | Message type | Draft |
Each row clearly marked *"awaiting approval — will not send."*

### 6. After approval → execute + log (FirstTouch MCP)
On human approval per row:
- FirstTouch sends the LinkedIn action
- FirstTouch logs the touch to the HubSpot contact timeline
- Confirm log success; if it fails, alert (Gate 5)

### 7. Track
Tag these contacts with a `warm_engager_followup` property/list so the team can measure downstream replies, meetings, and influenced deals.

## Output (deliverable)
A **Warm Engager Follow-Up batch**:
- Prioritized engager list with signals
- Drafted messages, gated for approval
- Send log + HubSpot timeline confirmation
- Tracked cohort for attribution

## Examples
**Trigger:** "Follow up on everyone who engaged with my post this week."
**Signal source:** Their comment/like on your specific post — strongest possible "why now."
**Draft (connection request, ≤300 chars):** "Hi Maya — appreciated your comment on the HubSpot attribution post. Connecting with RevOps leaders thinking through social attribution. Happy to share how AskElephant measures theirs."

## Pitfalls
- **Treating all engagers equally** — a competitor employee who liked your post is not a lead. Filter by ICP.
- **Skipping the duplicate check** — half of engagers may already be in a sequence. Always gate.
- **Generic "thanks for the like"** — that's not a signal-led message. Tie it to their context.
- **Leadership-post ambiguity** — if the signal came from a CEO/exec/company profile, name that monitored profile and route through the right sender rather than pretending it was the rep's own post.
- **Sending without approval** — never. Gate 4.

## Reference
- Messaging: [`../../references/messaging-framework.md`](../../references/messaging-framework.md)
- Safety gates: [`../../references/safety-governance.md`](../../references/safety-governance.md)
- System model: [`../../references/system-grounding.md`](../../references/system-grounding.md)
