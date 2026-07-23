---
id: free-fax
name: Free Fax (FaxZero)
description: Use when an investigation step requires sending a fax — e.g. a records/FOIA request to an agency that only accepts fax — and you want to do it free without your own fax line.
url: https://faxzero.com/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Sending a free outbound fax (records requests, agency contact) from a browser without a fax machine or account.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Free tier sends up to 3 pages + cover, max 5 faxes/day, with FaxZero branding on the cover; $3.29/fax removes branding and raises the limit to 25 pages. No account or credit card needed for the free tier.
opsec: active
opsecNote: This is an outbound action — you are transmitting a document to a real recipient, and the fax cover shows the sender name/email you type. Use a dedicated investigative identity/email, never your personal one, and remember the recipient sees that you contacted them. Nothing about the subject is queried, but your own operational footprint is exposed to whoever receives the fax.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: Long-established free consumer fax service (30M+ faxes sent); a utility, not a data source, so "trust" is about reliable delivery rather than data quality.
missingPersonsRelevance: low
coverage:
- us
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- FaxZero
- faxzero.com
tags:
- fax
- records-request
- investigator-utility
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Free Fax (FaxZero)

> A free browser-based fax sender — the practical way to file a records/FOIA request with an agency that still only takes faxes, no fax line required.

## When to use
Not a lookup tool. Reach for this when a downstream OSINT step needs an *outbound fax*: many US courts, sheriff's offices, and government records desks accept requests only by fax. FaxZero lets you send a PDF/DOC from the browser for free so you can submit that request without owning a fax number.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://faxzero.com/.
2. Fill in sender name/email and the recipient's name + fax number (use an investigative identity, not personal details).
3. Attach the document (PDF, DOC, DOCX — up to 3 pages on the free tier) or type a cover-page message.
4. Solve the CAPTCHA / email-confirmation step, then send. You'll get a delivery-status email.
5. Free limits: 5 faxes/day, 3 pages, FaxZero branding on the cover. Pay $3.29 to drop branding and raise page limits.

## Inputs → Outputs
- **In:** a recipient fax number + a document (no OSINT selector — this is a delivery utility)
- **Out:** a sent fax and a delivery confirmation (no data returned about a subject)
- **Empty/negative result looks like:** a bounce/failure email if the destination number is wrong or the line is dead — retry or verify the number.

## Gotchas & OpSec
- Human-in-the-loop: a CAPTCHA and an email-confirmation link gate each send; complete them manually.
- OpSec: **active/outbound** — the cover page displays the sender name and email you enter, and the recipient knows they were contacted. Always use a dedicated sock-puppet identity and email.
- Free faxes carry FaxZero branding, which can look non-official; for a formal records request the paid, unbranded send may be worth $3.29.

## Overlaps ("do both")
- Complements records-request workflows: use it to submit the request that public-records portals (e.g. county clerk or FOIA sites) can't accept online. It produces the request; the returned records are worked with your document/metadata tools.

## Trust & verifiability
`trust: community` — a mature, widely-used consumer fax utility. It transmits your document but is not itself a source of investigative data, so evaluate it on delivery reliability, not data accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | free-fax |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (captcha) |
