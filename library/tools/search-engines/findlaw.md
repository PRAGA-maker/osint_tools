---
id: findlaw
name: FindLaw
description: Use when you have a `name` or firm and want to find a US attorney's practice, firm, and contact details — returns `employer-org`, `address`, and `phone`.
url: https://lawyers.findlaw.com/lawyer/state.jsp
category: search-engines
path:
- search-engines
bestFor: Locating a named US attorney's firm, office address, and contact details, or finding lawyers by location/specialty.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- address
- phone
status: live
pricing: free
costNote: The attorney directory is free to search and browse; profiles are free to read. (Enhanced/featured listings are a paid product for the lawyers themselves, not a paywall on searchers.)
opsec: passive
opsecNote: You are searching a public directory of professionals, not contacting anyone. No footprint on the subject unless you click through to a firm's "contact" form — don't, if you want to stay covert.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by FindLaw (a Thomson Reuters legal brand); one of the largest US attorney directories, with ~1.2M firm listings sourced from bar/firm data.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- list-of-criminal-charges-findlaw
- avvo-north-america
- lawyers-com
aliases:
- FindLaw Lawyer Directory
- lawyers.findlaw.com
tags:
- toddington
- specialty-search
- attorney-directory
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# FindLaw

> A large US attorney directory (Thomson Reuters): turn a lawyer's name into their firm, office address, phone, and practice areas — or find counsel by location and specialty.

## When to use
Your subject is (or is connected to) a US attorney, or you need to identify/reach the lawyer representing someone. FindLaw resolves a `name` or firm to a professional profile: firm affiliation, office `address`, `phone`, practice areas, jurisdictions, and bar admissions. It is also a way to corroborate a claimed legal career or to find the counsel behind a business dispute or a missing-person's estate.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://lawyers.findlaw.com/ and choose the search: by legal issue, by location (city/ZIP/county), or by attorney/firm name.
2. Enter the `name` (last name works best) and, if known, the state to narrow results.
3. Open the matching profile: read firm, office address, phone, practice areas, admissions, and any linked firm website.
4. Cross-check the person against the state bar's official licensee lookup to confirm the profile is current and the attorney is in good standing.
5. Pivot: the firm `address`/`phone` and website feed business-records and infrastructure lookups; bar admissions confirm identity and jurisdiction.

## Inputs → Outputs
- **In:** `name` (attorney) or `employer-org` (firm)
- **Out:** `employer-org` (firm), office `address`, `phone`, practice areas, jurisdictions
- **Empty/negative result looks like:** no matching attorney — the person may not be a practising US lawyer, may practise under a different name, or simply isn't listed; confirm against the state bar before concluding.

## Gotchas & OpSec
- US-focused: coverage is American attorneys; use national bar directories for other countries.
- Listings can lag: a lawyer may have moved firms or retired since their profile was last updated — verify currency via the state bar.
- Featured placement is paid by lawyers, so ranking is not authority; read the actual profile data, not the position.
- OpSec: passive browsing only; avoid submitting the "contact this attorney" form on a target.

## Overlaps ("do both")
- Pairs with `[[avvo-north-america]]` and `[[lawyers-com]]` (overlapping attorney directories with reviews/ratings) and `[[list-of-criminal-charges-findlaw]]` (FindLaw's legal-reference side) — cross-check profiles across directories since each has gaps.

## Trust & verifiability
`trust: trusted` — a major, long-established Thomson Reuters directory; profile data is generally reliable but should be confirmed against the authoritative state bar record before you act on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | findlaw |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → employer-org, address, phone |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
