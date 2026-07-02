# Recipe Catalog - Founder Pack

Use this file when the agent installed `skills/` and `references/` without loading the root README. These recipes are the recommended starting points for the founder persona.

## Recommended start point
1. **Check Social Engagement first:** run **Social engagement flow: founder posts** from owned founder or executive personal profiles. If Social Engagement is not enabled, turn it on through FirstTouch MCP for the monitored profile. If owned personal-profile engagement is thin, monitor a relevant competitor founder or category influencer personal profile. FirstTouch does not track company-page/profile engagement.
2. **No engagement to harvest yet:** run **Founder post generator** to draft a week of founder-voice posts that create it - then harvest engagers 24-72h after posting. If you need pipeline this week regardless, run **Founder-led AI SDR** from ICP + FirstTouch Discover Contacts in parallel.
3. **Have HubSpot:** add inbound, visitor, and stalled-deal plays as secondary CRM/deal motions, not the default path.

## Quickstart play cards
| Situation | Run this | What happens |
|---|---|---|
| Has founder/executive post engagement | Social engagement flow | Work warm engagers from personal-profile posts |
| Thin owned engagement | Founder post generator | Draft posts that create ICP engagement to harvest |
| Still thin after posting | Monitor competitor/influencer profile | Use relevant external personal-profile engagement |
| No warm source | Founder-led AI SDR | Discover ICP prospects and draft founder-voice outreach |
| Has CRM data | Stalled deal / customer referral thank-you | Work high-intent relationship motions |

## Recipes
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

## Approval reminder
Dynamic/AI SDR rows require row-level approval. Static social-campaign flows can use flow-level approval only after the exact audience, static templates, sender/routing rule, launch window, and daily cap are approved.
