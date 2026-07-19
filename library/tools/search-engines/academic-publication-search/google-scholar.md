---
id: google-scholar
name: Google Scholar
description: Use when you have a `name` (or `employer-org`) and want the subject's academic output, co-authors and affiliations — returns papers, citations, and (often) a profile with a photo and institution.
url: https://scholar.google.com/
category: search-engines
path:
- search-engines
- academic-publication-search
bestFor: Mapping a person's publications, co-authors, affiliations and academic timeline.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
status: live
pricing: free
costNote: Free to search; no account needed to read. Authors may create a public Scholar profile (that's what exposes photo/affiliation/co-authors).
opsec: passive
opsecNote: Searching is passive and the subject isn't notified. Clicking through to publisher PDFs hits third-party sites (normal browsing). Heavy scripted querying triggers Google's CAPTCHA/rate limiting — search manually or throttle. Use a clean browser profile.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: Google's academic index — broad and authoritative for discovery, though it indexes some non-peer-reviewed material, so treat a hit as "published somewhere," then check the venue.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- scholar.google.com
- Google Scholar profiles
tags:
- academic
- scholarly
- search
source: arf-seed
lastVerified: '2026-07-19'
enrichment: full
---

# Google Scholar

> Google's index of scholarly literature — the fastest way to pull a person's publication trail, co-authors, affiliations and, when they've made a profile, a photo and current institution.

## When to use
Your subject has any academic footprint — a student, researcher, clinician, engineer, or expert witness. A `name` search reveals their papers, who they published with (`associate`), where they were affiliated over time (`employer-org`), and their approximate active years. An author's Scholar *profile* page is especially rich: photo, verified email domain (institution), research interests, and a full co-author list.

## How to use it (`bestInteractionPattern`: web-manual)
1. Search the subject's `name` at https://scholar.google.com/ (quote it; add an institution or field keyword to disambiguate common names).
2. Look for a linked **author profile** (a hyperlinked name at the top) — open it for the photo, verified-email institution, interests, and co-authors.
3. Scan the paper list: co-authors are `associate` leads, affiliations on papers trace an `employer-org` history, and publication dates build a timeline.
4. Use "Cited by" and "Related articles" to expand the network.
5. Pivot: institution → staff directory/ORCID; co-authors → further `name` searches; a verified email domain → email-pattern guessing.

## Inputs → Outputs
- **In:** `name` (optionally + field/`employer-org` to disambiguate)
- **Out:** publications, co-authors (`associate`), affiliation history (`employer-org`), and often a profile photo/institution
- **Empty/negative result looks like:** no results or only namesakes — the person may not publish, or publishes under a variant/maiden name or in a non-indexed language; try ORCID and institutional pages.

## Gotchas & OpSec
- Common names collide heavily; verify by co-author overlap, institution, and topic before attributing papers to your subject.
- Scholar indexes preprints, theses and some grey literature — a "hit" isn't automatically peer-reviewed; check the venue.
- Human-in-the-loop: rapid/scripted searches trip a CAPTCHA — do it by hand or slow down.
- OpSec: passive; no subject notification.

## Overlaps ("do both")
- Pairs with ORCID, ResearchGate and [[open-secrets]]-style records depending on the case — Scholar is the broad discovery layer; ORCID gives a curated, disambiguated ID and institutional history to confirm attribution.

## Trust & verifiability
`trust: trusted` — Google's authoritative academic index; publications are verifiable at the linked venue, and author profiles are self-created (so treat profile self-claims as needing the usual corroboration).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-scholar |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
