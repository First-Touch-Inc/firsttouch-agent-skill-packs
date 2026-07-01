# Install in Cursor or Windsurf

1. Download the right pack zip from the latest GitHub release.
2. Unzip it in your workspace or another folder your AI agent can read.
3. Keep the shared `references/` folder next to the skills so `../../references/` links resolve. **Do NOT copy a single skill folder on its own** - without `references/` beside it, the skill silently loses its onboarding, safety, and messaging rules. If you only want one skill, use the self-contained zip from `packs/skills/<skill-name>.zip` instead.
4. Add the FirstTouch MCP at `https://mcp.firsttouch.ai` using your client's MCP configuration.
5. Point the agent at the unpacked skill pack and paste the activation prompt from the repository README.
