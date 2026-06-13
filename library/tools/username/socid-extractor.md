---
id: socid-extractor
name: socid-extractor
description: Extracts structured account data (IDs, names, bios) from profile URLs across 150+ sites.
url: https://github.com/soxoj/socid-extractor
category: username
path:
- username
bestFor: Pulling hidden account IDs and metadata from a known profile URL
selectorsIn:
- social-profile
selectorsOut:
- username
- name
- email
- device-id
- metadata-exif
- dob
status: unknown
pricing: free
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: trusted
trustNote: By soxoj (Maigret author); the extraction engine behind Maigret (1k stars).
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
- profile-parsing
- account-id
- metadata
- python
source: gh-topic-osint-framework
lastVerified: ''
enrichment: full
---

# socid-extractor

> Extracts structured account data (IDs, names, bios) from profile URLs across 150+ sites.

- **URL:** https://github.com/soxoj/socid-extractor
- **Best for:** Pulling hidden account IDs and metadata from a known profile URL
- **Source:** harvested from `gh-topic-osint-framework`

pip install socid-extractor. Give it a profile URL and it returns structured fields (internal user IDs, registration dates, linked emails). Excellent for pivoting from one profile to another via shared IDs.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
