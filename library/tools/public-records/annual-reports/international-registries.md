---
id: international-registries
name: International Registries
description: Use when you have an `employer-org` in a foreign jurisdiction and want the official company registry to verify it — returns `employer-org`, `domain`.
url: https://www.gov.uk/government/publications/overseas-registries/overseas-registries
category: public-records
path:
- public-records
- annual-reports
bestFor: Finding the official government company-registration authority for a given country before searching it.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
- domain
status: live
pricing: free
costNote: Free UK-government reference page; no account, key, or payment.
opsec: passive
opsecNote: You are reading a static gov.uk publication, not touching the target's registry. No target interaction and nothing logged against your subject. OpSec matters only at the downstream registry you are routed to.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published and maintained by Companies House (UK government) as guidance for verifying overseas companies; the links point to official national registries.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- buzzfile
aliases:
- Overseas Registries
- Companies House overseas registries list
tags:
- company
- registry
- corporate
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# International Registries

> Companies House's curated index of official company registries country-by-country — the "where do I even look?" step for foreign corporate research.

## When to use
You have an `employer-org` (a company, or a person's stated employer/business) tied to a specific country and you need the *authoritative* place to confirm it exists, who its officers are, and its filings — rather than a data-broker aggregate. This page tells you which national body registers companies in that jurisdiction and links straight to it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the gov.uk "Overseas registries" page.
2. Scroll (or Ctrl-F) to the country your `employer-org` is registered in.
3. Follow the listed link to that country's official registry (e.g. Companies Registration Office, Handelsregister, ASIC).
4. On the registry, search the company name / number to pull officers, addresses, incorporation date and status.
5. Pivot: an officer or registered-agent `name`/`address` feeds people-search; the company's own `domain` feeds domain-OSINT.

## Inputs → Outputs
- **In:** `employer-org` (+ the country it sits in)
- **Out:** the official registry `domain`/link for that jurisdiction, and from it the verified `employer-org` record (officers, address, status)
- **Empty/negative result looks like:** the country isn't in the list (it is not exhaustive) — fall back to a web search for "official company registry <country>" or a broker like [[buzzfile]].

## Gotchas & OpSec
- Human-in-the-loop: none for this index page; individual registries downstream may charge for full filings or throw a captcha.
- The list is curated for UK due-diligence needs, so coverage skews toward major economies — small jurisdictions may be missing or stale.
- OpSec: passive here; treat the *target* registry search with normal care (some registries log searches).

## Overlaps ("do both")
- Pairs with [[buzzfile]] — Buzzfile aggregates US business profiles quickly, while this routes you to the primary-source national registry for authoritative, jurisdiction-correct records.

## Trust & verifiability
`trust: trusted` — it is a UK-government (Companies House) publication and each link resolves to an official national registry, so the pointer itself is authoritative even where a given registry's own data quality varies.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | international-registries |
| category | public-records |
| selectorsIn → selectorsOut | employer-org → employer-org, domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
