---
id: posteo-de
name: posteo.de
description: Use when an email address ends in @posteo.de/@posteo.* and you need to understand the provider — a German privacy email host that yields little subscriber data.
url: https://posteo.de/en
category: email
path:
- email
bestFor: Recognizing and reasoning about a Posteo-hosted email address (privacy-focused German provider).
selectorsIn:
- email
selectorsOut:
- metadata-exif
status: live
pricing: freemium
costNote: Paid mailbox service (~1 EUR/month); no free OSINT lookup. Listed here only as a provider, not a search tool.
opsec: passive
opsecNote: Simply recognizing the domain is passive. Do not attempt to log in or probe accounts.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Posteo is a reputable real email provider, but it is NOT an OSINT lookup tool. It was harvested into an email list and is miscategorized as a research utility.
missingPersonsRelevance: low
coverage:
- de
- global
auth: account
api: false
localInstall: false
registration: true
aliases: []
tags:
- email
- Email Related Sites
- provider
source: uk-osint
lastVerified: ''
enrichment: full
---

# posteo.de

> Posteo is a paid, privacy-first German email/host provider — not an OSINT search tool. Its only investigative value is recognizing that a target uses a privacy-oriented mailbox.

## When to use
You have an `email` address on the `@posteo.de` (or `@posteo.net/.org/.com`) domain and want to understand the provider before deciding how to enrich it. Knowing the host is Posteo tells you the subject likely cares about privacy and that subpoena/registrar pivots will be limited (Posteo strips IP metadata and minimizes logging by design).

## How to use it (`bestInteractionPattern`: web-manual)
1. Note the domain of the target email. If it is a Posteo domain, this entry is informational only.
2. Do NOT expect a lookup form — posteo.de is a mailbox sign-up page, not a search engine.
3. Pivot the email itself to dedicated lookup tools (`[[reverse-whois]]`, breach search, social-profile checks) rather than to Posteo.

## Inputs → Outputs
- **In:** `email`
- **Out:** provider/`metadata-exif` knowledge only (which host, privacy posture).
- **Empty/negative result looks like:** there is no result surface here; the page is a marketing/sign-up site.

## Gotchas & OpSec
- Human-in-the-loop: none for recognition; never attempt account login.
- OpSec: passive. Posteo deliberately minimizes IP/header metadata, so emails sent from it leak little. Treat Posteo addresses as low-yield for header-based geolocation.

## Overlaps ("do both")
- Pairs with breach-search tools (`[[scatteredsecrets-com]]`) and email verifiers (`[[proofy]]`) — the address still routes to those, even if Posteo itself reveals nothing.

## Trust & verifiability
`trust: unverified` — Posteo is a legitimate, well-known provider, but it is mislisted as an OSINT tool. Rated unverified because it returns no investigative data on a subject.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | posteo-de |
| category | email |
| selectorsIn → selectorsOut | email → metadata-exif |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
