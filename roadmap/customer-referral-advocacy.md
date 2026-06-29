# Customer Referral / Advocacy Ask — 🔜 Not yet implemented

**Status:** Spec only. Not in the installable pack.
**Persona(s):** Founder, RevOps

## What it does
After a customer thank-you touch lands and the relationship is warm, this play takes the next step: asking the customer for a referral, a case-study conversation, or an introduction. It reads post-thank-you engagement signals (reply sentiment, milestone depth) and produces a staged outreach sequence — relationship deepening first, then a small advocacy ask when the moment is right. Currently `customer-champion` handles the warm touch but stops before the ask; this play adds the ask layer.

## Composes from
- `customer-champion` — identifies milestone hits and drafts the initial warm touch; this play picks up where it stops
- `firsttouch-messaging` — drafts the advocacy ask message in the right tone and at the right timing
- `hubspot-signal-to-linkedin-touch` — tracks engagement signals and triggers the ask step at the appropriate moment

## Trigger
A customer-champion touch was sent and received a positive reply, OR a second milestone is hit (expansion, anniversary, second product adoption) — indicating the relationship is warm enough for a small ask.

## Deliverable
A staged outreach plan: (1) a relationship-deepening touch if not yet warm enough, or (2) a specific, low-pressure advocacy ask (referral intro, case-study conversation, LinkedIn testimonial) with a drafted message gated for human approval before send.
