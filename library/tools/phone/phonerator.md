---
id: phonerator
name: Phonerator
url: https://www.martinvigo.com/phonerator/
category: phone
path:
- phone
description: Use when you have a partial/masked `phone` (e.g. a recovery hint) and want the full number — returns valid candidate numbers to test against other lookups.
bestFor: Turning a masked phone hint (like a password-recovery "•••• ••89") into a shortlist of valid, dialable candidate numbers.
selectorsIn:
- phone
selectorsOut:
- phone
status: live
pricing: free
costNote: Free web tool by security researcher Martin Vigo; no account or payment.
opsec: passive
opsecNote: Generation is local/reference-based — it does NOT dial or query subscribers, so it is passive. The active risk is in what you do next: validating candidates against other services or calling them can be active/attributable, so throttle and use passive validators first.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Built by a known security researcher and widely cited in phone-OSINT workflows; it generates candidates from real numbering-plan/rate-center data, but output is a candidate set, not confirmed numbers.
missingPersonsRelevance: high
coverage:
- us
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Phonerator
- Martin Vigo phone number generator
tags:
- phone
- number-generation
- masked-recovery
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Phonerator

> An advanced valid-phone-number generator — the classic tool for completing a masked recovery hint into a shortlist of real, dialable candidate numbers.

## When to use
You have a partial or masked `phone` — most often the "we'll text a code to •••-•••-••89" hint leaked by a password-recovery flow (see `[[account-live-com]]`) — and you want to reconstruct the full number. Phonerator generates numbering-plan-valid candidates matching the known digits and region, giving you a finite set to test against reverse lookups until one confirms.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.martinvigo.com/phonerator/.
2. Set the country and (for the US) state and rate center to constrain to valid numbering.
3. Enter the known/masked digits pattern; generate the candidate list of valid numbers.
4. Take the candidates to passive validators/reverse lookups (`[[ipqualityscore-com-2]]`, `[[spydialer-reverse-phone-lookup]]`) to find which one resolves to the subject.
5. Pivot: a confirmed number feeds phone-OSINT, messaging-app checks, and account-existence pivots.

## Inputs → Outputs
- **In:** partial/masked `phone` + region
- **Out:** a shortlist of numbering-plan-valid candidate `phone` numbers
- **Empty/negative result looks like:** a very large candidate set (too few known digits to narrow) — meaning you need more masked digits/region before candidates are testable. The tool never confirms a number; it only enumerates valid possibilities.

## Gotchas & OpSec
- Output is candidates, not answers — you must validate each externally to find the real number.
- Too little known information yields an unmanageable list; it works best with several fixed digits + region.
- OpSec: generation is passive, but validating/calling candidates is where attribution risk lives — start with passive lookups and throttle; never mass-dial.

## Overlaps ("do both")
- Pairs with `[[account-live-com]]` (source of masked hints), then `[[ipqualityscore-com-2]]`/`[[spydialer-reverse-phone-lookup]]` to test candidates — generate here, validate there.

## Trust & verifiability
`trust: community` — a well-regarded researcher tool that generates from real numbering data; reliable at producing *valid* candidates, but confirming *the* number is always a downstream verification step.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | phonerator |
| category | phone |
| selectorsIn → selectorsOut | phone → phone |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
