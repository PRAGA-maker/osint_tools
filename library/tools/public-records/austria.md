---
id: austria
name: Austria
description: Use when you have an Austrian company `employer-org` or a person's `name` and want the registered beneficial owners behind it — returns name, dob, and address of controlling persons (access-gated).
url: https://wieregms.bmf.gv.at/at.gv.bmf.wiereg-p/wiereg?execution=e1s1
category: public-records
path:
- public-records
bestFor: Identifying the ultimate beneficial owners of Austrian companies and other legal entities via the WiEReG register.
selectorsIn:
- employer-org
- name
selectorsOut:
- name
- dob
- address
status: live
pricing: freemium
costNote: Government register (WiEReG). Public inspection extracts carry a small per-extract fee (~€3) and require an authenticated Unternehmensserviceportal (USP)/FinanzOnline account; broader access requires demonstrating a legitimate interest after the 2022 CJEU ruling.
opsec: active
opsecNote: Access is via authenticated Austrian portal login (USP/FinanzOnline/eID). Every query is logged against your identity and extracts are paid/receipted — this is a named, auditable interaction, not anonymous OSINT. Do not access under a false identity.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
- legal-gate
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Austrian Federal Ministry of Finance register of beneficial owners (Register der wirtschaftlichen Eigentümer); data is legally mandated and authoritative.
missingPersonsRelevance: high
coverage:
- at
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- belgium
- opencorporates-com
- gleif-org
aliases:
- WiEReG
- Register der wirtschaftlichen Eigentuemer
- Austrian beneficial ownership register
tags:
- companysites
- Company Related Sites
- beneficial-ownership
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Austria

> Austria's WiEReG — the legally-mandated register of beneficial owners: find the natural persons who control an Austrian company, behind an authenticated, paid access gate.

## When to use
You have an Austrian `employer-org` (company, partnership, foundation, or trust) and need the ultimate beneficial owners — the natural persons who own or control it — or you have a `name` and want the Austrian entities they beneficially own. WiEReG records the owner's name, date of birth, nationality, residence, and the nature/extent of their control, tying a subject to companies, assets, and co-owners.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to the WiEReG management system (https://wieregms.bmf.gv.at/...) and authenticate via Unternehmensserviceportal (USP), FinanzOnline, or Austrian eID.
2. For public inspection ("öffentliche Einsicht"), request an extract for the target entity; a small fee applies per extract, and legitimate-interest justification may be required.
3. Search by the entity's Firmenbuch (company register) number or name.
4. Read the beneficial-owner extract: name, DOB, nationality, residence, and control details.
5. Pivot: named owners and their DOB/residence feed people-search; the Firmenbuch number feeds the Austrian company register and [[opencorporates-com]].

## Inputs → Outputs
- **In:** `employer-org` (entity / Firmenbuch number) or `name`
- **Out:** `name`, `dob`, `address` (residence) of beneficial owners, plus control percentage/nature
- **Empty/negative result looks like:** access denied (no legitimate interest / not authenticated), or an entity relying on a "top management" fallback beneficial owner when no qualifying owner exists — not a data error.

## Gotchas & OpSec
- **Access tightened** after the 2022 CJEU ruling — general anonymous public browsing was curtailed; expect authentication, a fee, and possibly a legitimate-interest gate.
- German-language interface; entity identification is via the Firmenbuch number.
- Human-in-the-loop: authenticated portal login **and** paid extract.
- OpSec: **active and named** — access is tied to your verified identity and receipted. Treat as a formal request, not covert OSINT.

## Overlaps ("do both")
- Pairs with [[opencorporates-com]] and [[gleif-org]] (identify the Austrian entity and its directors/LEI without the gate first), and mirrors [[belgium]] as the equivalent EU beneficial-ownership register — use the same standing/access playbook.

## Trust & verifiability
`trust: trusted` — it is the official Austrian beneficial-ownership register with legally mandated, penalty-backed filings, so the data is authoritative where you can access it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | austria |
| category | public-records |
| selectorsIn → selectorsOut | employer-org, name → name, dob, address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login, payment-wall-partial, legal-gate) |
