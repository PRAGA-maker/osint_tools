---
id: crown-prosecution-service-uk
name: Crown Prosecution Service (UK)
description: Use when you have a `name` possibly involved in a UK criminal case and want official prosecution coverage — returns CPS news/press releases confirming charges, convictions, and case outcomes.
url: https://www.cps.gov.uk/
category: search-engines
path:
- search-engines
bestFor: Confirming UK prosecutions/convictions via the CPS newsroom and press releases naming defendants.
selectorsIn:
- name
selectorsOut:
- name
- geolocation
status: live
pricing: free
costNote: Free UK government website; no account or payment.
opsec: passive
opsecNote: Reading a public government site is read-only and never contacts the subject. As a .gov.uk site it may log traffic; use a clean session. Convictions named here are public record, but note this is official UK-government content.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official website of the Crown Prosecution Service, the principal public prosecutor for England and Wales; press releases are authoritative statements of case outcomes.
missingPersonsRelevance: low
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- courtserve-uk
- the-gazette-uk
aliases:
- CPS
- cps.gov.uk
tags:
- uk
- criminal-records
- government
- prosecution
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# Crown Prosecution Service (UK)

> The official site of England and Wales's public prosecutor; its newsroom and press releases name defendants and state case outcomes, making it a way to confirm a UK prosecution or conviction.

## When to use
You have a `name` you suspect was involved in a criminal case in England or Wales and want an authoritative confirmation. The UK has no public criminal-record search, but the CPS publishes press releases when it prosecutes notable cases — naming the defendant, the charges, the court/region, and the outcome (conviction, sentence). Searching the CPS site can corroborate that a specific person was prosecuted and pin the case to a place and date, which general news may report inconsistently.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.cps.gov.uk/ and use the site search (or `site:cps.gov.uk "<name>"` in a web engine) for the person's name.
2. Open matching news/press releases: read the charges, the CPS region/court (`geolocation`), the defendant details, and the outcome/sentence.
3. Corroborate with independent news coverage of the same case and, where possible, the court listing.
4. Note that only cases the CPS chose to publicize appear — routine cases are not press-released.
5. Pivot: the court/region and date feed `[[courtserve-uk]]` court listings; a company/insolvency angle feeds `[[the-gazette-uk]]`.

## Inputs → Outputs
- **In:** `name` (suspected defendant in England/Wales)
- **Out:** `name`/case confirmation, charges and outcome, `geolocation` (CPS region/court and offence location)
- **Empty/negative result looks like:** no press release mentioning the name — the vast majority of prosecutions are never press-released, so absence is NOT evidence the person was never prosecuted. It only means CPS didn't publicize that case.

## Gotchas & OpSec
- Coverage is selective: CPS press-releases only a small fraction of cases (typically higher-profile), so this confirms prosecutions but can never rule one out.
- England & Wales only — Scotland (COPFS) and Northern Ireland (PPS) have separate prosecutors.
- OpSec: **passive** — reading a public government site; the subject is not alerted.

## Overlaps ("do both")
- Pairs with `[[courtserve-uk]]` (court listings/results) and independent news search — CPS gives the official statement, court listings give the docket, and news fills gaps for cases CPS didn't publicize.

## Trust & verifiability
`trust: trusted` — it is the official prosecutor's own site, so a press release is an authoritative record of that case's outcome; its limitation is coverage (selective), not accuracy.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | crown-prosecution-service-uk |
| category | search-engines |
| selectorsIn → selectorsOut | name → name, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
