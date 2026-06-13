---
id: threatminer-org
name: ThreatMiner.org
description: Threat intelligence research, IOC investigation, malware/phishing link analysis
url: https://www.threatminer.org/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- reputation
bestFor: Threat intelligence research, IOC investigation, malware/phishing link analysis
input: Domain, IP, file hash (MD5/SHA1/SHA256), SSL certificate, or URL
output: Threat reports, IOC data, WHOIS info, malware associations, related indicators
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Queries aggregated threat intelligence data from multiple sources; does not probe targets.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
coverage: []
auth: none
api: true
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

# ThreatMiner.org

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.threatminer.org/
- **Best for:** Threat intelligence research, IOC investigation, malware/phishing link analysis
- **Input → Output:** Domain, IP, file hash (MD5/SHA1/SHA256), SSL certificate, or URL → Threat reports, IOC data, WHOIS info, malware associations, related indicators
- **OpSec:** passive. Queries aggregated threat intelligence data from multiple sources; does not probe targets.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
