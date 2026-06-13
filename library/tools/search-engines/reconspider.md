---
id: reconspider
name: reconspider
description: OSINT framework for scanning IP addresses, emails, websites, and organizations.
url: https://github.com/bhavsec/reconspider
category: search-engines
path:
- search-engines
bestFor: Multi-target OSINT lookups (IP, email, phone, domain, username) from one console.
selectorsIn:
- email
- phone
- ip-address
- domain
- username
selectorsOut:
- email
- ip-address
- geolocation
- social-profile
- phone
status: unknown
pricing: free
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Community OSINT framework; some modules depend on third-party APIs.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- bhavsec/reconspider
tags:
- osint-framework
- python
- ip-lookup
- email-lookup
source: gh-topic-reconnaissance
lastVerified: ''
enrichment: full
---

# reconspider

> OSINT framework for scanning IP addresses, emails, websites, and organizations.

- **URL:** https://github.com/bhavsec/reconspider
- **Best for:** Multi-target OSINT lookups (IP, email, phone, domain, username) from one console.
- **Source:** harvested from `gh-topic-reconnaissance`

Aggregates lookups for IPs, domains, emails, phone numbers and usernames. Mixed maintenance; verify modules still work against live APIs.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
