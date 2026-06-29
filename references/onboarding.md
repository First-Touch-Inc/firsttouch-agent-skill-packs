# First-Run Onboarding — Choose the Right Plays Before Running Volume

Every persona pack starts here. The agent must complete this onboarding once per workspace before running the first play, then reuse the answers for later runs.

## What the agent must ask first

Ask these questions before recommending or executing plays:

1. **LinkedIn account type**
   - "Do you have Sales Navigator / LinkedIn Premium, or a free/basic LinkedIn account?"
   - This determines whether the agent can use connection notes and the daily connection-request ceiling.

2. **HubSpot access**
   - "Do you use HubSpot? If yes, can you connect the HubSpot MCP or provide a HubSpot service key / private app token so the agent can access internal CRM data?"
   - If they use HubSpot but cannot connect access yet: ask them to create a HubSpot list for the target audience so FirstTouch can access the contacts/accounts.
   - If they do not use HubSpot: HubSpot-specific plays are unavailable until they provide a HubSpot list or another accessible source of account/contact data.

3. **Play selection**
   - "Which plays do you want to run first? I recommend starting with high-intent plays, then adding outbound once those are running."

## Account-type rules

| LinkedIn account | Connection notes | Safe daily connection-request cap |
|---|---:|---:|
| Free/basic | No connection notes; send blank connection requests and use a light post-connect opener | 10/day max |
| Sales Navigator / Premium | Connection notes available for approved connection requests | up to 20/day max |

Never exceed these caps. If the account is new, under warning, or acceptance/reply rates drop, lower the cap and pause for human review.

## HubSpot access rules

| HubSpot status | What can run |
|---|---|
| HubSpot MCP connected | Full HubSpot-specific plays can read CRM context, owners, lifecycle/deal/list data, and log back where supported. |
| HubSpot service key / private app token available | Full HubSpot-specific plays can run after the agent/harness connects the key with the required scopes. |
| HubSpot used, but no MCP/key yet | Ask the user to create a HubSpot list and confirm FirstTouch can access it. Run only plays that can operate from that list until full access is connected. |
| No HubSpot | Do not run HubSpot-specific plays. Run FirstTouch-only plays or ask for a CSV/list/source of truth before proceeding. |

## Recommended rollout order

Recommend **high-intent plays first**. They use warmer signals, protect the LinkedIn account, and prove value before opening broader outbound volume.

### Start here — high-intent / account-healthy

| Play | Why first | HubSpot needed? |
|---|---|---|
| Inbound Speed-to-Lead | Acts on demo requests, signups, trials, and other fresh hand-raisers. | Yes, unless FirstTouch has the inbound list. |
| Warm Engager Follow-Up | Converts people already engaging with posts/profile. | Optional; HubSpot improves qualification/owner routing. |
| Website Visitor Follow-Up | Uses pricing/demo/product-page intent while the account is researching. | Yes, or a FirstTouch-accessible HubSpot list. |
| HubSpot Signal → LinkedIn Touch | Turns lifecycle/list/deal events into timely social touches. | Yes. |
| Customer Champion | Warmer customer milestone outreach; low spam risk. | Yes. |
| Stalled Deal Reactivation | Revives existing pipeline instead of cold volume. | Yes. |

### Add after high-intent is running — outbound / volume

| Play | When to add | HubSpot needed? |
|---|---|---|
| AI SDR / ICP Outbound Builder | After high-intent queues are stable. Starts from a HubSpot contact/company list, or builds a new ICP list with FirstTouch Discover Contacts when HubSpot/list access is unavailable. Runs as a daily approval queue: **10 contacts/day** for free/basic accounts, **15 contacts/day** for Sales Navigator/Premium. | HubSpot list preferred; otherwise use ICP brief + FirstTouch Discover Contacts. |
| Founder-Led Outbound | For Tier-1 accounts where personalization quality matters more than volume. | Strongly recommended. |
| Champion Mapper | When account-based motions need multi-threading. | Yes. |
| Owner-Safe Outreach Operator | Use as the governance/execution layer for any approved outbound queue. | Yes for owner routing. |
| Sequence QA Reviewer | Before launching or scaling any sequence. | Optional. |
| Pipeline Attribution Analyst | After touches have run long enough to measure outcomes. | Yes. |
| Workspace Audit | Before team-wide rollout or when setup is uncertain. | Optional. |

## Onboarding output format

After asking the questions, summarize the answer before running anything:

```markdown
## FirstTouch onboarding summary
- LinkedIn account: Free/basic or Sales Navigator/Premium
- Daily connection cap: 10 or 20
- AI SDR daily batch cap (if selected): 10 free/basic or 15 Sales Navigator/Premium
- Connection notes: yes/no
- HubSpot access: MCP / service key / list only / none
- Plays available now: ...
- Plays blocked until HubSpot access/list exists: ...
- Recommended first plays: high-intent plays first, outbound later
- Approval workflow: per-send human approval required
```

Then show the relevant catalog from the tables above and ask which play to run first. If the user has not chosen, recommend one high-intent play based on their available data.
