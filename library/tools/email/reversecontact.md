---
id: reversecontact
name: ReverseContact
description: Finds a LinkedIn profile and enriched identity data from an email address.
url: https://www.reversecontact.com/
category: email
path:
- email
bestFor: Email-to-LinkedIn/identity pivot
selectorsIn:
- email
selectorsOut:
- name
- social-profile
- employer-org
status: unknown
pricing: freemium
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial enrichment service with limited free lookups (in the Social-Media-OSINT collection).
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: true
aliases: []
tags:
- email
- linkedin
- enrichment
source: gh-topic-osint-resources
lastVerified: ''
enrichment: full
---

# ReverseContact

> Finds a LinkedIn profile and enriched identity data from an email address.

- **URL:** https://www.reversecontact.com/
- **Best for:** Email-to-LinkedIn/identity pivot
- **Source:** harvested from `gh-topic-osint-resources`

Free tier limited; resolves an email to a real name and LinkedIn profile.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
