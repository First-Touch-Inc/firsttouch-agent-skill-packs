# Rep-Led AI SDR — 🔜 Not yet implemented

**Status:** Spec only. Not in the installable pack.
**Persona(s):** AE, BDR

## What it does
An ongoing AI SDR motion in the rep's own voice — not founder-voice. Today, `founder-led-outbound` provides high-personalization outreach in a founder/executive persona. Rep-led AI SDR overlays the individual rep's voice, territory context, and quota-driven pacing on top of the same ICP sourcing and safety infrastructure. This enables AEs and BDRs to run persistent LinkedIn outbound without it sounding like a generic sequence or being mistaken for a senior exec.

## Composes from
- `icp-outbound-builder` — sources and qualifies target accounts and personas within the rep's territory
- `owner-safe-outreach-operator` — routes, gates, and logs every send with owner verification
- `firsttouch-messaging` — drafts outreach calibrated to the rep's voice and the prospect's seniority
- `founder-led-outbound` — borrows the high-personalization, signal-led approach; needs a rep-voice overlay rather than founder-voice

## Trigger
Rep defines their territory, ICP criteria, and a weekly accounts-to-work target. The play runs on a rolling basis — pulling newly qualified accounts, drafting first touches, and batching them for weekly approval.

## Deliverable
A weekly batch of drafted LinkedIn first-touches in the rep's voice, tiered by ICP fit, gated for rep approval before any send. Execution report logged to HubSpot per send with `rep_led_ai_sdr` attribution tag.
