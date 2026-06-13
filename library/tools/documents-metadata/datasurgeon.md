---
id: datasurgeon
name: DataSurgeon
description: Quickly extracts emails, IPs, hashes, credit cards and other selectors from text.
url: https://github.com/Drew-Alleman/DataSurgeon
category: documents-metadata
path:
- documents-metadata
bestFor: Pulling structured selectors (emails, phones, IPs) out of dumps, logs or scraped text.
selectorsIn:
- metadata-exif
selectorsOut:
- email
- ip-address
- phone
status: unknown
pricing: free
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Lightweight Rust extraction utility, community maintained.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Drew-Alleman/DataSurgeon
tags:
- data-extraction
- regex
- rust
- parsing
source: gh-topic-reconnaissance
lastVerified: ''
enrichment: full
---

# DataSurgeon

> Quickly extracts emails, IPs, hashes, credit cards and other selectors from text.

- **URL:** https://github.com/Drew-Alleman/DataSurgeon
- **Best for:** Pulling structured selectors (emails, phones, IPs) out of dumps, logs or scraped text.
- **Source:** harvested from `gh-topic-reconnaissance`

Reads piped text/files and extracts emails, phone numbers, IPs, MACs, hashes, credit cards, URLs. Handy for triaging breach dumps or scraped pages tied to a person.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
