---
id: rcvs-org-uk
name: rcvs.org.uk
description: Use when you have a `name` and want to confirm/locate a UK veterinary surgeon or nurse — returns registration status, qualifications, and the practice `address`/`employer-org` from the RCVS official register.
url: https://findavet.rcvs.org.uk/home/
category: public-records
path:
- public-records
bestFor: Verifying a UK vet/veterinary nurse's registration and finding their practice location.
selectorsIn:
- name
- address
selectorsOut:
- address
- employer-org
- name
status: live
pricing: free
costNote: Free official register search. No account or payment.
opsec: passive
opsecNote: You search a public professional register; the registrant is not contacted or notified. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The Royal College of Veterinary Surgeons is the statutory UK regulator of vets and vet nurses; its "Find a Vet" register is the authoritative source for who is legally registered to practise.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- gmc-org-uk
- hcpc-org-uk
aliases:
- RCVS Find a Vet
- Royal College of Veterinary Surgeons register
tags:
- professionlicensing
- Profession & Licensing Sites
- veterinary
- uk
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# rcvs.org.uk

> The Royal College of Veterinary Surgeons' official "Find a Vet" register — confirm whether a person is a registered UK vet or veterinary nurse and where they practise.

## When to use
You have a `name` claimed to be a UK veterinary surgeon or nurse and want to verify it and locate them professionally. The register confirms current registration status, qualifications and year/place of qualification, and lists the practice/`employer-org` and its `address` — useful for confirming a subject's profession, catching false claims, and locating a vet through their workplace when a home address is unknown.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://findavet.rcvs.org.uk/home/.
2. Search the "Check the Register" / vet or vet-nurse search by `name` (or search practices by `address`/area).
3. Open the matching entry: registration status, qualifications, and the associated practice name and location.
4. Note the practice `address`/`employer-org` and registration validity.
5. Pivot: the practice location narrows `geolocation`; the confirmed identity/qualification corroborates the subject; cross-check other UK regulators (`[[gmc-org-uk]]`, `[[hcpc-org-uk]]`) if the person claims multiple professions.

## Inputs → Outputs
- **In:** `name` (or `address`/area for practice search)
- **Out:** registration status, qualifications, practice `employer-org` + `address`, confirmed `name`
- **Empty/negative result looks like:** no matching registrant — the person isn't a currently registered UK vet/vet-nurse under that name (possible false claim, name variant, or a non-UK/lapsed registration). It is a confident negative for *current UK registration*.

## Gotchas & OpSec
- Human-in-the-loop: none; a simple register lookup.
- OpSec: **passive** — a public regulator's register; nobody is notified.
- The register reflects current registration; a struck-off or lapsed individual may show as not registered or with a status note — read the status carefully.

## Overlaps ("do both")
- Pairs with other UK statutory registers — `[[gmc-org-uk]]` (doctors), `[[hcpc-org-uk]]` (allied health) — when a subject's claimed profession is uncertain; run the register matching the claim to confirm or debunk it.

## Trust & verifiability
`trust: trusted` — the statutory regulator's own register, so registration and practice data are authoritative. Confirm you have the right individual (common names) via qualification year and practice details before relying on a match.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rcvs-org-uk |
| category | public-records |
| selectorsIn → selectorsOut | name, address → address, employer-org, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
