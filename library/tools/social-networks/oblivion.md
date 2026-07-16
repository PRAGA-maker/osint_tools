---
id: oblivion
name: Oblivion
description: Use when you have an `email`, `username` or `domain` and want to monitor and aggregate credential-leak exposure across breach sources — returns breach hits and exposed credentials.
url: https://github.com/loseys/Oblivion
category: social-networks
path:
- social-networks
bestFor: Self-hosted, real-time monitoring and one-off scanning of an identifier against multiple breach/leak feeds with exportable reports.
selectorsIn:
- email
- username
- domain
selectorsOut:
- email
- metadata-exif
- social-profile
status: degraded
pricing: freemium
costNote: Free and open-source, but its power depends on third-party API keys (HaveIBeenPwned, IntelX, Scylla, CIRCL) — several of which are now paid — so meaningful results often require paid keys.
opsec: passive
opsecNote: Queries go to breach-database APIs, not to the target, so the subject is not alerted. Your API keys and query patterns are visible to those providers; run from an attributable-safe environment and store exported results (which contain plaintext credentials) encrypted.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Community project by loseys; the repository was archived (read-only) on 12 Dec 2025, so it is no longer maintained and API integrations may break as upstream services change.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
relatedTools:
- gosearch
- goblyn
aliases:
- loseys/Oblivion
tags:
- data-leak
- breach-monitoring
- credentials
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Oblivion

> A self-hosted breach-monitoring aggregator: point it at an email/username/domain and it fans the query across HaveIBeenPwned, IntelX, Scylla, CIRCL and Pastebin, then reports and (optionally) watches for new leaks.

## When to use
You have an `email`, `username` or `domain` and want a single tool that both does a one-shot breach lookup and can keep monitoring for *new* exposures (with alerts via Telegram/email). It fits when you are willing to self-host and supply API keys; for a quick single check, a hosted breach-search site is faster. Because it centres on leaked credentials, its missing-persons value is indirect — confirming an address is real/active and surfacing old aliases/usernames from breach records.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the (now archived) repo: `git clone https://github.com/loseys/Oblivion`; it needs Python 3.8 and runs a server (API) plus an optional graphical client on Windows/Linux.
2. Add API keys for the sources you have (HIBP, IntelX, Scylla, CIRCL) in the config — coverage is proportional to the keys you supply.
3. Run a scan against the target identifier; choose one-off or scheduled/looped monitoring.
4. Export results to `txt/json/xlsx/pdf/html/xml/db` (optionally encrypted) or ship them to S3/Drive/SSH/Telegram/email.
5. Pivot: any newly surfaced `username`/`email` from breach records feeds username enumeration and email tooling.

## Inputs → Outputs
- **In:** `email`, `username`, or `domain`
- **Out:** breach hits, exposed `email`/alias records, and `metadata-exif`-style breach context (which dump, when); some records reveal linked `social-profile` handles
- **Empty/negative result looks like:** no breach matches (address may be clean *or* your API keys don't cover the relevant dumps) — a null result with weak keys is not proof of no exposure.

## Gotchas & OpSec
- Human-in-the-loop: you must obtain and configure API keys; several sources (IntelX, HIBP) are paid, so a keyless run is nearly useless.
- Maintenance: **archived Dec 2025** — expect broken integrations over time and no fixes; verify each source still responds.
- OpSec: passive toward the target, but exported files hold plaintext credentials — encrypt at rest and handle lawfully.

## Overlaps ("do both")
- Pairs with `[[gosearch]]` and dedicated hosted breach-search sites — Oblivion aggregates and *monitors*, while a hosted lookup gives a faster one-shot answer; use both to cross-check coverage gaps.

## Trust & verifiability
`trust: community` — open-source but unmaintained since archival; the underlying data is only as good as the third-party feeds, so corroborate any single breach hit against the original source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | oblivion |
| category | social-networks |
| selectorsIn → selectorsOut | email, username, domain → email, metadata-exif, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
</content>
