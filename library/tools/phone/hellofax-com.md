---
id: hellofax-com
name: hellofax.com (Dropbox Fax)
description: Use when you have a `phone`/fax number and need to send or receive a fax — e.g. to submit a records request to an agency that only accepts fax — rather than to enrich a person.
url: https://www.hellofax.com/
category: phone
path:
- phone
bestFor: Sending/receiving faxes online (no fax machine) to reach agencies, courts or offices that only accept records requests by fax.
selectorsIn:
- phone
selectorsOut: []
status: live
pricing: freemium
costNote: Now Dropbox Fax (hellofax.com redirects to fax.dropbox.com). Free tier gives ~5 send pages (plus limited bonus pages); regular use needs a paid plan or pay-as-you-go. A receiving fax number is a paid feature.
opsec: active
opsecNote: This is a utility for contacting a number, not a lookup. Sending a fax reveals your sender line/cover details to the recipient — use a dedicated account and neutral sender info, never personal identifiers. Do not use it to probe or harass a target's line.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Legitimate commercial service operated by Dropbox (formerly HelloFax). It is a fax utility, not an OSINT data source — it returns no information about a person.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools: []
aliases:
- HelloFax
- Dropbox Fax
- fax.dropbox.com
tags:
- mobilephone
- Mobile & Phone Related
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# hellofax.com (Dropbox Fax)

> An online fax service (HelloFax, now Dropbox Fax) — a way to send/receive faxes without a machine, not a phone-lookup tool.

## When to use
This is an operational utility, not an enrichment source. Reach for it when an investigation step requires **faxing** — many US courts, county clerks, prisons, and government offices still accept records or public-information requests only by fax. It lets you send those from a browser and receive replies as PDFs. It does **not** take a number and return a name/address; the stub's `name`/`address`/`social-profile` outputs were mis-harvested.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.hellofax.com/ (redirects to fax.dropbox.com) and create/sign in to a dedicated account.
2. To send: upload the document, enter the recipient fax `phone` number, add a neutral cover page, and send. Free tier covers a few pages; more needs a paid plan.
3. To receive replies: provision a receiving fax number (paid) and read inbound faxes as PDFs in the inbox/email.
4. There is no "output" about a person — the deliverable is the transmitted/received document itself.

## Inputs → Outputs
- **In:** `phone` (destination fax number) + a document
- **Out:** none about a person — a sent/received fax (transmission confirmation, inbound PDF)
- **Empty/negative result looks like:** a failed/busy transmission report — meaning the number isn't a working fax line, not a data miss.

## Gotchas & OpSec
- Not a data-return tool: do not expect it to resolve a number to an identity. Use a proper phone-intel tool for that.
- Human-in-the-loop: account creation and login are required; a receiving number costs money.
- OpSec: **active** — every fax you send exposes sender/cover-page details to the recipient. Use a dedicated account and neutral sender info; never use it to bombard or probe a subject's line.

## Overlaps ("do both")
- Complements (does not replace) phone-intelligence lookups: use those to identify a number, use this only to formally transmit a request to one.

## Trust & verifiability
`trust: trusted` — a legitimate Dropbox-operated commercial service. The trust rating is about the service's reliability, not about any investigative data (it returns none).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hellofax-com |
| category | phone |
| selectorsIn → selectorsOut | phone → (none) |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
