---
id: collector
name: collector
description: Use when you have a `phone`, `ip-address`, or `username` (GitHub/Instagram) and want a quick one-command enrichment — returns carrier/geo for numbers, profile/repo data for GitHub, geolocation for IPs, and Instagram profile info.
url: https://github.com/galihap76/collector
category: phone
path:
- phone
bestFor: A single Python CLI that fans one selector (phone, IP, GitHub, or Instagram handle) into basic profile/metadata.
selectorsIn:
- phone
- ip-address
- username
selectorsOut:
- geolocation
- social-profile
- name
status: degraded
pricing: free
costNote: Free and open-source (GPLv3). No API key. Archived by the author since April 2023 — dependencies and Instagram/GitHub scraping paths may be stale.
opsec: passive
opsecNote: Phone and IP lookups are passive metadata queries and do not touch the target. The Instagram module actively scrapes and can get your IP/account rate-limited or blocked, per the author's own warning — run it from a sock-puppet context and expect breakage. It cannot geolocate a live person's exact position.
humanInLoop: false
humanInLoopReason:
- rate-limit
bestInteractionPattern: cli
trust: community
trustNote: Single-author open-source project, now archived/unmaintained. Code is inspectable; results are only as good as the free libraries and endpoints it wraps.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- phoneinfoga
- sherlock
aliases:
- galihap76/collector
tags:
- phone
- multi-selector
- cli
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# collector

> An archived Python CLI that enriches a single selector — phone number, IP, GitHub handle, or Instagram handle — into basic metadata and profile data.

## When to use
You want a fast, offline-installable one-liner to get baseline metadata on one of four selector types: a `phone` (country, region, carrier, timezone), an `ip-address` (geolocation and network details), a GitHub `username` (profile, repos, followers), or an Instagram `username` (followers, posts, bio, media). Handy as a quick triage before reaching for specialised tools — but it is unmaintained, so treat it as best-effort.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `git clone https://github.com/galihap76/collector.git && cd collector && pip install -r requirements.txt`.
2. Run one of:
   - Phone: `python3 main.py -n <phone number>`
   - IP: `python3 main.py -i <ip address>`
   - GitHub: `python3 main.py -g <username>`
   - Instagram: `python3 main.py -ig <username>`
3. Read the printed metadata for that selector.
4. Pivot: hand a phone result to `[[phoneinfoga]]` for deeper carrier/format work, and a username to `[[sherlock]]` to spread it across many sites.

## Inputs → Outputs
- **In:** `phone` / `ip-address` / GitHub or Instagram `username`
- **Out:** `geolocation` (IP/phone region), `social-profile` (GitHub/Instagram profile), `name` (where a handle exposes one)
- **Empty/negative result looks like:** a traceback or empty fields — an archived dependency broke or the scraped endpoint changed; the target isn't necessarily absent.

## Gotchas & OpSec
- Human-in-the-loop: **rate-limit** — the Instagram path throttles and can block your IP/account; the author warns against heavy use.
- OpSec: phone/IP lookups are **passive**; the Instagram scrape is not — sock-puppet it.
- **Degraded/archived** since 2023: expect dependency rot; pin an older Python/library set or prefer maintained alternatives if it fails.
- It explicitly cannot track a person or resolve an accurate public IP — don't over-read the geolocation.

## Overlaps ("do both")
- Pairs with `[[phoneinfoga]]` (far deeper phone footprinting) and `[[sherlock]]` (username across hundreds of sites) — collector is the quick generalist; those are the specialists you escalate to.

## Trust & verifiability
`trust: community` — an unmaintained single-author wrapper around free libraries. Verify anything it returns against a current, maintained tool before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | collector |
| category | phone |
| selectorsIn → selectorsOut | phone, ip-address, username → geolocation, social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
