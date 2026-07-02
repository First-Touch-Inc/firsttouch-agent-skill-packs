# First-Run Onboarding - Choose the Right Plays Before Running Volume

Every persona pack starts here. The agent must complete this onboarding once per workspace before running the first play, then reuse the answers for later runs.

## What the agent must ask first
Ask these questions before recommending or executing plays:

1. **LinkedIn account type**
   - "Do you have Sales Navigator / LinkedIn Premium, or a free/basic LinkedIn account?"
   - This determines whether the agent can use connection notes and the daily connection-request ceiling.

2. **HubSpot access**
   - "Do you use HubSpot? If yes, can you connect the HubSpot MCP or provide a HubSpot service key / private app token so the agent can access internal CRM data?"
   - Getting access is easy for reps: ask your admin to approve HubSpot MCP access (a quick approval), or request a **read-only service key** that lets the agent read deals, contacts, and companies with no write risk. Do not mint credentials yourself.
   - If they use HubSpot but cannot connect access yet: ask them to create a HubSpot list for the target audience so FirstTouch can access the contacts/accounts.
   - If they do not use HubSpot: HubSpot-specific plays are unavailable, but FirstTouch-only plays can still run from Discover Contacts, social engagement, one-time social campaigns from imported lists, or FirstTouch-accessible lists.

2b. **Credits note**
   - New FirstTouch workspaces start with **100 credits** - plenty for your first discoveries and enrichments. The agent checks the balance before any bulk run and asks before spending; you never get surprise-charged mid-play.

3. **ICP / source data**
   - "If HubSpot is not connected, what ICP or list should we use? Please provide target industries, company size, geography, titles/seniority, exclusions, and any must-have signals, or provide a CSV/imported list."
   - Do not qualify warm engagers, AI SDR prospects, or Discover audiences without either HubSpot context, a saved ICP, or a user-provided list.

4. **Play selection**
   - Recommend the persona-specific start point below, not a generic catalog dump.
   - Then show the available recipes and ask which one to run first.

## Account-type rules

| LinkedIn account | Connection notes | Recommended safe connection-request cap | FirstTouch max |
|---|---|---:|---:|
| Free/basic | No connection notes; send blank connection requests and use a light post-connect opener | 10/day | 20/day |
| Sales Navigator / Premium | Connection notes are available for approved warm-signal requests | 20/day | 30/day |

FirstTouch enforces these limits automatically - you can adjust volume in the FirstTouch app and can never go over the peak limits; hitting a limit just puts the seat on cooldown until the next window. Use the recommended cap by default; if the account is new or acceptance/reply rates drop, lower the cap.

**Shared cap rule:** AI SDR uses the same daily connection-request budget as every other play. If AI SDR and another play run on the same day, keep combined connection requests under the recommended 10/day free/basic or 20/day Sales Navigator/Premium cap unless the user explicitly approves a higher day; never exceed the FirstTouch max of 20/day free/basic or 30/day Sales Navigator/Premium.

**Message cap:** already-connected LinkedIn message rows use a separate FirstTouch-supported message cap. Free/basic max and recommended safe cap are 20/day. Sales Navigator/Premium max is 30/day and the recommended safe cap is also 30/day. Reduce volume if acceptance or reply quality drops.

**Connection-note rule:** Sales Nav/Premium accounts can use connection notes for warm signals such as post engagement, inbound hand-raisers, customer milestones, and HubSpot events. For cold AI SDR and one-time social campaigns, default to blank connection requests even with Sales Nav unless the user explicitly approves a strong note.

## HubSpot access rules

| HubSpot status | What can run |
|---|---|
| HubSpot MCP connected | Full HubSpot-specific plays can read CRM context, owners, lifecycle/deal/list data, and log back where the connected FirstTouch-HubSpot integration supports it. |
| HubSpot service key / private app token available | Full HubSpot-specific plays can run after the agent/harness connects the key with the required scopes. |
| HubSpot used, but no MCP/key yet | Ask the user to create a HubSpot list and confirm FirstTouch can access it. Run only plays that can operate from that list until full access is connected. |
| No HubSpot | Run FirstTouch-only plays: Social Engagement Flow from owned or relevant external profiles, Social Campaigns from Discover Contacts/imported lists, AI SDR / ICP Outbound from Discover Contacts, Founder-Led AI SDR, Sequence QA, and FirstTouch-only Workspace Audit. Do not run HubSpot-specific plays until a HubSpot list/source exists. |

**FirstTouch-accessible list/import means:** a CSV, static list, audience, or HubSpot list that FirstTouch can read. If the list is manually uploaded, the play is list-based, not fully automated. For true inbound automation, connect HubSpot or another source that continuously feeds FirstTouch.

## Persona-specific first play recommendations

| Persona | Start here if HubSpot is connected | Start here without HubSpot |
|---|---|---|
| Founder | Social engagement flow first; customer referral thank-you or stalled deal only when CRM data exists | Enable Social Engagement through FirstTouch MCP for founder/executive personal-profile posts or a relevant competitor/influencer personal profile. FirstTouch does not track company-page/profile engagement. If no monitored profile or engager list is available, start with Founder-led AI SDR from Discover Contacts. |
| AE | Auto-connect on meeting or signup is the #1 AE use case; meeting-booked stakeholder follow-up is next for multi-threading; stalled deal after RevOps/admin workflow support is clear | Social engager flow can use leadership/executive personal profiles, competitor founder profiles, or influencer personal profiles. FirstTouch does not track company-page/profile engagement. Position the AE pack as much stronger with HubSpot. |
| BDR | Auto-connect on meeting/signup for inbound; otherwise BDR AI SDR is the daily engine | BDR AI SDR first when no inbound feed exists; add warm engager follow-up from leadership/competitor/influencer profiles. Social campaigns are special pushes, usually row-level dynamic actions. |
| RevOps | Pre-launch rollout audit, then Team-wide AI SDR, HubSpot signal, or team-wide high-intent flows | FirstTouch-only workspace audit, sequence QA, Team-wide AI SDR from Discover Contacts, social engagement setup via FirstTouch MCP on owned or external personal profiles, and Discover/imported-list campaigns |

## Recommended rollout order

Recommend **high-intent plays first**. They use warmer signals, protect the LinkedIn account, and prove value before opening broader outbound volume.

### Start here - high-intent / account-healthy

| Play | Why first | HubSpot needed? |
|---|---|---|
| Social Engagement Flow | Converts people already engaging with personal-profile posts. For founders, run this first from owned founder/executive personal-profile posts; if owned engagement is thin, monitor a relevant competitor founder, category influencer, or executive personal profile. FirstTouch does not track company-page/profile engagement. Profile views are not a signal. | No HubSpot. Enable Social Engagement through FirstTouch MCP for monitored profiles; a user-provided/exported engager list can work without monitored-profile access. |
| Inbound Speed-to-Lead | Acts on demo requests, signups, trials, and other fresh hand-raisers. | HubSpot or a FirstTouch-accessible inbound list/import. True automation needs a connected source. |
| Website Visitor Follow-Up | Uses pricing/demo/product-page intent while the account is researching. | HubSpot tracking or RB2B/list source required. If no signal source exists, this play is unavailable. |
| HubSpot Signal → LinkedIn Touch | Turns lifecycle/list/deal events into timely social touches. | Yes. |
| Customer Referral Thank-You | Warmer new-customer thank-you, feedback, and light referral outreach; low spam risk. | HubSpot Closed Won/customer source or imported customer list required. |
| Stalled Deal Reactivation | A contact-based HubSpot workflow for contacts associated to open deals not Closed Won/Lost with no engagement for 60+ days. Deal-based triggers are unsupported. | Yes. May need RevOps/admin setup if workflow creation is unavailable. |

### Add after high-intent is running - outbound / volume

| Play | When to add | HubSpot needed? |
|---|---|---|
| AI SDR / ICP Outbound Builder | For BDRs with no inbound feed or HubSpot, this is the daily engine. For other personas, add after warm/high-intent queues are stable. Starts from a HubSpot contact/company list, or builds a new ICP list with FirstTouch Discover Contacts. | HubSpot list optional; otherwise use ICP brief + FirstTouch Discover Contacts. |
| Founder-Led AI SDR | Founder-specific AI SDR with founder voice and a stricter taste bar. | HubSpot list optional; otherwise use ICP brief + FirstTouch Discover Contacts. |
| Social Campaigns | When the user has a very narrow segment. Rep/BDR mode should feel like AI SDR: curated rows approved one at a time. RevOps/founder campaign mode can use static flow templates with flow-level approval. | No HubSpot for Discover/imported/connection-list campaigns; HubSpot required for CRM/deal/customer/no-show criteria. |
| Sequence QA Reviewer | Before launching or scaling any sequence. | No. HubSpot improves duplicate/owner checks. |
| Workspace Audit | Before team-wide rollout or when setup is uncertain. | No for FirstTouch-only checks; HubSpot improves CRM/owner/logging checks. |

## Approval model

| Motion | Approval style |
|---|---|
| AI SDR / founder AI SDR / dynamic actions | Row-level approval. Each first-touch row must be approved individually; if the workspace uses approval tasks, the task is sent to the owner in HubSpot or appears in the FirstTouch app under **Tasks**. |
| Warm engager, inbound, website visitor, HubSpot signal, customer referral thank-you, stalled deal | Row-level approval unless the connected FirstTouch/approval system records an equivalent per-contact approval; approval tasks route to the owner in HubSpot or the app **Tasks** view when that workflow is enabled. |
| Social campaigns | Two modes: rep/BDR dynamic rows use row-level approval like AI SDR; one-time static campaigns can use flow-level approval with exact audience, templates, sender/routing rule, launch window, and daily cap approved. This does not authorize future dynamic or AI-generated campaigns. |

## Onboarding output format

After asking the questions, summarize the answer before running anything:

```markdown
## FirstTouch onboarding summary
- Persona: Founder / AE / BDR / RevOps
- LinkedIn account: Free/basic or Sales Navigator/Premium
- Daily connection cap: recommended 10/day free/basic or 20/day Sales Nav/Premium; FirstTouch max 20/day free/basic or 30/day Sales Nav/Premium
- Daily message cap: 20/day free/basic; 30/day Sales Nav/Premium
- Connection notes: yes for approved warm signals / no for free-basic / blank by default for cold AI SDR
- HubSpot access: MCP / service key / list only / none
- Social Engagement enabled: yes/no/unknown
- ICP/list available if no HubSpot: yes/no + source
- Plays available now: ...
- Plays blocked until HubSpot access/list exists: ...
- Recommended first play for this persona: ...
- Approval workflow: per-row approval for dynamic plays; approval tasks route to the owner in HubSpot or FirstTouch app Tasks when enabled; flow-level approval allowed only for one-time social campaigns with exact audience + static templates
```

Then show the relevant recipe catalog and ask which play to run first. If the user has not chosen, recommend the persona-specific first play above.
