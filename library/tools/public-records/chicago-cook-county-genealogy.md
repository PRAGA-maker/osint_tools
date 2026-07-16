---
id: chicago-cook-county-genealogy
name: Steve Morse One-Step — Cook County (Chicago) Vital Records
description: Use when you have a name tied to Chicago/Cook County and want vital-record indexes — returns birth, marriage and death index entries to order the underlying certificate.
url: https://stevemorse.org/vital/cook.html
category: public-records
path:
- public-records
bestFor: Searching Cook County (Chicago) birth, marriage and death indexes to confirm dates and family links.
selectorsIn:
- name
selectorsOut:
- name
- dob
- associate
- document-id
status: live
pricing: freemium
costNote: The One-Step search forms are free; they query official/genealogical indexes, and ordering the actual certificate from the county/state costs a fee.
opsec: passive
opsecNote: You search public genealogical/government indexes, not the individual — no one is alerted. Steve Morse's forms are front ends that submit to the underlying record providers; use a VPN for sensitive work. This is historical vital-record research, inherently passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Steve Morse's One-Step Webpages are a long-respected, widely-cited genealogy resource; the forms query authoritative vital-record indexes (Illinois/Cook County, FamilySearch, etc.).
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- Steve Morse One-Step Cook County
- Chicago vital records search
- stevemorse.org cook
tags:
- vital-records
- genealogy
- chicago
- cook-county
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
relatedTools:
- brooklyn-genealogy
- decoding-social-security-numbers
- encoding-and-decoding-driver-s-license-numbers
- familysearch-s-united-states-record-collections
- new-jersey-voter-records
- new-york-state-prison-records
- new-york-state-voter-records
- social-security-death-index
- street-name-changes
---

# Steve Morse One-Step — Cook County (Chicago) Vital Records

> A single hub of search forms into Cook County / Chicago birth, marriage and death indexes — the genealogist's shortcut to confirming a person's dates and family before ordering the certificate.

## When to use
You have a `name` with a Chicago / Cook County connection and want to pin down a birth, marriage or death: exact dates, a mother's maiden name, a spouse, or confirmation someone is deceased. Steve Morse's One-Step page bundles the fiddly official and genealogical index searches (Illinois statewide indexes, Cook County clerk, FamilySearch) into clean forms, so you can confirm vital facts and family links that anchor identity and timeline.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://stevemorse.org/vital/cook.html.
2. Pick the record type — birth, marriage, or death index — and the corresponding search form.
3. Enter the `name` (and, where offered, year range, spouse, or parents) and submit; the form queries the underlying index provider.
4. Read the index hit: names, dates, certificate/registration numbers (`document-id`), and related parties (spouse, parents).
5. Pivot: a certificate number lets you order the full record from the county/state; parent/spouse names are `associate`s for further searches; a death index entry confirms status and date.

## Inputs → Outputs
- **In:** a `name` (optionally with year range, spouse or parents)
- **Out:** index entries giving `name`, `dob`/event dates, `associate`s (spouse/parents), and certificate `document-id`s
- **Empty/negative result looks like:** no index match — the event may fall outside the indexed years, be spelled differently, or sit in another county. Adjust name spelling and year range, and try the statewide (not just Cook) forms.

## Gotchas & OpSec
- These are **indexes**, not the certificates themselves; the index confirms existence and gives the number, then you order the document (paid) for full detail.
- Indexed date ranges vary by record type — an absence often means "outside the covered years," not "no record."
- Forms depend on the upstream providers (FamilySearch, county/state sites); if one form breaks, the provider changed, not necessarily the fact.
- Passive historical research — nobody is notified.

## Overlaps ("do both")
- Pairs with `[[free-public-records-directory-us]]` and `[[state-appellate-and-supreme-courts]]` to move from a vital-record confirmation into court/property records for the same person.
- Complements broader people-search once a maiden name, spouse or parent emerges.

## Trust & verifiability
`trust: trusted` — Steve Morse's One-Step is a decades-established, heavily-used genealogy resource that queries authoritative vital-record indexes; the index is reliable for confirming existence/dates, and the ordered certificate is the definitive proof.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | chicago-cook-county-genealogy |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, associate, document-id |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
