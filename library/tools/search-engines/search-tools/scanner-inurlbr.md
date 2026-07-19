---
id: scanner-inurlbr
name: SCANNER-INURLBR
description: Use when you have a search dork or `domain` and want to mass-harvest matching URLs and exposed `email`s across many search engines from the CLI — returns `domain`s and `email`s.
url: https://github.com/googleinurl/SCANNER-INURLBR
category: search-engines
path:
- search-engines
- search-tools
bestFor: Automated multi-engine dorking from the command line to collect URLs/emails matching a pattern (advanced recon), rather than one-off manual Google queries.
selectorsIn:
- domain
- name
selectorsOut:
- domain
- email
status: live
pricing: free
costNote: Free, open-source (GPL) PHP tool on GitHub; you self-host and run it locally.
opsec: active
opsecNote: This automates high-volume queries against Google/Bing/Yandex and can validate discovered targets, which is active and easily fingerprinted — search engines will CAPTCHA/ban the source IP and touched hosts may log the visits. Run from a disposable VPS/proxy chain, throttle it, and never point it at infrastructure you are not authorised to probe.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: cli
trust: community
trustNote: Long-standing open-source project (googleinurl, ~880 stars) widely used in pentest/recon circles; unaudited PHP, so review before running and treat output as leads.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- inurlbr
- inurl scanner
tags:
- dorking
- recon
- cli
- search-tools
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# SCANNER-INURLBR

> A CLI dork engine: give it a search pattern and it harvests matching URLs and exposed emails across many search engines at once.

## When to use
You want to run search-engine dorking at scale — sweeping Google, Bing, Yandex and others for pages matching a pattern (a `domain`, a `name` used as a keyword, a filetype, an inurl string) and pulling back the matching URLs plus any `email` addresses found on them. This is the automated version of typing dozens of `site:`/`inurl:` queries by hand.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo: `git clone https://github.com/googleinurl/SCANNER-INURLBR` and ensure PHP + cURL are installed.
2. Run with a dork, e.g. `php inurlbr.php --dork 'inurl:"target-name"' -s save.txt`. Add engine flags and an output file.
3. Read the output: a list of matching URLs (`domain`s) and any harvested `email`s, written to the save file.
4. Pivot: feed harvested emails into email-OSINT (`account.live.com`, breach lookups) and URLs into archive/cache tools; corroborate every hit manually.

## Inputs → Outputs
- **In:** a search dork / `domain` / keyword (e.g. a `name`)
- **Out:** matching URLs (`domain`s) and scraped `email`s
- **Empty/negative result looks like:** zero results often means engines rate-limited or CAPTCHA-blocked the run, not that nothing exists — re-run slower from a fresh IP before concluding.

## Gotchas & OpSec
- It is an old (2014-era) PHP tool; expect to fix dependencies and adapt to current search-engine anti-bot behaviour, which frequently breaks scrapers.
- Human-in-the-loop: rate-limiting/CAPTCHA is the main friction — throttle and rotate IPs.
- OpSec: **active** and noisy. Never aim it at systems you lack authorisation to probe; use disposable infrastructure.

## Overlaps ("do both")
- Complements manual `site:`/`inurl:` dorking and curated CSEs — this automates breadth; a hand-crafted query gives precision. Feed its output into email/breach and archive tools.

## Trust & verifiability
`trust: community` — popular open-source recon tool but unaudited; review the code before running and validate every harvested selector at its source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scanner-inurlbr |
| category | search-engines |
| selectorsIn → selectorsOut | domain, name → domain, email |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (rate-limit) |
