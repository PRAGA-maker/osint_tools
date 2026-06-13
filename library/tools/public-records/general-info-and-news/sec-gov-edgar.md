---
id: sec-gov-edgar
name: SEC.gov - EDGAR
description: Researching US public company financials, ownership, and regulatory filings
url: https://www.sec.gov/submit-filings
category: public-records
path:
- public-records
- general-info-and-news
bestFor: Researching US public company financials, ownership, and regulatory filings
input: Company name, ticker symbol, or CIK number
output: SEC filings including annual reports, quarterly reports, insider transactions, and prospectuses
selectorsIn: []
selectorsOut: []
status: live
pricing: free
opsec: passive
opsecNote: Government public database; searches do not interact with the target company.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: ''
missingPersonsRelevance: medium
coverage: []
auth: none
api: true
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

# SEC.gov - EDGAR

> **Stub** — seeded from OSINT-Framework (`arf-seed`). Body not yet authored.
> Enrich per `schema/templates/tool.template.md`, then set `enrichment: full`.

- **URL:** https://www.sec.gov/submit-filings
- **Best for:** Researching US public company financials, ownership, and regulatory filings
- **Input → Output:** Company name, ticker symbol, or CIK number → SEC filings including annual reports, quarterly reports, insider transactions, and prospectuses
- **OpSec:** passive. Government public database; searches do not interact with the target company.

_To enrich:_ verify `trust` & `missingPersonsRelevance`, set `selectorsIn/Out` and `bestInteractionPattern`, write the How-to and Gotchas, link overlaps in `relatedTools`.
