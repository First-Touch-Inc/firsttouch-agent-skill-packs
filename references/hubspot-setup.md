# HubSpot setup reference for FirstTouch-triggered workflows

Use this when a play needs HubSpot as the source of truth but the agent cannot create or inspect HubSpot workflows directly. These are RevOps/admin setup steps, not a claim that FirstTouch can build HubSpot UI objects by itself.

## Where to confirm FirstTouch action cards
1. In HubSpot, open **Settings → Integrations → Connected apps** and confirm FirstTouch is connected.
2. Open **Automation → Workflows**, create or edit a **contact-based** workflow, then add an action and search for **FirstTouch**.
3. If FirstTouch action cards appear, confirm the card can enroll/add the contact to the intended FirstTouch flow or source.
4. If no FirstTouch action card appears, use a HubSpot static/active list or exported source that FirstTouch can read/import, then enroll those contacts from FirstTouch. Do not promise a native HubSpot action card until it is visible in the customer's portal.

## Contact-based workflow pattern
1. Go to **Automation → Workflows → Create workflow → From scratch → Contact-based**.
2. Define enrollment criteria using contact properties and, when needed, associated-company or associated-deal criteria.
3. For deal-driven motions, do **not** use a deal-based workflow trigger. Build a contact-based workflow that enrolls contacts associated to qualifying deals.
4. Add suppression criteria before enrollment: DNC/opt-out, wrong owner, active sequence, recently contacted, bad/missing LinkedIn URL, and any customer-specific exclusions.
5. Choose the handoff:
   - **Preferred when available:** FirstTouch workflow action card that enrolls/adds the contact to the approved FirstTouch flow/source.
   - **Fallback:** add contacts to a HubSpot static/active list or export/import source that FirstTouch can access.
6. After publishing the HubSpot workflow/list, confirm the awaiting contacts inside FirstTouch, explicitly enroll approved items, then verify they moved to in-progress.

## Stalled open-deal one-time list
For a one-time AE/admin run, first build the filtered contact list in HubSpot:
- associated deal is open
- deal stage is not Closed Won and not Closed Lost
- last activity / last engagement is more than 60 days ago
- contact has a usable LinkedIn URL or enough data for enrichment
- owner/sender routing is approved

FirstTouch/MCP cannot natively infer that exact stalled-deal cohort without the HubSpot source/list. If the list is missing, stop and ask the user/admin to create or expose it.
