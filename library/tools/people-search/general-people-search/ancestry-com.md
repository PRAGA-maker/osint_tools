---
id: ancestry-com
name: Ancestry.com
description: Use when you have a name + approximate DOB/location and want family-tree links, relatives, and historical records to extend a missing person's identity graph.
url: https://www.ancestry.com/search/
category: people-search
path:
- people-search
- general-people-search
bestFor: Building a family/relative graph and confirming identity from historical records (census, birth/marriage/death, immigration).
input: Name, date of birth, location, or family details
output: Historical records, family trees, relatives, immigration/census records, DNA matches (subscriber)
selectorsIn:
- name
- dob
- geolocation
selectorsOut:
- associate
- dob
- address
- name
status: live
pricing: freemium
costNote: Free record-hint search and tree building during a 14-day trial; full record images, most indexed records and DNA matching require a paid Family History / All-Access subscription.
opsec: passive
opsecNote: Searching the index does not contact the target; building/saving trees and DNA results requires an account, so use a research account, not a personal one. Records are historical, not real-time location.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Ancestry.com LLC, the largest commercial genealogy provider; source records are scanned government/vital documents, though user-submitted trees are unverified.
missingPersonsRelevance: high
coverage:
- us
- uk
- ca
- au
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- ancestry-genealogy-family-trees-and-family-history-records
aliases:
- Ancestry
- Ancestry.com
tags:
- genealogy
- people-search
source: arf-seed
lastVerified: '2026-06-13'
enrichment: full
---

# Ancestry.com

> The largest commercial genealogy database — best for reconstructing a missing person's family network and anchoring identity in historical vital records.

## When to use
You have a `name` plus an approximate `dob` and/or `geolocation` (birthplace, hometown) and need to map `associate` links (parents, siblings, spouse, children) or confirm a `dob`/maiden name from census, birth, marriage, death, and immigration records. Useful when modern people-search tools come up empty and you need to pivot through relatives, or to verify two records describe the same person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.ancestry.com/search/ and sign in with a research account (a 14-day free trial unlocks most search).
2. Enter `name`; add `dob`/birth year and birth/residence `geolocation` to cut false matches. Use the lived-in and family-member fields to constrain.
3. Read results grouped by collection (Census, Vital, Immigration, Public Member Trees). Strong hits give exact name + year + place; open the record to see household members → these are your `associate` pivots.
4. Pivot: feed surnames/relatives into other people-search tools; use a confirmed relative's current details to reach the subject. Cross-check the UK-focused `[[ancestry-genealogy-family-trees-and-family-history-records]]` for British records.

## Inputs → Outputs
- **In:** `name`, `dob`, `geolocation`
- **Out:** `associate` (family network), `dob`, `name` (maiden/aliases), `address` (historical)
- **Empty/negative result looks like:** no exact-name + place match, only loose soundex suggestions, or only paywalled "view record" stubs — do not treat a fuzzy soundex hit as confirmation.

## Gotchas & OpSec
- Human-in-the-loop: account login required; record images and many collections are behind a subscription paywall (free hints/trees during trial only).
- Public Member Trees are user-submitted and frequently wrong — treat as leads, not proof; rely on the indexed source documents.
- Data is historical/genealogical, not a current-address service; pair with a live people-search tool for present-day location.
- OpSec: passive on search, but DNA and saved-tree activity ties to your account — keep it on a sock-puppet research login.

## Overlaps ("do both")
- Pairs with `[[ancestry-genealogy-family-trees-and-family-history-records]]` (ancestry.co.uk) when the subject's records are UK census/parish based.

## Trust & verifiability
`trust: trusted` — established commercial genealogy provider with scanned primary-source records; verify any claim against the underlying document image, not the user tree.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ancestry-com |
| category | people-search |
| selectorsIn → selectorsOut | name, dob, geolocation → associate, dob, address, name |
| pricing / cost | freemium (trial free; records subscription) |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (login, paywall) |
