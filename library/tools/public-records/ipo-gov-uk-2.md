---
id: ipo-gov-uk-2
name: ipo.gov.uk
description: Use when you have a `name` or `employer-org` and want UK trademark filings tied to them — returns the owner/applicant `name`, `address`, and `employer-org` on the mark.
url: https://trademarks.ipo.gov.uk/ipo-tmtext
category: public-records
path:
- public-records
bestFor: Finding UK trademarks by owner/applicant to link a person or brand to a registered mark and its filing address.
selectorsIn:
- name
- address
- employer-org
selectorsOut:
- employer-org
- name
- address
status: live
pricing: free
costNote: Free public search on the UK Intellectual Property Office site; no account required.
opsec: passive
opsecNote: Searching a government trademark register is passive and does not notify the owner. No login is needed; queries are ordinary web requests.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the UK Intellectual Property Office (a government agency); filing data — including applicant name and address — is authoritative public record.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: true
localInstall: false
registration: false
aliases:
- UK IPO trademark search
- IPO tmtext
tags:
- companysites
- Company Related Sites
- trademark
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# ipo.gov.uk

> The UK Intellectual Property Office trademark search — look up marks by text or by owner to tie a person/brand to a registered trademark and its filing details.

## When to use
You have a person's `name`, a brand, or an `employer-org` and want to find UK trademark filings connected to them. A trademark record exposes the applicant/owner's name and a filing address (often a home or business address, or an agent's), plus the goods/services and dates — useful for confirming that a person runs a brand, locating an address, or mapping a business's IP footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://trademarks.ipo.gov.uk/ipo-tmtext (the text search); use the "by owner" search to query a person or company `name`.
2. Enter the mark text or the owner `name`/`employer-org`.
3. Open a matching mark: read the owner/applicant `name`, the filing `address`, the associated company (`employer-org`), status, and dates.
4. Note whether the address is the owner's or a representative/agent's before treating it as the subject's.
5. Pivot: an owner name + address feeds people-search and Companies House; a company feeds `[[companies-house]]`.

## Inputs → Outputs
- **In:** mark text, or owner `name`/`employer-org` (and you can cross-check an `address`)
- **Out:** owner/applicant `name`, filing `address`, `employer-org`, goods/services, dates, status
- **Empty/negative result looks like:** no marks — most people never file a trademark, so absence is expected and uninformative. The listed address may belong to a trademark agent, not the subject.

## Gotchas & OpSec
- Filing addresses are frequently the agent's/representative's, not the owner's home — verify before relying on the address.
- UK-only; for other jurisdictions use WIPO Global Brand Database or national offices.
- Name matching can catch common-name collisions; corroborate with the associated company/goods.

## Overlaps ("do both")
- Pairs with `[[companies-house]]` and the WIPO Global Brand Database — Companies House confirms the owner's corporate/officer footprint, WIPO extends the brand search internationally.

## Trust & verifiability
`trust: trusted` — first-party UK government IP register; owner, address, and filing data are authoritative public record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ipo-gov-uk-2 |
| category | public-records |
| selectorsIn → selectorsOut | name, address, employer-org → employer-org, name, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
