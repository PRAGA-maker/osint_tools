---
id: stegosuite
name: StegOSuite
description: Graphical steganography tool to hide and extract data in image files.
url: https://github.com/osde8info/stegosuite
category: documents-metadata
path:
- documents-metadata
bestFor: GUI-based detection/extraction of hidden data in images.
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
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Optionally installed in the Trace Labs VM (install_stegosuite).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- StegOSuite
tags:
- steganography
- gui
- ctf
source: tracelabs-repos
lastVerified: ''
enrichment: full
---

# StegOSuite

> Graphical steganography tool to hide and extract data in image files.

- **URL:** https://github.com/osde8info/stegosuite
- **Best for:** GUI-based detection/extraction of hidden data in images.
- **Source:** harvested from `tracelabs-repos`

Java GUI; marked optional in the TL VM build. CTF/forensics relevance.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
