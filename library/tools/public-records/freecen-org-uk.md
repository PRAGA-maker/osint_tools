---
id: freecen-org-uk
name: freecen.org.uk
description: Use when you have a `name` and rough year/place in 19th–early-20th-century Britain and want free transcribed census records to place a person and their household — returns `name`, `address`, `associate` (household members), `employer-org` (occupation).
url: https://www.freecen.org.uk/
category: public-records
path:
- public-records
bestFor: Free, searchable UK census transcriptions (1841–1911) for placing historical individuals and mapping households.
selectorsIn:
- name
- address
selectorsOut:
- name
- address
- associate
- employer-org
status: live
pricing: free
costNote: Completely free; run by the Free UK Genealogy charity. No account required to search, though registration unlocks some features. Donations requested but never mandatory.
opsec: passive
opsecNote: A historical records archive — you query an index, not the target, and no account is required to search, so it leaks nothing about the subject. Standard browser hygiene only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Free UK Genealogy CIO, a registered charity; a well-established, volunteer-transcribed dataset — accurate but with known transcription/original-record errors.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- FreeCEN
- Free UK Genealogy census
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- census
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# freecen.org.uk

> Free, charity-run transcriptions of the British censuses (1841–1911) — search 50M+ records to place a historical person in a household and location at no cost.

## When to use
You have a `name` and a rough year and place in Britain (England, Wales, Scotland, Ireland, Channel Islands) between 1841 and 1911, and you want to place that person in a specific household and address, or map their family, occupation, and neighbours. Strongest for genealogy/deep-background work where you need free access to census households without a paid subscription.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.freecen.org.uk/ and go to the search.
2. Enter surname (required) plus optional forename, birth-year range, birth county, and census county/district; enable Soundex for spelling variants.
3. Filter by sex, marital status (1851+), or occupation to narrow common names.
4. Open a matching record to read the full household: everyone at that `address`, relationships, ages, birthplaces, and occupations.
5. Pivot: household members become `associate` leads; occupation gives `employer-org`; birthplaces/years feed BMD lookups on `[[scotlandspeople-gov-uk-2]]` or GRO/FreeBMD.

## Inputs → Outputs
- **In:** `name` (+ approximate year, birth county, census place)
- **Out:** `name`, `address` (census address), `associate` (household members + relationships), `employer-org` (occupation)
- **Empty/negative result looks like:** no matching entries — note coverage is incomplete (transcription is volunteer-driven and ongoing), so absence may mean "not yet transcribed for that district," not "not in the census." Try spelling variants and Soundex.

## Gotchas & OpSec
- Coverage is uneven by county/year because transcription is ongoing — a blank result is not conclusive.
- Both the original census and the transcription contain errors; verify against original images where it matters.
- Historical only (1841–1911) — no use for living-person lookups.
- Fully passive and free; no account needed.

## Overlaps ("do both")
- Pairs with `[[scotlandspeople-gov-uk-2]]` (authoritative Scottish records, pay-per-view) and paid aggregators like Ancestry/FindMyPast — FreeCEN is free but incomplete, so run both when a district isn't yet transcribed here.

## Trust & verifiability
`trust: trusted` — run by the Free UK Genealogy charity, a long-established transcription project. Reliable within its coverage; corroborate individual entries with original census images.
