---
id: gitsint-rs
name: gitsint-rs
description: Platform for uncovering connections and exposed secrets across GitHub.
url: https://github.com/gitsint-rs/gitsint-rs
category: username
path:
- username
bestFor: Finding emails/identities linked to a GitHub account
selectorsIn:
- username
- email
selectorsOut:
- email
- username
- associate
status: unknown
pricing: free
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Community GitHub-OSINT tool in Rust (33 stars).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- gitsint
tags:
- github
- email
- secrets
- rust
source: gh-topic-osint-framework
lastVerified: ''
enrichment: full
---

# gitsint-rs

> Platform for uncovering connections and exposed secrets across GitHub.

- **URL:** https://github.com/gitsint-rs/gitsint-rs
- **Best for:** Finding emails/identities linked to a GitHub account
- **Source:** harvested from `gh-topic-osint-framework`

Pivots from a GitHub username to associated emails (via commit metadata) and connected accounts. Useful when a subject has a developer footprint.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
