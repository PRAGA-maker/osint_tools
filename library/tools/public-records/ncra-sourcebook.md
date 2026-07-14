---
id: ncra-sourcebook
name: NCRA Sourcebook
description: Use when you have a `name` you believe belongs to a court reporter, captioner, or legal videographer and want to confirm the professional and find their firm/contact — returns employer-org, address, and social-profile.
url: https://portal.ncra.org/sourcebook
category: public-records
path:
- public-records
bestFor: Confirming and locating a US court reporting / captioning professional by name and finding their firm and business contact details.
selectorsIn:
- name
selectorsOut:
- employer-org
- address
- social-profile
status: live
pricing: free
costNote: Free public member-directory search operated by the NCRA; no account or payment needed to browse.
opsec: passive
opsecNote: A read-only directory lookup against the NCRA membership site; no notice to the subject and no login required. Standard passive browsing hygiene is enough.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Official directory of the National Court Reporters Association; records are self-maintained by members, so contact details are usually current but scope is limited to NCRA members.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- truepeoplesearch
- linkedin
aliases:
- National Court Reporters Association Sourcebook
- NCRA member directory
tags:
- court
- professional-directory
- inmate
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# NCRA Sourcebook

> The National Court Reporters Association's official member directory — a niche people-finder for one profession: court reporters, captioners, and legal videographers.

## When to use
Narrow but decisive: your subject is (or claims to be) a court reporter, stenographer, CART captioner, or legal videographer in the US, and you have a `name`. The Sourcebook confirms the professional exists in NCRA's membership and hands you their firm (`employer-org`), business city/state, and contact details — a fast identity corroboration and a pivot to their workplace. Do not reach for this for the general public; it only covers NCRA members.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://portal.ncra.org/sourcebook.
2. Search by the subject's `name` (and narrow by state/firm if the name is common).
3. Read the member record: professional certifications, firm/employer, business location, and any listed contact info or photo the member added.
4. Empty result → the person is not a current NCRA member (they may be a state-only or lapsed reporter).
5. Pivot: the firm name feeds a company lookup; the confirmed full name + city feeds `[[truepeoplesearch]]` or `[[linkedin]]` for personal contact details.

## Inputs → Outputs
- **In:** `name`
- **Out:** `employer-org` (firm), `address` (business city/state), `social-profile` / contact details, certifications
- **Empty/negative result looks like:** "no members found" — means not an NCRA member, NOT that the person isn't a court reporter (many work without NCRA membership).

## Gotchas & OpSec
- Coverage is limited to NCRA members — a huge blind spot; absence proves nothing about the general population.
- Records are self-updated by members, so a stale entry means the person let their listing lapse, not necessarily that they moved.
- No login, no CAPTCHA — clean passive lookup.

## Overlaps ("do both")
- Pairs with `[[linkedin]]` — the Sourcebook confirms the professional credential and firm; LinkedIn adds work history and a face; run both to triangulate the same person.

## Trust & verifiability
`trust: trusted` — first-party association directory. The credential is authoritative; the contact details are member-maintained, so verify currency before relying on an address.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ncra-sourcebook |
| category | public-records |
| selectorsIn → selectorsOut | name → employer-org, address, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
