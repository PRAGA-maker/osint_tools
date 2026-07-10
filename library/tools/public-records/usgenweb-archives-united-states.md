---
id: usgenweb-archives-united-states
name: USGenWeb Archives (United States)
description: Use when you have a `name` and want transcribed US genealogical records — obituaries, wills, cemetery, census, and marriage records — returns `associate`, `address`, and `dob`/death dates from historical documents.
url: http://www.usgwarchives.net
category: public-records
path:
- public-records
bestFor: Free county-by-county US genealogical records (wills, cemeteries, obituaries, census, marriages) transcribed by volunteers.
selectorsIn:
- name
- address
selectorsOut:
- associate
- address
- dob
status: live
pricing: free
costNote: Entirely free and volunteer-run; no account, subscription, or payment. Funded by donations.
opsec: passive
opsecNote: Passive reading of a public archive — the target is not notified and nothing is submitted. Standard sock-puppet browsing hygiene is enough; there is no login or query that reaches the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Volunteer-transcribed records under the long-running USGenWeb Project; transcriptions are generally reliable but can contain typos or gaps and should be confirmed against original documents where accuracy matters.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- rootsweb-2
- cyndi-s-list
- billiongraves-com
aliases:
- USGenWeb Archives
- usgwarchives.net
tags:
- toddington
- curated-directory
- genealogy
- specialty-search
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# USGenWeb Archives (United States)

> A free, volunteer-built library of transcribed US public records — wills, cemeteries, obituaries, census, marriages — organised state-by-state and county-by-county.

## When to use
You have a `name` (and ideally a US state or county) and need historical or genealogical corroboration: a death/obituary, a will naming relatives, a cemetery listing, a census household, or a marriage record. This is a strong pivot when building a family tree around a missing person or confirming an older subject's relatives, dates, and last-known places.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.usgwarchives.net (if the apex host is briefly unavailable, use the state index directly, e.g. `/ny/nyfiles.htm`).
2. Drill down by **state → county**, then choose the record type (Obituaries, Wills, Cemeteries, Census, Marriages, Court, Pension, Special Collections).
3. Browse or use the site search to find the subject `name`. Records are transcribed text files, so exact spelling matters — try `name` variants.
4. Read the transcription for pivotable detail: relatives named in a will (`associate`), residence (`address`), and birth/death (`dob`/death) dates.
5. Pivot: feed named relatives back into people-search, or cross-check a death date against `[[billiongraves-com]]` and obituary sites.

## Inputs → Outputs
- **In:** `name` (+ US state/county context helps enormously), sometimes `address`
- **Out:** `associate` (relatives, executors, witnesses), `address` (residence, cemetery), `dob` and death dates
- **Empty/negative result looks like:** a county with sparse coverage returns nothing for a common name — absence here is not proof the person is absent from records; coverage is uneven because it depends on volunteer transcription.

## Gotchas & OpSec
- Human-in-the-loop: none; it is a browse-and-read archive.
- OpSec: fully passive — no login, no query reaches the subject.
- Coverage is patchy and uneven by state/county because everything is volunteer-transcribed. Missing data ≠ no data; the original may exist off-site.
- Transcriptions can contain errors; confirm critical facts (dates, spellings) against the cited original source.

## Overlaps ("do both")
- Pairs with `[[rootsweb-2]]` — both are community genealogy archives with different holdings; run the same name through each.
- Use `[[cyndi-s-list]]` as a directory to find additional record collections for the same locale, and `[[billiongraves-com]]` to confirm burial/death details.

## Trust & verifiability
`trust: community` — part of the long-running USGenWeb Project, staffed by volunteers. Individual transcriptions are usually faithful but unverified against originals, so treat findings as strong leads and cite the underlying document when precision counts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | usgenweb-archives-united-states |
| category | public-records |
| selectorsIn → selectorsOut | name, address → associate, address, dob |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
