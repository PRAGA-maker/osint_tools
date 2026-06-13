---
id: fedifinder
name: Fedifinder
description: Finding Twitter contacts who moved to Mastodon/Fediverse
url: https://fedifinder.glitch.me/
category: social-networks
path:
- social-networks
- fediverse-mastodon
bestFor: Finding Twitter contacts who moved to Mastodon/Fediverse
input: Twitter/X account (via OAuth login)
output: CSV list of discovered Fediverse handles from your Twitter contacts
selectorsIn: []
selectorsOut: []
status: down
pricing: free
opsec: active
opsecNote: Requires Twitter OAuth authentication; scans public bios and tweets of followed accounts.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: high
coverage: []
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: true
relatedTools: []
aliases: []
tags: []
source: arf-seed
lastVerified: ''
enrichment: stub
---

# Fedifinder

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://fedifinder.glitch.me/
- **Best for:** Finding Twitter contacts who moved to Mastodon/Fediverse
- **Input → Output:** Twitter/X account (via OAuth login) → CSV list of discovered Fediverse handles from your Twitter contacts
- **OpSec:** active. Requires Twitter OAuth authentication; scans public bios and tweets of followed accounts.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
