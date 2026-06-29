---
name: owner-safe-outreach-operator
description: Ensure every LinkedIn outreach action respects owner routing, duplicate checks, account-safety limits, and human approval before it sends — then logs to HubSpot. Acts as the safety wrapper around any other FirstTouch play that executes sends. Use whenever outreach is about to be sent, when the user wants to "make sure this is safe to send," or to batch-approve and execute a queued set of drafted messages.
metadata:
  author: firsttouch
  version: "1.0"
  category: play
  requires: [firsttouch-mcp, hubspot-mcp]
---

# Play 05 — Owner-Safe Outreach Operator

**Outcome:** Guarantee that no outreach goes out without passing all 5 safety gates, and that every send is correctly logged. This is the **execution safety layer** that wraps plays 01, 02, 04, 06, 10.

## First-run onboarding gate
Before running this skill for the first time in a workspace, load `../../references/onboarding.md` and complete the onboarding questions. Do not proceed until you know: LinkedIn account type (free/basic = no connection notes and 10 connection requests/day max; Sales Navigator/Premium = connection notes available and up to 20/day), HubSpot access (MCP, service key/private app token, HubSpot list only, or none), and which play the user wants to run. Recommend high-intent plays before outbound to keep the LinkedIn account healthy. If HubSpot is unavailable, do not run HubSpot-specific steps unless the user provides a HubSpot list FirstTouch can access.

## When to use
- A play has produced a batch of drafted, approved messages and it's time to send
- The user asks "is it safe to send these?" / "run the safety checks"
- You need to batch-execute a queue with per-send gating
- Setting up the default safety posture for all outreach

## When NOT to use
- You're only drafting (no send) — safety gates still conceptually apply but execution doesn't happen
- Internal review/analysis only

## The 5 gates (all must pass before any send)

This play operationalizes [`safety-governance.md`](../../references/safety-governance.md). Every queued send runs through:

1. **Duplicate check** — not in an active sequence, not contacted in cooldown window (FirstTouch)
2. **Owner routing** — contact has an owner and the authorized user may message on their behalf (HubSpot)
3. **Account-safety limits** — the LinkedIn seat is under daily/weekly caps (FirstTouch)
4. **Human approval** — the exact draft is approved per-send (first-touch) or per-batch (follow-ups)
5. **Log after send** — touch written to HubSpot timeline within minutes (FirstTouch)

## Step-by-step

### 1. Receive the queue
Take the drafted batch from whatever play produced it (01/02/04/06/10). Each item: recipient, company, owner, message type, draft, source signal.

### 2. Run gates 1–3 programmatically (FirstTouch + HubSpot MCP)
For each queued item, evaluate:
- Gate 1 (duplicate): FirstTouch campaign history check → PASS/SKIP
- Gate 2 (owner): HubSpot owner lookup → PASS/ROUTE/FLAG
- Gate 3 (limits): FirstTouch seat usage → PASS/STOP

Produce a status table:
| # | Recipient | Owner | G1 Dup | G2 Owner | G3 Limit | Status |
|----|-----------|-------|--------|----------|----------|--------|
| 1 | Dana Lee | Riley | PASS | PASS | PASS | ✅ Ready to send |
| 2 | Devon C. | (none) | PASS | **ROUTE** | PASS | ⚠ Needs owner |
| 3 | Maya P. | Riley | **SKIP** | PASS | PASS | 🚫 Recently contacted |

### 3. Present the cleared batch for approval (Gate 4)
Show only items that passed G1–G3. Each with its full draft. **First-touch sends require per-send approval; follow-ups may be batch-approved.**

### 4. Execute approved sends (FirstTouch MCP)
Send each approved message via FirstTouch. After each:
- Confirm send success
- Trigger HubSpot timeline log
- Mark item complete

### 5. Verify logging (Gate 5)
Confirm each send appears on the contact timeline. If a log fails → **alert**, do not mark complete; retry or surface.

### 6. Produce the execution report
```
Execution Report — {date}
Sent: 7 | Skipped (duplicate): 3 | Rerouted (no owner): 1 | Held (over limit): 0
All sends logged to HubSpot: ✅
Seat usage after batch: 18/25 daily connection requests
```

## Output
- Pre-send safety status table
- Execution report (sent/skipped/rerouted/held)
- HubSpot logging confirmation per send
- Updated seat-usage status

## Examples
**In:** 12 drafted connection requests from play 01.
**Gates run:** 8 pass all 3, 2 skipped (recently contacted), 1 rerouted (no owner), 1 held (over limit).
**Out:** 8 sent + logged; clear report of the other 4.

## Why this play wins
It turns "AI outreach" from scary to enterprise-safe. A buyer who trusts the gates will let the agent run; one who doesn't will throttle it to zero. This play is what makes the whole pack deployable.

## Pitfalls
- **Batch-approving first touches** — never. First-touch sends are per-send only.
- **Skipping the log verification** — a send that didn't log is a blind spot. Always confirm Gate 5.
- **Ignoring the seat-usage trend** — if usage creeps up over days, the account is at risk. Surface trends, not just per-batch numbers.

## Reference
- Full gate definitions + limits: [`../../references/safety-governance.md`](../../references/safety-governance.md)
- System model: [`../../references/system-grounding.md`](../../references/system-grounding.md)
