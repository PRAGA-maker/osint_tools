---
id: sunxdcc
name: SunXDCC
description: Use when you have a filename/keyword and want to find files offered by XDCC bots on IRC — returns the network, bot, pack number, and filename to request via IRC.
url: http://sunxdcc.com
category: search-engines
path:
- search-engines
bestFor: Searching for files distributed by XDCC bots across IRC networks.
selectorsIn: []
selectorsOut:
- document-id
status: degraded
pricing: free
costNote: Free to search (donation-supported). Note the operator has announced the service is migrating to skullxdcc.com and sunxdcc.com may be retired — verify the live domain.
opsec: active
opsecNote: Searching the index is passive, but actually retrieving a file means joining an IRC network and messaging a bot, which exposes your IRC client and IP to that network and the bot operator. Use a sock-puppet IRC identity and consider a bouncer/VPN.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: A small hobbyist-run search index over IRC XDCC offers; it only lists what bots advertise, and both the index and the files are unvetted.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- SunXDCC
- sunxdcc.com
tags:
- Filesharing Search Engines
- irc
- xdcc
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# SunXDCC

> A search engine over the files that XDCC bots advertise on IRC — type a name, get the network/bot/pack you would need to request it.

## When to use
Niche: you are chasing a specific file (a leaked archive, a named release, a document) that you suspect circulates via IRC's XDCC distribution rather than the open web. SunXDCC indexes what XDCC bots across IRC networks are offering, so you can locate which network and bot hold a given filename before switching to an IRC client to actually fetch it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the current site (sunxdcc.com, or its successor skullxdcc.com if sunxdcc has been retired).
2. Enter your filename/keyword and search; there is also an API endpoint for programmatic queries.
3. Read each result row: IRC **network**, **bot** name, **pack number**, filename, and size.
4. To retrieve, connect to that IRC network in a client and message the bot `/msg <bot> xdcc send #<pack>` — this is a separate, active step.
5. Pivot: the file itself (once obtained and scanned) yields `metadata-exif` and content leads; the index only gives you the `document-id`/filename and where to ask.

## Inputs → Outputs
- **In:** a filename or keyword
- **Out:** network + bot + pack + filename records (a `document-id`-level pointer to the file)
- **Empty/negative result looks like:** no rows — the file is not currently advertised by any indexed bot (offers are transient), or the index is mid-migration; try again or check the successor domain.

## Gotchas & OpSec
- Human-in-the-loop: retrieval requires you to join IRC and command a bot by hand — the search only points the way.
- OpSec: the search is passive; **fetching is active** and exposes your IRC identity/IP to the network and bot operator. Use a burner IRC nick and a VPN/bouncer.
- Service is in flux (operator announced migration to skullxdcc.com); the domain and availability may change — hence `status: degraded`.
- Files are unvetted and may be mislabeled or malicious; scan anything you pull in a sandbox.

## Overlaps ("do both")
- Complements general filesharing/torrent search engines: SunXDCC covers the IRC-XDCC channel specifically, which those other indexes miss. Run both when hunting a file that is not on the open web.

## Trust & verifiability
`trust: unverified` — a small, migrating hobbyist index that merely mirrors what bots advertise; confirm any result by actually locating the pack on IRC, and never trust the file's integrity until you have scanned it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sunxdcc |
| category | search-engines |
| selectorsIn → selectorsOut |  → document-id |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
