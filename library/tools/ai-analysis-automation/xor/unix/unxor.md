---
id: unxor
name: unxor
description: Known-plaintext XOR cracking against malware and encoded artifacts
url: https://github.com/tomchop/unxor
category: ai-analysis-automation
path:
- ai-analysis-automation
- xor
- unix
bestFor: Known-plaintext XOR cracking against malware and encoded artifacts
input: XOR-encoded file plus known plaintext fragments
output: Recovered keystream segments and decoded content
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Local command-line analysis avoids submitting artifacts to remote services.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: ''
missingPersonsRelevance: low
coverage: []
auth: none
api: false
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

# unxor

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://github.com/tomchop/unxor
- **Best for:** Known-plaintext XOR cracking against malware and encoded artifacts
- **Input → Output:** XOR-encoded file plus known plaintext fragments → Recovered keystream segments and decoded content
- **OpSec:** passive. Local command-line analysis avoids submitting artifacts to remote services.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
