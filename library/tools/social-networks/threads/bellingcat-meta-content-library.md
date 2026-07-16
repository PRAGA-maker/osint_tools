---
id: bellingcat-meta-content-library
name: Meta Content Library (via Bellingcat toolkit)
description: Use when you have a `name`, `username` or keyword and need to search the full public archive of Facebook, Instagram and Threads — returns public social-profile posts, associates and metadata, for vetted researchers only.
url: https://bellingcat.gitbook.io/toolkit/more/all-tools/meta-content-library
category: social-networks
path:
- social-networks
- threads
bestFor: Vetted-researcher access to Meta's full public-content archive (Facebook, Instagram, Threads) with search, filters and an API.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- associate
- metadata-exif
status: live
pricing: freemium
costNote: The library itself is free to approved researchers, but access is gated by eligibility (academic/non-profit research) and application via ICPSR. As of January 2026 the SOMAR virtual data enclave charges new teams (~USD 1,000 one-time + ~USD 371/month) for the compute environment.
opsec: passive
opsecNote: Research happens inside Meta's Secure Research Environment against an archive — you are not touching the target's live account, so it is passive and does not notify the subject. Access is tied to your vetted researcher identity, so this is not a covert tool; use it within the approved research scope only.
humanInLoop: true
humanInLoopReason:
- manual-review
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Meta's first-party research platform, documented here via Bellingcat's respected toolkit. Data is authoritative (Meta's own public-content records); the gate is eligibility, not data quality.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: true
aliases:
- Meta Content Library
- MCL
tags:
- meta
- facebook
- instagram
- threads
- research-api
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- about-maps-and-satellites
- bellingcat-s-online-investigation-toolkit-2
- china-related-resources
- license-plate-maps
---

# Meta Content Library (via Bellingcat toolkit)

> Meta's controlled-access research platform — near-real-time search across the full public archive of Facebook, Instagram and Threads, with filters, dashboards and an API. Gold-standard data, but only for vetted academic/non-profit researchers.

## When to use
You are an eligible researcher (academic institution or public-interest non-profit) investigating a subject's Meta footprint and need comprehensive, filterable access to public Facebook/Instagram/Threads content that the consumer apps won't give you — keyword search, engagement filters, date ranges, even text-within-images. Powerful for building a subject's social presence and network at scale, if you can pass the eligibility gate.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read the Bellingcat toolkit page (this URL) for the current access process and capabilities.
2. Apply for access through ICPSR (University of Michigan) — eligibility is limited to vetted academic/non-profit researchers; review typically takes 2–6 weeks.
3. On approval, use the web UI or programmatic API inside Meta's Secure Research Environment (SRE) / SOMAR enclave.
4. Search by `name`, `username`, keyword, engagement, language and date; browse Threads via the UI (no CSV export for Threads).
5. Pivot: public posts surface `associate` links (commenters, tagged accounts, group co-members), posting patterns and locations; export (where permitted) for link analysis.

## Inputs → Outputs
- **In:** `name`, `username`, or keyword query with filters
- **Out:** public `social-profile` content across Facebook/Instagram/Threads, `associate` interactions, and post `metadata-exif` (timestamps, engagement, language; image-text search covers ~last 180 days)
- **Empty/negative result looks like:** no matching public content — the subject may post privately (not in the public archive), or outside the covered window. Absence is not proof of no Meta presence.

## Gotchas & OpSec
- **Eligibility gate:** this is the hard barrier — access is restricted to vetted researchers and takes weeks; individual investigators/journalists without an eligible affiliation generally can't get in.
- Public content only: private profiles/posts and DMs are not included.
- Cost: the SOMAR enclave now charges new teams (from Jan 2026) — budget for it.
- OpSec: passive against an archive, but tied to your real researcher identity — not a covert capability; stay within approved scope.

## Overlaps ("do both")
- Pairs with consumer-level Meta search/monitoring tools for cases where you lack MCL access, and with `[[zesty-facebook-search]]`-style helpers — MCL is the authoritative, comprehensive layer where it's available.

## Trust & verifiability
`trust: trusted` — Meta's first-party research data, documented via Bellingcat. The content is authoritative; verifiability is high, with the only caveat being coverage windows (e.g. image-text search ~180 days) and public-only scope.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bellingcat-meta-content-library |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, associate, metadata-exif |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review, account-login) |
