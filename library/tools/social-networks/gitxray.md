---
id: gitxray
name: gitxray
description: Security tool using GitHub REST APIs for reconnaissance, forensics, and pentesting of repos/users.
url: https://github.com/kulkansecurity/gitxray
category: social-networks
path:
- social-networks
bestFor: Profiling a GitHub user/contributor (emails, activity, identities)
selectorsIn:
- username
selectorsOut:
- email
- social-profile
status: unknown
pricing: free
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Vendor-maintained (181 stars).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases: []
tags:
- github
- recon
- python
source: gh-topic-osint-resources
lastVerified: ''
enrichment: full
---

# gitxray

> Security tool using GitHub REST APIs for reconnaissance, forensics, and pentesting of repos/users.

- **URL:** https://github.com/kulkansecurity/gitxray
- **Best for:** Profiling a GitHub user/contributor (emails, activity, identities)
- **Source:** harvested from `gh-topic-osint-resources`

Can surface a developer's email and linked identities from GitHub metadata.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
