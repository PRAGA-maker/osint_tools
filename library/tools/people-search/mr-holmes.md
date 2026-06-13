---
id: mr-holmes
name: Mr.Holmes
description: All-in-one OSINT tool for usernames, emails, phones, and domain info.
url: https://github.com/Lucksi/Mr.Holmes
category: people-search
path:
- people-search
bestFor: Quick multi-selector lookups (username, phone, email, domain) from one CLI
selectorsIn:
- username
- email
- phone
- domain
- name
selectorsOut:
- social-profile
- email
- phone
- domain
status: unknown
pricing: free
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular community OSINT multi-tool (3.6k stars); maintained by an individual.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- mr holmes
- mrholmes
tags:
- multi-tool
- username
- phone
- email
source: gh-topic-osint-framework
lastVerified: ''
enrichment: full
---

# Mr.Holmes

> All-in-one OSINT tool for usernames, emails, phones, and domain info.

- **URL:** https://github.com/Lucksi/Mr.Holmes
- **Best for:** Quick multi-selector lookups (username, phone, email, domain) from one CLI
- **Source:** harvested from `gh-topic-osint-framework`

Python CLI/GUI bundling phone (PhoneInfoga-style), username, and Google-dorking modules. Results quality varies by module; verify hits. Works on Linux/Termux.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
