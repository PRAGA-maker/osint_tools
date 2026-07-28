---
id: encoding-and-decoding-driver-s-license-numbers
name: Encoding and Decoding Driver's License Numbers
description: Use when you have a `name` + `dob` + sex (or a `document-id`) and want the algorithmic driver's-license number a state assigns — returns a candidate `document-id`, or reverses one back to identity fields.
url: https://stevemorse.org/dl/dl.html
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Encoding identity fields into (or decoding) the soundex-based driver's-license numbers used by certain US states.
selectorsIn:
- name
- dob
- document-id
selectorsOut:
- document-id
- name
- dob
status: live
pricing: free
costNote: Free; runs in-browser, part of Steve Morse's public genealogy toolset.
opsec: passive
opsecNote: The calculation runs client-side in JavaScript — nothing you type is sent to a server or to any subject. Fully local and passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-standing, well-regarded Steve Morse genealogy/OSINT toolset; the formulas apply ONLY to states that derive DL numbers algorithmically — states that assign random/sequential numbers cannot be encoded or decoded.
missingPersonsRelevance: low
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- brooklyn-genealogy
- chicago-cook-county-genealogy
- decoding-social-security-numbers
- familysearch-s-united-states-record-collections
- new-jersey-voter-records
- new-york-state-prison-records
- new-york-state-voter-records
- social-security-death-index
- street-name-changes
aliases:
- Steve Morse DL decoder
- driver's license number decoder
tags:
- driver-license
- document-id
- identity
- genealogy
source: osint4all
lastVerified: '2026-07-28'
enrichment: full
---

# Encoding and Decoding Driver's License Numbers

> Several US states build a driver's-license number from a soundex of the holder's name plus their birth date and sex — this tool computes that number, or reverses it back into those identity fields.

## When to use
- **Encode:** you have a subject's `name`, `dob`, and sex and want to derive the driver's-license `document-id` a formula-based state would assign — to corroborate or cross-check a claimed DL number.
- **Decode:** you have a `document-id` (a DL number) from a formula state and want to recover the encoded `name` initials, `dob`, and sex to verify it matches a person of interest.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://stevemorse.org/dl/dl.html.
2. Select the **state** (the tool supports the states that use algorithmic formats — e.g. Florida, Illinois, Wisconsin, Maryland, etc.).
3. To encode: enter name, date of birth, and sex → it outputs the computed DL number.
4. To decode: paste a DL number → it outputs the encoded birth date, sex, and name-soundex information.
5. Pivot: a matching encode/decode corroborates an identity; a mismatch flags a possibly fabricated or mistyped DL number. Cross-reference with other Steve Morse tools like [[decoding-social-security-numbers]].

## Inputs → Outputs
- **In:** `name` + `dob` + sex (encode) or `document-id` (decode)
- **Out:** a candidate DL `document-id`, or the decoded `name`/`dob`/sex fields
- **Empty/negative result looks like:** the chosen state doesn't use an algorithmic format (many don't), so no meaningful decode is possible — the number there is random/sequential and carries no embedded identity.

## Gotchas & OpSec
- **Formula states only.** Most states have moved to random numbers; this tool is useless for those, and a decode that "works" only means the format matched, not that the person is confirmed.
- Soundex encoding is lossy — decode gives name *initials/soundex*, not the full exact name; treat as corroboration, not identification.
- OpSec: fully client-side; nothing leaves your browser.

## Overlaps ("do both")
- Part of the Steve Morse toolset — pair with [[decoding-social-security-numbers]] and the genealogy/records tools it links to for broader identity corroboration.

## Trust & verifiability
`trust: community` — a respected, long-lived public tool; the math is deterministic and self-verifiable (encode then decode), but its usefulness is bounded to states with algorithmic DL formats.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | encoding-and-decoding-driver-s-license-numbers |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | name, dob, document-id → document-id, name, dob |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
