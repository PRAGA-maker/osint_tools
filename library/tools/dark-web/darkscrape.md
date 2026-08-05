---
id: darkscrape
name: DarkScrape
description: Use when you have a Tor `.onion` `domain` and want to harvest the images/media it hosts (with optional face recognition) — returns downloaded `image` files and `face` matches.
url: https://github.com/itsmehacker/DarkScrape
category: dark-web
path:
- dark-web
bestFor: Bulk-extracting and downloading media (images) from .onion sites, with a face-recognition option for triage.
selectorsIn:
- domain
selectorsOut:
- image
- face
status: live
pricing: free
costNote: Free and open-source (MIT); costs only your own Tor infrastructure.
opsec: active
opsecNote: It fetches and downloads content directly from the target .onion over Tor, so run it on an isolated VM through Tor only, never clearnet. Downloading dark-web media carries legal/malware risk — sandbox everything and know the legal limits in your jurisdiction before scraping.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source project (500+ GitHub stars); code is auditable, but it's a community tool — review it before running and treat downloaded content as untrusted.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- DarkScrape onion scraper
tags:
- darkweb
- scraper
- media
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# DarkScrape

> A Python CLI that pulls the media links off a Tor hidden service and downloads them — with an optional face-recognition pass to flag images of interest.

## When to use
You have a specific `.onion` `domain` (a marketplace, forum, or leak site) and need to collect the images it hosts — for evidence capture, face triage, or offline analysis — rather than clicking through manually. Useful when a missing-person or actor lead surfaces on a dark-web page full of images.

## How to use it (`bestInteractionPattern`: cli)
1. On an isolated VM with Tor running, install: `git clone https://github.com/itsmehacker/DarkScrape && cd DarkScrape && pip3 install -r requirements.txt`.
2. Run against a single site: `python3 darkscrape.py -u http://<address>.onion` (it routes over Tor).
3. Use flags for batch input (text/CSV/Excel lists of onions), media download, and the face-recognition option to surface images containing faces.
4. Review downloaded `image`/`face` results in the sandbox; pivot notable faces into reverse-image/face-search tools.

## Inputs → Outputs
- **In:** `domain` (a `.onion` URL, or a list of them)
- **Out:** `image` (downloaded media), `face` (face-recognition hits)
- **Empty/negative result looks like:** no media links found means the page has no reachable images (or is down / requires login) — not that the site is empty of intel.

## Gotchas & OpSec
- Active and risky: you are downloading from hostile infrastructure over Tor — isolate hard, scan downloads, and never run on your real host.
- Legal exposure: dark-web media can be illegal to possess; understand the boundaries before scraping.
- It grabs media, not text/structured data — pair it with an onion text scraper for full coverage.

## Overlaps ("do both")
- Pair with `[[pitch]]`-style actor tracking and reverse-image/face tools: DarkScrape collects the images, face/image search attributes them.

## Trust & verifiability
`trust: community` — a well-starred open-source scraper; inspect the code, and remember its output is raw dark-web content that must be corroborated and handled carefully.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | darkscrape |
| category | dark-web |
| selectorsIn → selectorsOut | domain → image, face |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
