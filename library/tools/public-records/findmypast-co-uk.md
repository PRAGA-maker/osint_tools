---
id: findmypast-co-uk
name: Findmypast
description: Use when you have a `name` (and rough era/place) and want UK/Irish genealogy and historical records — returns census, BMD, electoral, military and newspaper records revealing addresses, family and dates.
url: https://www.findmypast.co.uk/home.jsp
category: public-records
path:
- public-records
bestFor: UK & Irish family-history research — census, birth/marriage/death, electoral rolls and newspapers to reconstruct a person's history and relatives.
selectorsIn:
- name
- address
selectorsOut:
- address
- associate
- dob
- name
status: live
pricing: freemium
costNote: Free to register and search the indexes (hit counts and snippets), but viewing full records/images requires a paid subscription or pay-as-you-go credits.
opsec: passive
opsecNote: Searching queries Findmypast's own record indexes; the subject is never contacted. A subscription ties searches to an account and a payment method — use a sock-puppet identity, and cancel to avoid auto-renewal. Handle any living-person data (recent electoral rolls) within your legal basis.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Findmypast is a major, established UK/Irish genealogy provider with digitised primary-source collections (incl. the British Newspaper Archive). Records are authoritative primary sources; transcription/OCR errors occur.
missingPersonsRelevance: high
coverage:
- uk
- ie
auth: account
api: false
localInstall: false
registration: true
aliases:
- findmypast.co.uk
- Find My Past
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- genealogy
- census
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Findmypast

> A major UK/Irish genealogy platform indexing census, BMD, electoral, military and newspaper records — used to reconstruct a subject's address history, relatives and life dates.

## When to use
You have a `name` (with an approximate era, birth year, or place) and want to build the historical picture: where the person and their family lived (census, electoral rolls), when they were born/married/died (BMD), military service, and press mentions (British Newspaper Archive). Strong for UK/Irish subjects, for deceased persons, and for growing the `associate` graph around a living subject via older relatives and electoral-roll co-residents.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register (free) at https://www.findmypast.co.uk/ and open the record search.
2. Enter `name`, an approximate year/date range, and a place; filter by record set (census, BMD, electoral, newspapers, military).
3. Read the index hits — counts and snippets tell you which record is your subject before you pay.
4. Subscribe or use credits to open the full record/image when a snippet matches.
5. Pivot: census/electoral records give historical `address` and co-resident `associate`s; BMD gives `dob`/marriage/death; newspapers add narrative and named relatives.

## Inputs → Outputs
- **In:** `name` (+ approximate `dob`/era, place); sometimes `address` to search by residence
- **Out:** historical `address`, family/co-resident `associate`s, `dob`/BMD dates, confirmed `name` variants
- **Empty/negative result looks like:** zero index hits, or only same-name noise your date/place filters can't resolve — the person may be too recent (privacy windows redact recent census/electoral data) or simply not in these sets. Cross-check `[[ancestry]]`/`[[archives-com]]`.

## Gotchas & OpSec
- Human-in-the-loop: searching is free but full records sit behind a **subscription/credits** wall that auto-renews — cancel when done.
- Privacy windows redact recent census (100-yr) and current electoral data, so living subjects show limited results.
- Transcriptions/OCR carry errors — search with year tolerances and name variants; different providers digitise different sets, so a miss here isn't definitive.

## Overlaps ("do both")
- Pairs with `[[archives-com]]`, Ancestry and `[[rip-ie]]` — providers hold overlapping-but-different collections and transcribe the same source differently, so run more than one before concluding a record doesn't exist.

## Trust & verifiability
`trust: trusted` — a mainstream commercial genealogy provider indexing genuine primary-source records; authoritative, with transcription accuracy the main caveat.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | findmypast-co-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, address → address, associate, dob, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
