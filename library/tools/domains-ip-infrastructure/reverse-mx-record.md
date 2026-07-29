---
id: reverse-mx-record
name: Reverse MX Record (osint.sh)
description: Use when you have a mail-server hostname (MX) and want the other domains that use it for email — returns a list of `domain`s sharing that mail infrastructure.
url: https://osint.sh/reversemx/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Finding all domains that route mail through a given MX host — useful for clustering domains behind a shared or self-hosted mail server.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free web tool in the osint.sh suite; no account. Rate-limited on the free front-end.
opsec: passive
opsecNote: The lookup runs against osint.sh's dataset of DNS/MX records, not the target's servers, so you never touch the subject's mail infrastructure. You do disclose the queried MX host to osint.sh.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-run osint.sh toolkit; convenient and free, but a third-party dataset snapshot — corroborate hits against live DNS before relying on them.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- reverse-domain
- osint-sh
- crt-sh
aliases:
- osint.sh reverse mx
- reverse mx lookup
tags:
- reverse-mx
- mail-infrastructure
- domain-footprint
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Reverse MX Record (osint.sh)

> An osint.sh lookup that inverts MX records: give it a mail-server hostname and get back every domain that uses it for email.

## When to use
You've found the MX (mail exchanger) host a subject's domain uses — especially a self-hosted or niche mail server rather than a giant provider — and you want the *other* domains pointing their mail at that same host. Domains sharing an unusual MX often belong to the same operator, organisation, or hosting setup, so this expands one lead into a cluster.

## How to use it (`bestInteractionPattern`: web-manual)
1. First find the target domain's MX host (via a DNS lookup / `dig MX example.com`).
2. Open https://osint.sh/reversemx/ and enter that MX hostname.
3. Submit and read the list of domains whose mail routes through it.
4. Triage by specificity: a shared MX from Google/Microsoft/a big host is meaningless (millions use it); a self-hosted or boutique MX is a strong "same operator" signal.
5. Pivot: run related domains through `[[reverse-domain]]` (co-hosted web) and `[[crt-sh]]` (certs/subdomains), then WHOIS for registrant ties.

## Inputs → Outputs
- **In:** `domain` — a mail-server (MX) hostname.
- **Out:** `domain` list — domains using that MX for email.
- **Empty/negative result looks like:** no domains returned — the MX is unique/unindexed, or the query wasn't the actual MX host. For big providers, a huge undifferentiated list is effectively "no signal."

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — you query osint.sh's data, never the target's mail server.
- Provider noise: shared MX hosts (Google Workspace, Outlook, etc.) return meaningless mass results — only self-hosted/niche MX hosts give useful clustering.
- Third-party snapshot: data can be stale or partial; confirm any relationship against live DNS.

## Overlaps ("do both")
- Pairs with `[[reverse-domain]]` — that clusters by web hosting/registrant while this clusters by mail infrastructure; run both to find domains one method misses.
- Feeds `[[crt-sh]]` for certificate-based expansion of the same footprint.

## Trust & verifiability
`trust: community` — a free community toolkit over third-party DNS data. Treat results as leads and verify with a live MX/DNS query before asserting a link.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reverse-mx-record |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
