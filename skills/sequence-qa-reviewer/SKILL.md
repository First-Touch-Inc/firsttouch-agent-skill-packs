---
name: sequence-qa-reviewer
description: Review a FirstTouch LinkedIn campaign/sequence for risk and quality before it launches — checking send safety, messaging quality, personalization depth, duplicate risk, and compliance with the FirstTouch messaging framework. Produces a risk-scored review with specific fixes. Use when the user wants to QA a campaign, review a sequence before launch, check if outreach is safe/good, or audit existing live campaigns.
metadata:
  author: firsttouch
  version: "1.1"
  category: play
  requires: [firsttouch-mcp]
---

# Sequence QA Reviewer

**Outcome:** Catch a bad campaign before it launches — protecting the account and improving reply rates.

## First-run onboarding gate
Before running this skill for the first time in a workspace, load `../../references/onboarding.md` and complete the onboarding questions. Do not proceed until you know: LinkedIn account type (free/basic = no connection notes; recommend 10 connection requests/day and never exceed the FirstTouch max of 20/day; Sales Navigator/Premium = connection notes available; recommend 20 connection requests/day and never exceed the FirstTouch max of 30/day), HubSpot access (MCP, service key/private app token, HubSpot list only, or none), and which play the user wants to run. Recommend high-intent plays before outbound to keep the LinkedIn account healthy. If HubSpot is unavailable, do not run HubSpot-specific steps unless the user provides a HubSpot list FirstTouch can access.

## When to use
- "Review this campaign before I launch"
- QA-ing a sequence a rep or agent built
- Auditing already-live campaigns for drift/risk
- Pre-flight check for any new batch

## Step-by-step

### 1. Pull the campaign (FirstTouch MCP)
List the workspace's flow plans with `list_flow_plans` and pull the matching definition (use `get_flow_workspace` for workspace context and `get_flow_available_variables` to see which personalization variables the flow can resolve). Get the campaign/flow/sequence definition: steps, message types, timing, target list, sender seat, and personalization variables used. If the MCP cannot retrieve the full definition, ask the user to paste or export the sequence steps and mark missing fields as `manual review required` rather than failing silently.

### 2. Run the 5 review dimensions

#### A. Send safety
- Total volume vs. seat daily/weekly limits
- Step timing (too aggressive = account risk)
- Mix of action types (connection request, LinkedIn message, email/call/manual task where supported) within safe bounds
- Any active account warnings? → **hard stop**

#### B. Messaging quality (load `firsttouch-messaging`)
For each step's message, run the quality gate:
- Signal present or just template?
- Meeting ask in an opener/connection request? (violation)
- Jargon / flattery / em-dashes?
- Length within limits?
- Seniority-calibrated?

#### C. Personalization depth
- Variables used (just {first_name}? or real signals?)
- Does the message read generically if variables are stripped? (bad)
- Tier-appropriate depth (T1 deep / T3 light)

#### D. Duplicate / conflict risk
- Overlap with active sequences (same contacts in 2 campaigns?)
- Cooldown respected between steps and across campaigns
- "Already contacted" gate enabled

#### E. Compliance & brand
- Claims verifiable (no fabricated proof points)
- Unsubscribe/opt-out path for email or any message type that requires one
- Tone matches brand voice

### 3. Score each dimension
Each: ✅ Pass / ⚠ Issues / ❌ Fail, with specifics.

### 4. Produce the review report
```
CAMPAIGN QA — "{campaign name}" — {date}
Overall: ⚠ REVIEW REQUIRED (2 issues, 1 hard block)

A. Send safety:        ❌  — 180 connection requests in one step exceeds the 30/day Sales Nav or 20/day free/basic FirstTouch connection-request max; recommended safe limits are 20/day and 10/day respectively (HARD BLOCK above max)
B. Messaging quality:  ⚠  — Step 2 has a meeting ask in an opener (violates iron rule)
C. Personalization:    ✅  — uses hiring-signal variable, tier-appropriate
D. Duplicate risk:     ✅  — cooldown + duplicate gate enabled
E. Compliance:         ✅  — claims verifiable, opt-out present

FIXES (in order):
1. HARD BLOCK: split step 1 into batches within the documented daily cap: recommended ≤10/day on free/basic and ≤20/day on Sales Nav/Premium for recurring queues; never exceed the FirstTouch max of 20/day free/basic or 30/day Sales Nav/Premium
2. Step 2: remove meeting ask; convert to value touch (see messaging-framework)
3. Optional: add {recent_post} variable to step 1 for deeper personalization
```

### 5. Recommend go/fix/no-go
- All pass → ✅ **Go**
- Issues but no hard blocks → ⚠ **Fix recommended** (list)
- Any hard block → ❌ **Do not launch** until fixed

## Output
- Risk-scored review (5 dimensions)
- Specific, ordered fixes
- Go/fix/no-go recommendation

## Examples
**Campaign:** rep built a 4-step sequence targeting 500 contacts.
**QA finds:** step 1 batches 180 connects (hard block) + step 2 asks for a meeting early.
**Outcome:** ❌ Do not launch. Fix the two issues, re-QA, then go.

## Why this play wins
One bad launch can restrict a LinkedIn account for weeks. This play is cheap insurance — a 5-minute review that prevents the most common, most damaging mistakes.

## Pitfalls
- **QA-ing the copy but not the volume** — the message can be perfect and still get the account flagged if volume is unsafe. Always check send safety first.
- **Approving with an unverified proof point** — "our customers see 10x ROI" must be real. Flag unverified claims.
- **Ignoring cross-campaign duplicates** — a contact in 2 active sequences is a fast track to spam-feel. Always check overlap.

## Reference
- Messaging framework (dimension B): [`../../references/messaging-framework.md`](../../references/messaging-framework.md)
- Safety limits (dimension A/D): [`../../references/safety-governance.md`](../../references/safety-governance.md)
