---
id: spiderfoot-poppopjmp-fork
name: SpiderFoot (poppopjmp fork)
description: Automated OSINT collection engine for threat analysis and attack-surface mapping across 200+ modules.
url: https://github.com/poppopjmp/spiderfoot
category: search-engines
path:
- search-engines
bestFor: Automated multi-source enrichment of a name/email/domain/IP/phone
selectorsIn:
- name
- email
- phone
- domain
- ip-address
- username
selectorsOut:
- email
- social-profile
- domain
- ip-address
- address
status: unknown
pricing: free
opsec: active
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Fork of the well-known SpiderFoot framework (174 stars on fork).
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- spiderfoot
tags:
- automation
- framework
- enrichment
source: gh-topic-osint-resources
lastVerified: ''
enrichment: full
---

# SpiderFoot (poppopjmp fork)

> Automated OSINT collection engine for threat analysis and attack-surface mapping across 200+ modules.

- **URL:** https://github.com/poppopjmp/spiderfoot
- **Best for:** Automated multi-source enrichment of a name/email/domain/IP/phone
- **Source:** harvested from `gh-topic-osint-resources`

Powerful all-in-one enrichment; some modules are active (DNS/port scans). Configure passive-only mode for OPSEC-sensitive cases.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
