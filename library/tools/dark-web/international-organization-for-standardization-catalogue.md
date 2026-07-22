---
id: international-organization-for-standardization-catalogue
name: International Organization For Standardization Catalogue
description: Use when you have an `employer-org` or a standard number and want to confirm which ISO standards apply/are cited — returns `document-id` standard references.
url: https://www.iso.org/standards.html
category: dark-web
path:
- dark-web
bestFor: Looking up ISO standard numbers, titles and scopes when a document, product or company cites compliance.
selectorsIn:
- employer-org
- document-id
selectorsOut:
- document-id
status: live
pricing: freemium
costNote: Browsing and searching the catalogue (numbers, titles, scopes, abstracts) is free; the full text of a standard must be purchased.
opsec: passive
opsecNote: A public reference catalogue; searching it is passive and unconnected to any target. Only iso.org's own web logs see your queries.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The official International Organization for Standardization site; the catalogue metadata (numbers, titles, statuses) is authoritative.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ISO catalogue
- iso.org standards
tags:
- toddington
- curated-directory
- specialty-search
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# International Organization For Standardization Catalogue

> The official ISO standards catalogue — a reference lookup for standard numbers, titles and scopes, useful for decoding compliance claims rather than finding people.

## When to use
Marginal for missing-persons work, but a solid reference when a document, product datasheet, certificate or company profile in your investigation *cites an ISO standard* (e.g. "ISO 9001 certified", "conforms to ISO/IEC 27001"). Use the catalogue to confirm the standard exists, what it actually covers, and its current/withdrawn status — so you can judge whether a compliance claim is real, current, or misrepresented. Also handy for translating a bare standard number found in metadata or a spec into a human-readable subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.iso.org/standards.html (the site redirects legacy `/iso/home.html` links here).
2. Search by standard number (e.g. `27001`) or keyword/subject, or by the certifying `employer-org` context you're checking.
3. Read the result: number, full title, scope/abstract, edition, and status (published / under development / withdrawn).
4. Pivot: confirm a certification claim's plausibility, then verify the *actual* certificate through the relevant accreditation body (ISO itself does not certify companies); a withdrawn/superseded standard is a red flag on a "current compliance" claim.

## Inputs → Outputs
- **In:** a standard number (`document-id`) or an `employer-org`/subject keyword
- **Out:** `document-id` — the confirmed standard reference, title, scope and status
- **Empty/negative result looks like:** no matching standard for the number/term — the citation may be fabricated, mistyped, or refer to a national (non-ISO) standard.

## Gotchas & OpSec
- ISO publishes standards; it does **not** certify organisations — a real ISO number does not prove a company is certified. Verify certificates with the accreditation body.
- Only metadata/abstracts are free; full standard text is paywalled (this is a legitimate freemium boundary, not grounds to delete the reference).
- Passive reference lookup; no target exposure.

## Overlaps ("do both")
- Pairs with corporate-registry and accreditation-body lookups when validating a company's compliance claims — this confirms the standard is real; those confirm the *certification* is real.

## Trust & verifiability
`trust: trusted` — the first-party ISO catalogue, so standard numbers, titles and statuses are authoritative source-of-truth.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | international-organization-for-standardization-catalogue |
| category | dark-web |
| selectorsIn → selectorsOut | employer-org, document-id → document-id |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
