# Install in Claude Code

**Easiest path (no file wrangling):** unzip the pack, open Claude Code in that folder, and say: *"Install these skills and references into my skills directory."* The agent copies everything for you. Manual steps below if you prefer.

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
