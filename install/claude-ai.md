# Install in Claude.ai

1. Download the right pack zip from the latest GitHub release.
2. Open Claude.ai settings.
3. Go to Features, Skills.
4. Upload the pack zip.
5. If uploading individual skill folders instead, also upload/include the shared `references/` folder so every skill can load onboarding, safety, and messaging rules.
6. Connect the FirstTouch MCP at `https://mcp.firsttouch.ai`.
7. Paste the activation prompt from the repository README.

If Claude.ai only registers one skill from a multi-skill zip, unzip the pack locally and upload individual skill folders as separate zips. Include the shared `references/` folder with those uploads so the skills retain their shared grounding.
