---
id: association-assq-qc-ca
name: Association des statisticien·ne·s du Québec (ASSQ)
description: Use when you have a `name` and want to confirm a Québec statistician's professional membership — returns `employer-org` affiliation and `social-profile` directory listing.
url: https://www.association-assq.qc.ca/
category: public-records
path:
- public-records
bestFor: Verifying whether a named person is a listed member of Québec's professional statisticians' association.
selectorsIn:
- name
selectorsOut:
- employer-org
- social-profile
status: live
pricing: free
costNote: Free public site; member and institutional directories are viewable without payment (some detail may sit behind a member login).
opsec: passive
opsecNote: Browsing the public directory is passive and unconnected to any subject. Logging into "Mon compte" requires membership and is attributable — do not.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Official site of a small (~100-member) professional association (founded 1995, based at Université Laval); directory listings are self/association-maintained, not a government register.
missingPersonsRelevance: medium
coverage:
- ca
auth: none
api: false
localInstall: false
registration: false
aliases:
- ASSQ
- association-assq.qc.ca
- Association des statisticiennes et statisticiens du Québec
tags:
- professional-association
- directory
- quebec
source: osint4all
lastVerified: '2026-07-22'
enrichment: full
relatedTools:
- alcool-r-gie-des-alcools-des-courses-et-des-jeux-racj
- banq-num-rique
- rechercher-par-entreprise
- rechercher-par-r-gion-ou-type-de-travaux
- rechercher-par-r-pondant
- services-en-ligne
- trouver-une-d-cision
---

# Association des statisticien·ne·s du Québec (ASSQ)

> The professional association for statisticians in Québec — a niche membership directory that ties a name to a profession, an employer sector, and colleagues.

## When to use
You have a `name` and a reason to think the person works in statistics/data in Québec (public service, education or private sector). ASSQ's member and institutional directories can confirm professional membership, surface an affiliated `employer-org`/institution, and place the person within a small professional community — useful for verifying a claimed occupation, distinguishing same-named people by profession, or finding associates via shared institutional membership.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.association-assq.qc.ca/ (French-language site).
2. Use the "membres" / member and institutional-member directory links to browse or search for the `name`.
3. Read the listing for institutional affiliation, role and any contact/profile link; the association's *Convergence* bulletin and colloquium pages can also name active members.
4. Pivot: an `employer-org`/university feeds staff-directory and LinkedIn checks; membership corroborates a claimed statistician/data profession.

## Inputs → Outputs
- **In:** `name`
- **Out:** `employer-org`/institution, `social-profile`/directory listing, professional-community links
- **Empty/negative result looks like:** no directory match — the person isn't an ASSQ member (a small association, so many Québec statisticians won't appear); some member detail may be members-only and thus invisible to you.

## Gotchas & OpSec
- Tiny membership (~100): absence proves nothing about a person's profession.
- Full member detail may require a member login you shouldn't attempt; work from the public directory only.
- French-language; watch for accent/spelling variants of names.

## Overlaps ("do both")
- Pairs with university staff directories, LinkedIn and other professional-body registries — this confirms a Québec-statistics affiliation specifically, which broader tools may not categorise.

## Trust & verifiability
`trust: community` — an official but small professional-association site; listings are association-maintained (not a statutory register), so treat as a strong lead, corroborated elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | association-assq-qc-ca |
| category | public-records |
| selectorsIn → selectorsOut | name → employer-org, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
