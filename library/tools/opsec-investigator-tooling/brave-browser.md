---
id: brave-browser
name: Brave Browser
description: Privacy-focused Chromium browser shipped in the Trace Labs VM with OSINT extensions pre-installed.
url: https://brave.com/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Privacy-respecting browsing for investigations with the Forensic OSINT capture extension.
selectorsIn: []
selectorsOut: []
status: unknown
pricing: free
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Installed and configured (with forced Forensic OSINT extension) in the Trace Labs VM.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases: []
tags:
- browser
- privacy
- chromium
- opsec
source: tracelabs-repos
lastVerified: ''
enrichment: stub
---

# Brave Browser

> Privacy-focused Chromium browser shipped in the Trace Labs VM with OSINT extensions pre-installed.

- **URL:** https://brave.com/
- **Best for:** Privacy-respecting browsing for investigations with the Forensic OSINT capture extension.
- **Source:** harvested from `tracelabs-repos`

TL VM installs Brave via its apt repo and force-installs the Forensic OSINT capture extension. Good base browser for sock-puppet research.

_Enrichment: stub. If stub, complete per `schema/templates/tool.template.md`._
