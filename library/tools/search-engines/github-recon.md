---
id: github-recon
name: GitHub-Recon
description: Methodology and reference for reconnaissance and dorking against GitHub to surface leaked data.
url: https://github.com/TheBinitGhimire/GitHub-Recon
category: search-engines
path:
- search-engines
bestFor: Finding secrets, emails, and identity leads in public GitHub repos via dorks
selectorsIn:
- name
- username
- email
- domain
selectorsOut:
- email
- username
- social-profile
status: unknown
pricing: free
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: 124 stars; reference/methodology repo rather than an executable tool.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- github-dorking
- code-search
- leaks
- methodology
source: gh-topic-intelligence-gathering
lastVerified: ''
enrichment: full
---

# GitHub-Recon

> Methodology and reference for reconnaissance and dorking against GitHub to surface leaked data.

- **URL:** https://github.com/TheBinitGhimire/GitHub-Recon
- **Best for:** Finding secrets, emails, and identity leads in public GitHub repos via dorks
- **Source:** harvested from `gh-topic-intelligence-gathering`

Documents GitHub dorking techniques. A person active on GitHub may leak their real name/email in commits; this methodology helps pivot a username/email to a real identity. Reference material, not a standalone tool.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
