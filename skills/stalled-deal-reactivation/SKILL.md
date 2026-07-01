---
name: stalled-deal-reactivation
description: Build and govern a contact-based HubSpot workflow for contacts associated to open deals that are not Closed Won and not Closed Lost and have had no engagement for 60+ days. Deal-based workflow triggers are unsupported, so the workflow enrolls associated contacts, identifies stalled opportunities, diagnoses the likely stall cause, drafts a low-pressure LinkedIn reactivation touch, gates for owner approval, executes through FirstTouch, and logs back to HubSpot. Use when the user wants to revive stalled open pipeline, reactivate quiet opportunities, or reduce no-decision losses.
metadata:
  author: firsttouch
  version: "1.1"
  category: play
  requires: [firsttouch-mcp, hubspot-mcp]
---

**Access note:** this is a HubSpot-dependent motion. Skip it until HubSpot/CRM data or a FirstTouch-accessible HubSpot list exists.

# Stalled Deal Reactivation

**Outcome:** Find contacts associated to open deals that are not Closed Won/Lost and have had no engagement for 60+ days, then build an owner-approved LinkedIn reactivation queue. **AE self-serve path:** for a one-time run, use a manually filtered HubSpot contact list of open deals with no engagement for 60+ days. RevOps/admin setup is only needed for recurring workflow automation. If RevOps wants automation, create or document the contact-based HubSpot workflow as an optional setup step. If the connected HubSpot portal or MCP cannot create workflows, output exact RevOps/admin setup steps and do not pretend it was automated.

## First-run onboarding gate
Before running this skill for the first time in a workspace, load `../../references/onboarding.md` and complete the onboarding questions. Do not proceed until you know: LinkedIn account type (free/basic = no connection notes; recommend 10 connection requests/day and never exceed the FirstTouch max of 20/day; Sales Navigator/Premium = connection notes available; recommend 20 connection requests/day and never exceed the FirstTouch max of 30/day), HubSpot access (MCP, service key/private app token, HubSpot list only, or none), and which play the user wants to run. Recommend high-intent plays before outbound to keep the LinkedIn account healthy. This is a HubSpot-specific play; do not run it unless HubSpot MCP/service-key access is connected.

## When to use
- "Reactivate stalled deals" / "Which open deals have gone quiet?"
- A deal is still open but has no email, meeting, note, call, or LinkedIn engagement for 60+ days
- RevOps wants a contact-based HubSpot workflow that automatically catches no-decision risk before quarter-end
- You, or an AE/BDR if you have one, need owner-routed reactivation queues for quiet opportunities

## Inputs
- **Workflow object:** contact-based HubSpot workflow only. Deal-based workflow triggers are unsupported; deal-based triggers are unsupported for this motion. Enroll contacts associated to qualifying deals instead.
- **Deal stages in scope:** default = contacts associated to deals in open pipeline stages excluding `Closed Won` and `Closed Lost`
- **Engagement threshold:** default = associated deal/contact has no engagement for **60+ days**
- **Engagement fields:** last activity date, last contacted date, last meeting date, notes/calls/emails, and FirstTouch LinkedIn timeline activity where available
- **Owner routing:** HubSpot deal owner/contact owner and authorized FirstTouch sender
- **Workflow action:** create list/queue, enroll in FirstTouch flow, or prepare an approval table depending on the connected portal's available workflow actions

## AE self-serve: build the list yourself (no admin needed)
You can build the one-time list in HubSpot's UI with a normal sales seat:
1. In HubSpot: **Contacts -> Lists -> Create list -> Active list** (contact-based).
2. Add filters:
   - **Associated deal** -> Deal stage -> is none of -> Closed Won, Closed Lost
   - **Last activity date** -> is more than -> 60 days ago
3. Optional: add "Contact owner is me" to scope it to your book.
4. Name it (for example "Stalled open deals - 60d quiet") and give the list name to the agent.
Property labels vary slightly by portal; if a filter is missing, ask RevOps which property tracks last engagement. RevOps is only needed when you want this to run automatically every day as a workflow.

## Step-by-step

### 1. Query or define the contact-based stalled-deal audience
FirstTouch/MCP cannot natively query the full stalled-open-deal cohort by itself; compound deal-stage plus engagement-age filtering must come from a HubSpot list or contact-based workflow. For a one-time founder/admin or AE run, first build or accept a HubSpot filtered contact list: associated deal is open, not Closed Won/Lost, and last activity/engagement is more than 60 days ago. RevOps is needed only to automate recurring enrollment. Build a workflow through the connected HubSpot/FirstTouch action cards only when the portal supports it and the user explicitly wants recurring automation. If the agent lacks workflow-create capability or the AE lacks HubSpot admin permissions, use `../../references/hubspot-setup.md` to produce the manual RevOps/admin setup steps and stop before launch. Either way, this must be a **contact-based** HubSpot workflow. Deal-based workflow triggers are unsupported for this motion, so enroll contacts associated to qualifying deals. Use enrollment criteria that identify contacts where the associated deal has:
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
- before queueing any one-contact LinkedIn action, run `get_dynamic_action_guide`, then call `add_dynamic_action` in the supported order
- if a LinkedIn message should only send after a connection request is accepted, append it to the `connection_accepted` branch rather than queueing it as an immediate message
- send or queue the approved FirstTouch action
- run Gate 5 by logging the executed action to the HubSpot deal + contact timeline within minutes when the connected FirstTouch-HubSpot integration supports it; otherwise keep the FirstTouch execution record and state CRM logging was skipped
- tag `stalled_open_deal_60d` and the stall cause for attribution
- if HubSpot workflow action cards are unavailable in the connected portal, or the user lacks admin rights, output the manual HubSpot workflow/list setup steps from `../../references/hubspot-setup.md` for RevOps/admin instead of pretending the UI exists

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
**Angle:** New proof point. **Draft (value touch to connected champion):** "Dana, saw our pricing thread went quiet, so I wanted to share one approved proof point on the attribution question. If that was still the open thread, I can send the short version here."

## Why this play wins
"No decision" is the #1 competitor. This workflow catches quiet open deals while they can still be revived, routes by owner, and keeps every touch approval-gated and attributable.

## Pitfalls
- **Including Closed Won or Closed Lost deals** - do not. This play is only for open deals not Closed Won/Lost.
- **Using a 14-day default** - too noisy for a workflow. Default to 60+ days with configurable thresholds.
- **"Just checking in"** - the kiss of death. Always lead with new value/context.
- **Ignoring the cause** - a reactivation message that doesn't address why it stalled wastes the touch.
- **Skipping suppression checks** - RevOps must be able to prove DNC/opt-out handling before any workflow-based outreach.

## Reference
- HubSpot setup reference: [`../../references/hubspot-setup.md`](../../references/hubspot-setup.md)
- Messaging: [`../../references/messaging-framework.md`](../../references/messaging-framework.md)
- Safety: [`../../references/safety-governance.md`](../../references/safety-governance.md)
- For generic HubSpot event touches, use [`../hubspot-signal-to-linkedin-touch/SKILL.md`](../hubspot-signal-to-linkedin-touch/SKILL.md).
