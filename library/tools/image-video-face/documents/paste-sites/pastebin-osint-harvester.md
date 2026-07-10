---
id: pastebin-osint-harvester
name: Pastebin OSINT Harvester (sniff-paste)
description: Use when you want to continuously scrape Pastebin for a target's `email`, `ip-address`, `phone`, or `crypto-wallet` appearing in pastes/dumps — returns extracted identifiers linked back to source pastes.
url: https://github.com/needmorecowbell/sniff-paste
category: image-video-face
path:
- image-video-face
- documents
- paste-sites
bestFor: Automated, multithreaded Pastebin monitoring that extracts and databases emails, IPs, phones, URLs, and crypto addresses from recent pastes.
selectorsIn:
- email
- ip-address
selectorsOut:
- email
- ip-address
- phone
- crypto-wallet
status: live
pricing: free
costNote: Free and open-source (Python). Needs a local MySQL database and (for higher rates) a Pastebin Pro/scraping API subscription; the free public scrape is rate-limited.
opsec: passive
opsecNote: You scrape Pastebin's public pastes, not the target — passive toward any subject. The tool also port-scans harvested IPs, which is an ACTIVE, potentially unlawful action against third-party hosts; disable/avoid the port-scan feature unless you have authorization for those IPs.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: A community Python OSINT tool; straightforward scraping/regex extraction, but review the code and be mindful its IP port-scanning goes beyond passive collection.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- sniff-paste
- Pastebin OSINT Harvester
tags:
- pastebin
- paste-sites
- breach-monitoring
- data-harvesting
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Pastebin OSINT Harvester (sniff-paste)

> A multithreaded Python scraper that watches Pastebin, pulls out emails/IPs/phones/URLs/crypto addresses, and stores them in a searchable database — for catching a target's identifiers in dumps and leaks.

## When to use
You want to monitor Pastebin (a common dumping ground for leaks, credential dumps, and doxes) for a subject's identifiers — their `email`, `ip-address`, `phone`, or `crypto-wallet` — as those artefacts often surface in pastes tied to breaches. Run it to continuously harvest and index pastes, then query the database for your target's selectors.

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/needmorecowbell/sniff-paste and set up its MySQL database + Python deps.
2. (Optional) add a Pastebin scraping API key to raise rate limits.
3. Run `python3 sniff-paste.py` to scrape N pastes or run continuously (Ctrl+C to stop).
4. It parses each paste, extracts emails/IPs/phones/URLs/crypto/secrets, dedupes, and writes to the DB with links back to the source paste.
5. Query the DB for your target's selectors; open the source pastes for context. **Skip/disable the IP port-scan feature** unless authorized.

## Inputs → Outputs
- **In:** target selectors to search the harvested corpus for (`email`, `ip-address`, `phone`, `crypto-wallet`), plus a running scrape
- **Out:** extracted `email`, `ip-address`, `phone`, `crypto-wallet`, URLs, and "secrets" with links to the source pastes
- **Empty/negative result looks like:** the corpus has no hit for your selector — meaning it hasn't appeared in the pastes scraped so far (coverage is forward-looking from when you start). Absence isn't proof; combine with breach-search tools for historical data.

## Gotchas & OpSec
- Only sees pastes scraped while running — it's a going-forward monitor, not a historical archive.
- **Port-scanning harvested IPs is active and possibly illegal** — leave it off unless you own/are authorized for those hosts.
- Pastebin rate-limits the free scrape; a Pro/scraping key helps.

## Overlaps ("do both")
- Pairs with breach/leak search engines (Intelligence X, HIBP, Dehashed) — those cover historical dumps, sniff-paste catches new pastes in near-real-time; together they span past and future.

## Trust & verifiability
`trust: community` — an open-source scraper; its extractions are only as good as its regexes, so verify each hit against the actual paste and treat identifier co-occurrence as a lead, not proof of linkage.
