---
id: the-province-news
name: The Province (Vancouver newspaper)
description: Use when you have a `name` or `address` tied to British Columbia and want local news coverage — returns `associate`, `employer-org` and event context from published articles.
url: https://theprovince.com
category: communities-forums
path:
- communities-forums
bestFor: Finding local news coverage of a person or incident in Metro Vancouver / British Columbia.
selectorsIn:
- name
- address
selectorsOut:
- associate
- employer-org
status: live
pricing: freemium
costNote: Free article previews; a Postmedia metered paywall limits full articles after a few reads. Search and headlines are free.
opsec: passive
opsecNote: Reading and searching a public news site leaks nothing about your target. The paywall may set cookies / prompt registration; use a private window and decline the account to stay anonymous.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established daily newspaper (Postmedia Network), published in Vancouver since 1898; a reliable secondary source, subject to the usual journalistic caveats.
missingPersonsRelevance: medium
coverage:
- ca
aliases:
- The Province
- theprovince.com
- Vancouver Province
tags:
- toddington
- curated-directory
- news-journalism
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# The Province (Vancouver newspaper)

> A major Metro Vancouver daily — searchable for local coverage of people, crimes, court cases, obituaries and community events across British Columbia.

## When to use
Your subject lived, worked, went missing, or was involved in an incident in the Vancouver / Lower Mainland / BC area. Local newspapers often carry names, photos, employer references, family/associate names, and case details that never reach national outlets — including missing-persons appeals, court reporting, and obituaries.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://theprovince.com and use the site's search box, or run a scoped Google query: `site:theprovince.com "Full Name"`.
2. Skim headlines/leads for the person, address, or incident; note dates, quoted names, and locations.
3. When the metered paywall blocks the full article, read the cached copy (Google cache / `web.archive.org`) or the syndicated version on a sister Postmedia site (Vancouver Sun often runs the same wire copy).
4. Record associates (family, witnesses, officials named) and any employer/organisation mentioned.
5. Pivot: named associates feed people-search and social-profile tools; a case date/location feeds court-record and police-blotter searches.

## Inputs → Outputs
- **In:** `name` / `address` (BC-linked)
- **Out:** `associate` (people named alongside the subject), `employer-org`, event/date context
- **Empty/negative result looks like:** no article matches — the person may simply not have been covered by this outlet; try the Vancouver Sun, CBC BC, and Google News before concluding no coverage exists.

## Gotchas & OpSec
- Postmedia metered paywall after a few free reads — the archive/cache workaround usually recovers the full text.
- Coverage is BC-centric; a person outside the region will not appear.
- Fully passive — searching a news archive tells no one you are looking.

## Overlaps ("do both")
- Pairs with the Vancouver Sun (its Postmedia sister paper, often carrying the same or complementary local reporting) — run both to catch bylines and details one drops.

## Trust & verifiability
`trust: trusted` — a long-established daily paper of record for Vancouver; treat individual articles as reliable secondary sourcing, and confirm dates/quotes against the original where they matter.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-province-news |
| category | communities-forums |
| selectorsIn → selectorsOut | name, address → associate, employer-org |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
