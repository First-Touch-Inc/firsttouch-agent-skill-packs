# FirstTouch Agent Skill Packs

FirstTouch agent skill packs turn Claude, Cursor, Windsurf, and other AI workspaces into LinkedIn revenue operators through the FirstTouch MCP.

## Download packs

| Role | Download |
|---|---|
| RevOps | [https://github.com/First-Touch-Inc/firsttouch-agent-skill-packs/releases/latest/download/revops-pack.zip](https://github.com/First-Touch-Inc/firsttouch-agent-skill-packs/releases/latest/download/revops-pack.zip) |
| Founder | [https://github.com/First-Touch-Inc/firsttouch-agent-skill-packs/releases/latest/download/founder-pack.zip](https://github.com/First-Touch-Inc/firsttouch-agent-skill-packs/releases/latest/download/founder-pack.zip) |
| AE | [https://github.com/First-Touch-Inc/firsttouch-agent-skill-packs/releases/latest/download/ae-pack.zip](https://github.com/First-Touch-Inc/firsttouch-agent-skill-packs/releases/latest/download/ae-pack.zip) |
| BDR | [https://github.com/First-Touch-Inc/firsttouch-agent-skill-packs/releases/latest/download/bdr-pack.zip](https://github.com/First-Touch-Inc/firsttouch-agent-skill-packs/releases/latest/download/bdr-pack.zip) |

## Required MCP

Connect the FirstTouch MCP first:

```txt
https://mcp.firsttouch.ai
```

Most plays also assume HubSpot is connected when the workflow needs CRM context, ownership, logging, or workflow triggers.

## Install by client

- Claude.ai: upload the selected pack zip in Settings, Features, Skills.
- Claude Code: unzip the pack and copy each folder in `skills/` into `~/.claude/skills/` or a project `.claude/skills/` directory.
- Cursor / Windsurf: unzip the pack and place the folder where your agent can read it.
- ChatGPT: connect the FirstTouch MCP. If using project knowledge or a custom GPT, upload the pack README and skill files as knowledge. ChatGPT does not currently install Agent Skills folders the same way Claude does.

See the install guides in [`install/`](install/).

## Activation prompt

After installing or uploading a pack, paste:

```txt
Use the FirstTouch MCP at https://mcp.firsttouch.ai. I have installed the FirstTouch agent skill pack. Ask whether I want RevOps, Founder, AE, or BDR. Then load that installed pack's plays, recommend 3 plays, and ask whether approval should be on or off.
```

## What is included

Each pack zip contains:

- `README.md`, role-specific setup and play guide
- `skills/`, the installable Agent Skills folders
- `references/`, shared FirstTouch MCP, messaging, safety, and system grounding docs
- `roadmap/`, honest specs for plays that are not yet fully shipped

## Safety

Approval can be on or off based on your workspace policy. Packs are designed around owner-safe routing, LinkedIn account limits, and CRM logging.
## Webflow Custom Embed

Paste this into a Webflow Custom Embed element:

```html
<div data-ftmcp-embed></div>
<script src="https://cdn.jsdelivr.net/gh/First-Touch-Inc/firsttouch-agent-skill-packs@v0.1.3/embed/ftmcp-landing.js"></script>
```

The embed loader injects the FirstTouch MCP landing section, styles, and interactivity.

