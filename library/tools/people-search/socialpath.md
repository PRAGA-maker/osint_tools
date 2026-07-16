---
id: socialpath
name: SocialPath
description: Use when you have a `username` and want to track its reuse across social platforms and profile it — returns matching profiles, activity, and mentioned-contact (associate) data as social-profile.
url: https://github.com/woj-ciech/socialpath
category: people-search
path:
- people-search
bestFor: De-anonymising a username by correlating its reuse across Facebook, Twitter, Instagram, Reddit, GitHub and more, with CSV output.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
status: degraded
pricing: free
costNote: Free and open-source (Python/Django). No purchase, but you must supply your own platform API credentials, which are increasingly hard to obtain.
opsec: active
opsecNote: The tool uses authenticated platform APIs/scraping with YOUR credentials, so activity is tied to those accounts — use dedicated sock-puppet API keys, never personal ones. Heavy querying can trip platform rate limits or bans. Results (and CSVs) are stored locally.
humanInLoop: true
humanInLoopReason:
- api-key
- rate-limit
bestInteractionPattern: cli
trust: community
trustNote: Open-source project by woj-ciech (a known OSINT developer). Low commit count and dependence on platform APIs mean modules break as those APIs change; inspect and test before relying.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- sherlock
- maigret
- leaklooker
aliases:
- woj-ciech/socialpath
tags:
- people-search
- open-source
- cli
- username-deanon
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# SocialPath

> An open-source username-deanonymisation tool: track a handle's reuse across major platforms and pull profile + interaction data into CSVs.

## When to use
You have a `username` and want more than "does this account exist on site X" — SocialPath collects profile details and activity across Facebook, Twitter, Instagram, Reddit, Stack Overflow, Steam, Pinterest, Tumblr, Pastebin, and GitHub, and exports structured data (CSV) you can visualise. Useful for building a picture of who a handle belongs to and who they interact with (`associate` links). Because it leans on platform APIs, expect setup friction.

## How to use it (`bestInteractionPattern`: cli)
1. `git clone https://github.com/woj-ciech/socialpath` and install Python deps + Redis.
2. Add your (sock-puppet) API credentials to the JSON config; run Django migrations.
3. Start the Django server and a Celery worker (background tasks).
4. Enter a target username; collect the generated profile data and CSVs from the per-user output directory.
5. Pivot: for pure existence-enumeration across hundreds of sites (no API keys), run `[[sherlock]]` or `[[maigret]]` alongside it.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` (profiles + activity across supported platforms), `associate` (interaction/mention links), CSV exports
- **Empty/negative result looks like:** empty CSVs or module errors — usually missing/expired API credentials or a platform that changed its API; not proof the handle is unused.

## Gotchas & OpSec
- Human-in-the-loop: **api-key** setup is mandatory, and **rate-limit**/ban risk is real under load.
- OpSec: **active** — queries run under your credentials; use dedicated sock-puppet API accounts.
- **Degraded:** platform API lockdowns (especially Twitter/Facebook) break several modules; treat as best-effort and verify which platforms still return data.

## Overlaps ("do both")
- Pairs with `[[sherlock]]` and `[[maigret]]` — those give fast, keyless breadth across hundreds of sites; SocialPath adds deeper per-platform profile/activity data where you have API access.

## Trust & verifiability
`trust: community` — a credible-author open-source tool, but unmaintained enough that modules rot with API changes. Read the code, use burner keys, and corroborate matches before attributing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | socialpath |
| category | people-search |
| selectorsIn → selectorsOut | username → social-profile, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key) |
