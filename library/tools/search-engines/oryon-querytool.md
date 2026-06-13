---
id: oryon-querytool
name: Oryon querytool
description: Google-Spreadsheet-based OSINT framework for complex searches of people, emails, files.
url: https://github.com/oryon-osint/querytool
category: search-engines
path:
- search-engines
bestFor: Dork-driven searches for people, emails, usernames, and files via a spreadsheet
selectorsIn:
- name
- email
- username
- phone
- domain
selectorsOut:
- social-profile
- email
- document-id
status: unknown
pricing: free
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community Google-Sheets dorking framework (316 stars).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: true
aliases:
- querytool
- oryon
tags:
- google-dorking
- spreadsheet
- search-operators
source: gh-topic-osint-framework
lastVerified: ''
enrichment: full
---

# Oryon querytool

> Google-Spreadsheet-based OSINT framework for complex searches of people, emails, files.

- **URL:** https://github.com/oryon-osint/querytool
- **Best for:** Dork-driven searches for people, emails, usernames, and files via a spreadsheet
- **Source:** harvested from `gh-topic-osint-framework`

A Google Sheet that builds dork URLs across many engines/sites for a given term. Requires a Google account. Handy for systematic name/email/username searching.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
