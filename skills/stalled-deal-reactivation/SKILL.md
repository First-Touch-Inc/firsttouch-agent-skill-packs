---
name: stalled-deal-reactivation
description: Restart stuck or stalled HubSpot deals using timely, low-pressure LinkedIn touches backed by social proof and fresh context. Identifies deals with no activity past a threshold, diagnoses why they stalled, drafts a reactivation message, and gates for approval. Use when the user wants to revive stalled deals, reactivate dead pipeline, follow up on stuck opportunities, or reduce "no decision" losses.
metadata:
  author: firsttouch
  version: "1.0"
  category: play
  requires: [firsttouch-mcp, hubspot-mcp]
---

# Play 04 — Stalled Deal Reactivation

**Outcome:** Recover pipeline stuck in "no decision" by re-engaging the buying committee with a contextual LinkedIn touch.

## First-run onboarding gate
Before running this skill for the first time in a workspace, load `../../references/onboarding.md` and complete the onboarding questions. Do not proceed until you know: LinkedIn account type (free/basic = no connection notes and 10 connection requests/day max; Sales Navigator/Premium = connection notes available and up to 20/day), HubSpot access (MCP, service key/private app token, HubSpot list only, or none), and which play the user wants to run. Recommend high-intent plays before outbound to keep the LinkedIn account healthy. If HubSpot is unavailable, do not run HubSpot-specific steps unless the user provides a HubSpot list FirstTouch can access.

## When to use
- "Which deals have gone quiet?" / "Reactivate my stalled pipeline"
- A deal hasn't had activity in X days
- Reducing losses to "no decision" / "closed-lost"
- Quarter-end pipeline recovery

## Inputs
- **Stall threshold:** days with no activity (default: 14)
- **Deal stages in scope:** which stages count (default: everything after "Qualified")
- **Lookback:** how stale a deal can be to still reactivate (default: 90 days)

## Step-by-step

### 1. Find stalled deals (HubSpot MCP)
Query deals with no activity in `threshold` days, within `lookback`, in scope stages. For each: deal name, company, amount, stage, last activity date, owner, associated contacts.

### 2. Diagnose the stall
For each stalled deal, infer the likely cause from context:
- Single-threaded (only one contact) → need to multi-thread (play 03)
- Lost champion (contact left) → find successor
- Went quiet after pricing → value/objection gap
- No activity at all → priority slipped
- Competitor in the mix → differentiation needed

### 3. Pick the reactivation angle
| Stall cause | Angle | Message type |
|-------------|-------|--------------|
| Single-threaded | Introduce to a second stakeholder | Connection request |
| Lost champion | Re-engage successor with context | Opener |
| Post-pricing silence | New proof point / ROI data | Value touch |
| Priority slipped | Trigger event (their news) | Re-engage |
| Competitor | Differentiation / neutral compare | Value touch |

### 4. Draft (load `firsttouch-messaging`)
The reactivation must feel **fresh**, not like a nag. Lead with new context (a proof point, their recent news, a new stakeholder) — never "just checking in."

### 5. Present for approval (Gate 4)
Table: deal, company, amount, stall cause, target contact, angle, draft.

### 6. Execute + log (FirstTouch MCP)
Send via FirstTouch, log to deal + contact timeline, tag `stalled_reactivation` + stall cause for attribution.

### 7. Track
Measure reactivation rate by angle → which stall causes respond best to which message. Feeds play 07.

## Output
- Stalled-deal list with diagnosed cause per deal
- Reactivation drafts, gated for approval
- Send + log confirmation
- Tagged cohort for attribution

## Examples
**Deal:** Acme — $48k — no activity 21 days, post-pricing silence.
**Angle:** New proof point. **Draft (value touch to connected champion):** "Dana — circling back with something timely: we just published how RB2B attributed $30M+ ARR to social-first outbound. Given the attribution question came up in your eval, worth a look? No ask — flagging because it's directly relevant."

## Why this play wins
"No decision" is the #1 competitor. Most reps give up after one follow-up. This play systematizes **context-led reactivation** — the highest-ROI use of social touches.

## Pitfalls
- **"Just checking in"** — the kiss of death. Always lead with new value/context.
- **Reactivating dead deals** — respect the lookback; a deal cold for 6 months is likely truly dead.
- **Ignoring the cause** — a reactivation message that doesn't address *why* it stalled wastes the touch.

## Reference
- Messaging: [`../../references/messaging-framework.md`](../../references/messaging-framework.md)
- For multi-threading stalled deals: load play `03-champion-mapper`.
