# First-Run Onboarding - Founder Pack

This onboarding is scoped to the skills and recipes actually included in this installed pack.

## Ask before running anything
1. **LinkedIn account type:** free/basic or Sales Navigator/Premium.
   - Free/basic: no connection notes; recommend 10 connection requests/day; FirstTouch max 20/day.
   - Sales Navigator/Premium: connection notes available for approved warm signals; recommend 20 connection requests/day; FirstTouch max 30/day.
   - AI SDR and all other connection-request plays share the same daily budget.
   - If AI SDR and a social campaign run on the same sender/day, pause/reduce one motion or split the recommended daily cap explicitly before queueing sends; never exceed the FirstTouch max.
   - Already-connected LinkedIn message rows use a separate FirstTouch-supported message cap: 20/day on free/basic LinkedIn and 30/day on Sales Navigator/Premium. Reduce volume if acceptance or reply quality drops.
   - FirstTouch enforces these limits automatically - you can adjust volume anytime in the FirstTouch app, and you can never go over the peak limits. If a seat hits its daily limit it simply goes on cooldown until the next window.
2. **HubSpot access:** MCP connected by an admin, service key/private app token from an admin, HubSpot list only, or none. Getting access is easy: ask an admin to approve HubSpot MCP access (a quick approval) or to issue a **read-only service key** that lets the agent read deals, contacts, and companies with no write risk. Do not ask a rep/BDR to mint credentials they do not own.
3. **ICP/list/source data:** if HubSpot is absent, ask for ICP criteria or an imported/FirstTouch-accessible list before qualifying prospects.
4. **Persona start point:** recommend the persona-specific start point below, not a generic catalog dump.

## Persona start point
1. **Check Social Engagement first:** run **Social engagement flow: founder posts** from owned founder or executive personal profiles. If Social Engagement is not enabled, turn it on through FirstTouch MCP for the monitored profile. If owned personal-profile engagement is thin, monitor a relevant competitor founder or category influencer personal profile. FirstTouch does not track company-page/profile engagement.
2. **No engagement to harvest yet:** run **Founder post generator** to draft a week of founder-voice posts that create it - then harvest engagers 24-72h after posting. If you need pipeline this week regardless, run **Founder-led AI SDR** from ICP + FirstTouch Discover Contacts in parallel.
3. **Have HubSpot:** add inbound, visitor, and stalled-deal plays as secondary CRM/deal motions, not the default path.

- Social engagement / warm engager flows are delivered by `warm-engager-followup`. They use LinkedIn post likes and comments from Social Engagement monitoring; if Social Engagement is not enabled, enable it through FirstTouch MCP for the monitored profile when permissions allow, or use a user-provided/exported engager list. Profile-view capture is not treated as MCP-native.
- Founder voice capture is mandatory: collect 2-3 sample posts/messages or tone rules before founder-led outbound.

## Quickstart play cards
| Situation | Run this | What happens |
|---|---|---|
| Has founder/executive post engagement | Social engagement flow | Work warm engagers from personal-profile posts |
| Thin owned engagement | Founder post generator | Draft posts that create ICP engagement to harvest |
| Still thin after posting | Monitor competitor/influencer profile | Use relevant external personal-profile engagement |
| No warm source | Founder-led AI SDR | Discover ICP prospects and draft founder-voice outreach |
| Has CRM data | Stalled deal / customer referral thank-you | Work high-intent relationship motions |

## Available recipes in this pack
#### Start here - no HubSpot needed
| Recipe | What it does | Needs |
|---|---|---|
| Social engagement flow - founder posts | Social Engagement can be enabled through FirstTouch MCP; Start with the warmest founder motion: ICP-qualify people engaging with your posts, or a relevant competitor founder/influencer profile if your own engagement is thin, then draft a light founder-voice touch for approval. No HubSpot required. | No HubSpot required; Social Engagement can be enabled through FirstTouch MCP for monitored profiles; profile views unavailable |
| Founder-led AI SDR - daily approval queue | Use a HubSpot contact/company list or discover a new ICP list, enrich each prospect, and draft up to the recommended 10/day free/basic or 20/day Sales Nav/Premium founder-voice touches for approval. | No HubSpot required with ICP brief + FirstTouch Discover Contacts; HubSpot list optional |
| Social campaigns - founder-led narrow audience push | Build a one-time founder-led campaign such as leadership connections for feature feedback, VP Sales coffee invites during a travel week, or a focused product-update push, using approved static templates and flow-level approval. | No HubSpot required for Discover Contacts or connection/list sources; HubSpot required only for CRM-history segments |
| Founder post engine | Draft 3-5 founder-voice posts per week that attract ICP engagers, then harvest them into warm conversations | No HubSpot required; drafts only - the founder posts from their own account |
#### Needs HubSpot, RB2B, or a FirstTouch-accessible source
| Recipe | What it does | Needs |
|---|---|---|
| Fast personal inbound follow-up | Connect with high-intent signups and demo requests on LinkedIn same day, in your voice. | HubSpot or FirstTouch-accessible inbound list/import required |
| Website visitor play | Turn pricing/demo/product-page visits into LinkedIn touches while intent is active, when HubSpot tracking or an RB2B/list source exists. | HubSpot tracking or RB2B/list source required; if no visitor signal source exists, use the persona AI SDR recipe as a separate prospecting motion |
| Scoop-up slipped leads | Use HubSpot lifecycle/deal/list data to find personal lost deals and dormant contacts worth a second look. This is a secondary CRM motion, not the no-HubSpot founder start. | HubSpot required |
| Stalled deal reactivation - 60-day open-deal workflow | Find contacts associated to open HubSpot deals that are not Closed Won/Lost and have had no engagement for 60+ days, then build an owner-approved LinkedIn reactivation queue. This is a secondary HubSpot motion after the no-HubSpot founder starts. | HubSpot required; RevOps/admin may be needed only for recurring workflow setup |
| Customer referral thank-you | Connect with new customers, thank them for choosing the product, ask how the product could be better, and add a light network-value/referral line after row-level approval. | HubSpot Closed Won/customer source or imported/FirstTouch-accessible customer list required; HubSpot improves owner/CSM routing and logging |

## Included skills and dependency status
| Skill | Needs |
|---|---|
| `firsttouch-messaging` | No HubSpot required |
| `inbound-speed-to-lead` | HubSpot or FirstTouch-accessible inbound list/import required; true automation needs a connected source |
| `warm-engager-followup` | No HubSpot required; enable Social Engagement through FirstTouch MCP for monitored profiles; user-provided/exported engager lists also work |
| `website-visitor-followup` | HubSpot tracking or RB2B/list source required |
| `founder-led-outbound` | No HubSpot required with ICP brief + FirstTouch Discover Contacts; HubSpot list optional |
| `social-campaigns` | No HubSpot for pure ICP/imported/connection-list campaigns; HubSpot required for CRM/deal/customer segments |
| `stalled-deal-reactivation` | HubSpot required; may need RevOps/admin for workflow setup |
| `customer-referral` | HubSpot Closed Won/customer source or imported/FirstTouch-accessible customer list required; HubSpot improves owner/CSM routing and logging |
| `hubspot-signal-to-linkedin-touch` | HubSpot required |
| `campaign-pause-and-fix` | No HubSpot required; works on any running FirstTouch flow |
| `founder-post-generator` | No HubSpot required; drafts posts only, sends nothing |

## HubSpot access rules for this pack
- If HubSpot is connected, HubSpot-specific recipes can read CRM context, owner, lifecycle/deal/list data, and log back where the connected FirstTouch-HubSpot integration supports it.
- If HubSpot is used but no MCP/key is connected, ask for a HubSpot list or other FirstTouch-accessible source before running HubSpot-dependent motions.
- If HubSpot is not used, run only the recipes above whose Needs column says no HubSpot or imported/Discover/list source is enough.

## Social Engagement source options
Social Engagement can be enabled through FirstTouch MCP and can monitor relevant LinkedIn profiles for post likes and comments. Prefer the user's own founder/leadership personal profile when available; if they do not have enough owned engagement yet, monitor a relevant competitor founder, category influencer, or executive profile and work the ICP-fit people engaging there. Profile views are not an available signal.

## Approval model
Approval always happens in chat first: the agent shows the exact draft and waits for a yes. FirstTouch's optional in-product human-in-the-loop layer (off by default) additionally pauses sends as approval tasks in the FirstTouch app under **Tasks** or in HubSpot. Approval tasks have **no automatic escalation or SLA** - if one sits unactioned, following up is manual, so recurring plays should check the pending-approval queue as part of the routine.

Publishing a flow activates it but does **not** enroll awaiting contacts. After approval, explicitly enroll the approved contacts/items, then confirm they moved from awaiting to in-progress.

| Motion | Approval style |
|---|---|
| AI SDR / dynamic actions | Row-level approval. Each first-touch row must be approved individually; if approval tasks are confirmed enabled, route them to the owner in HubSpot or the FirstTouch app under **Tasks**. |
| Warm engager, inbound, website visitor, HubSpot signal, customer/stalled deal | Row-level approval unless FirstTouch records an equivalent per-contact approval; approval tasks route to the owner in HubSpot or app **Tasks** when enabled. |
| Social campaigns | Two modes: rep/BDR dynamic rows use row-level approval like AI SDR; RevOps/founder one-time static campaigns can use flow-level approval after exact audience, templates, sender/routing rule, launch window, and daily cap are approved. |

## Trial-window expectation
FirstTouch trials run **two weeks**. Sequence the rollout so the user sees real results inside that window: high-intent plays in the first days (they convert fastest), outbound added once warm motions are running. Do not quote benchmark accept/reply/meeting rates - FirstTouch does not publish them. Instead, measure the user's own numbers with the team-metrics tools and compare week 1 to week 2.

## Onboarding output format
```markdown
## FirstTouch onboarding summary
- Persona: founder
- LinkedIn account: Free/basic or Sales Navigator/Premium
- Daily connection cap: recommended 10/day free/basic or 20/day Sales Nav/Premium; FirstTouch max 20/day free/basic or 30/day Sales Nav/Premium
- Daily message cap: 20/day free/basic or 30/day Sales Nav/Premium
- HubSpot access: MCP / service key / list only / none
- Social Engagement enabled: yes/no/unknown
- ICP/list available if no HubSpot: yes/no + source
- Plays available now from this pack: ...
- Plays blocked until HubSpot access/list or source data exists: ...
- Recommended first play: ...
- Approval workflow: row-level for dynamic plays; confirm whether approval tasks are enabled before routing to the owner in HubSpot or FirstTouch app Tasks; flow-level only for approved one-time social campaigns
```
