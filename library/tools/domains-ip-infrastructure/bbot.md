---
id: bbot
name: BBOT
description: Recursive internet scanner that chains modules for subdomains, emails, and attack surface.
url: https://github.com/blacklanternsecurity/bbot
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Recursive domain/email/subdomain enumeration
selectorsIn:
- domain
- ip-address
- email
selectorsOut:
- domain
- ip-address
- email
- social-profile
status: unknown
pricing: free
opsec: active
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Maintained by Black Lantern Security (9.9k stars); reputable infosec tooling.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- bbot
tags:
- recursive-scanner
- subdomains
- emails
- modules
source: gh-topic-osint-framework
lastVerified: ''
enrichment: full
---

# BBOT

> Recursive internet scanner that chains modules for subdomains, emails, and attack surface.

- **URL:** https://github.com/blacklanternsecurity/bbot
- **Best for:** Recursive domain/email/subdomain enumeration
- **Source:** harvested from `gh-topic-osint-framework`

pipx install bbot. Primarily infra recon; the email/username/social modules can occasionally surface a person's accounts but it is not a people-search tool.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
