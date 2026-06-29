---
name: stalled-deal-reactivation
description: Build and govern a contact-based HubSpot workflow for contacts associated to open deals that are not Closed Won and not Closed Lost and have had no engagement for 60+ days. Deal-based workflow triggers are unsupported, so the workflow enrolls associated contacts, identifies stalled opportunities, diagnoses the likely stall cause, drafts a low-pressure LinkedIn reactivation touch, gates for owner approval, executes through FirstTouch, and logs back to HubSpot. Use when the user wants to revive stalled open pipeline, reactivate quiet opportunities, or reduce no-decision losses.
metadata:
  author: firsttouch
  version: "1.1"
  category: play
  requires: [firsttouch-mcp, hubspot-mcp]
---

# Stalled Deal Reactivation

**Outcome:** Create a contact-based HubSpot workflow that enrolls contacts associated to open deals that are not Closed Won/Lost and have had no engagement for 60+ days, then prepare owner-approved LinkedIn reactivation touches.

## First-run onboarding gate
Before running this skill for the first time in a workspace, load `../../references/onboarding.md` and complete the onboarding questions. Do not proceed until you know: LinkedIn account type (free/basic = no connection notes and 10 connection requests/day max; Sales Navigator/Premium = connection notes available and up to 20/day), HubSpot access (MCP, service key/private app token, HubSpot list only, or none), and which play the user wants to run. Recommend high-intent plays before outbound to keep the LinkedIn account healthy. This is a HubSpot-specific play; do not run it unless HubSpot MCP/service-key access is connected.

## When to use
- "Reactivate stalled deals" / "Which open deals have gone quiet?"
- A deal is still open but has no email, meeting, note, call, or LinkedIn engagement for 60+ days
- RevOps wants a contact-based HubSpot workflow that automatically catches no-decision risk before quarter-end
- AEs need owner-routed reactivation queues for quiet opportunities

## Inputs
- **Workflow object:** contact-based HubSpot workflow only. Deal-based workflow triggers are unsupported; deal-based triggers are unsupported for this motion. Enroll contacts associated to qualifying deals instead.
- **Deal stages in scope:** default = contacts associated to deals in open pipeline stages excluding `Closed Won` and `Closed Lost`
- **Engagement threshold:** default = associated deal/contact has no engagement for **60+ days**
- **Engagement fields:** last activity date, last contacted date, last meeting date, notes/calls/emails, and FirstTouch LinkedIn timeline activity where available
- **Owner routing:** HubSpot deal owner/contact owner and authorized FirstTouch sender
- **Workflow action:** create list/queue, enroll in FirstTouch flow, or prepare an approval table depending on the connected portal's available workflow actions

## Step-by-step

### 1. Define the contact-based HubSpot workflow trigger
Build or document a **contact-based** HubSpot workflow. Deal-based workflow triggers are unsupported for this motion, so enroll contacts associated to qualifying deals. Use enrollment criteria that identify contacts where the associated deal has:
- Deal stage **is not** `Closed Won`
- Deal stage **is not** `Closed Lost`
- Deal is in an active/open pipeline stage
- Last engagement/activity is blank or older than **60 days**
- Deal has at least one associated contact with a LinkedIn URL or an enrichment path
- Associated contact is not suppressed, opted out, unsubscribed, or already in an active outreach sequence

Recommended HubSpot trigger label: `FT - Stalled open deal - 60d no engagement`.

### 2. Pull the stalled open-deal cohort through enrolled contacts (HubSpot MCP)
For each enrolled contact, capture the qualifying associated deal: deal name, company, amount, stage, deal owner, contact owner, last engagement date, associated contacts, known stakeholders, prior notes, and recent FirstTouch/LinkedIn timeline activity.

Do **not** include Closed Won or Closed Lost deals in this play. Closed-lost win-back is a separate motion.

### 3. Run governance gates before drafting
For every deal/contact:
- Run Gate 0 suppression/DNC from `../../references/safety-governance.md`
- Confirm the HubSpot owner and authorized FirstTouch sender match (Gate 2)
- Check duplicate/recent outreach and cooldown (Gate 1)
- Confirm the LinkedIn account has capacity under the user's daily cap (Gate 3)

### 4. Diagnose the stall
Infer the likely cause from HubSpot context:
- Single-threaded: only one active contact in the buying committee
- Champion quiet: champion stopped engaging but deal remains open
- Post-pricing silence: no response after commercial conversation
- Evaluation drift: no activity after discovery/demo
- Procurement/legal pause: stage advanced but no recent activity

### 5. Pick the reactivation angle
| Stall cause | Angle | Message type |
|-------------|-------|--------------|
| Single-threaded | Add a second stakeholder or ask who else should see the update | Connection request or opener |
| Champion quiet | Low-pressure value touch with a new proof point | Opener/value touch |
| Post-pricing silence | Specific ROI/proof point related to the pricing concern | Value touch |
| Evaluation drift | Fresh trigger or product update tied to their original pain | Re-engage |
| Procurement/legal pause | Helpful unblocker, not pressure | Re-engage |

### 6. Draft (load `firsttouch-messaging`)
The reactivation must feel **fresh**, not like a nag. Lead with new context: a proof point, their recent news, a product update, or a useful next stakeholder. Never write "just checking in."

### 7. Present for owner approval (Gate 4)
Output a table: deal, company, amount, stage, owner, last engagement date, stall cause, target contact, angle, draft, and intended FirstTouch action. Every row must be marked `awaiting approval`.

### 8. Execute + log (FirstTouch MCP)
After approval only:
- send or queue the approved FirstTouch action
- run Gate 5 by logging the executed action to the HubSpot deal + contact timeline within minutes
- tag `stalled_open_deal_60d` and the stall cause for attribution
- if HubSpot workflow action cards are unavailable in the connected portal, output exact manual HubSpot workflow/list setup steps instead of pretending the UI exists

### 9. Track
Measure: reactivation replies, meetings re-opened, stage movement, and influenced pipeline by stall cause and owner.

## Output
- HubSpot contact-based workflow criteria for `FT - Stalled open deal - 60d no engagement`
- Enrolled contacts associated to qualifying stalled open deals with diagnosed cause per deal
- Reactivation drafts, gated for owner approval
- Send/log confirmation after approval
- Tagged cohort for attribution

## Examples
**Deal:** Acme, $48k, Stage: Negotiation, no engagement 67 days, post-pricing silence.
**Angle:** New proof point. **Draft (value touch to connected champion):** "Dana, saw our pricing thread went quiet, so I wanted to share one relevant proof point: RB2B tied $30M+ ARR to social-first outbound after tightening attribution. If attribution was still the open question, this may help frame the next step."

## Why this play wins
"No decision" is the #1 competitor. This workflow catches quiet open deals while they can still be revived, routes by owner, and keeps every touch approval-gated and attributable.

## Pitfalls
- **Including Closed Won or Closed Lost deals** — do not. This play is only for open deals not Closed Won/Lost.
- **Using a 14-day default** — too noisy for a workflow. Default to 60+ days with configurable thresholds.
- **"Just checking in"** — the kiss of death. Always lead with new value/context.
- **Ignoring the cause** — a reactivation message that doesn't address why it stalled wastes the touch.
- **Skipping suppression checks** — RevOps must be able to prove DNC/opt-out handling before any workflow-based outreach.

## Reference
- Messaging: [`../../references/messaging-framework.md`](../../references/messaging-framework.md)
- Safety: [`../../references/safety-governance.md`](../../references/safety-governance.md)
- For generic HubSpot event touches, use [`../hubspot-signal-to-linkedin-touch/SKILL.md`](../hubspot-signal-to-linkedin-touch/SKILL.md).
