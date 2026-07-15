---
id: insto
name: insto
description: Use when you have an Instagram `username` and want a scripted, no-login dossier — posts, followers, geo-fingerprint and network intersections — returns social-profile, associate, geolocation and image data.
url: https://github.com/subzeroid/insto
category: social-networks
path:
- social-networks
bestFor: Command-line Instagram OSINT — building a full profile dossier, follower/network analysis and posting-pattern/geo fingerprint without logging into Instagram.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
- geolocation
- image
status: live
pricing: freemium
costNote: The tool itself is free/open-source (Python). Its default HikerAPI backend is a paid third-party Instagram API (needs an API key/credits); the alternate aiograpi backend can run against Instagram directly but then needs session credentials. So real cost/gating comes from the backend you choose.
opsec: passive
opsecNote: With the default HikerAPI backend you never touch Instagram with your own IP/account — queries go through HikerAPI, so it is effectively passive and the target isn't notified. If you switch to the aiograpi backend you use real IG session credentials — that becomes attributable and risks the account; only do so from a sock-puppet. Snapshots are stored locally in SQLite.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Open-source CLI (subzeroid/insto on GitHub); code is auditable. Data quality depends on the chosen backend (HikerAPI vs direct), and third-party IG APIs can break when Instagram changes.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- dumpor-io
- otzberg-net-find-your-instagram-user-id
aliases:
- subzeroid/insto
tags:
- instagram
source: awesome-osint
lastVerified: '2026-07-15'
enrichment: full
---

# insto

> An interactive Instagram OSINT CLI — scripts a full dossier (profile, media, followers, geo/posting fingerprint, network intersections) with pluggable backends and no interactive login.

## When to use
You have one or more Instagram `username`s and want structured, repeatable intelligence rather than manual browsing: full profile + media dump, follower/following lists, `/where` geographic fingerprinting, `/intersect` to find shared connections between accounts, `/dossier` for a packaged report, and snapshot diffs to track changes over time. Ideal when you're building a case file or monitoring an account across days.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and install: `git clone https://github.com/subzeroid/insto` and install its Python dependencies.
2. Configure a backend — HikerAPI key (default, no IG login) or aiograpi with sock-puppet session credentials.
3. Run interactively or one-shot: commands like `/info`, `/posts`, `/followers`, `/where`, `/intersect`, `/dossier`; feed multiple targets via stdin for batch mode.
4. Export results as JSON, CSV, or Maltego for graphing; media downloads land organised per user.
5. Pivot: `/intersect` shared followers → `associate` mapping; `/where` → `geolocation` leads; numeric IDs pair with `[[otzberg-net-find-your-instagram-user-id]]`.

## Inputs → Outputs
- **In:** `username` (single or batch)
- **Out:** `social-profile` data, `associate` (followers/intersections), `geolocation` fingerprint, `image`/media, snapshot diffs
- **Empty/negative result looks like:** private accounts return only public metadata; a backend/API error (rate limit, bad key) yields nothing — distinguish "private/blocked" from "no such user."

## Gotchas & OpSec
- Backend choice defines both cost and OpSec: HikerAPI = paid but detached/passive; aiograpi = free-ish but uses a real IG session (attributable, ban risk).
- Third-party IG APIs break when Instagram changes; keep the tool updated.
- OpSec: **passive** on the default backend; treat the direct-login mode as active and sock-puppet-only.

## Overlaps ("do both")
- Pair with `[[dumpor-io]]` for quick no-setup visual checks, and `[[otzberg-net-find-your-instagram-user-id]]` to anchor accounts to stable numeric IDs before batch-tracking them here.

## Trust & verifiability
`trust: community` — auditable open-source tooling. The intelligence is only as good as the backend feeding it, so corroborate key findings (especially geo inferences) against the live profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | insto |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, associate, geolocation, image |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
