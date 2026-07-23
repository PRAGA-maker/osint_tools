---
id: https-openphish-com-feed-txt
name: OpenPhish Community Feed
description: Use when you have a `domain`/URL and want to check whether it is a known phishing site — returns a live list of confirmed phishing URLs.
url: https://openphish.com/feed.txt
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- phishing
bestFor: Checking a URL/domain against a live public feed of confirmed phishing sites.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: The community feed (feed.txt) is free and public — a plain-text list refreshed regularly. Higher-frequency/enriched feeds are a paid commercial product.
opsec: passive
opsecNote: You download a static text list from OpenPhish and grep it locally, so you never touch the phishing site itself. Only OpenPhish sees your fetch of the feed. Do NOT visit the listed URLs directly to "check" them — they are live malicious pages.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: OpenPhish is a well-established, widely consumed phishing-intelligence source. The free community feed is a delayed/subset view of their commercial data, so absence from it is not proof a URL is safe.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- OpenPhish feed
- openphish.com/feed.txt
tags:
- phishing
- threat-intel
- blocklist
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# OpenPhish Community Feed

> A free, regularly refreshed plain-text list of confirmed phishing URLs — fetch it and check whether a domain/URL in your case is a known phishing site.

## When to use
You have a `domain` or URL (from a message, a lure, a suspicious link a subject sent or received) and want a fast, authoritative check: is this a *known* phishing page? The feed is also useful in bulk — cross-reference a set of collected URLs against it to flag the malicious ones before you touch any of them.

## How to use it (`bestInteractionPattern`: cli)
1. Fetch the feed non-interactively: `curl -s https://openphish.com/feed.txt -o openphish.txt` (a newline-separated list of phishing URLs).
2. Search it for your target: `grep -iF 'suspicious-domain.com' openphish.txt`.
3. A match means OpenPhish has confirmed that URL as phishing; note the exact listed URL and the time you fetched (the feed rotates).
4. **Do not open the listed URLs** to verify — they are live malicious pages. If you must inspect one, use a sandbox / URL scanner, not your real browser.
5. Pivot: a confirmed phishing domain feeds WHOIS/hosting lookups and infrastructure clustering to find sibling kits.

## Inputs → Outputs
- **In:** `domain` / URL to check (or a batch of them)
- **Out:** membership in the confirmed-phishing list (the exact malicious `domain`/URL)
- **Empty/negative result looks like:** no match — meaning it isn't in the *free community* feed at this moment, NOT that the URL is safe. New or paid-tier-only phishing won't appear here.

## Gotchas & OpSec
- The community feed is a delayed subset of OpenPhish's full commercial data; a clean result is weak evidence of safety.
- The feed is a rolling snapshot — entries age out. Re-fetch for current data; record your fetch time.
- OpSec: **passive** — you only download a text file. The danger is operator error: never browse to a listed phishing URL from a real identity/host.

## Overlaps ("do both")
- Complements URL scanners and other blocklists (PhishTank, urlscan) — cross-check across feeds, since each catches phishing the others miss.

## Trust & verifiability
`trust: trusted` — OpenPhish is a respected phishing-intel provider. A positive match is high-confidence; a negative is not clearance. Corroborate with a second feed/scanner for anything important.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | https-openphish-com-feed-txt |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
