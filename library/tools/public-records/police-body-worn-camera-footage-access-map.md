---
id: police-body-worn-camera-footage-access-map
name: Police Body-Worn Camera Footage Access Map
description: Use when you have a US `geolocation` (state) and want to know if/how police body-camera footage can be obtained — returns the state's access law status and citations.
url: https://www.rcfp.org/resources/bodycams/
category: public-records
path:
- public-records
bestFor: Checking, per US state, whether the public can access police body-worn camera footage and under what law.
selectorsIn:
- geolocation
- address
selectorsOut:
- image
- document-id
status: live
pricing: free
costNote: Free reference resource published by the nonprofit Reporters Committee for Freedom of the Press; no account.
opsec: passive
opsecNote: A published legal guide; reading it contacts no one. Any actual footage request you later file with a department is a separate, active step made in your own name.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by RCFP, an established press-freedom legal organisation; the map cites the underlying bills and cases.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- RCFP bodycam map
- body-worn camera access map
tags:
- public-records
- police-records
- foia
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# Police Body-Worn Camera Footage Access Map

> An interactive US map from the Reporters Committee showing, state by state, whether and how the public can obtain police body-worn camera footage — the first stop before trying to pull footage of an incident.

## When to use
An incident relevant to your case (a stop, an arrest, a missing-person contact, a use-of-force event) may have been recorded on police body cameras, and you want to know whether that footage is legally obtainable and how. This map tells you, for the state in question, whether access laws exist, are proposed, or rest on court rulings — and links the specific bills/cases. Use it to scope a public-records/FOIA request before you file one.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.rcfp.org/resources/bodycams/.
2. Find the relevant US state on the map; the color indicates status (e.g. access law passed, proposed, none, or court-established).
3. Click the state to read the summary and open links to the underlying bill(s) and/or case(s) (`document-id`s).
4. Use that legal basis to draft a records request to the specific department that would hold the footage.
5. Pivot: file the request under the cited authority; the resulting `image`/video footage can then feed identification and geolocation work.

## Inputs → Outputs
- **In:** `geolocation`/`address` (a US state / jurisdiction)
- **Out:** the state's access-law status, citations to bills/cases (`document-id`), and the path to obtaining `image`/video footage
- **Empty/negative result looks like:** a state marked as having no access law — meaning footage is likely withheld or discretionary, not that it doesn't exist. The map guides feasibility, not a guaranteed release.

## Gotchas & OpSec
- OpSec: **passive** to read; the *request* you later file is active and made in your own identity, subject to fees and denials.
- US-only, state-level; local department policies can be stricter than state law.
- Legal status changes — check the map's update date and confirm the current statute before filing.

## Overlaps ("do both")
- Pairs with state FOIA/public-records guides and department portals — this scopes whether footage is accessible; those are how you actually request it.

## Trust & verifiability
`trust: trusted` — a reputable press-freedom organisation's guide that cites the primary bills and rulings, so every status is traceable to law you can read yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | police-body-worn-camera-footage-access-map |
| category | public-records |
| selectorsIn → selectorsOut | geolocation, address → image, document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
