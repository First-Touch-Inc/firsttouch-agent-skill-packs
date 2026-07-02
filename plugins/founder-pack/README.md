# FirstTouch Founder Pack

*Pack version 1.4.1*

> Looking automated or spammy on LinkedIn risks the reputation you spent years building: these are the plays for the job you actually do.

## Who this is for
You do your own sales. Your name is your brand, and every automated-feeling LinkedIn message risks undoing years of relationship-building. You need outreach that sounds exactly like you - in the signals you'd actually notice, at the volume that feels personal, not like a drip campaign. These plays are designed for founders who want LinkedIn to feel like them, not like an SDR they hired.

## What is MCP?
MCP is the plug that lets your AI agent use FirstTouch. In **ChatGPT** and **Claude.ai** it shows up in settings as a **Connector**; in **Claude Code**, **Cursor**, **Windsurf**, and **Codex** it's called an **MCP server**. Same thing, different label. You set it up once (see `references/mcp-setup.md`), and it never sees your LinkedIn password - it only performs actions you approve.

## First-run onboarding (do this before any play)
Answer these once; every play depends on them:

1. **LinkedIn account type:** do you have Sales Navigator / Premium, or a free/basic account?
   - Free/basic: no connection notes; recommend **10/day** connection requests; FirstTouch max **20/day**.
   - Sales Navigator / Premium: connection notes available; recommend **20/day** connection requests; FirstTouch max **30/day**.
   - AI SDR shares the same daily connection-request budget. If AI SDR and another play run on the same day, the total across all plays should stay within the recommended 10 or 20 unless the user explicitly approves higher volume; never exceed the FirstTouch max of 20/day free/basic or 30/day Sales Navigator/Premium.
   - Already-connected LinkedIn message rows use a separate FirstTouch-supported message cap: 20/day on free/basic LinkedIn and 30/day on Sales Navigator/Premium.
   - FirstTouch enforces these limits automatically - adjust volume anytime in the FirstTouch app; you can never go over the peak limits. Hitting a limit just puts the seat on cooldown until the next window.
2. **HubSpot access:** getting access is easy - ask your admin to approve HubSpot MCP access (a quick approval), or request a **read-only service key** that lets the agent read deals, contacts, and companies with no write risk. If neither is available yet, plenty of plays below run without HubSpot; you can also ask an admin for a HubSpot list FirstTouch can access.
3. **Credits:** new FirstTouch workspaces start with **100 credits** - plenty for your first discoveries and enrichments. The agent checks the balance before any bulk run and asks before spending.
4. **Play choice:** pick from the persona start point below.

Use `references/onboarding.md` for the full question flow and account-type rules. Use `references/recipes.md` for the generated recipe catalog if the README is not loaded by the agent.

**Next:** answer the questions above once, then go straight to **Start here** below and pick your first play - that is the whole setup.

## Start here
1. **Check Social Engagement first:** run **Social engagement flow: founder posts** from owned founder or executive personal profiles. If Social Engagement is not enabled, turn it on through FirstTouch MCP for the monitored profile. If owned personal-profile engagement is thin, monitor a relevant competitor founder or category influencer personal profile. FirstTouch does not track company-page/profile engagement.
2. **No engagement to harvest yet:** run **Founder post generator** to draft a week of founder-voice posts that create it - then harvest engagers 24-72h after posting. If you need pipeline this week regardless, run **Founder-led AI SDR** from ICP + FirstTouch Discover Contacts in parallel.
3. **Have HubSpot:** add inbound, visitor, and stalled-deal plays as secondary CRM/deal motions, not the default path.

## Your week
- **Daily (10 min):** check new warm engagers from your monitored profile and approve any drafts.
- **2x per week:** post from the founder-post-generator batch; harvest engagers 24-72h later.
- **2-3x per week:** approve your founder AI SDR batch. 3-5 contacts per run is plenty for a solo founder - you have to service the conversations you start.
- **Friday:** scan replies, move anything warm to your calendar, and pause any motion that feels off-voice.

## Quickstart play cards
| Situation | Run this | What happens |
|---|---|---|
| Has founder/executive post engagement | Social engagement flow | Work warm engagers from personal-profile posts |
| Thin owned engagement | Founder post generator | Draft posts that create ICP engagement to harvest |
| Still thin after posting | Monitor competitor/influencer profile | Use relevant external personal-profile engagement |
| No warm source | Founder-led AI SDR | Discover ICP prospects and draft founder-voice outreach |
| Has CRM data | Stalled deal / customer referral thank-you | Work high-intent relationship motions |

## How to use this pack
- **Recipes** are the best starting point. They combine the right skills into the job you actually want done.
- **Skills** are the individual building blocks. Run a skill directly only when you know the exact motion you want.
- **Read once:** `references/system-grounding.md` explains how agents, FirstTouch, HubSpot, approvals, and measurement fit together.
- **FirstTouch terms:** a campaign/sequence/social campaign in this pack becomes a FirstTouch audience, flow plan, dynamic action, or enrollment depending on the play. "AI SDR" in this pack maps to `founder-led-outbound`. The agent should use FirstTouch's available execution objects and state the exact object it created.
- **Approval locations:** before assuming approval tasks are enabled, ask the user or check available FirstTouch task/workspace settings. If approval tasks are enabled, route them to the owner in HubSpot or the FirstTouch app under **Tasks**. If that workflow is not enabled or cannot be confirmed, present the table in chat and wait for explicit approval.

## HubSpot reality check
- **What works without HubSpot:** Social engagement flow from the founder's or executive's personal-profile posts, or a relevant competitor founder/influencer personal profile after enabling Social Engagement through FirstTouch MCP; user-provided/exported engager lists; Founder-led AI SDR from FirstTouch Discover Contacts; Social campaigns from Discover/imported/connection lists; and messaging QA. FirstTouch does not track company-page/profile engagement.
- **What needs HubSpot:** CRM lifecycle/deal criteria, owner routing, HubSpot timeline logging where the connected FirstTouch-HubSpot integration supports it, stalled-deal workflows, and contact/company lists stored only in HubSpot. Without HubSpot/list access, use the FirstTouch-only recipes and do not promise existing-pipeline/deal recovery.
- **FirstTouch-accessible list/import means:** a CSV, static list, audience, or HubSpot list that FirstTouch can read. For true inbound automation, connect HubSpot or another source that continuously feeds FirstTouch.
- **Enrichment is optional but useful:** FirstTouch can enrich contacts/companies when credits and data are available. Clay/Surfe or another enrichment MCP is an optional supplement, not a prerequisite. Without a usable LinkedIn URL or enough verified data, the agent should skip or queue incomplete records rather than fabricate.

## Your plays

### Skills catalog (check Needs before running)
#### Start here, no HubSpot needed
| Skill | What it does | Needs / access status | Runs |
|---|---|---|---|
| warm-engager-followup | Turn people who recently liked or commented on the sender's posts, an executive's posts, leadership/executive personal-profile content, or a relevant competitor founder/influencer profile into conversations and pipeline. | No HubSpot required; enable Social Engagement through FirstTouch MCP for monitored profiles; user-provided/exported engager lists also work | `warm-engager-followup` |
| founder-led-outbound | "Run the founder AI SDR motion (for founders/CEOs sending as themselves only): build a targeted prospect list from a HubSpot list or FirstTouch Discover Contacts, enrich each prospect, draft founder-voice LinkedIn outreach, and queue a small daily batch for founder approval. | No HubSpot required with ICP brief + FirstTouch Discover Contacts; HubSpot list optional | `founder-led-outbound` |
| campaign-pause-and-fix | Pause a live FirstTouch campaign/flow mid-send, diagnose what is wrong, cancel or hold the affected enrollments, fix the messaging or audience, and safely restart with re-enrollment - without duplicate sends. | No HubSpot required; works on any running FirstTouch flow | `campaign-pause-and-fix` |
| founder-post-generator | Turn founder POV, customer proof, market observations, and real sales conversations into LinkedIn posts that attract the right engagers - then route those engagers into warm follow-up. | No HubSpot required; drafts posts only, sends nothing | `founder-post-generator` |

#### Needs HubSpot, RB2B, or a FirstTouch-accessible source
| Skill | What it does | Needs / access status | Runs |
|---|---|---|---|
| inbound-speed-to-lead | "Attach LinkedIn connection requests and lightweight follow-up to booked meetings, inbound signups, trial starts, demo requests, or other high-intent inbound lists. | HubSpot or FirstTouch-accessible inbound list/import required; true automation needs a connected source | `inbound-speed-to-lead` |
| website-visitor-followup | Turn website-visitor intent into LinkedIn outreach by using identified-visitor data or HubSpot website-visitor signals, checking connection status, drafting a lightweight message, and gating execution for approval. | HubSpot tracking or RB2B/list source required | `website-visitor-followup` |
| social-campaigns | "Build a ONE-TIME (not recurring) LinkedIn social campaign for a very narrow ICP segment: define precise audience criteria, source/enrich contacts from FirstTouch and optional HubSpot lists, then choose either row-level dynamic actions for rep/BDR one-at-a-time execution or static flow templates for RevOps/founder-approved one-time campaigns. | No HubSpot for pure ICP/imported/connection-list campaigns; HubSpot required for CRM/deal/customer segments | `social-campaigns` |
| stalled-deal-reactivation | Build and govern a contact-based HubSpot workflow for contacts associated to open deals that are not Closed Won and not Closed Lost and have had no engagement for 60+ days. | HubSpot required; may need RevOps/admin for workflow setup | `stalled-deal-reactivation` |
| customer-referral | Auto-prepare LinkedIn connection requests and thank-you/referral messages for new customers after they choose the product. | HubSpot Closed Won/customer source or imported/FirstTouch-accessible customer list required; HubSpot improves owner/CSM routing and logging | `customer-referral` |
| hubspot-signal-to-linkedin-touch | Turn a HubSpot CRM event - lifecycle stage change, deal stage movement, form fill, list addition - into a timely, personalized LinkedIn touch. | HubSpot required | `hubspot-signal-to-linkedin-touch` |

### Support skills (called by plays)
| Skill | What it does | Needs / HubSpot status | Runs |
|---|---|---|---|
| firsttouch-messaging | Write on-brand, high-converting LinkedIn outreach messages - connection requests, openers, follow-ups, and meeting asks - calibrated to the prospect's seniority and a real signal. | No HubSpot required | `firsttouch-messaging` |

### Recipes (recommended starting points)
#### Start here - no HubSpot needed
| Play | What it does | Needs | Composes from |
|---|---|---|---|
| Social engagement flow - founder posts | Social Engagement can be enabled through FirstTouch MCP; Start with the warmest founder motion: ICP-qualify people engaging with your posts, or a relevant competitor founder/influencer profile if your own engagement is thin, then draft a light founder-voice touch for approval. No HubSpot required. | No HubSpot required; Social Engagement can be enabled through FirstTouch MCP for monitored profiles; profile views unavailable | `warm-engager-followup` + `firsttouch-messaging` |
| Founder-led AI SDR - daily approval queue | Use a HubSpot contact/company list or discover a new ICP list, enrich each prospect, and draft up to the recommended 10/day free/basic or 20/day Sales Nav/Premium founder-voice touches for approval. | No HubSpot required with ICP brief + FirstTouch Discover Contacts; HubSpot list optional | `founder-led-outbound` |
| Social campaigns - founder-led narrow audience push | Build a one-time founder-led campaign such as leadership connections for feature feedback, VP Sales coffee invites during a travel week, or a focused product-update push, using approved static templates and flow-level approval. | No HubSpot required for Discover Contacts or connection/list sources; HubSpot required only for CRM-history segments | `social-campaigns` + `firsttouch-messaging` |
| Founder post engine | Draft 3-5 founder-voice posts per week that attract ICP engagers, then harvest them into warm conversations | No HubSpot required; drafts only - the founder posts from their own account | `founder-post-generator` + `warm-engager-followup` + `firsttouch-messaging` |
#### Needs HubSpot, RB2B, or a FirstTouch-accessible source
| Play | What it does | Needs | Composes from |
|---|---|---|---|
| Fast personal inbound follow-up | Connect with high-intent signups and demo requests on LinkedIn same day, in your voice. | HubSpot or FirstTouch-accessible inbound list/import required | `inbound-speed-to-lead` + `firsttouch-messaging` |
| Website visitor play | Turn pricing/demo/product-page visits into LinkedIn touches while intent is active, when HubSpot tracking or an RB2B/list source exists. | HubSpot tracking or RB2B/list source required; if no visitor signal source exists, use the persona AI SDR recipe as a separate prospecting motion | `website-visitor-followup` + `firsttouch-messaging` |
| Scoop-up slipped leads | Use HubSpot lifecycle/deal/list data to find personal lost deals and dormant contacts worth a second look. This is a secondary CRM motion, not the no-HubSpot founder start. | HubSpot required | `hubspot-signal-to-linkedin-touch` + `firsttouch-messaging` |
| Stalled deal reactivation - 60-day open-deal workflow | Find contacts associated to open HubSpot deals that are not Closed Won/Lost and have had no engagement for 60+ days, then build an owner-approved LinkedIn reactivation queue. This is a secondary HubSpot motion after the no-HubSpot founder starts. | HubSpot required; RevOps/admin may be needed only for recurring workflow setup | `stalled-deal-reactivation` + `firsttouch-messaging` |
| Customer referral thank-you | Connect with new customers, thank them for choosing the product, ask how the product could be better, and add a light network-value/referral line after row-level approval. | HubSpot Closed Won/customer source or imported/FirstTouch-accessible customer list required; HubSpot improves owner/CSM routing and logging | `customer-referral` + `firsttouch-messaging` |

### How to run each recipe

**Social engagement flow - founder posts**
1. Confirm Social Engagement is enabled on your profile (or a relevant external profile) - `warm-engager-followup`, step 1. 2. Pull recent engagers and keep the ICP fits. 3. Draft founder-voice openers with `firsttouch-messaging`, approve, queue.

**Founder-led AI SDR - daily approval queue**
1. Capture founder voice and ICP once (`founder-led-outbound`, steps 0-0b). 2. The agent discovers, enriches, and drafts 3-5 founder-voice rows. 3. Approve the small batch each run; the agent queues and tracks accepts/replies.

**Social campaigns - founder-led narrow audience push**
1. Define a narrow segment you personally care about (25-100 people). 2. `social-campaigns` drafts founder-voice touches with `firsttouch-messaging`. 3. Approve, enroll, monitor replies personally.

**Fast personal inbound follow-up**
1. Pull fresh signups/demo requests from HubSpot or your inbound list (`inbound-speed-to-lead`). 2. Draft a founder-voice connection + opener the same day. 3. Approve, queue - speed is the whole play.

**Website visitor play**
1. Confirm a visitor source exists (HubSpot tracking or an RB2B/list source); stop if none. 2. `website-visitor-followup` qualifies visitors and picks a contact-level or account-level motion. 3. Draft soft, non-creepy touches, approve, queue.

**Scoop-up slipped leads**
1. Build or request the recovery list (no-shows, old MQLs, quiet signups). 2. Qualify and draft low-pressure re-openers with `firsttouch-messaging`. 3. Approve, queue, and put non-responders on cooldown.

**Stalled deal reactivation - 60-day open-deal workflow**
1. Get or self-build the HubSpot list of open-deal contacts quiet for 60+ days (the skill includes the exact filter recipe). 2. `stalled-deal-reactivation` qualifies and drafts value-first touches - never 'just checking in'. 3. Owner approves, queue, log to the deal.

**Customer referral thank-you**
1. Pull the Closed Won/customer list. 2. `customer-referral` checks connection state and drafts a thank-you plus light referral ask (both connected and unconnected paths). 3. The account owner approves, then queue.

**Founder post engine**
1. Feed the generator one real input (customer lesson, market POV, build-in-public moment); get 3-5 drafts with suggested days. 2. Post from your own account; no hard CTA on most posts. 3. 24-72h later, run warm-engager-followup on the ICP-fit engagers while the post is fresh.

## Example prompts
- "Run the founder social engagement flow from my latest post: qualify the engagers, draft light founder-voice LinkedIn touches, and do not send until I approve each row."
- "Use Founder-led AI SDR for this ICP, keep it under my recommended daily cap, use blank connection requests if they are not connected, and draft in my voice for approval."
- "A new customer just chose us. Connect with the champion and draft a founder thank-you that asks what we could make better and whether anyone in their network would also get value."
- "From this HubSpot list of open deals with no engagement in 60+ days, draft owner-approved founder-voice reactivation touches; do not infer the cohort without the list."

## Install
1. Download this pack zip and extract it so `skills/` and `references/` sit side by side. Keep the `references/` folder with the skills; many skills link to `../../references/...`.
2. Install for your agent:
   - **Claude Code (easiest path):** open Claude Code in the unzipped pack folder and say: *"Install these skills and references into my skills directory."* The agent does the copying for you.
   - **Claude Code (manual):** copy `skills/<skill-name>/` folders into your skills directory and `references/` next to them. On Windows that is `C:\Users\<you>\.claude\skills\` and `C:\Users\<you>\.claude\references\`; on Mac/Linux it is `~/.claude/skills/` and `~/.claude/references/`. The generated recipe catalog lives in `references/recipes.md` and the onboarding/play chooser in `references/onboarding.md`, so recipes survive non-zip installs.
   - **Claude.ai:** Settings → Features → Skills → upload the full persona pack `.zip` first. If uploading a single skill manually, include the specific referenced markdown files inside that skill folder before zipping, because `../../references/` paths may not resolve in single-skill Claude.ai uploads.
   - **Cursor / Windsurf:** copy this pack into the project or workspace location your agent reads for skills; keep `skills/` and `references/` together at the same root.
   - **ChatGPT:** connect `https://mcp.firsttouch.ai` as an MCP connector. ChatGPT does not consume the skills folder directly; use the README/skill text as operating prompts if needed.
3. Connect **FirstTouch MCP**. Connect **HubSpot MCP** only for HubSpot-specific plays. See `references/mcp-setup.md`.
4. Complete first-run onboarding before choosing a play.

## Safety
- The agent never sends a message or publishes a flow without showing it in chat and getting an explicit yes. FirstTouch also offers an optional in-product human-in-the-loop layer (off by default) that pauses sends as approval tasks in the FirstTouch app under Tasks or in HubSpot - enable it on send actions for any flow that keeps enrolling contacts after the chat ends.
- Dynamic outbound and AI SDR require row-level approval. Approval tasks have no automatic escalation or SLA; checking the pending-approval queue is part of the routine. Social campaigns support two modes: rep/BDR one-at-a-time dynamic rows use row-level approval; one-time static campaign flows can use flow-level approval only after the exact audience, templates, sender routing, launch window, and daily cap are approved.
- Publishing a flow activates it but does **not** enroll awaiting contacts. After approval, explicitly enroll the approved contacts/items, then confirm they moved from awaiting to in-progress.
- Built around FirstTouch-supported limits and safer recommendations: recommend 10/day free/basic or 20/day Sales Navigator/Premium connection requests; never exceed 20/day free/basic or 30/day Sales Navigator/Premium. When possible, inspect current queue/usage before adding more connection-request rows, rather than relying on estimates.
- See `references/safety-governance.md`.
