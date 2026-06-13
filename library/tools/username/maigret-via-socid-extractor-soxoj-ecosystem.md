---
id: maigret-via-socid-extractor-soxoj-ecosystem
name: Maigret (via socid_extractor / soxoj ecosystem)
description: Extracts account details and identifiers (names, IDs, linked profiles) from social media and other pages.
url: https://github.com/soxoj/socid_extractor
category: username
path:
- username
bestFor: Pulling hidden identifiers (real name, user ID, linked accounts) from a profile URL
selectorsIn:
- social-profile
- username
selectorsOut:
- name
- email
- device-id
- social-profile
status: unknown
pricing: free
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: trusted
trustNote: By soxoj; widely used companion to Maigret (listed in the Social-Media-OSINT collection).
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- socid_extractor
tags:
- identifier-extraction
- username
- python
source: gh-topic-osint-resources
lastVerified: ''
enrichment: full
---

# Maigret (via socid_extractor / soxoj ecosystem)

> Extracts account details and identifiers (names, IDs, linked profiles) from social media and other pages.

- **URL:** https://github.com/soxoj/socid_extractor
- **Best for:** Pulling hidden identifiers (real name, user ID, linked accounts) from a profile URL
- **Source:** harvested from `gh-topic-osint-resources`

Extracts metadata/IDs from a known profile to pivot to other accounts. Surfaced inside the Social-Media-OSINT collection.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
