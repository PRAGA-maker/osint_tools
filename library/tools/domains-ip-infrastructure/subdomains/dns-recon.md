---
id: dns-recon
name: DNS Recon
description: DNS enumeration, zone transfer testing, subdomain brute forcing, DNS security assessment
url: https://github.com/darkoperator/dnsrecon
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- subdomains
bestFor: DNS enumeration, zone transfer testing, subdomain brute forcing, DNS security assessment
input: Domain name, IP range/CIDR, subdomain wordlist, DNS server address
output: NS/SOA/MX/A records, discovered subdomains, zone transfer results, PTR records, wildcard resolution status
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Performs active DNS queries and brute force attempts; does not probe target services directly but makes repeated DNS requests.
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

# DNS Recon

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/darkoperator/dnsrecon
- **Best for:** DNS enumeration, zone transfer testing, subdomain brute forcing, DNS security assessment
- **Input → Output:** Domain name, IP range/CIDR, subdomain wordlist, DNS server address → NS/SOA/MX/A records, discovered subdomains, zone transfer results, PTR records, wildcard resolution status
- **OpSec:** active. Performs active DNS queries and brute force attempts; does not probe target services directly but makes repeated DNS requests.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
