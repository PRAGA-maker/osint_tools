---
id: courtlistener
name: CourtListener
description: Use when you have a party `name`, docket number, or judge and want free US court records — returns opinions, dockets, and filings that often expose addresses and associates.
url: https://courtlistener.com/
category: public-records
path:
- public-records
- court-criminal-records
bestFor: Free full-text search of US federal (and growing state) court opinions and PACER dockets by party name or case number.
selectorsIn:
- name
- document-id
selectorsOut:
- name
- associate
- address
status: live
pricing: free
costNote: Free and nonprofit (Free Law Project); the RECAP archive and API are free. Some documents not yet in RECAP require a (paid) PACER pull done elsewhere.
opsec: passive
opsecNote: Searching is anonymous and parties aren't notified. No account needed to search (an optional free account enables alerts). Court records are public but contain sensitive PII — handle responsibly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Run by the Free Law Project, a respected nonprofit; data is sourced from official court opinions and the RECAP archive of PACER filings.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- courtlistener-recap
- pacer
- docket-alarm
aliases:
- Free Law Project CourtListener
- courtlistener.com
tags:
- court-records
- litigation
- recap
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# CourtListener

> The Free Law Project's free court-records search — opinions plus the RECAP archive of PACER dockets, searchable by party without a paywall.

## When to use
You want to know if a subject appears in US court records without paying PACER/Docket Alarm fees. CourtListener covers federal appellate/district opinions and a large, growing archive of PACER dockets (via RECAP), plus increasing state coverage. Filings routinely name a person's address, employer, relatives, and associates and pin their situation to a date — valuable for locating someone or reconstructing a background. Start here as the free first pass before paid tools.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://courtlistener.com/ and search by party `name`, docket number, judge, or full-text keyword.
2. Filter by court, date, and document type; open opinions or docket entries.
3. For dockets, read the party/filing list; documents already in RECAP are free to view (those not yet archived link to PACER, which charges).
4. Optionally create a free account to set alerts on a name or case for new filings.
5. Pivot: addresses/relatives/employers in filings → people-search and address tools; a docket number → cross-check `[[pacer]]`/`[[docket-alarm]]`; install the RECAP extension to auto-contribute/pull docs.

## Inputs → Outputs
- **In:** party `name`, docket/case number (`document-id`), or judge
- **Out:** opinions, dockets, filings; filings often reveal `address`, `associate`, employer, and confirmed `name`
- **Empty/negative result looks like:** no results — the person isn't in covered records, the matter is in a not-yet-archived court, or the name differs; a null isn't proof of no litigation (try PACER/Docket Alarm and name variants).

## Gotchas & OpSec
- RECAP is huge but not complete — some dockets/documents aren't archived yet and require a paid PACER pull; absence here ≠ absence of a case.
- State-court coverage is growing but uneven; federal is strongest.
- Court filings contain sensitive PII (SSNs are usually redacted, but addresses/relatives aren't) — handle with care.

## Overlaps ("do both")
- Pairs with `[[docket-alarm]]` — Docket Alarm has broader state coverage and richer alerts (paid); CourtListener is the free federal-strong option. Run both.
- Pairs with `[[pacer]]` for authoritative federal documents not yet in RECAP.

## Trust & verifiability
`trust: trusted` — a respected nonprofit sourcing official opinions and PACER filings. Records are authoritative; verify any not-yet-archived document against PACER directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | courtlistener |
| category | public-records |
| selectorsIn → selectorsOut | name, document-id → name, associate, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
