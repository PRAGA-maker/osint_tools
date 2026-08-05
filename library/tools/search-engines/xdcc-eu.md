---
id: xdcc-eu
name: Xdcc.eu
description: Use when you have a filename, release name, or keyword and want to locate files being distributed as XDCC packs across IRC networks — returns bot/pack listings, not personal identifiers.
url: https://www.xdcc.eu
category: search-engines
path:
- search-engines
bestFor: Finding which IRC bots/packs are serving a named file across the XDCC ecosystem.
selectorsIn:
- name
selectorsOut:
- name
status: live
pricing: free
costNote: Free public search interface; no account required to search.
opsec: passive
opsecNote: Searching the index is passive (you only query a web page). Actually downloading a listed pack means connecting to an IRC server/bot, which exposes your IP to that network — do that only from a VM over a VPN/sock-puppet, never your real identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Community-run aggregator of third-party IRC bot listings; results are only as accurate as the bots that submit them and are not vetted.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- XDCC Search Engine
- xdcc eu
tags:
- Search engines
- Filesharing Search Engines
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# Xdcc.eu

> A search engine over XDCC file-serving bots on IRC — index the "who is serving this file" layer of the IRC filesharing world.

## When to use
Niche and rarely relevant to a person hunt. Reach for it only when your lead is a *file* — a specific release name, leaked archive, or media filename — and you want to know whether it is circulating via XDCC packs and on which IRC bots/networks. It maps a filename to distribution points; it does not identify people.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.xdcc.eu in a browser.
2. Enter your filename/keyword. Spaces act as wildcards; prefix a term with `-` to exclude it.
3. Read the results: matching packs are listed with the serving bot, network, pack number, and file size.
4. To actually retrieve a listed file you must join the named IRC network and message the bot with its XDCC command — do this only from a disposable, VPN'd environment.
5. Pivot: a confirmed distribution channel can feed dark-web / filesharing investigation, but this tool itself yields no `name`/`email`/`ip` for a person.

## Inputs → Outputs
- **In:** `name` (a filename or release keyword)
- **Out:** `name` (matching pack/bot/network listings)
- **Empty/negative result looks like:** no rows returned — the file isn't indexed here, which does not mean it isn't on IRC (coverage depends on which bots report in).

## Gotchas & OpSec
- The index reflects only bots that submit to xdcc.eu; absence is not proof.
- Downloading is the risky step: connecting to an IRC bot reveals your IP to that network. Keep collection passive (search only) unless you have a hardened, attributable-to-nobody setup.
- Listings are unvetted and may point to malware or mislabeled content.

## Overlaps ("do both")
- Stands largely alone in this library as an XDCC-specific index; pair it with general filesharing search engines when a file may also live on direct-download hosts.

## Trust & verifiability
`trust: unverified` — it is a community aggregator republishing whatever IRC bots advertise, with no curation or provenance guarantee, so treat every listing as a lead to confirm, not a fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | xdcc-eu |
| category | search-engines |
| selectorsIn → selectorsOut | name → name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
