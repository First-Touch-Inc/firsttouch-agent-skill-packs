---
name: founder-post-generator
description: Turn founder POV, customer proof, market observations, and real sales conversations into LinkedIn posts that attract the right engagers - then route those engagers into warm follow-up. Drafts posts only; sends nothing. Use when a founder wants to post more consistently, has thin post engagement to feed the warm-engager play, asks "what should I post," or wants a week of posts drafted in their voice.
metadata:
  author: firsttouch
  version: "1.0"
  category: play
  requires: []
---

# Founder Post Generator

**Outcome:** A steady stream of founder-voice LinkedIn posts that create the engagement the rest of this pack harvests. Posts feed Social Engagement monitoring; engagers feed `warm-engager-followup`; conversations feed pipeline. This skill drafts - the founder posts from their own account.

## First-run note
This skill sends nothing and uses no daily send budget. Before the first run, capture two things (reuse them every run):
1. **Founder voice profile:** 2-3 sample posts or messages the founder actually wrote, plus tone rules - phrases they use, phrases they hate, formality level, topics they will not touch. **Save this as a reusable profile:** restate it in the first run's output so the founder can keep it (notes file, saved prompt, agent memory). On every later run, if a profile exists, confirm "still accurate?" and reuse it - never make the founder re-explain their voice. Re-calibrate when a draft sounds off or roughly monthly.
2. **Audience:** who should engage (the ICP from `../../references/onboarding.md`). A post that attracts the wrong engagers creates busywork downstream.

## When to use
- "What should I post this week?"
- Post engagement is thin and the warm-engager play has nothing to harvest
- Before launching Social Engagement monitoring on the founder's own profile
- A customer win, product lesson, or strong opinion is sitting unused

## Step-by-step

### 1. Collect raw material
Ask for whichever exists - one strong input beats five weak ones:
- A recent customer conversation, win, or objection that surprised the founder
- A market observation ("everyone is doing X, we keep seeing Y")
- A build-in-public moment: something shipped, broken, learned, or changed
- A strong opinion the founder actually holds and will defend in comments
When HubSpot is connected, closed-won stories and common deal objections are good seeds - but never use customer names or details without explicit approval.

### 2. Pick the post type
Five types, rotate across the week - do not post the same shape twice in a row:

| Type | Shape | Best for |
|---|---|---|
| Customer lesson | "A customer taught us X. Here's what changed." | Proof without bragging |
| Contrarian market POV | "Everyone says X. We keep seeing Y." | Comments and debate |
| Build-in-public | "We shipped/broke/learned X this week." | Relatability, follower growth |
| Problem/solution teardown | "Here's the exact problem and how we think about it." | Attracting ICP practitioners |
| What we're seeing | "3 patterns from the last 20 customer conversations." | Authority, saves/shares |

### 3. Draft in founder voice
Apply the voice profile and the `firsttouch-messaging` quality bar, adapted for posts:
- First line earns the click-through ("see more") - a specific claim or tension, never a greeting
- Short paragraphs, plain words, no jargon, no em dashes, no engagement-bait cliches
- One idea per post; depth beats breadth
- It must sound like the founder on a good day, not a content marketer

### 4. CTA rules
- **No hard demo CTA on every post.** Most posts end with an invitation to think or reply: "Curious how others handle this" beats "Book a demo."
- At most 1 in 5 posts may carry a soft product mention, and only when the story earns it.
- The goal of a post is engagement from the right people. Warm engagement IS the downstream signal - the pack converts it, the post does not have to.

### 5. Deliver the batch
Output 3-5 posts per run with: post type, the draft, a suggested posting day, and a one-line note on who it should attract. Founder edits and posts from their own account - this skill never publishes.

### 6. Bridge to warm follow-up
After each post has been live 24-72 hours, run `warm-engager-followup` on the qualified engagers (Social Engagement monitoring must be enabled on the founder's profile - see that skill, step 1). Likes and comments from ICP-fit people are the whole point; route them into warm conversations while the post is still fresh.

## Output
- 3-5 founder-voice post drafts with type, suggested day, and target-audience note
- First run only: the voice profile (samples, tone rules, exclusions) restated in a copy-saveable block for reuse
- A rotation suggestion for next week's types
- Reminder of the 24-72h warm-engager bridge

## Examples
**Founder:** "I have nothing to post and my last post got 4 likes."
**Run:** collect one customer lesson + one contrarian POV from this week's sales calls -> draft a customer-lesson post for Tuesday and a contrarian post for Thursday -> Thursday's post draws 22 ICP-fit engagers -> Friday, warm-engager-followup drafts openers for the 8 best fits.

## Why this play wins
Every warm play in this pack assumes engagement exists. Most founders do not post consistently, so the funnel starves at the top. This skill fixes the input: posts create engagers, engagers become conversations, and the founder never sends a cold message that a warm one could have replaced.

## Pitfalls
- **Posting for reach instead of for the ICP** - 500 likes from peers beats nothing, but 20 likes from buyers beats 500 from peers.
- **Product-pitching every post** - the fastest way to train your audience to scroll past you.
- **Ghost-written voice drift** - if the founder would not say it out loud, cut it. Re-calibrate against the voice samples every few weeks.
- **Posting and not harvesting** - the post is step one; skipping the warm-engager bridge wastes the engagement you earned.

## Reference
- Voice and quality bar: [`../../references/messaging-framework.md`](../../references/messaging-framework.md)
- Harvesting engagers: `warm-engager-followup` (this pack)
