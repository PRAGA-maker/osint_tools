---
id: wayback-machine-2
name: Wayback Machine
description: Browse historical snapshots of websites and deleted/changed pages.
url: https://archive.org/web/
category: archives-cache
path:
- archives-cache
bestFor: Recovering deleted social posts, profiles or pages tied to a subject.
selectorsIn:
- domain
- social-profile
- username
selectorsOut:
- social-profile
- name
- metadata-exif
status: unknown
pricing: free
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Listed in Trace Labs awesome-osint (Documentation & Capture); Internet Archive.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Internet Archive
- web.archive.org
tags:
- archive
- cache
- deleted-content
source: tracelabs-repos
lastVerified: ''
enrichment: full
---

# Wayback Machine

> Browse historical snapshots of websites and deleted/changed pages.

- **URL:** https://archive.org/web/
- **Best for:** Recovering deleted social posts, profiles or pages tied to a subject.
- **Source:** harvested from `tracelabs-repos`

Passive (queries the archive, not the target). Essential for recovering content a subject has since removed.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
