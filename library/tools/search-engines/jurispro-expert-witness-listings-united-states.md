---
id: jurispro-expert-witness-listings-united-states
name: JurisPro Expert Witness Listings (United States)
description: Use when you have a `name` or field and want to find a US expert witness's professional profile — returns employer-org, credentials and contact leads.
url: http://www.jurispro.com
category: search-engines
path:
- search-engines
bestFor: Locating US expert witnesses by specialty/state and reading their self-published CV, credentials and contact details.
selectorsIn:
- name
selectorsOut:
- employer-org
- social-profile
- address
status: live
pricing: free
costNote: Free to browse and search the directory; only experts pay/register to list themselves.
opsec: passive
opsecNote: Read-only directory browsing; the expert has published this profile themselves, but your visit is not disclosed to them. Do not use the site's contact features against a subject during an investigation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Profiles are self-submitted marketing CVs by the experts; credentials are as claimed, not independently verified — corroborate qualifications separately.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- JurisPro
- jurispro.com
tags:
- toddington
- curated-directory
- expert-witness
- specialty-search
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# JurisPro Expert Witness Listings (United States)

> A free directory of US expert witnesses — search by field/state and read their self-published CV, credentials and contact details.

## When to use
Your subject is (or claims to be) a professional expert/consultant who does litigation work. JurisPro lists expert witnesses across 20+ categories and all US states, with self-authored profiles that often include full name, credentials, employer/firm, CV, website and contact info. Use it to confirm a professional identity, pull a resume/employer, or find a working contact address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.jurispro.com.
2. Browse by category (e.g. accident reconstruction, medical) and/or by state, or search a `name`/specialty.
3. Open the expert's profile: CV, credentials, `employer-org`/firm, website (`social-profile`), and listed contact `address`.
4. Treat the credentials as claimed — verify degrees/licences with the issuing body.
5. Pivot: the firm/website feeds domain and LinkedIn OSINT; the CV yields employers and affiliations to corroborate.

## Inputs → Outputs
- **In:** `name` or specialty + state
- **Out:** `employer-org`/firm, `social-profile` (website), contact `address`, credentials/CV
- **Empty/negative result looks like:** no listing — the person isn't a JurisPro-listed expert (many experts use other directories or none), not proof they lack expertise.

## Gotchas & OpSec
- Profiles are **self-submitted marketing** — credentials are as claimed; verify independently.
- Directory is opt-in and US-focused, so coverage is partial.
- Contact details are the expert's professional channel; don't use them to approach a subject mid-investigation.

## Overlaps ("do both")
- Pairs with other expert-witness directories and LinkedIn — cross-check the same person's claims across listings, and confirm licences with the relevant board.

## Trust & verifiability
`trust: unverified` — a self-listed marketing directory; the profile is a genuine lead to the person, but its credential claims must be corroborated elsewhere.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jurispro-expert-witness-listings-united-states |
| category | search-engines |
| selectorsIn → selectorsOut | name → employer-org, social-profile, address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
