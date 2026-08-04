---
id: international-name-generator
name: International Name Generator (Behind the Name)
description: Use when you need a culturally-consistent persona `name` for a sock puppet — returns randomized first/middle/surname combinations filtered by nationality and gender.
url: https://www.behindthename.com/random/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Generating believable, nationality-appropriate names for investigative sock-puppet accounts.
selectorsIn: []
selectorsOut:
- name
status: live
pricing: free
costNote: Free to use with no account; part of the well-known Behind the Name reference site.
opsec: passive
opsecNote: This is an OpSec construction tool — it invents a name, it does not query anyone. Generate the persona name here, but build the actual account elsewhere with clean infrastructure (fresh email, sock-puppet browser, VPN). Avoid names distinctive enough to collide with a real, searchable person.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Behind the Name is a long-standing, reputable onomastics reference; its name and nationality data are well-sourced, making generated combinations culturally plausible.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- behind-the-name-arabic-names
- behindthenames
aliases:
- Behind the Name random name generator
- BTN random names
tags:
- sock-puppet
- persona-building
source: osint4all
lastVerified: '2026-08-04'
enrichment: full
---

# International Name Generator (Behind the Name)

> A nationality-aware random name generator — the persona-naming step of building a sock puppet that doesn't look machine-made or culturally out of place.

## When to use
You are creating an investigative sock-puppet identity and need a `name` that fits a chosen background: an account posing as, say, a Spanish or Japanese user needs a name that reads natively, not a random Western default. This generator produces first/middle/surname combinations filtered by 60+ nationalities and by gender, so the persona's name aligns with its claimed origin.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.behindthename.com/random/.
2. Set the filters: gender (masculine/feminine/ambiguous), nationality/origin, whether to include a surname, and how many middle names.
3. Generate one or several candidates; regenerate until you get a plausible, non-distinctive combination.
4. Sanity-check the chosen name isn't an existing well-known/searchable real person.
5. Pivot: take the name into your account-creation workflow with a matching, clean email and a hardened browser like [[gnu-icecat]].

## Inputs → Outputs
- **In:** none (you pick filters, not a subject selector)
- **Out:** a generated persona `name` (first + optional middle(s) + surname), nationality-consistent
- **Empty/negative result looks like:** N/A — it always returns names; the real failure is picking a name that's too rare/distinctive or accidentally matches a real person.

## Gotchas & OpSec
- **Consistency matters:** the name must match the persona's claimed nationality, age cohort and the rest of the backstory — a mismatched name is a tell.
- Cross-check the generated name against search engines/social sites so you don't impersonate a real, findable individual.
- Naming is only step one; the account's email, IP, device fingerprint and history must be equally clean or the persona is exposed.

## Overlaps ("do both")
- Pairs with the sock-puppet/OpSec tooling in this category — this supplies the name; a hardened browser ([[gnu-icecat]]), a burner email, and VPN/Tor supply the rest of the identity.

## Trust & verifiability
`trust: trusted` — a reputable, well-sourced onomastics site; the generated names are culturally accurate, which is exactly the property that makes them useful for believable personas.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | international-name-generator |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | — → name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
