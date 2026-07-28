---
id: torrent-to-magnet
name: Torrent to Magnet
description: Use when you have a `.torrent` file and want its magnet link / infohash — returns a magnet URI computed locally in your browser.
url: https://nutbread.github.io/t2m/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Converting a .torrent file into a magnet URI (and its infohash) without uploading it anywhere.
selectorsIn: []
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free, open-source, static web page; no account.
opsec: passive
opsecNote: Fully passive and client-side — the conversion runs in JavaScript in your browser, so the .torrent file never leaves your machine and no server sees it. Safe for analysing a torrent file you obtained without tipping off anyone.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Small open-source GitHub Pages utility (nutbread/t2m); code is public and does the hashing locally, but it is a hobby project with no ongoing guarantees.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- t2m
- torrent2magnet
tags:
- utility
- torrents
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Torrent to Magnet

> A tiny in-browser tool that turns a `.torrent` file into a magnet URI and exposes its infohash — entirely client-side, nothing uploaded.

## When to use
You have a `.torrent` file (recovered from a device, an email, a download folder) and need its magnet link or, more usefully for OSINT, its **infohash** — the unique fingerprint you can then search on DHT/torrent-tracking indexes to see who else is sharing the same content and where. This tool extracts that without exposing the file to any server.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://nutbread.github.io/t2m/.
2. Drag-and-drop the `.torrent` file onto the page (or use the file picker).
3. Read the generated magnet URI; the `xt=urn:btih:<infohash>` portion is the content fingerprint.
4. Pivot: paste the infohash into torrent-tracking/DHT-monitoring services to enumerate peers, upload dates, and other files in the same swarm.

## Inputs → Outputs
- **In:** a `.torrent` file (not a standard selector)
- **Out:** a magnet URI + infohash (`document-id`-style content fingerprint)
- **Empty/negative result looks like:** the page rejects a file that isn't a valid bencoded torrent — nothing to convert.

## Gotchas & OpSec
- Purely a converter — it does not download, connect to peers, or reveal who is sharing; that requires a separate tracking service and the infohash it produces.
- Runs client-side, so it works offline once loaded — good for handling a sensitive file air-gapped.
- A hobby GitHub Pages project; if it disappears, any bittorrent library reproduces the same infohash locally.

## Overlaps ("do both")
- Pairs with torrent/DHT peer-tracking tools — this produces the infohash, and those tools turn that hash into peer `ip-address`es and swarm activity.

## Trust & verifiability
`trust: community` — open-source, does the math locally (verifiable), but an unmaintained-risk hobby utility; the output infohash is deterministic and can be cross-checked with any torrent library.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | torrent-to-magnet |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
