# System Grounding - How FirstTouch, HubSpot, and Agents Fit Together

*Read this once. This reference is shared across packs; execute only the skills and recipes included in the installed pack.*

---

## The three layers

```
┌─────────────────────────────────────────────────────────┐
│  REASONING LAYER                                        │
│  Claude / ChatGPT / Cursor / Codex - the AI agent       │
│  Reads signals, decides who + what + when, drafts copy  │
└───────────────┬─────────────────────────────────────────┘
                │ calls tools via MCP
┌───────────────▼─────────────────────────────────────────┐
│  EXECUTION LAYER                                        │
│  FirstTouch - "the hands"                               │
│  Performs LinkedIn actions, respects safety limits,     │
│  routes by owner, logs every touch                      │
└───────────────┬─────────────────────────────────────────┘
                │ logs + attributes to
┌───────────────▼─────────────────────────────────────────┐
│  OPTIONAL SYSTEM OF RECORD                              │
│  HubSpot - CRM memory when connected                    │
│  Contacts, companies, deals, lifecycle, owners,         │
│  activity timelines, pipeline                           │
└─────────────────────────────────────────────────────────┘
```

**The key idea:** the AI agent is the brain and FirstTouch is the governed execution layer. FirstTouch can run standalone through Audiences, Flow Plans, Discover Contacts, Dynamic Actions, and Social Engagement. HubSpot adds CRM memory: owner routing, lifecycle/deal signals, and timeline logging when connected. An agent without FirstTouch can *think* about outreach but can't *perform* it safely or log it.

---

## What FirstTouch actually does (the execution layer)

FirstTouch is a **governed LinkedIn outreach and social selling platform** that can run standalone and integrates deeply with HubSpot when connected. Through its MCP, an agent can:

- **Trigger** supported LinkedIn/social actions (connection requests, messages, flow steps, manual tasks) from HubSpot workflows or directly
- **Track** every touch and **attribute** it to contacts, companies, and deals
- **Log** LinkedIn activity to HubSpot where the FirstTouch-HubSpot integration and workspace permissions support it
- **Respect** routing rules (owner-based), approval gates, and account-safety limits
- **Expose** a public MCP server (`mcp.firsttouch.ai`) so AI agents run outreach without a browser

Customer-facing positioning reference: works standalone for FirstTouch audiences, flow plans, Discover Contacts, Dynamic Actions, and Social Engagement; works with HubSpot-connected workflows where configured; and is built around **human-in-the-loop** execution. Check the live pricing and compliance pages before quoting price, HubSpot edition coverage, or certification details.

---

## What HubSpot provides (the system of record)

When the **HubSpot MCP** is connected, the agent can read:

- **Contacts & companies** - properties, lifecycle stage, owner, recent activity
- **Deals** - stage, amount, last activity date, probability
- **Lists** - static and active (e.g. "engaged but no meeting," "staged > 14 days")
- **Timeline activity** - emails, meetings, notes, and (via FirstTouch) LinkedIn touches
- **Owners** - who owns the relationship (critical for routing)

This makes CRM-sourced plays **attribution-aware** and **owner-safe**. Without HubSpot context, the agent should use FirstTouch-only sources, imported lists, Discover Contacts, or Social Engagement, and should not claim CRM owner routing, deal context, or HubSpot timeline logging.

---

## The loop every play follows

Most plays implement a version of this cycle:

```
1. SIGNAL      ← a HubSpot event, a LinkedIn engagement, or a time condition
2. QUALIFY     ← is this the right person, right account, right moment?
3. DRAFT       ← personalize the touch (see messaging-framework.md)
4. GATE        ← human approval before any send (see safety-governance.md)
5. EXECUTE     ← FirstTouch performs the LinkedIn action
6. LOG         ← FirstTouch logs to HubSpot timeline
7. MEASURE     ← track replies, meetings, influenced pipeline
```

Steps 1-4 and 6-7 are where the agent earns its keep. Step 5 is FirstTouch. **Step 4 (the gate) is non-negotiable** - it's what makes this safe for real accounts.

---

## Which MCPs each play needs

| MCP | What it gives the agent | Required by |
|-----|------------------------|-------------|
| **FirstTouch MCP** | LinkedIn action execution, engagement data, logging | Every play |
| **HubSpot MCP** | CRM context, lifecycle, owners, deals, lists | Required for HubSpot signal touches, stalled deal reactivation, and CRM/deal/customer segments when those plays are installed. Optional but useful for inbound speed-to-lead, website visitor follow-up, AI SDR, warm engagement, and social campaigns when those can start from FirstTouch/imported/Discover sources. |
| **FirstTouch enrichment + optional external enrichment MCP** | LinkedIn URLs, emails, firmographics | FirstTouch can enrich when credits/data are available; Clay/Surfe/etc. are optional supplements, not prerequisites |

Full setup instructions: [`mcp-setup.md`](mcp-setup.md).

## Publish and enroll rule
Publishing a flow activates it but does **not** enroll awaiting contacts. After approval, explicitly enroll the approved contacts/items, then confirm they moved from awaiting to in-progress before telling the user the motion is live.

## Social Engagement source note

LinkedIn Social Engagement monitoring is a FirstTouch feature for post likes and comments. Prefer the user's own founder or executive personal profile when there is enough owned engagement; FirstTouch does not track company-page/profile engagement. If owned engagement is thin, monitor a relevant competitor founder, category influencer, or executive profile and work the ICP-fit people engaging there. Do not use profile views as a signal.

## FirstTouch object glossary

This pack uses human-friendly terms because users ask for "campaigns," "sequences," and "queues." When executing, translate them into the object the connected FirstTouch MCP supports:

| Pack term | FirstTouch execution concept |
|---|---|
| Play | The overall workflow the agent follows |
| Audience/list | The contacts/accounts selected for a motion |
| Flow plan/campaign/sequence | The approved series of LinkedIn actions and timing |
| Dynamic action queue | Per-contact actions awaiting row-level approval |
| `connection_accepted` branch | Dynamic Action append target for a LinkedIn message that should run only after a connection request is accepted |
| Enrollment | Adding approved contacts to the flow/campaign |
| Discover Contacts | FirstTouch's built-in prospect search - builds a new ICP list from filters (title, industry, geography) when no HubSpot list exists; consumes credits |
| FirstTouch-accessible list/source | Any contact source FirstTouch can read: a shared HubSpot list, an imported CSV, a FirstTouch audience, or a Discover Contacts result |
| Social Engagement | FirstTouch monitoring of likes/comments on a designated LinkedIn personal profile; collected engagers can feed the warm-engager play |
| Exclusion/DNC list | Contacts FirstTouch must never touch - checked at Gate 0 before any motion |
| Credits | FirstTouch's metered currency for Discover Contacts and enrichment; check balance before bulk operations |

**LinkedIn account types** (they are not the same thing):

| Account | Connection notes | Caps |
|---|---|---|
| Free/basic | No | Recommend 10 connection requests/day, FirstTouch max 20/day |
| LinkedIn Premium | Yes (for approved sends) | Recommend 20/day, FirstTouch max 30/day |
| Sales Navigator | Yes (for approved sends) - plus advanced search/lists | Recommend 20/day, FirstTouch max 30/day |

**Message types** (full methodology in `messaging-framework.md`): connection request → opener (post-accept, no ask) → value touch (no ask) → meeting ask (only after an exchange) → break-up.

The agent should state the exact FirstTouch object used so the user does not have to guess where approval or execution happened.

---

## Agent persona: the "competent team member"

The agent should behave like a **competent, cautious SDR**, not a script:

- It **checks context before acting** (never messages a contact already in an active sequence)
- It **drafts for review** by default (never sends without the gate)
- It **logs what it did** so the human can audit
- It **knows when to stop** and ask, rather than push volume

This persona is reinforced in every play's `SKILL.md`. If an agent ever seems to be racing to send volume, something is wrong - pull it back to draft-and-gate.

## Attribution is automatic
FirstTouch auto-tags every enrollment - no custom tag schema is needed. When the HubSpot integration is connected and engagement tracking is enabled, FirstTouch logs supported LinkedIn activity back automatically: contact properties, app events (connection request sent, connection accepted, message sent, reply received), and timeline entries for LinkedIn messages. Verify the integration settings once during setup (`mcp-setup.md`), then attribution runs on its own.

## Reply and sentiment scope
Reply sentiment is limited to FirstTouch-managed outreach metrics where available. The agent must not claim arbitrary LinkedIn inbox, email inbox, or unmanaged-thread sentiment access.

## When a prospect replies

The agent's job ends after the approved touch is queued and executed. Replies belong to the human who owns the relationship:

1. Agent drafts → human approves → FirstTouch executes the touch.
2. The prospect replies or engages. FirstTouch captures this in its managed metrics; when HubSpot is connected, the touch is already on the contact timeline for the owner to see.
3. **The owner/rep responds personally.** The agent does not send autonomous follow-ups to a reply - a follow-up is a new motion that goes back through drafting and the approval gate.
4. If the prospect asks to stop, says "not interested," or objects to being contacted: the agent's only correct actions are to add them to the exclusion/DNC list, note it in HubSpot when connected, and confirm to the user that the contact will not be touched again.
5. Replies and sentiment can be summarized in team performance reports for coaching - never for automated re-targeting.

If a user asks the agent to "handle my replies," explain this boundary: FirstTouch plays are human-in-the-loop by design, and inbox conversation is where the human takes over.
