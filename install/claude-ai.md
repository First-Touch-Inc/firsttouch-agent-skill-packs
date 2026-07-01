# Install in Claude.ai

Claude.ai registers **one skill per uploaded zip**. Use the per-skill zips - they are self-contained (each bundles the reference files that skill needs plus the license), so nothing else is required.

1. Download the per-skill zips you want from `packs/skills/<skill-name>.zip` in this repository.
2. Open Claude.ai settings.
3. Go to Features, Skills.
4. Upload each skill zip individually.
5. Connect the FirstTouch MCP at `https://mcp.firsttouch.ai`.
6. Paste the activation prompt from the repository README.

**Verify the install:** ask Claude *"What FirstTouch plays do you have available?"* - it should list the skills you uploaded. If a skill can't find its onboarding or safety rules, re-download the zip from `packs/skills/` (older zips did not bundle references).

The full persona pack zips (`packs/<persona>-pack.zip`) are intended for Claude Code, Cursor, and Windsurf, where the whole folder structure is preserved. Avoid uploading a multi-skill pack zip to Claude.ai - it may register only the first skill.
