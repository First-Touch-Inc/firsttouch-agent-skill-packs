---
name: founder-led-outbound
description: Run founder-style LinkedIn outbound — high-personalization, signal-led outreach from a founder or executive persona to strategic accounts, with social proof and owner-safe gating. Combines HubSpot target-account context, enrichment, FirstTouch messaging, and the safety operator. Use when a founder/executive wants to do their own outbound, run strategic-account outreach, book meetings from their network, or do founder-led growth.
metadata:
  author: firsttouch
  version: "1.0"
  category: play
  requires: [firsttouch-mcp, hubspot-mcp]
---

# Play 10 — Founder-Led Outbound

**Outcome:** Let a founder/executive run high-converting, brand-aligned LinkedIn outbound to strategic accounts — without it eating their day or risking the account.

## First-run onboarding gate
Before running this skill for the first time in a workspace, load `../../references/onboarding.md` and complete the onboarding questions. Do not proceed until you know: LinkedIn account type (free/basic = no connection notes and 10 connection requests/day max; Sales Navigator/Premium = connection notes available and up to 20/day), HubSpot access (MCP, service key/private app token, HubSpot list only, or none), and which play the user wants to run. Recommend high-intent plays before outbound to keep the LinkedIn account healthy. If HubSpot is unavailable, do not run HubSpot-specific steps unless the user provides a HubSpot list FirstTouch can access.

## When to use
- "I'm the founder — help me do my own outreach"
- Founder-led growth / founder-mode GTM
- Strategic (Tier 1) accounts where the founder's voice matters
- Booking meetings from the founder's existing network + engagement

## When NOT to use
- High-volume SDR outbound (use plays 01/02 instead — founder voice doesn't scale to volume)
- The founder isn't the authorized LinkedIn seat (routing/owner issues)

## What makes founder outbound different

Founder outreach is **not** scaled SDR outreach. The rules shift:
- **Lower volume, higher personalization** — every message is deeply researched
- **Founder voice** — brief, direct, no SDR-speak, no "just checking in"
- **Social proof as currency** — lead with outcomes, not features
- **Network-leveraged** — warm paths and mutual connections matter more
- **Strategic accounts only** — this is for Tier 1, not the whole TAM

## Step-by-step

### 1. Define the strategic-account list (HubSpot MCP)
Pull Tier 1 target accounts — by ICP fit, strategic value, existing engagement, or a founder-curated list. For each: company, why it's strategic, known contacts, owner.

### 2. Research deeply (enrichment + FirstTouch + HubSpot)
For each account, gather:
- Recent company signal (funding, hiring, product, news)
- The founder's mutual connections / shared context with stakeholders
- Key stakeholders (load play `03-champion-mapper` for the map)
- Any existing HubSpot activity / relationship

### 3. Draft in founder voice (load `firsttouch-messaging`, override tone)
Drafts must be:
- **First person from the founder** ("I noticed…", not "Our team…")
- **Brief** — founders respect time; write like one
- **Signal-led with proof** — tie the signal to a real outcome ("we helped {comparable} do X")
- **Soft, specific CTA** — "worth a 20-min compare?" with 2 times, or "mind if I send the one-pager?"

Run the quality gate, then apply the **founder-voice check**: if it sounds like an SDR wrote it, rewrite.

### 4. Present for founder approval (Gate 4 — non-negotiable)
The founder personally approves every first touch — this is their name and reputation. Batch approval is acceptable only for follow-ups in an already-approved thread.

### 5. Execute + log (FirstTouch MCP, via play 05)
Send through the owner-safe operator. Every touch logged to the account/contact timeline under the founder's identity.

### 6. Hand off warm leads
When a prospect responds interested, **route to the owner/AE** in HubSpot with full context — the founder opens the door, the team carries it. Don't let interested replies sit in the founder's inbox.

### 7. Measure (play 07)
Tag as `founder_led` → attribution report shows which founder touches influenced strategic pipeline.

## Output
- Researched strategic-account briefs
- Founder-voiced drafts, gated for personal approval
- Send + log confirmation
- Warm-lead handoff to owners
- Attribution tag

## Examples
**Account:** Strategic target, Series B fintech.
**Signal:** Just raised $40M, hiring 5 GTM roles.
**Draft (connection request, founder voice, ≤300 chars):** "Congrats on the Series B, Priya. We helped RB2B turn social-first outbound into $30M attributed ARR post-raise — different space, same 'hire SDRs, need attribution yesterday' problem. Connecting in case useful as you scale. — Jared"

## Why this play wins
Founder-led outreach has ~5–10x the reply rate of SDR outreach when done right — but only when it sounds like the founder, not a template. This play operationalizes that without burning the founder's time or account.

## Pitfalls
- **Scaling founder outreach like SDR outreach** — defeats the purpose. Keep volume low, personalization high.
- **SDR-voice leakage** — if the draft says "I'd love to learn about your challenges," it failed. Rewrite in the founder's actual voice.
- **Bottlenecking replies on the founder** — interested leads must route to the team fast, or they die in the founder's inbox.
- **Skipping founder approval** — never send in the founder's name without their explicit OK.

## Reference
- Messaging (with founder-voice override): [`../../references/messaging-framework.md`](../../references/messaging-framework.md)
- Safety execution: load play `05-owner-safe-outreach-operator`
- Account mapping: load play `03-champion-mapper`
- Attribution: load play `07-pipeline-attribution-analyst`
