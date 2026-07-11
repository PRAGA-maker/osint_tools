---
id: directorwho-co-uk
name: DirectorWho
description: Use when you have a `name` and want the UK companies they are/were a director of, plus co-directors and DOB/address hints — returns employer-org, associate, dob and address.
url: https://www.directorwho.co.uk/
category: public-records
path:
- public-records
bestFor: Reverse-searching a person's name across UK company directorships and their co-directors.
selectorsIn:
- name
selectorsOut:
- employer-org
- associate
- dob
- address
status: live
pricing: free
costNote: Free to search; a front-end that re-presents live Companies House data (which is itself free and public).
opsec: passive
opsecNote: Searches public Companies House-derived records; the director is not notified. Only your IP touches the site. Note that Companies House exposes director month/year of birth and a service/registered address — public but personal.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party interface over authoritative Companies House data; its name/DOB merging is convenient but heuristic — confirm merged profiles against the official register before treating them as one person.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- Director Who
- directorwho.co.uk
tags:
- companysites
- Company Related Sites
- companies-house
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# DirectorWho

> A person-first view of UK company data — search a name to see every company they direct and who they direct alongside.

## When to use
You have a `name` and want to know their UK corporate footprint: which companies they are or were a director of, their co-directors (`associate`s), and the DOB month/year and service address Companies House exposes. It is built for the reverse question the official register handles less fluidly — start from a person and fan out to companies and business associates, merging matching name+DOB profiles onto one page.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.directorwho.co.uk/.
2. Search the person's `name`; DirectorWho merges directorships that share a name and date of birth into a combined profile.
3. Review the linked companies (`employer-org`), appointment/resignation dates, co-directors (`associate`s), the director's month/year of birth (`dob`), and service/registered `address`.
4. Verify the merge is correct (name+DOB collisions happen) against the official Companies House record.
5. Pivot: companies feed corporate deep-dives (filings, PSCs, addresses); co-directors become new subjects; the service address and DOB corroborate identity elsewhere.

## Inputs → Outputs
- **In:** `name`
- **Out:** `employer-org` (directorships), `associate` (co-directors), `dob` (month/year), service `address`
- **Empty/negative result looks like:** no directorships — the person may simply never have been a UK company officer; absence says nothing about non-director roles or overseas companies.

## Gotchas & OpSec
- **Merging is heuristic** — two different people sharing a name and birth month/year can be conflated; verify against Companies House.
- UK-only, and only captures director/officer roles (not shareholders unless they are also PSCs/officers).
- Passive: the director is not notified.

## Overlaps ("do both")
- Pairs with the official Companies House register and PSC data — DirectorWho gives the fast person-centric overview; the official register confirms each appointment and adds filings the front-end may not show.

## Trust & verifiability
`trust: community` — accurate as far as the authoritative Companies House data it mirrors, but its profile-merging is a convenience heuristic to double-check. Verify identity-critical links at the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | directorwho-co-uk |
| category | public-records |
| selectorsIn → selectorsOut | name → employer-org, associate, dob, address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
