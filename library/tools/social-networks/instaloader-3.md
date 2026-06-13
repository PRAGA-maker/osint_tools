---
id: instaloader-3
name: Instaloader
description: Downloads Instagram photos, videos, captions, comments and metadata for a profile or hashtag.
url: https://instaloader.github.io/
category: social-networks
path:
- social-networks
bestFor: Bulk-archiving a subject's Instagram content and metadata.
selectorsIn:
- username
selectorsOut:
- image
- metadata-exif
- social-profile
- associate
status: unknown
pricing: free
opsec: active
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Listed in Trace Labs awesome-osint (Social Media).
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases: []
tags:
- python
- instagram
- social-media
- scraping
source: tracelabs-repos
lastVerified: ''
enrichment: full
---

# Instaloader

> Downloads Instagram photos, videos, captions, comments and metadata for a profile or hashtag.

- **URL:** https://instaloader.github.io/
- **Best for:** Bulk-archiving a subject's Instagram content and metadata.
- **Source:** harvested from `tracelabs-repos`

Authenticated use risks Instagram rate-limiting/bans; use a burner account. Captures post timestamps, captions and tagged users useful for timelines and associates.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
