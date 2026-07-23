---
id: namescan
name: NameScan
description: Use when you have a `name` (person or business) and want to check it against global sanctions, PEP and adverse-media lists — returns match flags plus linked `associate` names.
url: https://namescan.io
category: public-records
path:
- public-records
- kyc-aml-tools
bestFor: Free sanctions/PEP/adverse-media screening of a person or company name.
selectorsIn:
- name
- employer-org
selectorsOut:
- name
- associate
status: live
pricing: freemium
costNote: Free instant scans are capped (a few per day/email); pay-as-you-go and MemberCheck enterprise plans add ongoing monitoring and higher volume.
opsec: passive
opsecNote: You submit the target's name to a third-party compliance vendor that logs the query; it is not disclosed to the subject. Use a sock-puppet email if you register for extra free scans, and don't enter identifying data beyond the name.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: unverified
trustNote: Commercial AML vendor aggregating third-party watchlists; sanctions/PEP matching is solid but adverse-media hits are keyword-driven and need manual confirmation.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- opensanctions-org
aliases:
- NameScan.io
- MemberCheck
tags:
- kyc
- aml
- sanctions
- pep
- adverse-media
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# NameScan

> Free-tier AML screening portal: paste a name, get sanctions / PEP / adverse-media hits back in seconds.

## When to use
You have a subject `name` (individual or `employer-org`) and want a fast read on whether they appear on government sanctions lists, are a Politically Exposed Person, or are surrounded by negative news. Useful early in a workup to flag whether a person or company is high-risk and to surface `associate` names (relatives, close associates, linked entities) that watchlists record alongside the primary subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://namescan.io and pick a free scan (Individual or Organisation; "PEP & Sanctions" or "Email Compromise").
2. Enter the subject's full `name` (optionally date of birth / country to narrow matches).
3. Submit and read the report:
   - **Sanctions / PEP:** each match shows the list source, matched name variants, and linked associates.
   - **Adverse media:** keyword-matched negative-news snippets.
4. When you hit the free daily limit, register a sock-puppet email for a few more complimentary scans, or move to pay-as-you-go.
5. Pivot: a confirmed match feeds `[[opensanctions]]` for the underlying primary-source records, and associate names feed name/relationship lookups.

## Inputs → Outputs
- **In:** `name` (person or `employer-org`)
- **Out:** sanctions/PEP match flags, `name` variants, linked `associate` names, adverse-media snippets
- **Empty/negative result looks like:** "No matches found" — the name isn't on the screened watchlists; NOT proof the person is clean, only that they're not sanctioned/PEP-listed.

## Gotchas & OpSec
- Human-in-the-loop: free scans are rate-limited; expect a daily cap and a registration prompt for more.
- Common names generate false positives — confirm DOB/nationality against the matched record before treating a hit as real.
- Adverse-media matching is keyword-based; read the actual articles rather than trusting the flag.
- OpSec: passive, but the vendor logs your queries; use a throwaway email for registration.

## Overlaps ("do both")
- Pairs with `[[opensanctions-org]]` — NameScan gives a fast screening verdict, while OpenSanctions exposes the underlying primary-source list entries you cite.

## Trust & verifiability
`trust: unverified` — a commercial AML aggregator; sanctions/PEP matches are reliable, but adverse-media and fuzzy name matches are automated and must be confirmed against the cited source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | namescan |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → name, associate |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
