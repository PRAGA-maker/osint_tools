---
id: business-govt-nz
name: business.govt.nz (ONECheck)
description: Use when you have a business `name`/brand and want to see if it is registered or claimed in New Zealand — returns availability across company/business name, trademark, web domain and social-media username in one search.
url: https://www.business.govt.nz/onecheck
category: public-records
path:
- public-records
bestFor: Cross-checking a New Zealand business/brand name against the companies register, IPONZ trademarks, domains and social handles at once.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- domain
- social-profile
- username
status: live
pricing: free
costNote: Free official New Zealand government tool (ONECheck); no account or payment required.
opsec: passive
opsecNote: A NZ government self-service lookup — you query registries, not the subject. No notification reaches anyone. Standard web hygiene (sock-puppet browser) is enough; the search itself is low-signal and unremarkable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the New Zealand Government (business.govt.nz), aggregating the Companies Register, IPONZ trademarks, and domain/social checks — an authoritative first-party source for the registry data.
missingPersonsRelevance: high
coverage:
- nz
auth: none
api: false
localInstall: false
registration: false
aliases:
- ONECheck
- OneCheck
- business.govt.nz
tags:
- companysites
- Company Related Sites
- new-zealand
- company-registry
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# business.govt.nz (ONECheck)

> New Zealand's official "one search" name checker — is this business name registered as a company, trademark, domain, or social handle?

## When to use
You have a business or brand `name` (perhaps a subject's claimed company, an employer, or a trading name from a document) and want to know whether it exists as a registered NZ entity and where else the name is claimed. Good for confirming whether an `employer-org` is a real registered company, and for spotting the matching web domain and social handles to pivot into.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.business.govt.nz/onecheck (it redirects to the tools2.business.govt.nz ONECheck app).
2. Type the business/brand `name` into the single search box and submit.
3. Read the four availability panels:
   - **Business/company name** — if "taken," the name maps to a registered NZ company (pivot into the Companies Register for directors/addresses).
   - **Trademark** — a registered IPONZ mark and its owner.
   - **Web domain** — whether the .nz/.com domain is registered (pivot to WHOIS).
   - **Social media username** — whether the handle exists on major platforms.
4. Interpret: "not available/taken" is the useful OSINT signal — it means the name is *in use* and points you to the record. "Available" means no registered footprint.
5. Pivot: a taken company name → NZ Companies Register for `employer-org` officers/`address`; a taken `domain` → WHOIS; a taken handle → `[[social-search-tools]]`.

## Inputs → Outputs
- **In:** business `name` / `employer-org`
- **Out:** registration status pointing to a registered `employer-org`, matching `domain`, and `social-profile`/`username` existence
- **Empty/negative result looks like:** all four panels show "available" — the name has no NZ business, trademark, domain, or social footprint, i.e. likely not a real trading entity under that exact name.

## Gotchas & OpSec
- It reports *availability*, not full records — it tells you a name is taken and links you onward, but you must open the Companies Register / IPONZ / WHOIS to get directors, addresses and dates.
- Exact-string matching: minor spelling/word-order variants read as "available." Try variants of the name.
- OpSec: **passive**, first-party government tool; nothing leaks to the subject.

## Overlaps ("do both")
- Pairs with `[[business-gov-au]]` for the Australian equivalent, and with a domain WHOIS lookup — ONECheck flags that a domain/company exists; the registries and WHOIS supply the officers, dates and contact records behind it.

## Trust & verifiability
`trust: trusted` — a New Zealand Government service aggregating official registers (Companies Office, IPONZ). The availability signals are authoritative; treat the linked underlying records as the verifiable evidence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | business-govt-nz |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org, domain, social-profile, username |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
