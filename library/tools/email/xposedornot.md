---
id: xposedornot
name: XposedOrNot
description: Searches an aggregated repository of compromised/breached passwords to check exposure.
url: https://github.com/Viralmaniar/XposedOrNot
category: email
path:
- email
bestFor: Checking whether an email/account appears in known password breaches
selectorsIn:
- email
- username
selectorsOut:
- email
status: unknown
pricing: free
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: 145 stars; queries breach datasets (XposedOrNot.com API).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- Xon
tags:
- breach
- password
- exposure
- haveibeenpwned-alternative
source: gh-topic-intelligence-gathering
lastVerified: ''
enrichment: full
---

# XposedOrNot

> Searches an aggregated repository of compromised/breached passwords to check exposure.

- **URL:** https://github.com/Viralmaniar/XposedOrNot
- **Best for:** Checking whether an email/account appears in known password breaches
- **Source:** harvested from `gh-topic-intelligence-gathering`

Breach-check utility backed by the XposedOrNot dataset/API. For missing persons, confirming which breaches an email is in can reveal sites/services the person used; passive lookup, free API.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
