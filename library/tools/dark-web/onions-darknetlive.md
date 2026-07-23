---
id: onions-darknetlive
name: Onions - Darknetlive
description: Use when you need current, curated `.onion` addresses for darknet markets and forums — returns verified onion `domain` links to reach dark-web venues from the clearnet.
url: https://darknetlive.com/onions/
category: dark-web
path:
- dark-web
bestFor: Getting a curated, uptime-checked directory of active darknet-market and forum .onion links from the clearnet before entering Tor.
selectorsIn:
- domain
selectorsOut:
- domain
- social-profile
status: live
pricing: free
costNote: Free clearnet directory; no account required to browse the onion listings.
opsec: active
opsecNote: Browsing the clearnet directory is low-risk, but it exists to send you into darknet markets. The moment you follow a link into Tor you are in a hostile, monitored, phishing-heavy environment — use a hardened Tor Browser on an isolated VM, never your real identity, and be aware many mirror links are scams or law-enforcement honeypots.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: Darknetlive is a well-known darknet news/directory site; its link lists are community-curated and uptime-checked but not guaranteed — phishing mirrors are a constant risk, so verify addresses against multiple sources.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- darknet-market-list
- darkweb-forums
aliases:
- Darknetlive Onions
- darknetlive.com/onions
tags:
- dark-web
- onion-directory
- darknet-markets
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Onions - Darknetlive

> The onion index of Darknetlive: a clearnet-accessible, uptime-checked list of current darknet-market and forum `.onion` addresses.

## When to use
An investigation has led you toward the dark web — a subject named a market, a leaked dataset points to a forum, or you're mapping where stolen data or a missing person's traffickers might operate — and you need **current, non-phished** entry points. Market onion addresses rotate constantly as sites are seized or migrate; Darknetlive maintains a curated list with uptime status so you start from a vetted address rather than a search-engine scam mirror.

## How to use it (`bestInteractionPattern`: web-manual)
1. From the clearnet, open https://darknetlive.com/onions/ to browse the directory (categorised by markets, forums, services).
2. Note the listed `.onion` `domain` and its uptime/status indicator; cross-check the same market's address against a second independent directory before trusting it.
3. When ready to visit, switch to a **hardened Tor Browser on an isolated VM** under a sock-puppet identity and paste the verified onion address — never navigate from your normal machine.
4. Treat everything inside as hostile: markets and forums are rife with phishing clones, scams, and monitored honeypots. Capture what you need (usernames, vendor handles → `social-profile`, wallet addresses) and leave.

## Inputs → Outputs
- **In:** a target venue name or category (`domain` you're trying to reach)
- **Out:** verified `.onion` `domain` links; downstream, vendor/forum `social-profile` handles once inside
- **Empty/negative result looks like:** a market listed as "down"/"scam" or absent — the venue is seized, offline, or was never indexed; do not trust a random mirror to fill the gap.

## Gotchas & OpSec
- **Phishing is the default threat:** attackers clone market addresses to steal logins and coins. A directory listing lowers but does not eliminate this — verify across sources.
- Uptime flags lag reality; a "live" market may have exit-scammed hours ago.
- Following these links is **active** and legally sensitive; do it only under authorization and proper isolation. Merely reading the clearnet directory is passive.
- Assume every darknet venue is monitored by law enforcement and adversaries alike.

## Overlaps ("do both")
- Pairs with [[darknet-market-list]] and [[darkweb-forums]] — cross-referencing multiple curated directories is the standard defense against phishing mirrors, since a legitimate address appears consistently across all of them.

## Trust & verifiability
`trust: community` — Darknetlive is a reputable darknet-news source and its lists are actively maintained, but link accuracy is best-effort; independently corroborate any onion address before you connect.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | onions-darknetlive |
| category | dark-web |
| selectorsIn → selectorsOut | domain → domain, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (manual-review) |
