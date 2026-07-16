---
id: laws-and-codes-search-directory-by-state
name: OnlineSearches Public Records & Laws/Codes Directory (By State)
description: Use when you have a `name` and a US state/county and want the right official record source (court, inmate, vital, property, plus state laws/codes) — returns links to local records yielding `address`, `dob`, and `document-id`.
url: https://publicrecords.onlinesearches.com/
category: public-records
path:
- public-records
bestFor: Finding the correct free state/county public-record source for a person or statute lookup.
selectorsIn:
- name
selectorsOut:
- address
- dob
- document-id
status: live
pricing: freemium
costNote: The directory and most linked government records are free; some "find a person" widgets on the site funnel to paid partners (e.g. Intelius) — stay on the official-record links to keep it free.
opsec: passive
opsecNote: Browsing the directory is passive and reveals nothing to the target. Exposure risk moves to whichever linked government record system you then query — most county sites are anonymous, but a few log searches; judge each one.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: OnlineSearches.com is a long-running aggregator that links out to official government record systems; the directory curation is reliable but always confirm you have reached the authoritative source, not a paid reseller page.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- court-records-search-directory
- free-public-records-directory-us
- jail-and-inmate-records-search-directory
- marriage-records-search-directory
- os-birth-records
- os-death-records
- os-divorce-records
- permits-and-inspections-search-by-state
- public-records-directory
- sex-offender-us
- unclaimed-and-abandoned-property-search-directory
aliases:
- OnlineSearches public records
- Laws and Codes Search Directory
- onlinesearches.com by state
tags:
- court
- inmate
- public-records-directory
source: metaosint
lastVerified: '2026-07-16'
enrichment: full
---

# OnlineSearches Public Records & Laws/Codes Directory (By State)

> OnlineSearches.com's state/county index: pick a location and it routes you to the official free source for court, inmate, vital, property, and statute records.

## When to use
You have a `name` and know (or suspect) the US state or county, and you need the *authoritative local* record — not a paid aggregator's teaser. This directory maps every US state and county to its available online record systems (property/assessor, vital records, court, warrants, jail/inmate, sex-offender, UCC, unclaimed property) and to state laws/codes/ordinances, and it flags whether each is available free online, paid, or offline. It's the "where do I actually look this up for this jurisdiction" tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://publicrecords.onlinesearches.com/.
2. Browse by **record type** (courts, inmate, vital, property, laws & codes) or by **geography** (state → county).
3. Pick the target jurisdiction; the page lists each available source and marks it free / paid / offline.
4. Click through to the **official government source** and run your `name` search there for `address`, `dob`, case/`document-id`, or custody status.
5. Avoid the site's own "find person" boxes that redirect to paid partners (Intelius) — stay on the government links.
6. Pivot: a court/inmate hit gives a case number (`document-id`) and location; a vital record gives `dob`/relatives to feed genealogy and people-search tools.

## Inputs → Outputs
- **In:** `name` + a US state/county
- **Out:** links to official records that return `address`, `dob`, and case/document identifiers (`document-id`)
- **Empty/negative result looks like:** a county whose records are marked "offline" or "paid only," or a record type with no online source for that jurisdiction — the directory tells you the gap exists rather than returning data itself.

## Gotchas & OpSec
- It's an index, not a database — it never returns a person directly; the linked government sites do the actual searching.
- Some on-page widgets are lead-gen for paid people-search resellers; distinguish those from the genuine `.gov`/county links.
- OpSec: passive to browse; each downstream government system carries its own (usually low) exposure.

## Overlaps ("do both")
- Do both with the type-specific directories it links, like [[court-records-search-directory]], [[jail-and-inmate-records-search-directory]], and [[free-public-records-directory-us]] — this is the geographic entry point; those drill into one record type.

## Trust & verifiability
`trust: community` — a well-established aggregator that curates links to official sources; trust the *destinations* (government systems) as authoritative, and treat the aggregator's own paid widgets with caution.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | laws-and-codes-search-directory-by-state |
| category | public-records |
| selectorsIn → selectorsOut | name → address, dob, document-id |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
