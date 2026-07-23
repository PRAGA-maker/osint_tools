---
id: cia-world-factbook
name: CIA World Factbook
description: Use when an investigation crosses into a country you don't know — returns authoritative reference on its geography, government, languages, and communications/internet infrastructure to contextualise other findings.
url: https://www.cia.gov/the-world-factbook/
category: public-records
path:
- public-records
bestFor: Getting authoritative country-level context (administrative divisions, languages, phone/internet infrastructure, borders) to interpret a subject's location and comms.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, public US-government reference; no account.
opsec: passive
opsecNote: Reading static reference pages on a US-government site; it reveals only which country you're researching, and only to CIA.gov's own web analytics. No interaction with any subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official US-government reference compiled from government and international sources; authoritative for country-level facts, though figures are periodically updated rather than real-time.
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
- cia-foia
aliases:
- World Factbook
- CIA Factbook
tags:
- data-and-statistics
- country-reference
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# CIA World Factbook

> The standard one-stop country reference — geography, government, economy, languages, and communications infrastructure for every nation, in a consistent format.

## When to use
Not a person-finder — it's *context*. When a case touches an unfamiliar country, the Factbook grounds your other findings: which languages/scripts a subject likely uses, how the country is administratively divided (to read an address), the state of its phone/mobile/internet infrastructure (to judge how someone there connects), border neighbours (for cross-border movement), and time zone. It turns a foreign location from a blank into a briefed environment.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.cia.gov/the-world-factbook/ and pick the country (search or map).
2. Read the relevant sections:
   - **Government** → administrative divisions (helps parse addresses/regions), official name, capital.
   - **People and Society** → languages, ethnic groups, religions (informs name/script and translation choices).
   - **Communications** → telephone system, mobile penetration, internet country code (`.xx`) and users (informs your comms/OSINT expectations).
   - **Geography** → borders, terrain, time zone.
3. Use it as a lens for other tools — e.g. interpret a phone/address format, choose a translation approach, or gauge whether a captured IP's geo is plausible.

## Inputs → Outputs
- **In:** a country/territory (no subject selector)
- **Out:** structured country facts (context, not a selector) — languages, admin divisions, internet/phone infrastructure, borders
- **Empty/negative result looks like:** N/A for reference lookups; the only gap is that figures are periodic estimates, so treat exact statistics as approximate and dated.

## Gotchas & OpSec
- It's **background**, not evidence about an individual — use it to interpret findings, never as a source about a person.
- Data is updated on a cycle, so population/economic figures can lag current reality.
- Entirely passive; no operational risk beyond CIA.gov seeing that you loaded a country page.

## Overlaps ("do both")
- Pairs with [[cia-foia]] and country-specific public-records portals — the Factbook frames the environment, while those provide the actual records within it.

## Trust & verifiability
`trust: trusted` — authoritative US-government reference with a consistent, well-sourced format; reliable for country-level facts, with the caveat that figures are periodic estimates.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cia-world-factbook |
| category | public-records |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
