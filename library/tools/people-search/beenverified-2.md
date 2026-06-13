---
id: beenverified-2
name: BeenVerified
description: Background-check service aggregating public records (addresses, relatives, phone, etc.).
url: https://beenverified.com
category: people-search
path:
- people-search
bestFor: US background checks combining addresses, relatives, phones and records
selectorsIn:
- name
- phone
- email
- address
selectorsOut:
- address
- phone
- associate
- name
status: unknown
pricing: freemium
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial US data broker; full reports are paid (subscription).
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: true
aliases: []
tags:
- background-check
- public-records
- people-search
source: gh-topic-footprinting
lastVerified: ''
enrichment: full
---

# BeenVerified

> Background-check service aggregating public records (addresses, relatives, phone, etc.).

- **URL:** https://beenverified.com
- **Best for:** US background checks combining addresses, relatives, phones and records
- **Source:** harvested from `gh-topic-footprinting`

Search is free but full reports require a paid subscription; included as freemium for awareness. US-only. Subject to FCRA restrictions.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
