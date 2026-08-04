---
id: search-for-company-documents
name: Search for Company Documents
description: Use when you have a Canadian public company or issuer `name` and want its official regulatory filings — returns prospectuses, financials and insider documents naming directors and officers.
url: https://www.sedarplus.ca/
category: public-records
path:
- public-records
bestFor: Retrieving official Canadian public-company / securities filings (SEDAR+) and the people named in them.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- name
- associate
- address
status: live
pricing: free
costNote: Free public access; SEDAR+ is the official filing system operated by the Canadian Securities Administrators. No account needed to search public filings.
opsec: passive
opsecNote: You are querying an official public-records system, not the subject, so the lookup is passive and undisclosed. Note SEDAR+ uses bot-protection; run searches manually in a browser rather than scripting them.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: SEDAR+ (sedarplus.ca) is the official electronic filing system of the Canadian Securities Administrators, replacing the legacy sedar.com; filings are authoritative primary regulatory records.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- SEDAR
- SEDAR+
- sedarplus
tags:
- company-filings
- public-records
- canada
- securities
source: osint4all
lastVerified: '2026-08-04'
enrichment: full
---

# Search for Company Documents

> SEDAR+, Canada's official securities-filing system: search a public company by name and read its regulatory documents — which name directors, officers, and often their business addresses.

## When to use
Your subject is tied to a Canadian public company, income trust, or investment fund (as a director, officer, or major shareholder), or you're vetting the company itself. SEDAR+ holds the mandatory public filings — prospectuses, annual/interim financials, management information circulars, and insider/continuous-disclosure documents — which routinely list the names of directors and executives (`associate`/`employer-org` links) and business `address`es. (The legacy sedar.com now redirects here.)

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.sedarplus.ca/ in a normal browser (it uses bot-protection, so solve any challenge manually).
2. Use the public filings search; enter the company/issuer `name` (or browse by industry/date).
3. Open the profile and its document list; management circulars and prospectuses are richest for people data.
4. Read out the named directors/officers (`name`, `associate`), the `employer-org` structure, and any listed head-office `address`.
5. Pivot: a director's name feeds a person search; the head-office address feeds mapping; cross-reference officers against other companies.

## Inputs → Outputs
- **In:** a Canadian company/issuer `name` (or the `employer-org`)
- **Out:** official filings listing `name`s of directors/officers, `associate` relationships, `employer-org` structure, business `address`
- **Empty/negative result looks like:** no matching issuer — the company may be private (not a reporting issuer), dissolved, or filed only provincially/elsewhere; try a provincial corporate registry instead.

## Gotchas & OpSec
- Scope is *reporting issuers* (public/regulated entities) only — private Canadian companies won't appear; use provincial registries for those.
- Bot-protection means human-in-the-loop (CAPTCHA/challenge); it resists automated scraping.
- Passive: querying the regulator never touches the subject.

## Overlaps ("do both")
- Complements provincial corporate registries and the U.S. SEC EDGAR — SEDAR+ covers Canadian securities filings; use EDGAR for U.S. issuers and a registry for private-company officers.

## Trust & verifiability
`trust: trusted` — SEDAR+ is the authoritative government-mandated filing system run by the Canadian Securities Administrators, so the documents are primary-source regulatory records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-for-company-documents |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, name, associate, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
