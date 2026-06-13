---
id: instaloader
name: Instaloader
description: Downloads Instagram pictures, videos, captions, and metadata for public (and own) accounts.
url: https://github.com/instaloader/instaloader
category: social-networks
path:
- social-networks
bestFor: Archiving an Instagram profile's media and metadata
selectorsIn:
- username
selectorsOut:
- image
- metadata-exif
- social-profile
status: unknown
pricing: free
opsec: active
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Long-established, widely trusted IG tool (listed in the Social-Media-OSINT collection).
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases: []
tags:
- instagram
- media-download
- python
source: gh-topic-osint-resources
lastVerified: ''
enrichment: full
---

# Instaloader

> Downloads Instagram pictures, videos, captions, and metadata for public (and own) accounts.

- **URL:** https://github.com/instaloader/instaloader
- **Best for:** Archiving an Instagram profile's media and metadata
- **Source:** harvested from `gh-topic-osint-resources`

Downloading touches IG servers (rate-limited; login increases ban risk). Captions/timestamps can place a person; geotags occasionally present.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
