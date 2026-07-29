---
id: osint-me-1
name: osint.me Dark Web Links (2023)
description: Use when you have a `username`/`email` and want a vetted starting list of Tor onion indexers, leak archives, and dark-web news to search for a subject — returns dark-web `social-profile` leads.
url: https://www.osintme.com/index.php/2023/06/30/darkweb-osint-links-and-new-2023-resources/
category: dark-web
path:
- dark-web
bestFor: A curated jump-off list of onion search engines, leak sites, and dark-web news for investigating a target on Tor.
selectorsIn:
- username
- email
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free blog article; the linked onion services are themselves free but require Tor.
opsec: active
opsecNote: Reading the osintme.com article is passive, but following its links means browsing .onion sites — do that only through the Tor Browser on a sock-puppet/isolated setup (ideally Tails/Whonix). The author explicitly warns the listed indexers are unvetted bot-collected links that may point to illegal content; do not click blindly.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: Maintained by Matt at osintme.com, an established OSINT practitioner/blogger; it is a hand-picked link roundup, not an automated tool, so link freshness decays over time.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- osint-list-of-public-sex-offenders-registers-osintme-com
- osint-me-2
- osint-me-3
- osintme-com
aliases:
- osintme darkweb links
- Dark Web OSINT Links 2023
tags:
- darkweb
- Dark Web Links
- link-directory
source: uk-osint
lastVerified: '2026-07-29'
enrichment: full
---

# osint.me Dark Web Links (2023)

> A practitioner-curated roundup of Tor onion indexers, leak archives, and dark-web news — the reading list to consult before you start hunting a subject on the dark web.

## When to use
You need to check whether a `username`, `email`, or handle surfaces on the dark web (onion services, leak dumps, breach archives) and want a trustworthy set of starting points rather than guessing at .onion addresses. This page organizes those entry points into onion indexing services, data-leak sites, dark-web news, and utilities.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the article on the clearnet to read and pick which categories you need (onion indexers vs leak archives vs news).
2. Copy the onion indexer / leak-site addresses you want to use.
3. Switch to the Tor Browser (on an isolated VM) and query those indexers with your `username`/`email`/handle.
4. Manually review results — the author stresses links are bot-collected and unvetted; screen for relevance and legality before opening.
5. Pivot: a hit on a dark-web forum or leak feeds breach-data and username correlation across the rest of your workflow.

## Inputs → Outputs
- **In:** `username` / `email` / handle to search across the linked services
- **Out:** dark-web `social-profile` presence, forum posts, or leak appearances
- **Empty/negative result looks like:** the indexers return no onion hits for the selector — meaning no indexed dark-web footprint, not proof of none (indexers cover a fraction of Tor).

## Gotchas & OpSec
- **Active** the moment you leave the clearnet page: browsing .onion links exposes you to hostile content and possible deanonymization. Use Tor Browser + Tails/Whonix, never your real environment.
- Link rot: this is a 2023 snapshot; some onion services will be dead or moved. Treat dead links as expected, not as an investigative signal.
- Legal-gate awareness: some linked material (leaked credentials, illicit marketplaces) carries legal risk depending on jurisdiction — review before accessing.

## Overlaps ("do both")
- Pairs with the sibling osint.me guides `[[osint-me-2]]`, `[[osint-me-3]]`, and `[[osintme-com]]` — same author, different resource categories — so consult them together for fuller coverage.

## Trust & verifiability
`trust: community` — a respected independent OSINT blogger's hand-curated list; reliable as a directory, but individual downstream links are third-party and must be judged on their own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-me-1 |
