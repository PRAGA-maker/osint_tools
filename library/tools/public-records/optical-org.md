---
id: optical-org
name: GOC Register (opticians, UK)
description: Use when you have a `name` and want to confirm a UK optician/optometrist's registration and practice — returns registrant status, registration number, and (for businesses) registered details.
url: https://www.optical.org/
category: public-records
path:
- public-records
bestFor: Confirming a person is a GOC-registered optometrist/dispensing optician in the UK and their registration status.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- employer-org
status: live
pricing: free
costNote: Free public register search operated by the UK General Optical Council; no account or payment required.
opsec: passive
opsecNote: Public register lookup — the registrant is not notified. Anonymous; standard browsing hygiene suffices.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the General Optical Council (GOC), the UK statutory regulator of optical professionals — a first-party authoritative register.
missingPersonsRelevance: medium
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- General Optical Council
- GOC register
- optical.org
tags:
- professionlicensing
- Profession & Licensing Sites
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# GOC Register (opticians, UK)

> The General Optical Council's public register — confirms whether a person is a registered UK optometrist or dispensing optician, and lists registered optical businesses.

## When to use
You have a `name` (or a business/`employer-org`) and want to confirm someone is a GOC-registered optical professional and in good standing. A licensing-verification/corroboration step: it confirms a stated profession and can tie a person to a registered optical business, but it is a narrow-scope tool (only optical professionals).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.optical.org/ and go to "Check the register."
2. Choose the search type: individual practitioner or body corporate (registered business); use advanced search to narrow.
3. Enter the `name` (or business/`employer-org`) and read the result: registrant name, registration number, category, and status.
4. Note any conditions/removals shown, which indicate fitness-to-practise outcomes.
5. Pivot: a confirmed registration corroborates identity/occupation; a registered business feeds company/records lookups.

## Inputs → Outputs
- **In:** `name` or business/`employer-org`
- **Out:** registrant `name`, registration number, category, status; registered optical business details
- **Empty/negative result looks like:** no match — the person isn't a current GOC registrant (not an optician/optometrist, registered elsewhere, or removed); absence is scope-limited, not proof of anything broader.

## Gotchas & OpSec
- Narrow scope: optical professionals only — irrelevant outside that occupation.
- Jurisdiction: UK-wide GOC register; other healthcare roles have their own regulators (GMC, NMC, GDC, etc.).
- OpSec: passive; the lookup is invisible to the registrant.

## Overlaps ("do both")
- Pairs with `[[lawsociety-org-uk]]` and other UK professional registers — same pattern (confirm a licensed profession and tie the person to a workplace), each covering a different occupation.

## Trust & verifiability
`trust: trusted` — a first-party GOC statutory register; a match authoritatively confirms optical-professional registration and status.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | optical-org |
| category | public-records |
| selectorsIn → selectorsOut | name → name, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
