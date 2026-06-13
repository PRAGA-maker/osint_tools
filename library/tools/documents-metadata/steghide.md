---
id: steghide
name: steghide
description: Steganography tool to detect and extract data hidden inside image and audio files.
url: https://github.com/StefanoDeVuono/steghide
category: documents-metadata
path:
- documents-metadata
bestFor: Recovering hidden/embedded data from images shared by a subject (CTF-style).
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
trustNote: Installed in the Trace Labs VM (install_steghide / apt steghide).
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
- forensics
- ctf
source: tracelabs-repos
lastVerified: ''
enrichment: full
---

# steghide

> Steganography tool to detect and extract data hidden inside image and audio files.

- **URL:** https://github.com/StefanoDeVuono/steghide
- **Best for:** Recovering hidden/embedded data from images shared by a subject (CTF-style).
- **Source:** harvested from `tracelabs-repos`

apt package 'steghide'. Mostly CTF/forensics relevance; occasionally surfaces hidden notes in shared media.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
