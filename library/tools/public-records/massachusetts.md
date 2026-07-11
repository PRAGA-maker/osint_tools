---
id: massachusetts
name: Massachusetts Inmate Locator (via VINELink)
description: Use when you have a `name` (or commitment number) and want to locate someone in a Massachusetts prison — the state directs you to VINELink to confirm custody and status, returning identity and a custody document-id.
url: https://www.mass.gov/how-to/find-an-inmate-in-a-massachusetts-prison
category: public-records
path:
- public-records
bestFor: Locating a person held in a Massachusetts Department of Correction facility via the state's VINELink service.
selectorsIn:
- name
- document-id
selectorsOut:
- name
- document-id
status: live
pricing: free
costNote: Free public service; VINELink search and the (866) 277-7477 phone line cost nothing.
opsec: passive
opsecNote: A public custody-lookup service; searching is passive and the subject is not notified. VINELink offers optional victim-notification registration — do NOT register for alerts on a target, as that is a distinct, logged action; use the search only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The mass.gov page is the official state instruction; it routes to VINELink, the state's designated inmate-location/notification partner (only the MA DOC participates). Authoritative for MA state custody.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Massachusetts DOC inmate search
- MA VINELink
tags:
- court
- inmate
- corrections
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# Massachusetts Inmate Locator (via VINELink)

> Massachusetts doesn't run its own web inmate lookup — this official mass.gov page points you to VINELink, the state's designated service for confirming whether someone is in MA Department of Correction custody.

## When to use
You have a `name` (or a commitment number) and need to establish custody status in Massachusetts state prison: is the person incarcerated, and in which facility? Relevant to missing-persons triage — a reported-missing adult may be in MA DOC custody, and VINELink is the state's sanctioned way to check.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the mass.gov instruction page (this URL) and follow it to VINELink.
2. Search VINELink with the person's full first and last name, or their commitment number.
3. Alternatively call the VINE line at (866) 277-7477 to search by phone.
4. Read the result: identity match and current custody status/facility.
5. Pivot: a commitment number + confirmed facility anchors current whereabouts and a mail/visitation channel; combine with county and federal (BOP) checks for jurisdictions VINE-MA doesn't cover.

## Inputs → Outputs
- **In:** `name` or commitment `document-id`
- **Out:** confirmed `name`, custody status/facility, and commitment `document-id`
- **Empty/negative result looks like:** no match on VINELink — means not in MA DOC state custody (per VINE's MA participation); it does not rule out county houses of correction, federal custody, or another state.

## Gotchas & OpSec
- **VINELink, not a DOC site:** the lookup runs on VINELink (a third-party partner); direct data questions there, not to state officials. Only the MA DOC participates in MA VINE, so scope is state prisons.
- Common-name collisions: confirm with a commitment number where possible.
- Don't register for victim-notification alerts on a target — that's a separate, logged action; use search only.
- OpSec: passive; no subject notification from a search.

## Overlaps ("do both")
- Pairs with the federal `[[federal-bureau-of-prisons-inmate-locator]]` and other states' DOC searches (`[[florida]]`, `[[maryland]]`) — run the subject against every jurisdiction where they have ties.

## Trust & verifiability
`trust: trusted` — official state instruction routing to the state's designated custody-lookup partner. The custody data is authoritative for Massachusetts state prisons.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | massachusetts |
| category | public-records |
| selectorsIn → selectorsOut | name, document-id → name, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
