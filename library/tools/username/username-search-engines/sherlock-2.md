---
id: sherlock-2
name: Sherlock
description: Mass username enumeration across 400+ sites
url: https://github.com/sherlock-project/sherlock
category: username
path:
- username
- username-search-engines
bestFor: Mass username enumeration across 400+ sites
input: Username(s)
output: List of discovered profile URLs across social networks
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Directly queries each target site to check username existence; supports Tor/proxy for anonymity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: high
coverage: []
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags: []
source: arf-seed
lastVerified: ''
enrichment: stub
---

# Sherlock

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/sherlock-project/sherlock
- **Best for:** Mass username enumeration across 400+ sites
- **Input → Output:** Username(s) → List of discovered profile URLs across social networks
- **OpSec:** active. Directly queries each target site to check username existence; supports Tor/proxy for anonymity.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
