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
> Ask the agent: *"List my active FirstTouch campaigns and the seats connected."*

If the agent can return campaign + seat data, the MCP is live.

**What it exposes (conceptual tool surface):**
- Campaign control — launch, pause, edit
- LinkedIn actions — connection request, message, InMail, profile view
- Engagement data — who liked/commented/viewed. Inbox reply reading is not currently available.
- Logging — write LinkedIn activity to HubSpot timelines
- Safety — seat usage, daily limits, duplicate checks

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

## 3. Enrichment MCP (optional for AI SDR, founder AI SDR, warm-engager qualification, and customer-champion plays)

For finding LinkedIn URLs, emails, and firmographics when HubSpot is missing them.

**Options:**
- **Clay MCP** — richest for ICP + waterfall enrichment
- **Surfe MCP** — LinkedIn-native enrichment + CRM sync
- **Any provider MCP** your team already uses

Connect per the provider's docs. Not required for the pack to function, but it materially improves AI SDR, founder AI SDR, warm-engager qualification, and customer-champion plays.

---

## Connection checklist (do this before running any play)

- [ ] FirstTouch MCP connected and returns campaign data
- [ ] LinkedIn account type captured: free/basic (10 connection requests/day max, no connection notes) or Sales Navigator/Premium (up to 20/day, connection notes available)
- [ ] HubSpot MCP or service key/private app token connected and returns contacts + owners (if your play needs it)
- [ ] If HubSpot is not connected, a HubSpot list or other FirstTouch-accessible source is available for any HubSpot-dependent play
- [ ] The authorized FirstTouch user's LinkedIn account is healthy (not near limits)
- [ ] You know **who owns** the target contacts in HubSpot (plays route by owner)
- [ ] You've decided the **approval workflow** — Slack, email, or in-agent review (see `safety-governance.md`)

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|-------------|-----|
| Agent says it "can't send" | FirstTouch MCP not connected or OAuth expired | Re-auth in workspace settings |
| Agent ignores owner routing | HubSpot MCP missing or no owner scope | Reconnect HubSpot MCP with owner read scope |
| Agent drafts but never logs | Logging not enabled / wrong HubSpot portal | Confirm FirstTouch↔HubSpot sync is active |
| Duplicate messages sent | Duplicate-check skipped | Ensure the play runs the "already contacted?" gate (see `safety-governance.md`) |
