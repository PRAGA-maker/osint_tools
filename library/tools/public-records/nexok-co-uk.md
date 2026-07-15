---
id: nexok-co-uk
name: Nexok
description: Use when you have a `name`, `address`/postcode, or `employer-org` in the UK and want to find associated companies and director records — returns company details, `address`, appointments, and director `associate` links.
url: https://www.nexok.co.uk/
category: public-records
path:
- public-records
bestFor: Pivoting a UK name/company/postcode into director records, company addresses, and appointment history via a Companies House front-end.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- employer-org
- address
- associate
- name
status: live
pricing: freemium
costNote: Search and filtering over UK company data are usable for free; bulk export (for direct-mail/marketing) is the paid product. The underlying data derives from Companies House, which is itself free at source.
opsec: passive
opsecNote: You query a public UK company database, not the subject — no notification to any individual. Ordinary web-logging only; a sock-puppet session is prudent for bulk work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Third-party value-add front-end over Companies House data (~5.7M active UK companies, 50+ filters). Data is only as current as its Companies House feed; cross-check anything critical against the official register.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- nexok.co.uk
tags:
- companysites
- Company Related Sites
- uk
- companies-house
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Nexok

> A UK company-data lookup and export front-end over Companies House — filter by 50+ data points including director name, occupation, age, postcode, and company attributes.

## When to use
You have a UK `name`, an `address`/postcode, or a company (`employer-org`) and want to map the person's business footprint: which companies they are or were a director of, the company's registered and correspondence addresses, appointment/resignation dates, and co-directors (`associate` links). Because it exposes rich filters (director occupation, age band, location radius), it is useful for **finding a specific individual among common names** and for uncovering address and network leads for a UK subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.nexok.co.uk/.
2. Search or filter — by company name/postcode, or by director attributes (name + occupation + age band + location) to pin down a person.
3. Read the results: company details, director appointments and timeline, company name-change history, and addresses.
4. Note co-directors and shared addresses as `associate` and location leads.
5. Pivot: confirm and deepen any hit on the free official register (Companies House) and cross-reference addresses with property/electoral tools.

## Inputs → Outputs
- **In:** `name`, `address`/postcode, or `employer-org`
- **Out:** `employer-org` (companies), registered/correspondence `address`, appointment history, co-director `associate` links
- **Empty/negative result looks like:** no companies match the name/filters — the person may simply have no UK directorships, so absence is not proof of anything about them personally.

## Gotchas & OpSec
- Data is a derived feed of Companies House — it can lag the official register; verify critical facts at source.
- Director records reflect *companies*, not residential facts; a "correspondence address" is often an accountant/registered office, not a home.
- Free tier covers search/view; bulk export is the paid marketing product — you rarely need it for a single subject.

## Overlaps ("do both")
- Pairs with the official Companies House register (authoritative, free) — use Nexok's richer filters to *find* the right record, then confirm on Companies House. Combine with UK electoral-roll and property tools to turn a directorship into a residential lead.

## Trust & verifiability
`trust: community` — a third-party aggregator; reliable as a discovery layer but not authoritative. Treat Companies House as the ground truth for anything you act on.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nexok-co-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → employer-org, address, associate, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
