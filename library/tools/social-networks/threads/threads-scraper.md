---
id: threads-scraper
name: Threads-Scraper
description: Use when you have a Threads profile or post URL (`social-profile`) and want its posts offline for analysis — returns post text, timestamps, and engagement as JSON/CSV/XML, surfacing `name`s and `associate`s.
url: https://github.com/Zeeshanahmad4/Threads-Scraper
category: social-networks
path:
- social-networks
- threads
bestFor: Bulk-extracting a Threads account's public posts into structured files for offline keyword/timeline analysis.
selectorsIn:
- social-profile
selectorsOut:
- associate
- name
status: degraded
pricing: free
costNote: Free open-source (Python/Playwright) tool; you run it yourself. No paid service.
opsec: active
opsecNote: It drives a real browser against Threads' public pages, generating traffic patterns Meta can rate-limit or flag. Run from a sock-puppet IP/proxy; do not point it at accounts from an attributable network. No login is used, so it stays on public data only.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: cli
trust: unverified
trustNote: A single-maintainer GitHub scraper (~120 stars); functional but brittle against Threads' changing DOM — review the code before running and expect breakage.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
aliases:
- Threads Scraper
tags:
- threads
- scraper
- social-media
source: arf-seed
lastVerified: '2026-07-14'
enrichment: full
---

# Threads-Scraper

> A local Python/Playwright scraper that pulls a Threads account's public posts into JSON/CSV/XML — for offline timeline reconstruction and keyword mining when the app's own search is too limited.

## When to use
You have a subject's Threads profile (a `social-profile`) and need their posts as data — to search across everything they've said, build a timeline, or extract mentioned people and topics — without scrolling the app. It captures visible posts, timestamps, and engagement metrics from public pages without login. Because it depends on Threads' page structure, treat it as `degraded`: verify it still runs against a test profile before relying on it.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/Zeeshanahmad4/Threads-Scraper`; install Python deps and Playwright (Docker is provided).
2. Configure target profile URL(s) in the YAML config and choose an output format (JSON/CSV/XML).
3. Run the scraper (ideally through a proxy/sock-puppet IP); it drives a headless browser over public Threads pages.
4. Review output: post text, timestamps, engagement — grep for names, places, and mentioned handles (`associate`s).
5. Pivot: mentioned handles → cross-platform username checks; timestamps/places → pattern-of-life; media → reverse-image.

## Inputs → Outputs
- **In:** `social-profile` (Threads profile or post URL)
- **Out:** structured posts (text, timestamps, engagement); extractable `name`s and `associate`s mentioned
- **Empty/negative result looks like:** zero posts or errors — usually a DOM change, rate-limiting, or a private/empty account, NOT proof the account is inactive.

## Gotchas & OpSec
- Brittle: Threads changes its markup and the scraper breaks; check for a maintained fork if it fails.
- Rate-limiting/blocking is likely at volume — throttle and proxy.
- Third-party code from a single maintainer — read it before executing, and only collect public data.

## Overlaps ("do both")
- Pairs with manual Threads review and cross-posting checks on Instagram (shared Meta account graph) — the scraper gives bulk data, manual review catches media/context it flattens.

## Trust & verifiability
`trust: unverified` — an individual's GitHub scraper; the data comes straight from public Threads pages (authentic), but the tool's reliability and safety require you to review the code and validate output.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | threads-scraper |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → associate, name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (rate-limit) |
