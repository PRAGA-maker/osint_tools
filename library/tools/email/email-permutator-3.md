---
id: email-permutator-3
name: Email Permutator
description: Use when you have a `name` and a company `domain` and want candidate email addresses to test — returns a list of likely `email` variants.
url: https://docs.google.com/spreadsheets/d/17URMtNmXfEZEW9oUL_taLpGaqTDcMkA79J8TRw4xnz8/edit#gid=0
category: email
path:
- email
bestFor: Generating the ~40 most common email formats for a person at a given domain, to then verify.
selectorsIn:
- name
- domain
selectorsOut:
- email
status: live
pricing: free
costNote: Free public Google Sheet; make your own copy (File → Make a copy) to use it. No account beyond a Google login to copy.
opsec: passive
opsecNote: Generation is entirely offline math in a spreadsheet — nothing is sent to the target. The OpSec risk is in the NEXT step (verifying the guesses), not here. Keep the sheet in a sock-puppet Google account if you're being careful about attribution.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A widely-shared community spreadsheet (the classic "email permutator" pattern); it only produces candidates, so there is no data-quality claim to trust — verification happens elsewhere.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- email permutator
- email generator
tags:
- Emails
- email-generation
- email-guessing
source: cyb-detective
lastVerified: '2026-07-11'
enrichment: full
---

# Email Permutator

> The classic "type a name and domain, get 40-odd plausible email formats" spreadsheet — a candidate generator, not a lookup.

## When to use
You have a subject's `name` (first/last, maybe middle) and a `domain` (their employer, school, or personal domain) and need the actual `email`. The permutator produces every common layout — `first.last@`, `flast@`, `first@`, `f.last@`, `firstl@`, etc. — so you have a finite list to run through a verifier or SMTP/existence check.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the sheet and **File → Make a copy** (you can't edit the public original).
2. Enter first name, middle (if any), last name, and the `domain` in the input cells.
3. The sheet auto-fills ~40+ permutations in the output column.
4. Copy the list into an email-verification tool / breach-lookup / SMTP check to find which one actually exists.
5. Pivot: a confirmed address feeds account-existence oracles like `[[account-live-com]]` and breach/enrichment tools.

## Inputs → Outputs
- **In:** `name`, `domain`
- **Out:** `email` (a list of candidate addresses)
- **Empty/negative result looks like:** the sheet always generates candidates — "empty" only means you left an input blank. The real negative signal comes downstream when *none* of the candidates verify.

## Gotchas & OpSec
- This step proves nothing: it emits guesses. Never treat a generated address as the subject's real email until a verifier confirms it.
- Non-Latin names, hyphenated surnames, and nicknames break the standard patterns — add manual variants.
- OpSec: generation is **passive**; the exposure risk is entirely in how you verify the guesses (SMTP probing can alert a mail admin) — choose a passive verifier where possible.

## Overlaps ("do both")
- Pairs with account-existence and breach tools — the permutator makes the list, those tools tell you which entry is real and active.

## Trust & verifiability
`trust: community` — it is just spreadsheet formulas replicating the well-known permutator pattern; correctness of an *individual* address is never implied, only that it is a plausible format to test.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | email-permutator-3 |
| category | email |
| selectorsIn → selectorsOut | name, domain → email |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
