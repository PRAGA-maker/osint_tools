---
id: canadian-charity-search
name: Canadian Charity Search
description: Use when you have a charity or person name and want the CRA registered-charity record — returns employer-org status, address, directors/trustees (associates), and financial filings.
url: https://apps.cra-arc.gc.ca/ebci/hacc/srch/pub/dsplyBscSrch?request_locale=en
category: search-engines
path:
- search-engines
bestFor: Verifying a Canadian registered charity and reading its status, address, directors, and annual (T3010) financial filings.
selectorsIn:
- employer-org
- name
selectorsOut:
- employer-org
- address
- associate
status: live
pricing: free
costNote: Free official CRA (Canada Revenue Agency) List of Charities; no account required.
opsec: passive
opsecNote: Reads public charity-registry data; no charity or individual is notified. Standard government-site logging only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official Canada Revenue Agency register; authoritative for Canadian registered-charity status and filings.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- CRA List of Charities
- Canada Revenue Agency charities
- cra-arc.gc.ca charitylists
tags:
- public-records
- charities
- canada
- nonprofits
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Canadian Charity Search

> The Canada Revenue Agency's official List of Charities — confirm a Canadian charity is registered and read its address, directors/trustees, and annual financial (T3010) filings.

## When to use
You have an `employer-org` (a charity/nonprofit) or a person `name` you suspect runs or sits on the board of one. The CRA register confirms registration status and reveals the charity's `address`, its directors/trustees (`associate` links to named people), activities, and annual financial filings. Useful for vetting an organization a subject is tied to, tracing where money and control sit, and connecting a person to a governing role.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CRA List of Charities search at https://apps.cra-arc.gc.ca/ebci/hacc/srch/pub/dsplyBscSrch?request_locale=en.
2. Search by charity name, registration (BN) number, or location; you can also browse by category.
3. Open the charity's record: registration status/effective dates, contact address, activities, and the T3010 annual returns (revenue, expenses, compensation, directors).
4. Pivot: named directors/trustees are `associate` leads; the address and BN feed corporate-registry cross-checks; financial filings can reveal salaries and related parties.

## Inputs → Outputs
- **In:** `employer-org` (charity name/BN) or a person `name`
- **Out:** `employer-org` (status/activities), `address`, `associate` (directors/trustees), plus financial filings
- **Empty/negative result looks like:** no match — the organization isn't a CRA-registered charity (it may be a nonprofit that isn't a registered charity, or defunct/revoked — the register also lists revoked charities), or the name differs.

## Gotchas & OpSec
- Human-in-the-loop: none; open public search.
- OpSec: passive — public data, no notification.
- Scope: Canadian registered charities only. Nonprofits that aren't registered charities won't appear; revoked/annulled charities are flagged as such — read the status carefully.

## Overlaps ("do both")
- Pairs with corporate registries and US `[[nonprofit-explorer]]` — the CRA register covers Canadian charities, the others cover companies and US nonprofits for the same people/entities.

## Trust & verifiability
`trust: trusted` — it is the official CRA register; status and filings are authoritative and verifiable by the charity's Business Number.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | canadian-charity-search |
| category | search-engines |
| selectorsIn → selectorsOut | employer-org, name → employer-org, address, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
