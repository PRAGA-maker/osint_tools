---
id: mailcat
name: Mailcat
description: Finds existing email addresses for a username via API and SMTP verification across providers.
url: https://github.com/sharsil/mailcat
category: email
path:
- email
bestFor: Discovering which email providers a username has accounts on
selectorsIn:
- username
selectorsOut:
- email
status: unknown
pricing: free
opsec: active
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular email-discovery tool (890+ stars).
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases: []
tags:
- email-enumeration
- smtp
- python
source: gh-topic-osint-resources
lastVerified: ''
enrichment: full
---

# Mailcat

> Finds existing email addresses for a username via API and SMTP verification across providers.

- **URL:** https://github.com/sharsil/mailcat
- **Best for:** Discovering which email providers a username has accounts on
- **Source:** harvested from `gh-topic-osint-resources`

SMTP verification touches mail servers (active); may be rate-limited or blocked. Good for pivoting username -> email.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
