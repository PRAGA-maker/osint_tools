---
id: iid-generator-by-georgy-bunin
name: IID Generator by Georgy Bunin
description: Use when you have an Israeli ID number (`document-id`) to validate, or need a format-valid Israeli ID for a sock puppet — returns a valid/invalid verdict or a checksum-valid number.
url: https://georgybu.github.io/IID_Generator/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Validating or generating checksum-correct Israeli national ID (Teudat Zehut) numbers.
selectorsIn:
- document-id
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free static web tool hosted on GitHub Pages; no account, open source.
opsec: passive
opsecNote: All computation is client-side (a checksum algorithm), so nothing is sent to a server and no record is queried — validating or generating a number touches no database and no target. A "valid" verdict means the number passes the check-digit formula only; it does NOT mean the ID belongs to a real, living person or matches any record. Never present a generated ID as a real person's identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Small open-source project (GitHub Pages, code public); the underlying Israeli ID check-digit algorithm is public and standard, so results are easy to verify.
missingPersonsRelevance: low
coverage:
- il
auth: none
api: false
localInstall: false
registration: false
aliases:
- Israeli ID generator
- Teudat Zehut validator
- IID Generator
tags:
- Sock Puppets
- id-validation
source: osint4all
lastVerified: '2026-08-05'
enrichment: full
---

# IID Generator by Georgy Bunin

> A client-side Israeli ID (Teudat Zehut) generator and validator — checks a number's control digit, or emits a format-valid one for a sock puppet.

## When to use
Two narrow, Israel-specific cases. Validation: you have encountered an Israeli ID number (`document-id`) in a document, listing, or leak and want a quick sanity check that it is at least structurally valid before treating it as real. Generation: you are building an Israeli-context sock puppet and a form needs a checksum-valid ID in the right format. It confirms structure only — it never proves a number maps to a real person, and it queries no register.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://georgybu.github.io/IID_Generator/.
2. To validate: paste the 9-digit ID; it reports "Valid" or "Not valid" based on the check-digit algorithm.
3. To generate: use the generate function for a checksum-correct number.
4. Interpret strictly: "valid" = passes the formula, nothing more.
5. Pivot: a structurally-invalid ID in a document is a red flag (typo or fabrication); a valid one still needs corroboration against an authoritative source you are permitted to use.

## Inputs → Outputs
- **In:** an Israeli ID `document-id` (to validate) — or none (to generate)
- **Out:** a valid/invalid verdict, or a checksum-valid `document-id`
- **Empty/negative result looks like:** "Not valid" — the number fails the control-digit check, so it is malformed or mistyped; it says nothing about whether a valid number is genuinely in use.

## Gotchas & OpSec
- Human-in-the-loop: none; instant client-side calculation.
- OpSec: fully passive and offline-capable — no server call, no lookup, no trace. The misuse line matters: a generated ID is format-only fiction; never assert it as a real identity on any legal/financial document.
- Israel-specific; useless for other jurisdictions' ID schemes.

## Overlaps ("do both")
- Pairs with `[[fake-generator-tools]]` and `[[vcc-generator]]` — those build the broader sock-puppet persona and its card field; this fills an Israeli ID field with a checksum-correct value when the context demands one.

## Trust & verifiability
`trust: community` — a tiny open-source utility implementing a public, well-known algorithm; you can independently re-check any verdict with the standard Teudat Zehut check-digit formula.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | iid-generator-by-georgy-bunin |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | document-id → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
