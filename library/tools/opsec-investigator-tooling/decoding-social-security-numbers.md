---
id: decoding-social-security-numbers
name: Decoding Social Security Numbers
description: Use when you have a pre-2011 US `document-id` (SSN) and want its likely issuing state and issue-year range — returns a geographic/temporal lead, not identity.
url: https://stevemorse.org/ssn/ssn.html
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Decoding the area/group digits of an older US Social Security Number to its likely state and approximate year of issue.
selectorsIn:
- document-id
selectorsOut:
- geolocation
- dob
status: live
pricing: free
costNote: Free single-page tool on Stephen Morse's One-Step site; no account, runs in the browser.
opsec: passive
opsecNote: A local/in-browser lookup table — it computes from the number you enter and does not query any government system, so nothing is logged externally about the SSN. You are still handling sensitive PII; only enter an SSN you are lawfully entitled to process, and do so on a trusted machine.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Part of Stephen P. Morse's well-known One-Step genealogy toolset; the SSA numbering scheme it decodes only applies to SSNs issued before randomization in June 2011.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- social-security-death-index
- encoding-and-decoding-driver-s-license-numbers
- brooklyn-genealogy
- chicago-cook-county-genealogy
- familysearch-s-united-states-record-collections
- new-jersey-voter-records
- new-york-state-prison-records
- new-york-state-voter-records
- street-name-changes
aliases:
- SSN decoder
- Stephen Morse SSN
- One-Step SSN
tags:
- ssn
- identity-analysis
- genealogy
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Decoding Social Security Numbers

> A One-Step lookup that reads the structure of an older US SSN — turning the area/group digits into a likely issuing state and issue-year range, a corroboration lead for identity work.

## When to use
You have a US Social Security Number issued **before June 2011** (as a `document-id` from a record, form, or genealogy source) and want to test whether it's consistent with a person's claimed history — e.g. does the number's implied issuing state and issue period match where and when the subject says they were around when they got it. It is a consistency/lead tool for genealogy and identity verification, not a way to look someone up from an SSN.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://stevemorse.org/ssn/ssn.html.
2. Enter the SSN (or just the area/group digits) into the decoder.
3. Read the output: the likely **state** the number was issued in (from the area number) and an approximate **issue-date range** (from the group number's known issuance timeline).
4. Compare against the subject's biography — a mismatch (e.g. a number issued in a state the person had no tie to) is a flag worth explaining.
5. Pivot: pair the decoded state/era with vital-records and death-index searches for the same person.

## Inputs → Outputs
- **In:** `document-id` (a pre-2011 US SSN or its area/group digits)
- **Out:** likely issuing-state `geolocation` and an approximate issue-year range (a loose `dob`-era corroborator, since SSNs were often issued in youth)
- **Empty/negative result looks like:** an SSN issued after mid-2011 decodes to nothing meaningful — randomization removed geographic/temporal structure, so treat "no signal" as expected for recent numbers.

## Gotchas & OpSec
- **Only works on pre-June-2011 SSNs.** The SSA randomized issuance in 2011, so numbers from then on carry no state/date information — do not infer anything from them.
- The result is the number's *issuing* state and era, not necessarily the person's birthplace or current location.
- Handle SSNs lawfully — this is sensitive PII; the tool runs locally and logs nothing, but your obligations around the number remain.

## Overlaps ("do both")
- Pairs with `[[social-security-death-index]]` — decode the number's origin here, then check the SSDI to see if the holder is recorded deceased and cross-check the issuing state.

## Trust & verifiability
`trust: community` — part of Stephen Morse's respected One-Step genealogy toolkit, encoding the publicly-documented SSA numbering scheme. Reliable within its scope (pre-2011 numbers); inherently silent on randomized modern SSNs.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | decoding-social-security-numbers |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | document-id → geolocation, dob |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
