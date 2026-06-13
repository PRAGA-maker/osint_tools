---
id: email-leak-tests
name: Email Leak Tests
description: Verifying email IP privacy, testing anonymous email service configurations
url: https://emailipleak.com/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
- anonymous-browsing
- vpn-tests
bestFor: Verifying email IP privacy, testing anonymous email service configurations
input: Send a test email to a provided address
output: IP addresses found in email headers with assessment of anonymization effectiveness
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: active
opsecNote: Requires sending a test email that includes your real email headers; use a dedicated test account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
coverage: []
auth: none
api: false
localInstall: false
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

# Email Leak Tests

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://emailipleak.com/
- **Best for:** Verifying email IP privacy, testing anonymous email service configurations
- **Input → Output:** Send a test email to a provided address → IP addresses found in email headers with assessment of anonymization effectiveness
- **OpSec:** active. Requires sending a test email that includes your real email headers; use a dedicated test account.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
