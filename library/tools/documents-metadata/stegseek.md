---
id: stegseek
name: stegseek
description: Fast steghide cracker that brute-forces passphrases to extract hidden data.
url: https://github.com/RickdeJager/stegseek
category: documents-metadata
path:
- documents-metadata
bestFor: Cracking steghide-protected files when the passphrase is unknown.
selectorsIn:
- image
selectorsOut:
- metadata-exif
status: unknown
pricing: free
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Installed in the Trace Labs VM (install_stegseek).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases: []
tags:
- steganography
- cracking
- ctf
source: tracelabs-repos
lastVerified: ''
enrichment: full
---

# stegseek

> Fast steghide cracker that brute-forces passphrases to extract hidden data.

- **URL:** https://github.com/RickdeJager/stegseek
- **Best for:** Cracking steghide-protected files when the passphrase is unknown.
- **Source:** harvested from `tracelabs-repos`

Companion to steghide; primarily CTF/forensics use.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
