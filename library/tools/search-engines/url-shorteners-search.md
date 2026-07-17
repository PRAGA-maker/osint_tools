---
id: url-shorteners-search
name: URL Shorteners Search
description: Use when you have a `name`, keyword, or `domain` and want short-link destinations exposing it — searches billions of expanded shortener URLs (GrayHatWarfare).
url: https://shorteners.grayhatwarfare.com/
category: search-engines
path:
- search-engines
bestFor: Searching a huge index of expanded URL-shortener links to surface exposed cloud files, documents, and destinations.
selectorsIn:
- name
- domain
selectorsOut:
- domain
- document-id
status: live
pricing: freemium
costNote: Free search with limited results; premium unlocks more results, regex is Enterprise-only.
opsec: passive
opsecNote: You search GrayHatWarfare's pre-collected index, not the live short links — targets aren't notified. Passive to search. Actually opening a discovered destination connects you to that host, which logs your IP; use a VPN/sock puppet before visiting a found link.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: GrayHatWarfare is an established security-research index (also known for its open-S3-bucket search); the shortener data is scraped/enumerated and unvetted per-item.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- buckets-grayhatwarfare-com
- grayhatwarfare
- public-buckets
aliases:
- GrayHatWarfare shorteners
- shorteners.grayhatwarfare.com
tags:
- url-shortener
- exposed-files
- osint-search
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# URL Shorteners Search

> GrayHatWarfare's shortener index — search billions of expanded bit.ly-style links to find destinations people assumed were private (short links are guessable, so their targets leak).

## When to use
People shorten links to "hide" private cloud files, documents, and pages — but short codes are short and enumerable, so services like GrayHatWarfare have crawled billions of them and their destinations. Search by a `name`, keyword, filename, or `domain` to surface exposed files (cloud storage, PDFs, invites) and destinations tied to a subject or organization. A niche exposure-discovery angle (low direct MP relevance) that can surface documents nothing else reaches.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://shorteners.grayhatwarfare.com/.
2. Search by keyword/name/domain; filter by file type/extension and sort by date/size.
3. Review the expanded destination URLs — many point at cloud storage, documents, or invites.
4. Free tier caps results (regex is Enterprise-only) — use precise keywords.
5. **Before opening a destination**, switch to a VPN/sandbox — the host logs your visit and files may be malicious.
6. Pivot: exposed cloud files → content + metadata; a `domain`/bucket → `[[buckets-grayhatwarfare-com]]` for related open storage.

## Inputs → Outputs
- **In:** a `name`, keyword, or `domain`
- **Out:** expanded shortener destination URLs → exposed files (`document-id`) and hosting `domain`s
- **Empty/negative result looks like:** no matches — nothing in the indexed shortener set references your term; absence is common and not meaningful given partial coverage.

## Gotchas & OpSec
- Freemium caps free results; a sparse free result is not the full index.
- Opening a discovered link is **active** toward that host — VPN/sandbox first; treat files as potentially malicious.
- Data is enumerated/unvetted; a hit doesn't confirm ownership — corroborate before attributing to a subject.

## Overlaps ("do both")
- Pairs with `[[buckets-grayhatwarfare-com]]` — same provider's open-cloud-storage search; a shortener destination often points into a bucket you can then explore there.

## Trust & verifiability
`trust: community` — an established security-research index, but individual entries are unvetted crawl results. Each destination is verifiable by resolving it (carefully); attribution to a person needs corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | url-shorteners-search |
| category | search-engines |
| selectorsIn → selectorsOut | name, domain → domain, document-id |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
