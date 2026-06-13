---
id: google-subdomains
name: Google Subdomains
description: Indexed subdomain discovery, publicly visible subdomain enumeration
url: https://www.google.com/?gws_rd=ssl#q=site:%3Cdomain.com%3E
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- subdomains
bestFor: Indexed subdomain discovery, publicly visible subdomain enumeration
input: 'Domain name (as Google Dork syntax: site:domain.com)'
output: Indexed subdomains and pages from Google search results
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Uses Google's search index; no direct contact with the target domain.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
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

# Google Subdomains

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.google.com/?gws_rd=ssl#q=site:%3Cdomain.com%3E
- **Best for:** Indexed subdomain discovery, publicly visible subdomain enumeration
- **Input → Output:** Domain name (as Google Dork syntax: site:domain.com) → Indexed subdomains and pages from Google search results
- **OpSec:** passive. Uses Google's search index; no direct contact with the target domain.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
