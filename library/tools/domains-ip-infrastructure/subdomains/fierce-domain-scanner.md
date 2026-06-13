---
id: fierce-domain-scanner
name: Fierce Domain Scanner
description: DNS recon and subdomain-to-IP mapping
url: https://github.com/davidpepper/fierce-domain-scanner
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- subdomains
bestFor: DNS recon and subdomain-to-IP mapping
input: Domain, DNS server options, and optional wordlist/range parameters
output: Subdomains, resolved IPs, and DNS reconnaissance findings
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Performs direct DNS lookups and optional scans that can be logged by infrastructure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: low
coverage: []
auth: none
api: false
localInstall: true
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

# Fierce Domain Scanner

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/davidpepper/fierce-domain-scanner
- **Best for:** DNS recon and subdomain-to-IP mapping
- **Input → Output:** Domain, DNS server options, and optional wordlist/range parameters → Subdomains, resolved IPs, and DNS reconnaissance findings
- **OpSec:** active. Performs direct DNS lookups and optional scans that can be logged by infrastructure.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
