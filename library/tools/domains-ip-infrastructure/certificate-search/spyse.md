---
id: spyse
name: Spyse
description: Domain intelligence, certificate discovery, subdomain enumeration, vulnerability identification
url: https://spyse.com/search/certificate
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- certificate-search
bestFor: Domain intelligence, certificate discovery, subdomain enumeration, vulnerability identification
input: Domain, IP, certificate, email, or organization name
output: Domain details, subdomains, certificates, WHOIS info, CVEs, open ports, scraped emails
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
opsec: passive
opsecNote: Queries Spyse's pre-scanned database; does not contact the target directly.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
coverage: []
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags: []
source: arf-seed
lastVerified: ''
enrichment: stub
---

# Spyse

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://spyse.com/search/certificate
- **Best for:** Domain intelligence, certificate discovery, subdomain enumeration, vulnerability identification
- **Input → Output:** Domain, IP, certificate, email, or organization name → Domain details, subdomains, certificates, WHOIS info, CVEs, open ports, scraped emails
- **OpSec:** passive. Queries Spyse's pre-scanned database; does not contact the target directly.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
