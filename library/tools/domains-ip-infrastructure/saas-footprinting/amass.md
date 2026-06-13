---
id: amass
name: Amass
description: Comprehensive external attack-surface and subdomain mapping
url: https://github.com/owasp-amass/amass
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- saas-footprinting
bestFor: Comprehensive external attack-surface and subdomain mapping
input: Domain names, ASN data, CIDRs, and optional API credentials
output: Correlated graph of domains, subdomains, infrastructure, and relationships
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Supports both passive and active techniques, including DNS probing and brute-force modes.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: low
coverage: []
auth: account
api: true
localInstall: true
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

# Amass

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/owasp-amass/amass
- **Best for:** Comprehensive external attack-surface and subdomain mapping
- **Input → Output:** Domain names, ASN data, CIDRs, and optional API credentials → Correlated graph of domains, subdomains, infrastructure, and relationships
- **OpSec:** active. Supports both passive and active techniques, including DNS probing and brute-force modes.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
