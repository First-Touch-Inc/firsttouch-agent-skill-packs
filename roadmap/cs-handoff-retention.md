# CS Handoff / Retention Connector — 🔜 Not yet implemented

**Status:** Spec only. Not in the installable pack.
**Persona(s):** RevOps

## What it does
At a defined onboarding milestone (first value delivered, onboarding complete, 30-day mark), this play routes outreach from the sales sender to the assigned CS owner as the new LinkedIn touchpoint. The CS owner receives full relationship context, sends a warm LinkedIn connection as themselves, and begins a retention-oriented touchpoint cadence. Today `customer-champion` handles the milestone touch but sends from the AE or founder seat — this play adds dedicated CS-as-sender routing and a structured handoff sequence.

## Composes from
- `customer-champion` — detects the onboarding or milestone trigger and drafts the initial CS touch
- `safety-governance.md` — routes the send to the CS owner's LinkedIn seat rather than the AE's when HubSpot owner data is connected
- `hubspot-signal-to-linkedin-touch` — reads the HubSpot lifecycle milestone that triggers the handoff event

## Trigger
HubSpot lifecycle property changes to "Customer" or a custom onboarding-complete property is set. The CS owner must be assigned in HubSpot and their LinkedIn seat connected in FirstTouch.

## Deliverable
A handoff package for the CS owner: customer context summary (deal history, AE notes, champion contacts), a drafted LinkedIn connection request or warm opener from the CS owner's persona, and a proposed 30/60/90-day retention touchpoint plan — all gated for CS owner approval before any send.
