# System Grounding — How FirstTouch, HubSpot, and Agents Fit Together

*Read this once. Every play assumes this mental model.*

---

## The three layers

```
┌─────────────────────────────────────────────────────────┐
│  REASONING LAYER                                        │
│  Claude / ChatGPT / Cursor / Codex — the AI agent       │
│  Reads signals, decides who + what + when, drafts copy  │
└───────────────┬─────────────────────────────────────────┘
                │ calls tools via MCP
┌───────────────▼─────────────────────────────────────────┐
│  EXECUTION LAYER                                        │
│  FirstTouch — "the hands"                               │
│  Performs LinkedIn actions, respects safety limits,     │
│  routes by owner, logs every touch                      │
└───────────────┬─────────────────────────────────────────┘
                │ logs + attributes to
┌───────────────▼─────────────────────────────────────────┐
│  SYSTEM OF RECORD                                       │
│  HubSpot — the brain / CRM                              │
│  Contacts, companies, deals, lifecycle, owners,         │
│  activity timelines, pipeline                           │
└─────────────────────────────────────────────────────────┘
```

**The key idea:** the AI agent is the brain, FirstTouch is the hands, HubSpot is the memory. An agent without FirstTouch can *think* about outreach but can't *perform* it safely or log it. FirstTouch is what turns intent into governed action.

---

## What FirstTouch actually does (the execution layer)

FirstTouch is the **HubSpot-native LinkedIn outreach and social selling platform**. Through its MCP, an agent can:

- **Trigger** LinkedIn actions (connection requests, messages, InMail) from HubSpot workflows or directly
- **Track** every touch and **attribute** it to contacts, companies, and deals
- **Log** LinkedIn activity to the HubSpot contact timeline automatically
- **Respect** routing rules (owner-based), approval gates, and account-safety limits
- **Expose** a public MCP server (`mcp.firsttouch.ai`) so AI agents run outreach without a browser

Customer-facing positioning reference: works with HubSpot-connected workflows where configured and is built around **human-in-the-loop** execution. Check the live pricing and compliance pages before quoting price, HubSpot edition coverage, or certification details.

---

## What HubSpot provides (the system of record)

When the **HubSpot MCP** is connected, the agent can read:

- **Contacts & companies** — properties, lifecycle stage, owner, recent activity
- **Deals** — stage, amount, last activity date, probability
- **Lists** — static and active (e.g. "engaged but no meeting," "staged > 14 days")
- **Timeline activity** — emails, meetings, notes, and (via FirstTouch) LinkedIn touches
- **Owners** — who owns the relationship (critical for routing)

This is what makes plays **attribution-aware** and **owner-safe**. Without HubSpot context, an agent would blindly message prospects regardless of relationship state.

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

Steps 1–4 and 6–7 are where the agent earns its keep. Step 5 is FirstTouch. **Step 4 (the gate) is non-negotiable** — it's what makes this safe for real accounts.

---

## Which MCPs each play needs

| MCP | What it gives the agent | Required by |
|-----|------------------------|-------------|
| **FirstTouch MCP** | LinkedIn action execution, engagement data, logging | Every play |
| **HubSpot MCP** | CRM context, lifecycle, owners, deals, lists | HubSpot signal touches, inbound speed-to-lead, website visitor follow-up, stalled deal reactivation, customer champion, and HubSpot-backed recipes |
| **Enrichment MCP** (Clay, Surfe, etc.) | LinkedIn URLs, emails, firmographics | Optional for AI SDR, founder AI SDR, warm-engager qualification, and customer-champion plays |

Full setup instructions: [`mcp-setup.md`](mcp-setup.md).

---

## Agent persona: the "competent team member"

The agent should behave like a **competent, cautious SDR**, not a script:

- It **checks context before acting** (never messages a contact already in an active sequence)
- It **drafts for review** by default (never sends without the gate)
- It **logs what it did** so the human can audit
- It **knows when to stop** and ask, rather than push volume

This persona is reinforced in every play's `SKILL.md`. If an agent ever seems to be racing to send volume, something is wrong — pull it back to draft-and-gate.
