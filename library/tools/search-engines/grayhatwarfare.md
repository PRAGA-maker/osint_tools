---
id: grayhatwarfare
name: GrayhatWarfare
description: Use when you have a `name`, `email`, or `domain` and want to find files a target accidentally exposed in misconfigured public cloud buckets or shortened URLs — returns `document-id`, `image`, `domain` leads.
url: https://grayhatwarfare.com/
category: search-engines
path:
- search-engines
bestFor: Searching the world's misconfigured/open cloud buckets and public link-shortener URLs for a target's leaked files.
selectorsIn:
- name
- email
- domain
selectorsOut:
- document-id
- image
- domain
status: live
pricing: freemium
costNote: Free account gives limited keyword searches and a capped number of results per query; deeper filters, larger result pages, and API access require a paid subscription.
opsec: passive
opsecNote: You query GrayhatWarfare's own pre-built index, not the target's infrastructure, so the search itself is passive. However, if you then open or download a discovered file you are hitting the origin bucket directly — do that from a sock-puppet IP, and never modify or exfiltrate at scale (that crosses into active/abusive territory).
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running security-research project widely cited in the infosec community; the index is real but only covers buckets/shorteners it has crawled, so absence is never proof of nothing exposed.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- buckets-grayhatwarfare-com
- public-buckets
- url-shorteners-search
aliases:
- grayhat warfare
- buckets.grayhatwarfare.com
tags:
- speciality-search-engines
- cloud-buckets
- leaked-files
source: awesome-osint
lastVerified: '2026-07-21'
enrichment: full
---

# GrayhatWarfare

> A search engine over the internet's open/misconfigured cloud buckets and public link-shortener URLs — a way to find files a person or org exposed without meaning to.

## When to use
You have a `name`, `email`, `domain`, or project keyword tied to the subject and want to check whether documents, photos, backups, or credentials belonging to them are sitting in a publicly readable Amazon S3 (or similar) bucket, or behind a shortened link that leaked. Useful when a person's or small business's files (invoices, ID scans, photos, address books) end up in an unsecured bucket — those can carry `address`, `image`, or `document-id` leads a normal people-search would never surface.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://grayhatwarfare.com/ (bucket search) — the shorteners engine is at `shorteners.grayhatwarfare.com`.
2. Enter a keyword: the subject's surname, username, company name, email local-part, or a project code. You can filter by file extension (e.g. `.pdf`, `.jpg`, `.xlsx`, `.sql`).
3. Register a free account when prompted — anonymous searching is capped at a small number of results per query; the free login raises that limit.
4. Read the results: each hit is a file path inside a public bucket. Filenames and folder structure alone are leads (they often embed a person's name, a client name, or a date).
5. Pivot: open a promising file **from a sock-puppet IP** to read its metadata/content, then feed any embedded `image` into face/EXIF tools and any `document-id`/`address` into records tools.

## Inputs → Outputs
- **In:** `name`, `email`, `domain`, or arbitrary keyword (plus optional file-extension filter)
- **Out:** file paths in public buckets, downloadable files, shortened-URL destinations → `document-id`, `image`, `domain`
- **Empty/negative result looks like:** zero matching files for the keyword. This only means GrayhatWarfare hasn't indexed an exposed file matching that term — it is NOT evidence the subject has nothing exposed elsewhere.

## Gotchas & OpSec
- Human-in-the-loop: a free account is needed to see beyond the first few results, and heavy querying is rate-limited; deep filtering/API is paid.
- OpSec: the index search is passive, but **downloading** a discovered file touches the origin server — use a sock puppet and stay read-only. Treat any credentials/PII you find as sensitive; do not test found credentials.
- Coverage is opportunistic — it reflects what the crawler found, heavily skewed toward Amazon S3 and common shorteners.

## Overlaps ("do both")
- Pairs with `[[buckets-grayhatwarfare-com]]` and `[[public-buckets]]` — same provider/adjacent bucket engines; run them together since indexes and crawl timing differ.
- Pairs with `[[url-shorteners-search]]` for the link-shortener side of the same exposure problem.

## Trust & verifiability
`trust: community` — an established, community-trusted security-research service. Findings are real files, but coverage is partial and time-lagged, so a hit is strong evidence and a miss is weak evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | grayhatwarfare |
| category | search-engines |
| selectorsIn → selectorsOut | name, email, domain → document-id, image, domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
