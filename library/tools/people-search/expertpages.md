---
id: expertpages
name: ExpertPages
description: Use when you have a specialty or a name and want to identify/verify an expert witness — returns names, credentials, location, and employer-org from an expert-witness directory.
url: https://expertpages.com
category: people-search
path:
- people-search
bestFor: Finding and vetting expert witnesses / litigation consultants by specialty and location, with names, credentials, and locations.
selectorsIn:
- name
- geolocation
selectorsOut:
- name
- employer-org
- address
status: live
pricing: free
costNote: Free to search and view expert listings; experts pay for membership (the search side is free).
opsec: passive
opsecNote: Public directory browsing; the expert is not notified unless you contact them. Standard web logging only. Contacting an expert would expose you — browse first.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running (since 1995) expert-witness directory; listings are member-submitted marketing profiles, so verify credentials independently.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- expertpages.com
- Expert Pages
tags:
- people-search
- expert-witness
- directory
source: awesome-osint
lastVerified: '2026-07-18'
enrichment: full
---

# ExpertPages

> A directory of expert witnesses and litigation consultants (operating since 1995) — search by specialty and location to identify an expert, or look one up to read their claimed credentials and base.

## When to use
You have a specialty + `geolocation` and need to identify an expert witness, or you have a `name` and want to verify someone's claim to be an expert/consultant. ExpertPages returns profiles with the expert's name, credentials, specialty, location, and often their practice/`employer-org`. Useful for vetting an expert cited in a matter, disambiguating a professional, and pulling contact/location leads.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://expertpages.com and search by specialty category and/or geographic location, or search a specific name.
2. Open matching expert profiles: read name, credentials, specialty, city/state, and any firm/practice and contact details.
3. Note the claimed qualifications and affiliations for independent verification.
4. Pivot: the location and firm feed people/company searches; the stated credentials should be checked against licensing boards, university faculty pages, and court records where the expert has testified.

## Inputs → Outputs
- **In:** a specialty + `geolocation`, or a `name`
- **Out:** `name`, `employer-org` (practice/firm), `address` (city/state, contact), plus credentials
- **Empty/negative result looks like:** no listing — the person isn't an ExpertPages member (many experts aren't listed here, or list on competing directories); absence doesn't disprove expertise.

## Gotchas & OpSec
- Human-in-the-loop: none to browse; contacting an expert is a separate, higher-exposure step.
- OpSec: passive while browsing — don't reach out from an attributable account if you're investigating rather than retaining.
- Marketing bias: profiles are self-submitted advertisements; independently verify credentials, licences, and testimony history before relying on them.

## Overlaps ("do both")
- Pairs with other expert-witness directories (JurisPro, SEAK) and licensing-board/court-record searches — the directory identifies the expert, official sources verify the credentials and track record.

## Trust & verifiability
`trust: community` — a legitimate, long-standing directory, but listings are self-promotional; confirm every credential against an authoritative source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | expertpages |
| category | people-search |
| selectorsIn → selectorsOut | name, geolocation → name, employer-org, address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
