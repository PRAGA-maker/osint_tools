---
id: guernseyroyalcourt-gg
name: Guernsey Royal Court — BDM, Wills & Deed Polls
description: Use when you have a `name` with a Guernsey nexus and need birth/death/marriage, will, deed-poll or power-of-attorney records — returns vital-record and legal-document access via a manual request to the Greffe.
url: https://www.guernseyroyalcourt.gg/article/1637/Births-Deaths-Marriages-Wills-and-Deed-Polls
category: public-records
path:
- public-records
bestFor: Obtaining Guernsey vital records (births, deaths, marriages), wills, deed polls and POAs by request from the Royal Court's Greffe.
selectorsIn:
- name
selectorsOut:
- name
- dob
- associate
status: live
pricing: freemium
costNote: The information page is free, but obtaining certificates is paid per document (birth/death certificates ~£40, marriage ~£31); archive (Strongroom) research is by appointment.
opsec: passive
opsecNote: Requesting a record from the Greffe is passive with respect to the subject (they are not notified), but you identify yourself to a court registry when you make the request. There is no anonymous online search.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: His Majesty's Greffier / Registrar-General of the Bailiwick of Guernsey; authoritative custodian of the island's vital and legal records.
missingPersonsRelevance: medium
coverage:
- gg
auth: none
api: false
localInstall: false
registration: false
aliases:
- HM Greffe Guernsey
- Guernsey Registrar-General
- Guernsey births deaths marriages wills
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- guernsey
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Guernsey Royal Court — BDM, Wills & Deed Polls

> The Bailiwick of Guernsey's official registry of births, deaths, marriages, wills, deed polls and powers of attorney — obtained by manual request, not online search.

## When to use
You have a subject with a Guernsey connection and need a genealogical or legal-document anchor: a birth/death/marriage record (which yields dates and family `associate` links), a will (heirs and executors), a deed poll (a formal name change — critical when a subject has changed names), or a power of attorney. This is the authoritative source for those records in Guernsey, but there is **no self-service online database** — access is by request to the Greffe.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the information page: https://www.guernseyroyalcourt.gg/article/1637/Births-Deaths-Marriages-Wills-and-Deed-Polls.
2. Identify which record you need (BDM certificate, will, deed poll, POA).
3. Submit a request via the listed channel — email (registrar@guernseyroyalcourt.gg), phone (+44 (0)1481 225277), or in person at the public counter (weekdays 9am–4pm); Strongroom archive research is by appointment.
4. Pay the applicable certificate fee and await the manual response.
5. Pivot: a deed-poll record breaks a name-change alias; BDM records give `dob` and family `associate`s that feed genealogy and people-search tools.

## Inputs → Outputs
- **In:** `name` (with Guernsey nexus; dates/relationships help narrow)
- **Out:** vital-record and legal-document data — confirmed `name`, `dob`, family/heir `associate`s, name-change (deed poll) records
- **Empty/negative result looks like:** the Greffe reports no matching record — the event may have occurred elsewhere (Jersey, mainland UK), predate held records, or the name may differ (check deed-poll changes).

## Gotchas & OpSec
- **Human-in-the-loop:** no online search — every request is manually handled by the Greffe, so expect delay and per-document fees.
- Guernsey is a separate jurisdiction from Jersey and the UK mainland; records here won't cover those — use the respective registries.
- OpSec: the subject isn't notified, but you disclose your identity to a court registry when requesting.

## Overlaps ("do both")
- Do both with mainland UK GRO and Jersey Greffe records for subjects who moved between jurisdictions, and with genealogy platforms that may hold indexed transcriptions pointing you to the exact record to request.

## Trust & verifiability
`trust: trusted` — first-party records held by HM Greffier, the statutory custodian of Guernsey's vital and legal records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | guernseyroyalcourt-gg |
| category | public-records |
| selectorsIn → selectorsOut | name → name, dob, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
