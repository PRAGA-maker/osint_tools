---
id: ollama
name: Ollama
description: Private AI analysis of sensitive OSINT data, local document processing without cloud exposure
url: https://ollama.com/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Private AI analysis of sensitive OSINT data, local document processing without cloud exposure
input: Text prompts, documents (via integration), API calls
output: LLM-generated responses using locally running open-source models
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Runs entirely on local hardware; no data leaves your machine. Ideal for sensitive investigations requiring AI analysis.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: low
coverage: []
auth: none
api: true
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases: []
tags: []
source: arf-seed
lastVerified: ''
enrichment: stub
---

# Ollama

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://ollama.com/
- **Best for:** Private AI analysis of sensitive OSINT data, local document processing without cloud exposure
- **Input → Output:** Text prompts, documents (via integration), API calls → LLM-generated responses using locally running open-source models
- **OpSec:** passive. Runs entirely on local hardware; no data leaves your machine. Ideal for sensitive investigations requiring AI analysis.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
