---
id: intelligence-x-2
name: Intelligence X
description: Use when you have an email and want to search a deep/dark-web and leak archive for that selector — returns breach hits, document references, and linked identifiers.
url: https://intelx.io/tools?tab=email
category: email
path:
- email
bestFor: Searching Intelligence X's archive of leaks, dark-web pages, and documents by email.
selectorsIn:
- email
- domain
- username
- ip-address
selectorsOut:
- email
- domain
- metadata
- document-id
status: live
pricing: freemium
costNote: Free account gives limited preview searches; full results and bulk access require paid plans.
opsec: passive
opsecNote: Searches are run server-side against IntelX's index; subject is not notified. Searches may be logged to your account — use a research account.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Intelligence X (intelx.io) is a well-established Czech-based commercial search engine and data archive widely used in professional OSINT; reputable, though full result access is paywalled.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- IntelX
- intelx.io
tags:
- email-search-email-check
- darkweb
- leaks
source: osint4all
lastVerified: ''
enrichment: full
---

# Intelligence X

> Commercial search engine and historical data archive — indexes leaks, dark-web pages, paste sites, and documents, queryable by email, domain, IP, or selector.

## When to use
You have a subject's `email` (or `domain`, `username`, `ip-address`) and want to find where it appears across breaches, paste sites, dark-web pages, and archived documents. The email tools tab is purpose-built for email selectors. In missing-persons work this surfaces breach exposure, leaked documents mentioning the subject, and linked identifiers to pivot on. Strong when you need historical/archived content others have since removed.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://intelx.io/tools?tab=email and sign in (free account for limited previews).
2. Enter the `email` (or use the domain/IP/selector tabs).
3. Review the results: a timeline of buckets (leaks, darknet, documents, web) with previews. Full content and exports require a paid plan.
4. Pivot: open associated documents/leaks for new `email`/`username`/`domain` selectors; cross-check with [[leakcheck]] and [[intelligence-x]] strategies. An API is available for automation.

## Inputs → Outputs
- **In:** `email`, `domain`, `username`, `ip-address`
- **Out:** breach/leak hits, `document-id` references, associated `email`/`domain`, source `metadata` (bucket, date)
- **Empty/negative result looks like:** "no results" across all buckets — the selector is not in IntelX's index for your access tier.

## Gotchas & OpSec
- Human-in-the-loop: account login required; previews are truncated and full records/exports are paywalled.
- OpSec: passive toward the subject, but queries are tied to your IntelX account — use a dedicated research account. Do not reuse a personal login.

## Overlaps ("do both")
- Pairs with [[leakcheck]] because IntelX excels at documents/dark-web/paste content while dedicated breach engines give cleaner credential-level hits.

## Trust & verifiability
`trust: trusted` — Intelligence X is an established commercial OSINT search engine with a long track record and transparent ownership. Individual archived items still warrant corroboration, and free-tier previews are limited.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | intelligence-x-2 |
| category | email |
| selectorsIn → selectorsOut | email, domain, username, ip-address → email, domain, metadata, document-id |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
