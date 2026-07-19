---
id: btdig
name: btdig
description: Use when you have a `name`, `username`, email or keyword and want to find files/torrents mentioning it on the BitTorrent DHT — returns file listings and torrent metadata.
url: https://btdig.com/
category: search-engines
path:
- search-engines
bestFor: Searching BitTorrent DHT content by keyword to surface leaked datasets, document dumps, or a subject's name/handle appearing inside shared file collections.
selectorsIn:
- name
- username
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free DHT search engine; no account. It indexes torrent metadata/file names from the DHT — it does not host files.
opsec: passive
opsecNote: Searching the index is passive and non-alerting. Actually downloading a torrent it points to is ACTIVE and exposes your IP to the swarm — never download from an attributable connection, and treat linked content as potentially malicious or illegal.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running DHT crawler/search engine; the index is genuine but reflects whatever is shared on BitTorrent — unvetted, often stale, and legally/ethically fraught content.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- btdig.com
- BTDigg
tags:
- torrent
- dht-search
- leaks
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# btdig

> A search engine over the BitTorrent DHT — query by keyword to find torrents and their file listings, useful for surfacing leaked datasets or a name/handle buried in shared file collections.

## When to use
You want to know whether a `name`, `username`, email, breach name, or unique phrase appears in files circulating on BitTorrent — leaked databases, document dumps, archives. BTDig indexes torrent metadata and file names from the DHT, letting you find and inspect *what's inside* a torrent (file names, sizes) without joining a swarm.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://btdig.com/ and search your keyword (a name, handle, breach label, or distinctive filename).
2. Scan results: torrent titles, contained file names and sizes, age, and the magnet/hash.
3. Read the **file listing** to judge relevance from names alone — you can often confirm a leak's contents without downloading.
4. Pivot: a confirmed dataset name feeds breach-analysis tooling; a filename/username hit feeds username-search and further keyword pivots. Do **not** download from an attributable connection.

## Inputs → Outputs
- **In:** `name`, `username`, email, or keyword/filename
- **Out:** torrent metadata and file listings (a `document-id`-like handle: title, hash/magnet, contained files)
- **Empty/negative result looks like:** no torrents match — the term simply isn't in DHT-shared content, or is named differently. Absence is not evidence a leak doesn't exist elsewhere.

## Gotchas & OpSec
- **Downloading is the risk, not searching.** Opening a magnet/torrent joins a public swarm and broadcasts your IP; content may be malware or illegal. Keep to reading metadata unless you have a controlled, authorised environment.
- Results are noisy, stale, and unvetted — file names can lie.
- OpSec: search passive; any download is active and exposing.

## Overlaps ("do both")
- Pairs with breach-lookup services and other leak-search engines — BTDig shows what's shared on BitTorrent, breach tools tell you if an email/handle is in a known dataset.

## Trust & verifiability
`trust: community` — a real, long-running DHT index, but it mirrors an unmoderated ecosystem. Verify any claim from actual (safely-obtained) contents, and never treat a filename as proof of what a file holds.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | btdig |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
