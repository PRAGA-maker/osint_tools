---
id: twitter
name: Twitter
description: Real-time monitoring, account verification, relationship mapping, sentiment analysis
url: https://www.twitter.com/
category: documents-metadata
path:
- documents-metadata
- android
- apps
- social-networking
bestFor: Real-time monitoring, account verification, relationship mapping, sentiment analysis
input: Usernames, hashtags, keywords, user IDs
output: Tweets, user profiles, follower networks, location data, media
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Mostly passive; API-based tools are rate-limited but account scraping can be detected
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
coverage: []
auth: account
api: true
localInstall: true
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags: []
source: arf-seed
lastVerified: ''
enrichment: stub
---

# Twitter

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.twitter.com/
- **Best for:** Real-time monitoring, account verification, relationship mapping, sentiment analysis
- **Input → Output:** Usernames, hashtags, keywords, user IDs → Tweets, user profiles, follower networks, location data, media
- **OpSec:** passive. Mostly passive; API-based tools are rate-limited but account scraping can be detected

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
