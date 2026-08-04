---
id: pirate-bay
name: Pirate Bay
description: Use when you have a `username` (an uploader handle) and want to enumerate their torrent-upload history and activity on the largest public torrent index — returns `social-profile`-style upload footprints.
url: http://piratebayo3klnzokct3wt5yyxb2vpebbuyjl7m623iaxmqhsd52coid.onion/
category: dark-web
path:
- dark-web
bestFor: Pivoting a known uploader username into its full torrent-upload catalogue and timing/activity pattern.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free public torrent index; no account required to browse or search.
opsec: active
opsecNote: Reach it through Tor (the .onion address) or a VPN — the clearnet mirrors are blocked in many countries and log visitors. Browsing/searching leaks nothing to the target, but downloading a torrent broadcasts your IP to the swarm; stay at the metadata/browse layer for OSINT and never open magnet links from your real IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Anonymous, unofficial torrent index with rotating domains and mirrors; listings are user-submitted and unverified, and phishing clones are common — confirm you're on a known-good mirror.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- TPB
- ThePirateBay
tags:
- darkweb
- Dark Web Links
- torrents
source: uk-osint
lastVerified: '2026-08-04'
enrichment: full
---

# Pirate Bay

> The long-running public BitTorrent index, reachable over Tor; useful in OSINT only as a way to pull an uploader handle's full catalogue and activity timeline.

## When to use
You have a `username` — specifically a torrent **uploader handle** — surfaced elsewhere and want to see everything that account has published: what content, in what order, over what timespan. That upload footprint can corroborate an identity's interests, timezone-implying activity pattern, or link to the same handle reused on other sites. This is a niche pivot: Pirate Bay does not index people, only torrents, so it earns its place solely when you already have an uploader alias to chase.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the .onion address in the **Tor Browser** (or a current known-good mirror via VPN — the primary domains rotate and are geo-blocked).
2. Use the search box for a filename/keyword, or click a torrent's uploader name to open that user's page.
3. On the uploader page, read their full list of uploads, upload dates, and any profile blurb — this is the `social-profile`-style footprint.
4. Cross-check the same handle on other trackers, forums, and social sites; reused uploader aliases are the real value.
5. Stay at the browse/metadata layer — do not download, which would expose your IP to the swarm.

## Inputs → Outputs
- **In:** `username` (uploader handle)
- **Out:** `social-profile` (upload catalogue, activity dates, uploader page)
- **Empty/negative result looks like:** the handle has no uploads or the user page 404s — the alias may be a downloader-only account (no public footprint here) rather than an uploader.

## Gotchas & OpSec
- OpSec: **active** — treat it as a dark-web resource. Use Tor; never touch it from your real IP, and never open magnet/download links during OSINT.
- Domain churn and clone/phishing sites are constant; verify the mirror before trusting any listing.
- Listings are unverified and user-submitted; filenames lie and comments are unreliable.

## Overlaps ("do both")
- Pair with cross-platform username-enumeration tools: Pirate Bay confirms an uploader alias's activity here, while a username checker tells you where else that same handle exists.

## Trust & verifiability
`trust: unverified` — anonymous operators, rotating domains, and user-submitted content mean nothing here is authoritative; use it to generate leads (the uploader footprint), then verify those leads independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pirate-bay |
| category | dark-web |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
