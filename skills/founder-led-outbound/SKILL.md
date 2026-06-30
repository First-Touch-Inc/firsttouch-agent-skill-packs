---
name: founder-led-outbound
description: Run the founder AI SDR motion: build a targeted prospect list from a HubSpot list or FirstTouch Discover Contacts, enrich each prospect, draft founder-voice LinkedIn outreach, and queue a small daily batch for founder approval. Use when a founder wants their own version of AI SDR, strategic-account outbound, founder-led growth, or daily founder-voice prospecting without sounding like an SDR.
metadata:
  author: firsttouch
  version: "1.1"
  category: play
  requires: [firsttouch-mcp]
---

# Founder-Led AI SDR

**Outcome:** Produce a daily approval-ready batch of founder-voice LinkedIn touches from either an existing HubSpot/contact list or a newly discovered ICP list, without requiring HubSpot to start.

## First-run onboarding gate
Before running this skill for the first time in a workspace, load `../../references/onboarding.md` and complete the onboarding questions. Do not proceed until you know: LinkedIn account type (free/basic = no connection notes and 10 connection requests/day max; Sales Navigator/Premium = connection notes available and up to 20/day), HubSpot access (MCP, service key/private app token, HubSpot list only, or none), and which play the user wants to run. For founders, recommend the **social engagement flow first**, then founder-led AI SDR once warm-signal motions are running. If HubSpot is unavailable, this play can still run by building a new ICP list with FirstTouch Discover Contacts.

## When to use
- "I'm the founder, help me do my own outbound"
- "Run AI SDR, but make it sound like me"
- Founder-led growth / founder-mode GTM
- Strategic accounts where the founder's voice matters
- Booking meetings from the founder's network, post engagement, or a newly discovered ICP list

## When NOT to use
- High-volume SDR outbound where the founder will not personally approve the queue
- Outreach from a sender who is not authorized to use the founder's LinkedIn seat
- Generic blasts with weak personalization or no real signal

## What makes founder AI SDR different
Founder-led AI SDR is the same motion as AI SDR, but with a founder lens:
- **Lower volume, higher taste bar** - every row must feel worthy of the founder's name.
- **Founder voice** - brief, direct, specific, and free of SDR-speak.
- **Real signal first** - post engagement, company change, role context, mutual connection, or a clear ICP reason.
- **Daily approval queue** - the agent drafts; the founder approves; FirstTouch executes.
- **No HubSpot required to start** - if there is no HubSpot list, use FirstTouch Discover Contacts from the founder's ICP.

## Daily volume rules for founder AI SDR

| LinkedIn account | Daily founder AI SDR batch cap | Connection request note |
|---|---:|---|
| Free/basic | 10 connection-request rows/day | No note |
| Sales Navigator / Premium | 20 connection-request rows/day | No note by default for cold AI SDR; connection notes are allowed only when the founder explicitly approves a strong, relevant reason |

Keep the cap lower if the account is new, warned, or acceptance/reply rates drop. The no-note default is conservative: cold connection notes often reduce acceptance or feel automated under a founder's name. Warm-signal plays can use notes when Sales Nav/Premium is available and the note is explicitly approved.

## Default outreach plan
For every approved prospect, first check LinkedIn connection status:

| Connection status | Sequence |
|---|---|
| Already connected | Send the first founder-voice message, wait 2 days, then send one follow-up if there is no reply. |
| Not connected | Send a blank connection request with no note. After the prospect accepts, send the first founder-voice message, wait 2 days, then send one follow-up if there is no reply. |

**Message rules:**
- First message and follow-up are each **2 sentences max**.
- Reference one real signal that might point to the prospect needing the user's solution.
- Use a lightweight ask CTA. Do **not** ask for a meeting in the connection request, first message, or first follow-up.
- Do **not** use em dashes in drafted outreach copy.
- Do not fabricate personalization. Use only HubSpot, FirstTouch, enrichment, or user-provided data.

## Step-by-step

### 0. Capture founder voice and define the founder ICP
Ask for 2-3 sample founder posts/messages or concise tone rules: phrases to use, phrases to avoid, level of formality, common founder POV, and topics the founder will not touch. Use this voice profile for every draft; if it is missing, draft one conservative sample and ask for calibration before building volume.

### 0b. Confirm or define the founder ICP
If HubSpot is unavailable or no saved ICP exists, ask the founder for a concise ICP before using Discover Contacts: industries, company size, geography, target titles/seniority, exclusions, and 1-3 must-have signals. Save that ICP summary in the output so future daily runs reuse it instead of guessing.

### 1. Choose the source path

**Path A - HubSpot list exists:**
- Open the HubSpot contact or company list the user provides.
- If it is a company list, select the founder-relevant personas at each company using the ICP and the user's target titles.
- Capture company/contact fields, owner if available, lifecycle/deal context, prior activity, and LinkedIn URL if present.

**Path B - no HubSpot access or no list:**
- Use the saved founder ICP from Step 0b, or ask for it if missing: target industries, company size, geography, titles/seniority, exclusions, and must-have signals.
- Use **FirstTouch Discover Contacts** to build a small prospect list from that ICP.
- Preview a small sample before larger imports because discovery/enrichment can consume FirstTouch credits.
- Save the discovered contacts into a FirstTouch audience or list for future daily runs.

### 2. Enrich and prioritize
For each contact/company, enrich missing fields before drafting:
- LinkedIn URL and current title
- company domain, size, industry, location
- relevant company/person signal when available
- mutual connection or social context when available

Before drafting, run Gate 0 suppression/DNC and Gate 1 duplicate/recent-contact checks from `../../references/safety-governance.md`. Exclude anyone who is suppressed, opted out, already in an active sequence, recently contacted, outside ICP, missing a usable LinkedIn profile, owned by someone else without routing approval, or not appropriate for the founder to contact personally.

Rank by ICP fit, signal strength, seniority, strategic account value, and whether the founder has a warm path.

### 3. Draft in founder voice
Load `firsttouch-messaging`, then override tone for the founder:
- first person from the founder, never "our team noticed"
- brief and direct
- signal-led with one concrete reason for reaching out
- soft CTA only, no early meeting ask
- no em dashes in drafted outreach copy

If the draft sounds like an SDR wrote it, rewrite before showing it.

### 4. Present the daily approval queue
Do **not** send automatically. Output an approval table:

| # | Prospect | Company | Source | Why them | Connection status | Signal | Founder-voice first message | 2-day follow-up | Action | Status |
|---|---|---|---|---|---|---|---|---|---|---|

Every row should be marked `awaiting founder approval`.

### 5. After approval, queue in FirstTouch
After founder approval:
- add approved contacts to the right FirstTouch flow/campaign, or queue dynamic actions
- remember: publishing a flow activates it but does **not** enroll awaiting contacts; explicitly enroll approved contacts/items, then confirm they moved from awaiting to in-progress
- enforce duplicate checks, account-safety limits, and approval status from `../../references/safety-governance.md`
- log execution and outcomes back to HubSpot when HubSpot is connected
- if HubSpot is not connected, keep the execution record in FirstTouch and clearly state that CRM owner routing/logging is unavailable
- keep rejected contacts out of the next daily batch unless the founder asks to revisit them

### 6. Recommend daily automation
Recommend a recurring daily motion only after the founder approves the first batch quality. This is an agent-harness schedule/reminder, not a FirstTouch autonomous-send feature:
> "Run the FirstTouch founder AI SDR play for today. Use my saved ICP/list, enrich fresh contacts, prepare up to my daily cap, and show me the approval table. Do not send anything until I approve."

## Output
- source summary: HubSpot list or newly discovered ICP list
- enriched account/contact table
- daily founder AI SDR batch capped at 10 free/basic or 20 Sales Navigator/Premium connection-request rows
- customized founder-voice first message and 2-day follow-up for each prospect
- approval table ready for founder review
- optional daily automation/agent setup prompt

## Examples
**Prospect:** Priya Shah, VP GTM at a Series B fintech.
**Signal:** Raised $40M and is hiring 5 GTM roles.
**Draft first message:** "Priya, congrats on the Series B. When teams add GTM headcount that quickly, LinkedIn activity usually gets hard to track back to pipeline, worth comparing notes on how others are handling it?"
**2-day follow-up:** "Quick follow-up, the reason I asked is that attribution usually breaks right when hiring ramps. Happy to send the short teardown we use with founders if useful."

## Pitfalls
- Treating founder AI SDR like a bulk SDR sequence.
- Letting weak personalization go out under the founder's name.
- Requiring HubSpot when the founder has no CRM list; define the ICP and use Discover Contacts instead.
- Asking for meetings too early.
- Skipping founder approval.

## Reference
- Onboarding: [`../../references/onboarding.md`](../../references/onboarding.md)
- Messaging: [`../../references/messaging-framework.md`](../../references/messaging-framework.md)
- Safety and approval gates: [`../../references/safety-governance.md`](../../references/safety-governance.md)
