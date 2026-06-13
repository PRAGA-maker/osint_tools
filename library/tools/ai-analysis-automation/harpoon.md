---
id: harpoon
name: Harpoon
description: CLI tool for open-source and threat intelligence with many plugin commands.
url: https://github.com/Te-k/harpoon
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Threat-intel-flavored OSINT lookups (domains, IPs, some social platforms)
selectorsIn:
- domain
- ip-address
- email
- username
selectorsOut:
- domain
- ip-address
- social-profile
status: unknown
pricing: free
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Mature CLI by Te-k (1.3k stars); broad plugin set.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- harpoon
tags:
- cli
- threat-intel
- plugins
source: gh-topic-osint-framework
lastVerified: ''
enrichment: full
---

# Harpoon

> CLI tool for open-source and threat intelligence with many plugin commands.

- **URL:** https://github.com/Te-k/harpoon
- **Best for:** Threat-intel-flavored OSINT lookups (domains, IPs, some social platforms)
- **Source:** harvested from `gh-topic-osint-framework`

pip install harpoon. Many commands need API keys. Mostly CTI/infra focused; has Twitter/Telegram/Instagram plugins that can help on the people side.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
