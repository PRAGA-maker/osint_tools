---
id: phishingseclists
name: PhishingSecLists
description: Use when you have a suspected phishing/scam `domain` and want wordlists to discover its hidden credential-capture files, admin panels, and campaign data — returns exposed paths/`document-id` leads on the malicious host.
url: https://github.com/spmedia/PhishingSecLists
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Content-discovery wordlists tuned to phishing/scam kits, for finding where a fraud site stores captured credentials and campaign artifacts.
selectorsIn:
- domain
selectorsOut:
- document-id
- domain
status: live
pricing: free
costNote: Free, open-source wordlists on GitHub (actively maintained); no cost.
opsec: active
opsecNote: Using these lists means directory-brute-forcing a live phishing host with gobuster/ffuf — that is active scanning that the operator (or their hosting/CDN) will see and can block or flag. Only do it within authorized scope, from sock-puppet infrastructure, and pace requests to avoid tipping the actor.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Maintained by spmedia, a threat-intel-focused author, with a substantial commit history; the lists are curated from real phishing-kit filenames across multiple languages.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- crypto-scam-and-crypto-phishing-url-threat-intel-feed
- telegram-channel-joiner
- threat-actor-usernames-scrape
aliases:
- spmedia PhishingSecLists
- phishing wordlists
tags:
- threat-intelligence
- content-discovery
- phishing
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# PhishingSecLists

> Content-discovery wordlists specifically tuned to phishing and crypto-scam kits — feed them to gobuster/ffuf to uncover where a fraud site hides captured credentials and campaign data.

## When to use
You are investigating a live phishing/scam `domain` and want to find its non-linked files: the folder holding stolen credentials, exposed admin panels, kit source zips, or campaign logs. Generic wordlists miss kit-specific filenames; PhishingSecLists (e.g. `Wizard.txt`, `Shells.txt`) is built from real threat-actor filename conventions across multiple languages, so it surfaces artifacts that turn a phishing page into attributable intel.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo: `git clone https://github.com/spmedia/PhishingSecLists`.
2. Point a content-discovery tool at the target host with a list, e.g. `ffuf -w PhishingSecLists/Wizard.txt -u https://phish.example/FUZZ` or the equivalent `gobuster dir -w ...`.
3. Review hits — an exposed `results.txt`/`log`/panel often contains captured victim data or reveals the kit author (`document-id`/kit artifacts).
4. Pivot: kit source or credential dumps feed victim-notification and actor-attribution; discovered admin panels/paths feed the wider infra map.

## Inputs → Outputs
- **In:** a target phishing `domain`/URL to fuzz
- **Out:** discovered hidden paths/files → `document-id` (kit/campaign artifacts), additional `domain` infrastructure
- **Empty/negative result looks like:** all requests 404 — the host is locked down, already taken down, or the kit uses non-standard paths; not proof it's benign.

## Gotchas & OpSec
- **Active scanning:** brute-forcing a live malicious host is noisy and attributable — authorized scope only, sock-puppet infra, throttled requests, and be aware the actor may be watching their own logs.
- Handle any recovered victim data lawfully — it may contain real PII/credentials; route to the proper CERT/registrar, don't hoard it.
- Lists are offensive tooling: use only against sites you're authorized to investigate.

## Overlaps ("do both")
- Pairs with `[[crypto-scam-and-crypto-phishing-url-threat-intel-feed]]` (find the phishing URLs) and `[[threat-actor-usernames-scrape]]` (attribute the operator) — this list is the content-discovery step between discovery and attribution.

## Trust & verifiability
`trust: community` — a well-maintained threat-intel author's curated lists; effective, but the value is in the wordlists, not any guarantee about what a given target exposes.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | phishingseclists |
