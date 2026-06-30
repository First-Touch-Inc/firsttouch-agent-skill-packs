# MCP Setup — Connecting the Tools Your Plays Need

Each play lists the MCPs it requires. Connect them once; they're shared across all plays.

**Before running the first play:** complete [`onboarding.md`](onboarding.md). The agent needs to know the user's LinkedIn account type (free/basic vs Sales Navigator/Premium), HubSpot access path, and first play choice before it recommends or queues any volume.

---

## 1. FirstTouch MCP (required by every play)

FirstTouch is the execution layer — it's what lets the agent actually perform LinkedIn actions and log them.

**Connect in Claude / Cursor / your harness:**
- **Server URL:** `https://mcp.firsttouch.ai`
- **Auth:** OAuth (browser flow) or API key from your FirstTouch workspace settings
- **Scope:** scoped to the authorized user's LinkedIn account and connected HubSpot

**Verify it's connected:**
> Ask the agent: *"Show my FirstTouch current user and workspace, then list my flow plans and audiences."*

If the agent can return campaign + seat data, the MCP is live.

**What it exposes (conceptual tool surface):**
- FirstTouch execution objects — audiences, flow plans/campaigns, dynamic actions, and enrollments depending on the connected workspace
- Campaign/flow control — launch, pause, edit when the connected workspace exposes those actions
- LinkedIn actions — connection request, message, email step, call task, or manual task depending on the flow/action type exposed in the workspace
- Engagement data — LinkedIn post likes and comments from monitored profiles. Profile-view signals are not available. The agent cannot read arbitrary inbox history; FirstTouch-tracked outreach can report reply/engagement status for actions it manages, and team metrics can summarize reply sentiment where available.
- Logging — FirstTouch/HubSpot activity logging where the workspace integration supports it
- Safety — seat usage, daily limits, duplicate checks

**Terminology note:** this skill pack uses human-friendly words like "play," "sequence," "campaign," and "queue." In FirstTouch, the actual object may be an **Audience**, **Flow Plan**, **Dynamic Action**, or **Enrollment**. The agent should state which FirstTouch object it created or used.

---

## 2. HubSpot MCP or service key (required by HubSpot-specific plays)

HubSpot is the system of record — it gives the agent the CRM context that makes outreach *smart* and *owner-safe*.

**Ask during onboarding:**
- "Do you use HubSpot?"
- "Can you connect the HubSpot MCP, or provide a HubSpot service key / private app token so the agent can access internal CRM data?"
- "If you cannot connect HubSpot yet, can you create a HubSpot list for the audience so FirstTouch can access it?"

**Connect:**
- **MCP URL:** `https://mcp.hubspot.com/anthropic` (Anthropic-hosted) — or your HubSpot MCP endpoint
- **Auth:** OAuth from HubSpot, or a service key / private app token connected in the user's agent/harness
- **Scopes typically needed:** contacts (read), companies (read), deals (read), owners (read), lists (read), timeline activity (read). Write scopes only if a play explicitly logs back.

**If HubSpot is not connected:**
- Do **not** run HubSpot-specific plays that require CRM owners, lifecycle/deal data, lists, or logging.
- Ask the user to create a HubSpot list that FirstTouch can access, then run only the list-based portions of the play.
- If neither HubSpot access nor a list exists, run only plays that can operate from FirstTouch data. For AI SDR, ask for the user's ICP and build the list with FirstTouch Discover Contacts.

**Verify:**
> *"Show me 5 contacts in lifecycle stage 'Marketing Qualified Lead' and their owner."*

**What it exposes:**
- Contacts & companies — properties, lifecycle, owner, activity
- Deals — stage, amount, last activity, close date
- Lists — active/static membership
- Owners — the humans who own relationships (for routing)

---

## 3. Enrichment (FirstTouch native; external MCP optional)

For finding LinkedIn URLs, emails, and firmographics when HubSpot is missing them.

**Options:**
- **Clay MCP** — richest for ICP + waterfall enrichment
- **Surfe MCP** — LinkedIn-native enrichment + CRM sync
- **Any provider MCP** your team already uses

Social Engagement note: monitor the user's own founder/leadership/company profile when available. If owned engagement is thin, monitor a relevant competitor founder, category influencer, or executive profile and work the ICP-fit people engaging there. Use post likes/comments only; profile views are not available.

Use FirstTouch enrichment when the MCP exposes contact/company enrichment and credits are available. Clay, Surfe, or another enrichment MCP is optional and can supplement FirstTouch data, but it is not a prerequisite for AI SDR or warm-engager qualification.

If no enrichment MCP is connected, the agent should use HubSpot, FirstTouch, CSV/imported-list, or user-provided fields. Records missing a usable LinkedIn URL should be skipped or queued for enrichment, never filled with guessed data.

---

## Connection checklist (do this before running any play)

- [ ] FirstTouch MCP connected and returns campaign data
- [ ] LinkedIn account type captured: free/basic (10 connection requests/day max, no connection notes) or Sales Navigator/Premium (up to 20/day, connection notes available)
- [ ] HubSpot MCP or service key/private app token connected and returns contacts + owners (if your play needs it)
- [ ] If HubSpot is not connected, a HubSpot list or other FirstTouch-accessible source is available for any HubSpot-dependent play
- [ ] The authorized FirstTouch user's LinkedIn account is healthy (not near limits)
- [ ] You know **who owns** the target contacts in HubSpot (plays route by owner)
- [ ] You've decided the **approval workflow** — Slack, email, or in-agent review (see `safety-governance.md`)

If Slack/email/FirstTouch approvals are not configured yet, use in-agent approval: the agent presents the approval table in chat, marks every row or flow as awaiting approval, and waits for the human before executing anything.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| Agent says it "can't send" | FirstTouch MCP not connected or OAuth expired | Re-auth in workspace settings |
| Agent ignores owner routing | HubSpot MCP missing or no owner scope | Reconnect HubSpot MCP with owner read scope |
| Agent drafts but never logs | Logging not enabled / wrong HubSpot portal | Confirm FirstTouch↔HubSpot sync is active |
| Duplicate messages sent | Duplicate-check skipped | Ensure the play runs the "already contacted?" gate (see `safety-governance.md`) |
