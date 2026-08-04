---
id: lookyloo
name: Lookyloo
description: Use when you have a `domain` (or suspicious URL) and want to see the full tree of hosts, redirects and third-party resources a page pulls in — returns linked `domain`s and `ip-address`es without visiting the site yourself.
url: https://lookyloo.circl.lu/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Safely capturing a suspicious URL and mapping every domain/redirect/resource it calls.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free public instance run by CIRCL (Luxembourg CERT); open-source and self-hostable if you want a private instance.
opsec: passive
opsecNote: You never load the target site from your own browser — Lookyloo's server does the capture, so your IP is not exposed to the target. Public captures are indexed and browsable by anyone unless you mark the capture unlisted; treat every submission as potentially public and never paste an authenticated or session-bearing URL.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built and operated by CIRCL, the Luxembourg national CERT; widely used in phishing/malware triage and referenced across the DFIR community.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- bgp-malicious-content-ranking
aliases:
- lookyloo.circl.lu
- CIRCL Lookyloo
tags:
- Domain/IP/Links
- Website analyze
- phishing-triage
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Lookyloo

> A CIRCL-run web-forensics sandbox: submit a URL and it captures the page server-side, then draws the tree of every domain, redirect and resource it loads.

## When to use
You have a `domain` or a suspicious/shortened URL (from a phishing message, a scam profile, a tracking link) and want to know where it really goes and what it pulls in — without opening it on your own machine. The capture reveals redirect chains, ad/tracker networks, embedded frames and the hosting infrastructure, which can tie a page to other domains or an operator's stack.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://lookyloo.circl.lu/ and paste the target URL into the capture box.
2. Optionally expand settings to set a user agent, viewport, timezone or proxy location (useful when a page cloaks based on geography or device).
3. Submit and wait for the capture to render; you'll get a screenshot plus an interactive tree of hostnames calling one another (redirects, JS, CSS, fonts, images).
4. Read the tree: click nodes to see the domains and `ip-address`es involved, download the HAR for full HTTP detail, and note any redirect that lands on a different host.
5. Pivot: feed newly surfaced domains/IPs into passive DNS or WHOIS tooling, or into `[[bgp-malicious-content-ranking]]` to gauge whether the hosting AS is known-bad.

## Inputs → Outputs
- **In:** `domain` / URL (optionally an `ip-address`-hosted URL)
- **Out:** linked `domain`s, `ip-address`es, redirect chain, screenshot, HAR
- **Empty/negative result looks like:** a capture that resolves to a single node with no third-party calls (a static, isolated page) — or a timeout/error if the site blocks headless capture; that's inconclusive, not proof the site is clean.

## Gotchas & OpSec
- Human-in-the-loop: none for a basic capture; it runs automatically server-side.
- OpSec: **passive** for you — the CIRCL server fetches the page, so the target sees CIRCL's infrastructure, not your IP. But public captures are searchable; mark sensitive submissions unlisted, and never submit URLs that carry your own session token or a one-time link tied to your identity.
- Sites that cloak on user agent or geo may render differently than a normal visitor sees; adjust capture settings before drawing conclusions.

## Overlaps ("do both")
- Pairs with `[[bgp-malicious-content-ranking]]` — Lookyloo surfaces the domains/IPs a page touches; the BGP ranking tells you whether the hosting network is reputationally dirty.

## Trust & verifiability
`trust: trusted` — operated by CIRCL (Luxembourg's national CERT), open-source, and a standard tool in phishing and malware investigations; the capture is a faithful server-side render, not a scraped guess.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lookyloo |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
