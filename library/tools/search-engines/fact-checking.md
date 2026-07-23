---
id: fact-checking
name: Fact-Checking
description: Use when you need to verify a claim or find a regional fact-checker — the Duke Reporters' Lab global database/map of fact-checking organisations worldwide (no subject selectors).
url: https://reporterslab.org/fact-checking/
category: search-engines
path:
- search-engines
bestFor: Locating credible fact-checking organisations by country/language to verify a claim, image, or narrative you've encountered in an investigation.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free academic resource from the Duke Reporters' Lab; no account.
opsec: passive
opsecNote: Browsing a public academic directory is passive and reveals nothing about a subject. The verification you do next (searching a claim, contacting a fact-checker) carries its own considerations.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by the Duke University Reporters' Lab, the standard academic census of fact-checking outlets; authoritative for who the fact-checkers are, though it indexes organisations rather than adjudicating individual claims.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- duke-reporters-lab
aliases:
- Duke Reporters' Lab fact-checking database
- fact-checking map
tags:
- verification
- fact-checking
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Fact-Checking

> The Duke Reporters' Lab global census of fact-checking organisations — a map/database to find a credible, regional fact-checker for the claim in front of you.

## When to use
An investigation surfaces a claim, viral image, or narrative you need to assess, and you want **established fact-checkers** — especially local-language ones — who may have already debunked it or can be trusted sources. This directory catalogues active fact-checking outlets worldwide with their country, language, and reach, so you can find the right one instead of guessing. It's a verification-workflow resource, not a per-claim search engine.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://reporterslab.org/fact-checking/ and use the interactive map/database.
2. Filter by country/region and language to find fact-checkers covering your subject's area.
3. Go to the identified outlet(s) and search their archives for the specific claim/image.
4. Weigh multiple fact-checkers where they exist; note that a listing means the org is recognised, not that it has covered your exact claim.
5. Pair with reverse-image search and primary-source checks for claims no one has yet addressed.

## Inputs → Outputs
- **In:** none (a directory — you browse/filter by region/language)
- **Out:** none as selectors — a shortlist of credible fact-checking organisations to consult
- **Empty/negative result looks like:** few or no fact-checkers for a region/language — common in under-covered areas; fall back to primary-source verification rather than assuming a claim is unchecked-because-true.

## Gotchas & OpSec
- It **indexes organisations, not claims** — you still have to go to the fact-checker and search the specific item.
- A listing is recognition of the outlet, not proof of its every conclusion — read the actual fact-check and its sourcing.
- Coverage is uneven globally; sparse regions need primary-source work.

## Overlaps ("do both")
- Part of the broader [[duke-reporters-lab]] resources — use this to find *who* checks facts in a region, then apply reverse-image/geolocation and primary-source tools for claims the fact-checkers haven't reached.

## Trust & verifiability
`trust: trusted` — an authoritative academic census of fact-checking outlets; reliable for identifying credible checkers, with the caveat that adjudicating a specific claim still requires reading their actual work.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fact-checking |
| category | search-engines |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
