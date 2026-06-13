---
id: flickr-2
name: Flickr
description: Photo metadata analysis, EXIF data extraction, location tracking, photographer identification
url: https://www.flickr.com/
category: documents-metadata
path:
- documents-metadata
- android
- apps
- pictures
bestFor: Photo metadata analysis, EXIF data extraction, location tracking, photographer identification
input: Usernames, tags, locations, URLs
output: Photos, metadata, EXIF data, location coordinates, user profiles
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Passive access to public photos; metadata freely available
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
coverage: []
auth: none
api: true
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

# Flickr

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.flickr.com/
- **Best for:** Photo metadata analysis, EXIF data extraction, location tracking, photographer identification
- **Input → Output:** Usernames, tags, locations, URLs → Photos, metadata, EXIF data, location coordinates, user profiles
- **OpSec:** passive. Passive access to public photos; metadata freely available

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
