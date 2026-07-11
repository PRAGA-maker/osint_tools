---
id: irelandnursing-com
name: irelandnursing.com
description: Use when you have a `name` and want to check if they're a registered Irish nurse/midwife — returns license status and directory details for ~127k nurses (an unofficial mirror; confirm against NMBI).
url: https://www.irelandnursing.com/
category: public-records
path:
- public-records
bestFor: Quickly checking whether a name appears among registered Irish nurses/midwives and their license status.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
status: live
pricing: free
costNote: Free to search the directory of ~127,560 licensed nurses by name. No account or payment.
opsec: passive
opsecNote: You search a public third-party directory; nothing reaches the subject. Passive. Because it's an unofficial site, don't treat its output as authoritative — verify status on the official NMBI register.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An independent, third-party directory (with a reviews feature) that mirrors Irish nursing registration data — NOT the official regulator. The Nursing and Midwifery Board of Ireland (nmbi.ie) is the authoritative source; use this only as a quick index and confirm there.
missingPersonsRelevance: high
coverage:
- ie
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- nmbi-ie
aliases:
- Ireland Nursing
- irelandnursing.com
tags:
- professionlicensing
- Profession & Licensing Sites
- nursing
- ireland
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# irelandnursing.com

> A third-party, searchable directory of registered Irish nurses and midwives — a fast name index into the profession, to be confirmed against the official NMBI register.

## When to use
You have a `name` claimed to belong to an Irish nurse or midwife and want a quick check of whether it appears among registered practitioners and with what status. The directory covers roughly 127k licensed nurses and lets you filter by status (Active, Registered, Inactive, Suspended). Use it as a rapid first pass to confirm a profession claim or narrow candidates — then verify anything important on the official regulator's register, since this is an unofficial mirror.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.irelandnursing.com/.
2. Search by nurse `name`.
3. Review the matching entry: license/registration status and any listed provider/`employer-org` details.
4. Treat the result as provisional — cross-check the person and status directly on the official NMBI register (`[[nmbi-ie]]`, nmbi.ie).
5. Pivot: a confirmed registration corroborates a subject's profession; the status/provider can hint at where they work; combine with other Irish public records.

## Inputs → Outputs
- **In:** `name`
- **Out:** matching registrant → registration status, provider/`employer-org` details, confirmed `name`
- **Empty/negative result looks like:** no match — the person isn't in this directory under that name (a variant, a lapsed record, or simply not a registered Irish nurse). Because the source is unofficial, absence here is weaker than an official-register negative — check NMBI before concluding.

## Gotchas & OpSec
- Human-in-the-loop: none to search, but mandatory follow-up verification on the official register.
- OpSec: **passive** — a public directory; the subject isn't notified.
- It is **not** the official regulator and includes a user-review feature; data currency and accuracy aren't guaranteed. Never rely on it alone for a licensure decision.

## Overlaps ("do both")
- Pairs with `[[nmbi-ie]]` (the official Nursing and Midwifery Board of Ireland register) — use irelandnursing.com as a quick index and NMBI as the authoritative confirmation. Always finish on the official source.

## Trust & verifiability
`trust: community` — a convenient unofficial mirror of Irish nursing registration, useful for a fast lookup but not authoritative. Confirm every consequential result on nmbi.ie before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | irelandnursing-com |
| category | public-records |
| selectorsIn → selectorsOut | name → name, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
