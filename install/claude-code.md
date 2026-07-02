# Install in Claude Code

**Recommended: install as a plugin** - two commands, and the FirstTouch MCP connects automatically:

```
/plugin marketplace add First-Touch-Inc/firsttouch-agent-skill-packs
/plugin install founder-pack@firsttouch        # or ae-pack / bdr-pack / revops-pack
```

The plugin registers the FirstTouch MCP but it still needs a one-time login: run `/mcp`, pick the **firsttouch** server, and complete the OAuth prompt ("Needs authentication" before this step is expected, not a bug). If you already connected the FirstTouch MCP manually, you can keep using that connection and skip this.

Verify with `/plugin list`, then ask *"What FirstTouch plays do you have available?"* The zip-based paths below still work if you prefer manual installs.

**Easiest zip path (no file wrangling):** unzip the pack, open Claude Code in that folder, and say: *"Install these skills and references into my skills directory."* The agent copies everything for you. Manual steps below if you prefer.

1. Download the right pack zip from [`packs/`](../packs/) in this repository (see the README download table) - the committed zips are always current with the latest source.
2. Unzip it locally.
3. Copy the shared `references/` folder alongside the skills so `../../references/` links resolve; for global installs, place it at `~/.claude/references/` (Windows: `C:\Users\<you>\.claude\references\`), and for project installs, place it at `.claude/references/`.
4. Copy every folder under `skills/` into one of these locations:
   - global: `~/.claude/skills/<skill-name>/`
   - project: `.claude/skills/<skill-name>/`
5. Connect the FirstTouch MCP at `https://mcp.firsttouch.ai`.
6. Start Claude Code and paste the activation prompt from the repository README.

**Verify the install** before running a play:

- Global install: confirm `~/.claude/references/onboarding.md` exists.
- Project install: confirm `.claude/references/onboarding.md` exists.

If that file is missing, the skills will run without their onboarding, safety, and messaging rules. Do not copy a single skill folder without also copying `references/` - the `../../references/` links break silently.
