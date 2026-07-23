---
id: pasta
name: Pasta
description: Use when you have a `username` (a Pastebin account) or want to sweep recent public pastes for leaked selectors — returns emails, usernames, and IPs extracted from paste text.
url: https://github.com/Kr0ff/Pasta
category: dark-web
path:
- dark-web
bestFor: Scraping a Pastebin user's pastes or the recent archive and extracting emails, usernames, and IPs.
selectorsIn:
- username
selectorsOut:
- email
- username
- ip-address
status: degraded
pricing: free
costNote: Free, open-source Python tool; no Pastebin API key or account required. Works only as well as Pastebin's anti-scraping defenses allow.
opsec: active
opsecNote: The tool fetches pages directly from Pastebin using your IP; Pastebin actively rate-limits and blocks scraping, and brute-forcing random paste IDs generates heavy, attributable traffic. Run behind a proxy/VPN, throttle requests, and expect blocks. Do not target or store others' credentials beyond what your investigation authorizes.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: Small community script (Kr0ff on GitHub); marked "academic purposes only" by the author, auditable but unmaintained-grade.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Kr0ff/Pasta
- Pastebin scraper
tags:
- pastebin
- leak-monitoring
- darknet-deepweb-search
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Pasta

> A no-API Pastebin scraper: pull a user's pastes or sweep the recent archive and auto-extract emails, usernames, and IPs from the text.

## When to use
You have a Pastebin `username` and want everything they've posted, or you want to monitor the recent public-paste archive for leaked selectors (credentials, email lists, IPs) tied to your subject. Pastes are a classic place breach data, doxes, and contact dumps surface, so a targeted or archive sweep can turn up an email/IP that connects to a person.

## How to use it (`bestInteractionPattern`: cli)
1. Clone: `git clone https://github.com/Kr0ff/Pasta` and install Python 3 requirements.
2. User scrape: point it at a Pastebin `username` to pull all their pastes across pages.
3. Archive scrape: download the most recent archive entries; optionally brute-force random 8-char IDs to discover unlisted pastes.
4. Let its detector scan the downloaded text for emails, usernames, and IPs (`selectorsOut`), saved to file; then pivot each selector into email/IP tooling.

## Inputs → Outputs
- **In:** `username` (Pastebin account) or no input for an archive/random sweep
- **Out:** `email`, `username`, `ip-address` extracted from paste bodies, plus raw paste text
- **Empty/negative result looks like:** no pastes returned or immediate HTTP blocks — often means Pastebin is rate-limiting/blocking you, NOT that the user has no pastes.

## Gotchas & OpSec
- Human-in-the-loop: none, but expect to babysit it around blocks.
- OpSec: **active** — direct fetches from your IP; random-ID brute-forcing is noisy and easily rate-limited. Proxy it and go slow.
- Pastebin has tightened anti-scraping heavily, so `status: degraded` — random-ID discovery in particular is unreliable now. Handle any recovered credentials lawfully and minimally.

## Overlaps ("do both")
- Complements paste-search aggregators (e.g. IntelligenceX / psbdmp-style paste-dump search) — those index historical pastes server-side, while Pasta scrapes live and extracts selectors locally; use aggregators first, Pasta for a specific user's live pastes.

## Trust & verifiability
`trust: unverified` — an open-source hobby script flagged "academic use only"; the code is readable but there's no institutional backing, and its reliability is at the mercy of Pastebin's defenses.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pasta |
| category | dark-web |
| selectorsIn → selectorsOut | username → email, username, ip-address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
