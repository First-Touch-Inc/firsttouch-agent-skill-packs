---
name: firsttouch-messaging
description: Write on-brand, high-converting LinkedIn outreach messages — connection requests, openers, follow-ups, and meeting asks — calibrated to the prospect's seniority and a real signal. Use this BEFORE any other FirstTouch play that involves drafting a message, or whenever the user asks to write LinkedIn outreach copy, draft a connection request, or personalize a sequence.
metadata:
  author: firsttouch
  version: "1.0"
  category: foundation
---

# FirstTouch Messaging

Every FirstTouch play that involves sending words to a human builds on this skill. It defines **how to draft** LinkedIn outreach that actually converts — signal-first, seniority-calibrated, and always gated for human approval before send.


## First-run onboarding gate
If onboarding has not already been completed in this session, load `../../references/onboarding.md` and complete the onboarding questions. Do not proceed until you know: LinkedIn account type (free/basic = no connection notes and 10 connection requests/day max; Sales Navigator/Premium = connection notes available and up to 20/day), HubSpot access (MCP, service key/private app token, HubSpot list only, or none), and which play the user wants to run. Recommend high-intent plays before outbound to keep the LinkedIn account healthy. If HubSpot is unavailable, do not run HubSpot-specific steps unless the user provides a HubSpot list FirstTouch can access.

## When to use

- A play asks you to "draft the message" (connection request, opener, follow-up)
- The user says "write LinkedIn outreach," "draft a connection note," "personalize this sequence"
- You're producing copy that will be reviewed before a FirstTouch send

## When NOT to use

- Generating email copy for a non-LinkedIn channel (use that channel's conventions)
- Writing internal notes / HubSpot activity logs

## Core principle

**Signal-first, not feature-first.** Find one specific, true thing about the prospect and lead with it. Never lead with your product.

## Step-by-step

### 1. Identify the signal (the "why now")
Find one verifiable fact about the prospect or their company. Sources, in priority order:
- **HubSpot context** (if HubSpot MCP connected): lifecycle change, recent deal activity, form fill, owner notes
- **LinkedIn activity**: recent post, comment, role change, hiring move
- **Company signals**: funding, product launch, hiring spike, tech-stack change
- **Mutual connection / referral**

If you cannot find a real signal, **do not fabricate one.** Either drop the tier to "light" (first-name + company only) or flag that you need enrichment.

### 2. Classify seniority → set tone
- IC/practitioner → peer, tactical, lead with "how"
- Manager/Director → process + outcomes, lead with efficiency/visibility
- VP/Founder/C-level → strategic, brief, signal-led, lead with risk/leverage

### 3. Pick the message type
- Connection request (first touch, no relationship) → goal: get accepted
- Opener (post-accept, day 1–3) → goal: earn a reply, **no ask**
- Value touch (warming) → share something useful, zero ask
- Meeting ask → only after ≥1 exchange; propose specific times
- Break-up / re-engage → last touch, low pressure

**Iron rule: never ask for a meeting in a connection request or opener.**

### 4. Draft using the structure
`Signal (why now) → Relevance (why you/this) → Soft CTA (what next)`

Adapt a template from [`../../references/messaging-framework.md`](../../references/messaging-framework.md) — but **never copy blindly**. Every {{variable}} must resolve to something real.

### 5. Run the quality gate (mandatory self-check)
Before presenting the draft, verify ALL:
- [ ] Signal is real and verifiable (not invented)
- [ ] No meeting ask if connection request or opener
- [ ] Length within limits: connection note ≤300 chars, opener ≤60 words, follow-up ≤80 words
- [ ] No jargon ("revolutionary," "leverage," "synergy," "supercharge")
- [ ] No lazy flattery ("I love what you're building at…")
- [ ] Do not use em dashes in outreach copy
- [ ] One ask max
- [ ] Tone matches seniority

If any check fails → **rewrite before showing.**

### 6. Present for approval (never send)
Output the draft(s) for human review. Format:
- **To:** {name} — {title} @ {company} (owner: {hubspot_owner})
- **Type:** {connection request / opener / follow-up}
- **Signal used:** {the one fact}
- **Draft:** "{message}"
- **Char/word count:** {n} / limit {m}

State clearly: *"Drafted for review. This will not send until you approve."*

## Examples

### Good opener (Manager tier)
> **Signal:** HubSpot shows Acme moved to "Scaling" lifecycle + 2 SDR hires last month
> **To:** Dana Lee, Dir. Sales Ops @ Acme
> "Dana, thanks for connecting. With the SDR team doubling, most ops leaders we talk to are scrambling to keep LinkedIn activity attributed in HubSpot. Is that on your plate? Happy to send how Drift set theirs up."

### Bad (do not do this)
> "Hi Dana, I'd love to learn about your challenges and show you how our AI-powered platform can supercharge your outreach. Do you have 15 mins this week?"
> *(No signal. Meeting ask too early. Jargon. Lazy.)*

## Composability

This skill is called by any installed play that drafts LinkedIn copy, including social engagement, AI SDR, founder-led outbound, inbound follow-up, HubSpot signal touches, stalled-deal reactivation, website visitor follow-up, and customer milestone outreach when those skills are present in the pack. When a play says "draft the message(s) per `firsttouch-messaging`," load this skill, then return to the play for the surrounding workflow.

## Pitfalls

- **Fabricated signals** — the #1 quality risk. If unsure, mark the field and ask for enrichment rather than inventing.
- **Meeting ask creep** — reps love to ask early. Enforce the iron rule.
- **Same message to everyone** — if your drafts across 10 prospects look identical, the personalization failed. Re-signal.
- **Sending without approval** — never. The gate is in `safety-governance.md` and every play.

## Reference

Full methodology, templates, and tier/tone matrix: [`../../references/messaging-framework.md`](../../references/messaging-framework.md)
