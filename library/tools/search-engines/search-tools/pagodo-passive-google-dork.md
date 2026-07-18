---
id: pagodo-passive-google-dork
name: pagodo - Passive Google Dork
description: Use when you have a `domain` and want to automate Google Hacking Database dorks against it — returns exposed/sensitive URLs (`document-id`s) matching known dork patterns.
url: https://github.com/opsdisk/pagodo
category: search-engines
path:
- search-engines
- search-tools
bestFor: Automating GHDB Google dorks against a target domain to surface exposed files, panels, and sensitive pages.
selectorsIn:
- domain
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free, open-source (GPL-3.0) Python tool; no paid account. Google may rate-limit/CAPTCHA heavy use, so pacing and proxies matter.
opsec: passive
opsecNote: pagodo issues Google searches; it does not connect to the target's server, so the target sees nothing. But Google sees YOUR queries — hammering it triggers CAPTCHAs and can burn your IP. Use the built-in delays (-i/-x) and a proxy (-p), and run from a sock-puppet/VPN.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: cli
trust: community
trustNote: Mature, well-starred open-source project (opsdisk); results depend on Google's live index and the current GHDB, both of which change.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- metagoofil
- yagooglesearch
aliases:
- pagodo
- opsdisk/pagodo
tags:
- google-dork
- ghdb
- recon
- passive
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# pagodo - Passive Google Dork

> Automates the Google Hacking Database against a domain: instead of pasting dorks by hand, it runs hundreds and returns the exposed URLs Google already knows about — without ever touching the target.

## When to use
You have a `domain` (a subject's site, an organisation) and want to know what sensitive material is publicly indexed: exposed documents, directory listings, login panels, config/backup files, leaked emails. pagodo pulls the latest GHDB dorks and runs them for you, turning manual dorking into a repeatable sweep. "Passive" is the point — findings come from Google's index, so the target's server logs nothing.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and install: `git clone https://github.com/opsdisk/pagodo.git && pip install -r requirements.txt`.
2. Refresh dorks: `python3 ghdb_scraper.py -j -s` (pulls current GHDB categories into files).
3. Run against a target: `python3 pagodo.py -d example.com -g dorks.txt -o results.json`.
4. Pace it: use `-i`/`-x` (min/max delay) and `-p` (proxy) to avoid Google CAPTCHAs; `-m` caps results per dork.
5. Read `results.json`: URLs grouped by dork. Triage anything exposing files, credentials, PII, or admin surfaces.
6. Pivot: a leaked document feeds metadata extraction; an exposed profile/URL feeds people/username OSINT.

## Inputs → Outputs
- **In:** `domain` (target) + a GHDB dork file
- **Out:** JSON of matching URLs (`document-id`s) per dork, with timestamps
- **Empty/negative result looks like:** few/no hits — either the domain genuinely exposes little, or Google throttled you mid-run (watch for CAPTCHA pages in output). Re-run slower before concluding "nothing there".

## Gotchas & OpSec
- Human-in-the-loop: **CAPTCHA** is the recurring blocker — Google detects automated dorking fast. Slow down, proxy, and be ready to solve challenges or rotate.
- Findings reflect Google's index, not the live site; a page could be de-indexed yet still exist (or vice-versa).
- OpSec: passive toward the target, but noisy toward Google — protect your own IP/identity, not the target's.
- Only dork domains you're authorised to assess; automated dorking at scale can violate Google's terms.

## Overlaps ("do both")
- Pairs with [[metagoofil]] (harvest and metadata-scrape the documents dorking finds) and [[yagooglesearch]] (the search backend); pagodo finds the exposed URLs, metagoofil mines what's inside them.

## Trust & verifiability
`trust: community` — a mature, widely-used open-source tool; reliable as a harness, but every result is a live-Google artifact that you should open and verify (and that may vanish on the next re-index).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pagodo-passive-google-dork |
| category | search-engines |
| selectorsIn → selectorsOut | domain → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (captcha) |
