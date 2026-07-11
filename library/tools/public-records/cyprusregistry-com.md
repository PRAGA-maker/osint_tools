---
id: cyprusregistry-com
name: cyprusregistry.com
description: Use when you have an `employer-org` or director `name` in Cyprus and want company officers, shareholders, and addresses — returns employer-org, address, and associate/name data.
url: https://cyprusregistry.com/
category: public-records
path:
- public-records
bestFor: Previewing Cyprus company records — directors, secretaries, shareholders, addresses, and historical changes — via a searchable third-party mirror.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- address
- employer-org
- name
status: live
pricing: freemium
costNote: Free preview of basic company data (key people, addresses); full reports (shareholders + addresses, historic changes, previous names/addresses, mortgages, documents) are paid and prepared within ~6 hours. Pricing not published on-page.
opsec: passive
opsecNote: Third-party aggregator (NOT the official Cyprus Registrar of Companies); it queries its own dataset, so the target is not notified and only the operator sees your search/IP. Buying a full report requires payment details — use appropriate payment hygiene and a sock-puppet account if the case is sensitive.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial aggregator mirroring Cyprus registry data, explicitly not affiliated with the official Registrar; useful and generally accurate, but confirm critical facts against the official registry.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- opencorporates
- ebra-be
aliases:
- Cyprus Registry
- cyprusregistry
tags:
- companysites
- Company Related Sites
- corporate-registry
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# cyprusregistry.com

> A searchable third-party mirror of Cyprus company records — fast way to preview directors, secretaries, shareholders, and addresses without the official registrar's clunky interface.

## When to use
You have a Cyprus `employer-org` (company) or a `name`/`address` you suspect is tied to Cyprus corporate structures — a common jurisdiction in cross-border and offshore tracing — and you want to see officers, shareholders, and registered addresses quickly. The free preview alone often confirms whether a person is linked to a company and surfaces co-directors (`associate`s); the paid report adds shareholder addresses and historical changes.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cyprusregistry.com/ and search by company name (or browse the A–Z listing).
2. Open the company page and read the **free preview**: key people (directors, secretaries), registered `address`, basic status.
3. If you need shareholders, historic changes, previous names/addresses, mortgages, or documents, order the **paid report** (delivered within ~6 hours).
4. Read the output: `employer-org` structure, officer/`name`s, `address`es, and co-officer `associate` links.
5. Pivot: co-directors feed people-search; a shareholder or previous address feeds property/records tools; corroborate against the official registrar.

## Inputs → Outputs
- **In:** `employer-org` (company name); `name`/`address` to correlate officers
- **Out:** director/secretary `name`s, registered `address`, shareholders (paid), historical changes/previous names (paid), `associate` officer links
- **Empty/negative result looks like:** no company match or a bare shell entry with no useful officers — the entity may be dissolved, unregistered in Cyprus, or a nominee shell; absence isn't proof of no Cyprus link.

## Gotchas & OpSec
- **Not** the official Registrar of Companies — a mirror. For anything you'll rely on, confirm against the official Cyprus registry.
- Cyprus is a nominee-heavy jurisdiction; listed directors/shareholders may be professional nominees, not the real controllers — treat officer names as leads.
- Human-in-the-loop: the valuable fields (shareholders, history) are behind a paid, delayed report.
- OpSec: passive toward the subject; payment for a report exposes your billing identity to the operator.

## Overlaps ("do both")
- Pairs with [[opencorporates]] (cross-jurisdiction correlation) and [[ebra-be]] (route to the *official* Cyprus registrar) — use this for a fast preview, the others to verify and to follow the company's links into other countries.

## Trust & verifiability
`trust: community` — a commercial aggregator, accurate enough for leads but explicitly unofficial. Verify anything load-bearing (ownership, current status) against the official Cyprus Registrar of Companies.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cyprusregistry-com |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → address, employer-org, name |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
