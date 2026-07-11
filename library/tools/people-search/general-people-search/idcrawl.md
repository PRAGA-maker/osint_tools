---
id: idcrawl
name: IDCrawl
description: Use when you have a `name`, `username`, `phone`, or `email` and want a fast, free aggregate of the person's social profiles and public-records footprint — returns social-profile, name, phone, address, associate.
url: https://www.idcrawl.com/
category: people-search
path:
- people-search
- general-people-search
bestFor: One-shot free aggregation of social profiles + US public records from a name, username, phone, or email.
selectorsIn:
- name
- username
- phone
- email
selectorsOut:
- social-profile
- name
- phone
- address
- associate
status: live
pricing: free
costNote: 100% free, no signup. Monetised by ads and by upsell links to paid background-report brokers; the core aggregation and social links are free.
opsec: passive
opsecNote: Third-party aggregator — querying it does not touch the target or alert them. Your own IP hits IDCrawl (Cloudflare-fronted); run from a VPN/sock-puppet if you don't want the lookup tied to you. Do not follow the paid "background report" upsells with real identifiers.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: Independent commercial aggregator, not an authoritative record source; results are scraped/indexed and can be stale or conflate same-name people. Corroborate every hit.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- cyberbackgroundchecks
- usersherlock-com
aliases:
- IDCrawl
- idcrawl.com
tags:
- people-search
- social-media-aggregator
- us-records
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# IDCrawl

> A free people-search aggregator that fans one identifier out into social profiles and a US public-records footprint in a single query.

## When to use
You have a starting `name` (optionally with a US state), a `username`, a `phone`, or an `email`, and you want a quick, free first pass that pulls together the person's social-media presence (Facebook, Instagram, X/Twitter, LinkedIn, YouTube, TikTok) and any indexed public-records/contact hits. It is a good early breadth tool before you commit to slower, deeper record sources.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.idcrawl.com/ in a clean/sock-puppet browser.
2. Pick the search type tab — Name, Username, Phone, or Email — and enter your `selectorsIn`. For a name, narrow with the state dropdown to cut down on same-name collisions.
3. Submit. If a Cloudflare/captcha challenge appears, solve it manually.
4. Read the results:
   - **Social section:** grouped candidate profiles per platform — these are the highest-value pivots.
   - **Public-records/contact section:** possible addresses, phones, and relatives/associates (often partly gated behind broker upsells).
5. Pivot: confirmed usernames feed `[[usersherlock-com]]` and other username sweeps; addresses/relatives feed `[[cyberbackgroundchecks]]`; each social profile feeds platform-specific enrichment.

## Inputs → Outputs
- **In:** `name`, `username`, `phone`, or `email`
- **Out:** `social-profile`, `name`, `phone`, `address`, `associate`
- **Empty/negative result looks like:** no social cards and a page that immediately pushes a paid "background report" with no free detail — treat as no free signal, not as proof the person has no footprint.

## Gotchas & OpSec
- Human-in-the-loop: expect an occasional Cloudflare interstitial or captcha; solve manually.
- Aggregators conflate people who share a name — verify each hit against a second identifier before trusting it.
- Do not click through the paid broker upsells with the target's real data; that hands identifiers to a third-party commercial data seller.
- Passive toward the target: the person is not notified. Only your IP is exposed to IDCrawl.

## Overlaps ("do both")
- Pairs with `[[cyberbackgroundchecks]]` — IDCrawl is stronger on social profiles, CyberBackgroundChecks is stronger on US addresses/phones/relatives.
- Pairs with `[[usersherlock-com]]` — feed any username IDCrawl surfaces into a dedicated cross-site username sweep.

## Trust & verifiability
`trust: community` — a popular, long-running commercial aggregator, but not an authoritative source. It indexes and scrapes, so entries can be outdated or mismatched; always corroborate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | idcrawl |
| category | people-search |
| selectorsIn → selectorsOut | name, username, phone, email → social-profile, name, phone, address, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
