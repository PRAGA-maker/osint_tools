---
id: thisnumber-com
name: thisnumber.com
description: Use when you have an international `phone` number and want to identify its country/region of origin and reach that country's phone directories — returns `geolocation` (country) and directory `name` leads.
url: https://www.thisnumber.com/country
category: phone
path:
- phone
bestFor: Identifying the country of an unknown international number and jumping to that country's national phone directory.
selectorsIn:
- phone
selectorsOut:
- geolocation
- name
status: live
pricing: free
costNote: Free to use; no account required. It aggregates links to national directories, some of which are themselves paid.
opsec: passive
opsecNote: Parsing a number's country code is passive and never touches the subject. Following through to a national directory may hand your query to that third-party site; judge each linked directory on its own.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Directory-of-directories aggregator; the country-code identification is reliable, but the onward directory links vary widely in quality and currency.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ThisNumber
- thisnumber phone directory
tags:
- mobilephone
- Mobile & Phone Related
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# thisnumber.com

> A worldwide phone directory index: paste an international number to confirm which country it belongs to, then hop to that country's white-pages/reverse-lookup services.

## When to use
You have a `phone` number in international format but aren't sure which of ~250 countries/territories it belongs to, or you know the country and want a jumping-off list of that country's phone directories. Best as a first, orienting step in phone OSINT — establishing the country so you can pick the right national tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.thisnumber.com/ and enter the full international `phone` number (with country code; the parser tolerates spaces, dashes, parentheses).
2. Read the country/region it resolves from the calling code (`geolocation`), plus any carrier/location hint it surfaces.
3. Use the per-country pages to open that nation's listed phone directories and reverse-lookup sites.
4. Run the actual name/address lookup on the appropriate national directory — thisnumber is the index, not usually the source of the name itself.
5. Pivot: a resolved country + a strong national directory can yield a `name`/`address`; feed those onward.

## Inputs → Outputs
- **In:** `phone` (international format, with country code)
- **Out:** `geolocation` (country/region of the number), links to national directories that may yield a `name`
- **Empty/negative result looks like:** country resolves but no listing details — expected for mobiles and unlisted numbers. A resolved country with no name is still useful; treat "no directory hit" as inconclusive, not as an unassigned number.

## Gotchas & OpSec
- It is a country-code resolver + directory portal, not a magic reverse-lookup; most of the actual identifying work happens on the linked national sites.
- Explicitly not an FCRA consumer-reporting service — no use for screening decisions.
- Onward links can be dead or paywalled; verify the destination before trusting it.

## Overlaps ("do both")
- Pairs with `[[numlookup]]`/`[[truecaller]]`-style reverse lookups and with country-specific directories — thisnumber tells you *which* national tool to use, then those tools do the identification.

## Trust & verifiability
`trust: community` — the calling-code-to-country mapping is dependable; the value and freshness of the onward directory links are uneven, so verify each.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | thisnumber-com |
| category | phone |
| selectorsIn → selectorsOut | phone → geolocation, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
