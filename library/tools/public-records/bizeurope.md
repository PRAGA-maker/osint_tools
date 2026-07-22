---
id: bizeurope
name: Bizeurope
description: Use when you have an `employer-org` or product/sector and want to find a European company's registered contact details — returns address, associated people and web/domain leads.
url: http://www.bizeurope.com
category: public-records
path:
- public-records
bestFor: Locating a small/mid European B2B company's listing, address and contact details from a company or trade-sector name.
selectorsIn:
- employer-org
- name
selectorsOut:
- address
- employer-org
- domain
status: live
pricing: freemium
costNote: The business directory and buyers' guide are free to search and browse. Companies pay for premium/featured listings, and adding your own company requires (free) registration; searching does not.
opsec: passive
opsecNote: Read-only directory browsing over HTTP. You are not querying the target directly, so nothing is disclosed to them. Do not register a company profile from a real identity if you want to stay anonymous.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running (since 1996/1997, Zeist, Netherlands) B2B trade directory; listings are self-submitted by companies, so entries can be stale or promotional rather than authoritative.
missingPersonsRelevance: medium
coverage:
- eu
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- BizEurope
- bizeurope.com
- Europe Business Directory
tags:
- company-research
- business-directory
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# Bizeurope

> A long-running self-submitted European B2B trade directory, useful for pinning down a small company's address and contact details when official registers come up empty.

## When to use
You have an `employer-org` (or a trade/product sector plus a country) tied to a subject — an employer, a small importer/exporter, a supplier — and you want a contact address, phone, or website to pivot on. Bizeurope indexes tens of thousands of small and mid-size European businesses that often do not appear prominently in official company registers, so it can surface a lead where a formal registry search stalls.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.bizeurope.com and use the business directory / buyers' guide search (`/bsr.htm`, `/business.html`, `/bsr/findsupplier.htm`).
2. Enter the `employer-org` name, or browse by country + trade sector if you only know the industry.
3. Read the listing: company name, self-described products, an `address`/country, sometimes a phone and a `domain`/website link.
4. Pivot: feed the website into WHOIS/domain tools, and the address/phone into people- and phone-OSINT to connect the company to individuals.

## Inputs → Outputs
- **In:** `employer-org` (company name) or `name` + sector/country
- **Out:** `address`, `employer-org` details, `domain`/website, sometimes phone
- **Empty/negative result looks like:** no matching listing, or only unrelated companies in the same sector — the directory skews toward firms that chose to list themselves, so absence is not proof the company does not exist.

## Gotchas & OpSec
- Listings are **self-submitted** and monetised via premium placement, so treat details as leads to verify, not authoritative facts; some entries are years out of date.
- Coverage is uneven by country and heavily B2B/trade oriented — good for importers/exporters and suppliers, weak for consumer-facing or purely local businesses.
- OpSec: passive read-only browsing; nothing is disclosed to the target. Site is HTTP (unencrypted) — avoid entering anything sensitive.

## Overlaps ("do both")
- Pair with an official registry search — Bizeurope surfaces small firms that self-list, while a national business register gives authoritative incorporation data; each finds what the other misses.

## Trust & verifiability
`trust: community` — an established but self-submitted trade directory with no verification of listings; corroborate any address or contact against a second source before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bizeurope |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → address, employer-org, domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
