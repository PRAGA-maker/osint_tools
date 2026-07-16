---
id: international-federation-of-accountants-ifac
name: International Federation of Accountants (IFAC)
description: Use when you have a `name`/`employer-org` in accountancy and want to trace their professional body — returns member-organization directories that lead to license verification.
url: https://www.ifac.org
category: public-records
path:
- public-records
bestFor: Identifying the national accountancy body a professional belongs to, as the routing point to verify a CPA/CA credential.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
status: live
pricing: free
costNote: Free public portal and member-organization directory. No account for browsing.
opsec: passive
opsecNote: Browsing IFAC's public directory is passive and touches nothing about the subject. Verifying a credential on a member body's register is also generally passive, though some registers log lookups.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: IFAC is the authoritative global umbrella body for the accountancy profession; its member-organization directory is reliable, though individual credential checks happen on each national body's site.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- IFAC
tags:
- toddington
- curated-directory
- company-search
- professional-body
source: toddington-resources
lastVerified: '2026-07-16'
enrichment: full
---

# International Federation of Accountants (IFAC)

> The global umbrella body for accountancy — its value in OSINT is as a routing directory: find which national professional body a subject belongs to, then verify their credential there.

## When to use
Your subject claims to be an accountant/CPA/CA, or works for an accountancy firm, and you want to test that professional identity. IFAC itself doesn't hold an individual register, but its directory of member organizations tells you which national body (AICPA, ICAEW, etc.) governs a given country's accountants — the body whose public register can confirm or refute the person's credential. A niche corroboration tool, low general relevance.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open ifac.org and go to its member-organizations directory.
2. Identify the relevant national/regional body for the subject's country.
3. Go to that body's site and use its member/credential register to look up the subject `name`.
4. Read the result: whether the person holds the claimed designation, and their `employer-org`/firm affiliation if listed.
5. Pivot: a confirmed credential + firm feeds employer verification; a *failed* check flags a possibly false professional claim.

## Inputs → Outputs
- **In:** `name` + country/`employer-org` (accountancy context)
- **Out:** the governing `employer-org`/professional body; via it, credential confirmation
- **Empty/negative result looks like:** IFAC lists the body but the person isn't on that body's register — the claimed credential may be false, lapsed, or held under a different name/jurisdiction.

## Gotchas & OpSec
- IFAC is a directory of organizations, not people — the actual person-check happens on a member body's site.
- Registers vary in completeness and search capability by country.
- OpSec: passive; note that a few professional registers log lookups.

## Overlaps ("do both")
- Pairs with national accountancy registers and general company-search — IFAC routes you to the right body; that body confirms the individual, and company tools confirm the firm.

## Trust & verifiability
`trust: trusted` — authoritative global body; the routing is reliable, and the final credential confirmation comes from an official national register.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | international-federation-of-accountants-ifac |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
