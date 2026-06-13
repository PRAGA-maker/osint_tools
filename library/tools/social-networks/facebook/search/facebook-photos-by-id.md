---
id: facebook-photos-by-id
name: Facebook Photos by ID
description: Opening specific Facebook photos from known numeric IDs
url: https://www.facebook.com/photo.php?fbid=PHOTO-ID-HERE
category: social-networks
path:
- social-networks
- facebook
- search
bestFor: Opening specific Facebook photos from known numeric IDs
input: Photo ID value inserted into the URL
output: Direct Facebook photo page for the supplied photo ID
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Accesses publicly available photo endpoints; visibility depends on the target photo privacy settings.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: high
coverage: []
auth: none
api: false
localInstall: false
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

# Facebook Photos by ID

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.facebook.com/photo.php?fbid=PHOTO-ID-HERE
- **Best for:** Opening specific Facebook photos from known numeric IDs
- **Input → Output:** Photo ID value inserted into the URL → Direct Facebook photo page for the supplied photo ID
- **OpSec:** passive. Accesses publicly available photo endpoints; visibility depends on the target photo privacy settings.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
