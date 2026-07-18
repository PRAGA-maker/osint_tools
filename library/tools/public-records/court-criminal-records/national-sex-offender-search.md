---
id: national-sex-offender-search
name: National Sex Offender Search (NSOPW)
description: Use when you have a `name` or `address` and want an authoritative US-wide offender check — the DOJ portal that searches all 50 states, DC, territories, and tribal registries at once.
url: https://www.nsopw.gov/
category: public-records
path:
- public-records
- court-criminal-records
bestFor: Authoritative nationwide (US) sex-offender lookup by name or location, querying every state/territory/tribal registry from one federal front end.
selectorsIn:
- name
- address
selectorsOut:
- address
- image
- physical-description
status: live
pricing: free
costNote: Free official U.S. Department of Justice public service; no account or payment.
opsec: passive
opsecNote: Passive — you query official public registries; the registrant is not notified. Registry data is provided for public safety only — using it to harass or discriminate is unlawful.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The Dru Sjodin National Sex Offender Public Website, operated by the U.S. Department of Justice, querying the authoritative state/territorial/tribal registries in real time — the primary source.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- NSOPW
- Dru Sjodin National Sex Offender Public Website
- nsopw.gov
tags:
- sex-offender
- registry
- public-records
- doj
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# National Sex Offender Search (NSOPW)

> The U.S. Department of Justice's single front door to every state, territorial, and tribal sex-offender registry — the authoritative national check by name or location.

## When to use
You have a `name` or an `address`/area and need an authoritative, nationwide US answer on registered sex offenders — a background check on a person of interest, vetting a location, or safeguarding work. Because NSOPW queries the official registries directly (rather than a third-party mirror), it's the source you confirm any aggregator hit against, and the one to lead with when accuracy matters.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.nsopw.gov/.
2. Search **by name** (national name search) or **by location** (pick a state and a 1–3 mile radius around an address).
3. NSOPW forwards the query to each jurisdiction's registry and returns matching records — offender name, photo, registered address, physical description, and offense details.
4. Open a match on its home-state registry (linked through) for the fullest, most current detail.
5. Pivot: a registered `address` feeds property/neighbor OSINT; the `image` feeds reverse-image/face search; offense/conviction data feeds court-record lookups.

## Inputs → Outputs
- **In:** `name` or `address` (US, incl. DC, territories, tribal lands)
- **Out:** matching registrant records — `address`, `image` (photo), `physical-description`, offense details
- **Empty/negative result looks like:** no match means no registrant found in the queried registries — not absolute proof (some jurisdictions limit public data, and search is name/spelling-sensitive); try name variants and confirm on the state site.

## Gotchas & OpSec
- **Legal gate:** registry data is published for public safety; using it to harass, intimidate, or discriminate is illegal. Keep use lawful and investigative.
- Coverage/format varies by jurisdiction — some states restrict what's shown publicly, so a thin record may reflect state policy, not the full file.
- Name searches are spelling- and alias-sensitive; corroborate a hit with photo + address before concluding identity.

## Overlaps ("do both")
- The authoritative counterpart to aggregators like `[[familywatchdog-sex-offender-search]]` — use Family Watchdog for a fast mapped first pass, then confirm every decisive hit here at the official source.

## Trust & verifiability
`trust: trusted` — a U.S. DOJ service that queries the official state/territorial/tribal registries in real time; it is the primary source, so a match here is authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | national-sex-offender-search |
| category | public-records |
| selectorsIn → selectorsOut | name, address → address, image, physical-description |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
