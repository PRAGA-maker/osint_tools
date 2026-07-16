---
id: archives-library-information-center-alic
name: Archives Library Information Center (ALIC)
description: Use when you have a `name` and want authoritative pointers to US vital/genealogy records (birth, death, marriage) — returns links toward address, employer-org, and family records.
url: https://www.archives.gov/research/alic/reference/vital-records.html
category: public-records
path:
- public-records
bestFor: A US National Archives (NARA) reference hub that points you to where birth, death, marriage, and genealogy records actually live.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- name
status: live
pricing: free
costNote: Free US federal government reference resource (NARA); no account or payment for the reference pages themselves. Records they point to may charge fees at the holding agency.
opsec: passive
opsecNote: You are reading NARA reference/link pages, not querying a database about the target, so nothing is attributable to the subject. Standard web hygiene (VPN/sock-puppet) is sufficient; the sensitive step is whichever record repository ALIC sends you to next.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party US National Archives (archives.gov) reference resource; authoritative as a signposting guide, though the actual records sit at state/agency repositories it links to.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- familysearch
- deathindexes-com
- access-to-archival-databases
- national-archives-and-records
aliases:
- ALIC
- NARA vital records reference
tags:
- toddington
- curated-directory
- specialty-search
- genealogy
source: toddington-resources
lastVerified: '2026-07-11'
enrichment: full
---

# Archives Library Information Center (ALIC)

> The US National Archives' reference desk on the web — a signposting hub that tells you *where* birth, death, marriage, and genealogy records are held, rather than holding them itself.

## When to use
You have a `name` (and often a rough era/location) and need to find the authoritative repository for a US vital record — birth, death, marriage, divorce — or for broader genealogy research. ALIC is a starting map, not a search box: reach for it when you're unsure which agency holds a given record type and want a trustworthy federal pointer instead of a random results page. Especially useful in missing-persons/next-of-kin work where a death or marriage record breaks a case open.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the ALIC vital-records reference page: https://www.archives.gov/research/alic/reference/vital-records.html.
2. Identify the record type and jurisdiction you need (vital records are generally held at the **state** level in the US, not federally).
3. Follow ALIC's links to the correct holder — state vital-records office, NARA genealogy resources, or partner databases (e.g. Ancestry/Fold3 references).
4. Also browse ALIC's broader genealogy reference section for census, immigration, and military pointers.
5. Pivot: execute the actual lookup at the linked repository ([[familysearch]], state indexes, [[deathindexes-com]]) to pull the `name`/`address`/family details.

## Inputs → Outputs
- **In:** `name` (plus era/jurisdiction to narrow the right repository)
- **Out:** authoritative *pointers* that lead to `address`, family/next-of-kin, and organizational (`employer-org`) records — ALIC itself returns guidance, not the record
- **Empty/negative result looks like:** the page directs you to a state office rather than an online database — expect to leave archives.gov to obtain the actual record; ALIC won't display it inline.

## Gotchas & OpSec
- ALIC is a *reference/signpost*, not a records database — don't expect to type a name and get a hit here; its value is routing you to the correct holder.
- US vital records are mostly state-administered with varying access rules and fees; the record you need may require a mail/in-person request at the state office.
- OpSec: passive — reading federal reference pages reveals nothing about your target.

## Overlaps ("do both")
- Pairs with [[familysearch]] and [[deathindexes-com]] — ALIC tells you *which* record and *where*; those tools are where you actually search and pull the data.

## Trust & verifiability
`trust: trusted` — a first-party US National Archives resource. As a signpost it is authoritative; verifiability of the underlying records rests with the state/agency repository ALIC directs you to.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | archives-library-information-center-alic |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
