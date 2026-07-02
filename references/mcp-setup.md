# MCP Setup - Connecting the Tools Your Plays Need

**What is MCP?** It's the plug that lets your AI agent use FirstTouch. In ChatGPT and Claude.ai it shows up in settings as a **Connector**; in Claude Code, Cursor, Windsurf, and Codex it's called an **MCP server**. Same thing, different label. You set it up once, and it never sees your LinkedIn password - it only performs the actions you approve.

Each play lists the MCPs it requires. Connect them once; they're shared across all plays.

**Before running the first play:** complete [`onboarding.md`](onboarding.md). The agent needs to know the user's LinkedIn account type (free/basic vs Sales Navigator/Premium), HubSpot access path, and first play choice before it recommends or queues any volume.

---

## 1. FirstTouch MCP (required by every play)

FirstTouch is the execution layer - it's what lets the agent actually perform LinkedIn actions and log them.

**Connect in Claude / Cursor / your harness:**
- **Server URL:** `https://mcp.firsttouch.ai`
- **Auth:** OAuth (browser flow) or API key from your FirstTouch workspace settings
- **Scope:** scoped to the authorized user's LinkedIn account and connected HubSpot

**Verify it's connected:**
> Ask the agent: *"Show my FirstTouch current user and workspace, then list my flow plans and audiences."*

If the agent can return campaign + seat data, the MCP is live.

**What it exposes (conceptual tool surface):**
- FirstTouch execution objects - audiences, flow plans/campaigns, dynamic actions, and enrollments depending on the connected workspace
- Campaign/flow control - launch, pause, edit when the connected workspace exposes those actions
- LinkedIn actions - connection request, message, email step, call task, or manual task depending on the flow/action type exposed in the workspace
- Engagement data - LinkedIn post likes and comments from monitored profiles. Profile-view signals are not available. The agent cannot read arbitrary inbox history; FirstTouch-tracked outreach can report reply/engagement status for actions it manages, and team metrics can summarize reply sentiment where available.
- Logging - FirstTouch/HubSpot activity logging where the workspace integration supports it
- Safety - seat usage, daily limits, duplicate checks, Exclusion Lists/suppression, and Sending Schedule/quiet-hours settings where exposed by the connected workspace

**Terminology note:** this skill pack uses human-friendly words like "play," "sequence," "campaign," and "queue." In FirstTouch, the actual object may be an **Audience**, **Flow Plan**, **Dynamic Action**, or **Enrollment**. The agent should state which FirstTouch object it created or used.

---

## 2. HubSpot MCP or service key (required by HubSpot-specific plays)

HubSpot is the system of record - it gives the agent the CRM context that makes outreach *smart* and *owner-safe*.

**Ask during onboarding:**
- "Do you use HubSpot?"
- "Can you connect the HubSpot MCP, or provide a HubSpot service key / private app token so the agent can access internal CRM data?"
- "If you cannot connect HubSpot yet, can you create a HubSpot list for the audience so FirstTouch can access it?"

**Connect:**
- **MCP URL:** If your agent has a native HubSpot connector option, use that. Otherwise use `https://mcp.hubspot.com/anthropic` (Anthropic-hosted), unless your agent/connector UI lists a different current HubSpot MCP endpoint.
- **Auth:** OAuth from HubSpot, or a service key / private app token connected in the user's agent/harness
- **Scopes typically needed:** contacts (read), companies (read), deals (read), owners (read), lists (read), tasks (read/write when using the HubSpot social task runner), timeline activity (read). Write scopes only if a play explicitly logs back or completes HubSpot tasks.

**If HubSpot is not connected:**
- Do **not** run HubSpot-specific plays that require CRM owners, lifecycle/deal data, lists, or logging.
- Ask the user to create a HubSpot list that FirstTouch can access, then run only the list-based portions of the play.
- If neither HubSpot access nor a list exists, run only plays that can operate from FirstTouch data. For AI SDR, ask for the user's ICP and build the list with FirstTouch Discover Contacts.

**Verify contacts/owners:**
> *"Show me 5 contacts in lifecycle stage 'Marketing Qualified Lead' and their owner."*

**Verify task access for the HubSpot social task runner:**
> *"Show my open HubSpot tasks due today that mention LinkedIn, connection request, message on LinkedIn, LI, or social touch. Confirm whether you can mark one selected test task complete, but do not complete it yet."*

**What it exposes:**
- Contacts & companies - properties, lifecycle, owner, activity
- Deals - stage, amount, last activity, close date
- Lists - active/static membership
- Owners - the humans who own relationships (for routing)
- Tasks - read due tasks and mark selected tasks complete when the HubSpot social task runner is approved and the connected MCP supports task writes

---

## 3. Enrichment (FirstTouch native; external MCP optional)

For finding LinkedIn URLs, emails, and firmographics when HubSpot is missing them.

**Options:**
- **Clay MCP** - richest for ICP + waterfall enrichment
- **Surfe MCP** - LinkedIn-native enrichment + CRM sync
- **Any provider MCP** your team already uses

Social Engagement note: monitor the user's own founder/leadership personal profile when available; FirstTouch does not track company-page/profile engagement. If owned engagement is thin, monitor a relevant competitor founder, category influencer, or executive profile and work the ICP-fit people engaging there. Use post likes/comments only; profile views are not available.

Use FirstTouch enrichment when the MCP exposes contact/company enrichment and credits are available. Clay, Surfe, or another enrichment MCP is optional and can supplement FirstTouch data, but it is not a prerequisite for AI SDR or warm-engager qualification.

If no enrichment MCP is connected, the agent should use HubSpot, FirstTouch, CSV/imported-list, or user-provided fields. Records missing a usable LinkedIn URL should be skipped or queued for enrichment, never filled with guessed data.

---

## Connection checklist (do this before running any play)

- [ ] FirstTouch MCP connected and returns campaign data
- [ ] LinkedIn account type captured: free/basic (recommend 10 connection requests/day, FirstTouch max 20/day, no connection notes) or Sales Navigator/Premium (recommend 20 connection requests/day, FirstTouch max 30/day, connection notes available)
- [ ] HubSpot MCP or service key/private app token connected and returns contacts + owners (if your play needs it)
- [ ] HubSpot MCP can read open tasks and supports task completion before running the HubSpot social task runner
- [ ] If HubSpot is not connected, a HubSpot list or other FirstTouch-accessible source is available for any HubSpot-dependent play
- [ ] The authorized FirstTouch user's LinkedIn account is healthy (not near limits)
- [ ] You know **who owns** the target contacts in HubSpot (plays route by owner)
- [ ] You've decided the **approval workflow** - FirstTouch/in-agent by default; Slack/email only if externally configured (see `safety-governance.md`)

Slack/email approval delivery requires external workspace configuration and is not assumed FirstTouch-native. If Slack/email/FirstTouch approvals are not configured yet, use in-agent approval: the agent presents the approval table in chat, marks every row or flow as awaiting approval, and waits for the human before executing anything.

---

## Troubleshooting

Setup and operational failures (MCP auth, cooldowns and limits, stalled queues, credit spend, suppression misses, mid-run recovery) are covered in [`troubleshooting.md`](troubleshooting.md). Load that file whenever something breaks after setup.
