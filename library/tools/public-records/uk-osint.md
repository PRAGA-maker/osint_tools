---
id: uk-osint
name: UK-OSINT
description: Use when you have a UK `name`, `address`, or `phone` and want a curated map of the right UK records, registries, and people-search tools — returns pointers toward `address`, `employer-org`, and record links.
url: https://www.uk-osint.net/
category: public-records
path:
- public-records
bestFor: A practitioner-curated portal of UK-specific people search, public records, company/land registries, and investigation techniques.
selectorsIn:
- name
- address
- phone
selectorsOut:
- address
- employer-org
status: live
pricing: free
costNote: Free portal by Neil Smith; the tools and registries it links to have their own pricing (many UK registries charge small per-record fees).
opsec: passive
opsecNote: Browsing the portal is passive and safe — you're reading a directory of techniques, not querying a subject. Each linked tool/registry has its own OpSec profile; evaluate those separately before running a lookup.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Long-running UK OSINT portal by practitioner Neil Smith, widely cited in the UK investigations community; curation is authoritative, though individual linked sites vary.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- UK-OSINT.net
- Neil Smith UK-OSINT
tags:
- public-records
- people-search
- uk
- registries
source: ultimate-osint
lastVerified: '2026-07-14'
enrichment: full
---

# UK-OSINT

> Neil Smith's UK-OSINT.net — the practitioner's map of where to find UK people, records, and registries, organized so you pick the right source instead of guessing.

## When to use
You have a UK lead — a `name`, `address`, or `phone` — and need the correct UK-specific source: electoral roll, Companies House, Land Registry, birth/death/marriage, court and insolvency records, or UK people-search sites. UK records are fragmented and often region- or registry-specific; this portal tells you which door to knock on for a given selector, which is faster and more accurate than generic global tools for British subjects.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.uk-osint.net/ and browse the categorized sections (people, company, property, records, techniques).
2. Match your selector to a section — e.g. `address` → electoral roll / property tools; `name` + company → Companies House; `name` → BMD and people-search.
3. Follow the recommended tool/registry link and run your actual query there (some registries charge a small fee).
4. Read the portal's technique notes — it explains how to use each source effectively, not just where it is.
5. Pivot: whatever the chosen source returns (an `address`, a director record `employer-org`, a BMD record) feeds the rest of your UK workflow.

## Inputs → Outputs
- **In:** UK `name`, `address`, or `phone` (you bring the selector; the portal points you to the tool)
- **Out:** pointers to UK records that yield `address`, `employer-org`, property, and BMD data
- **Empty/negative result looks like:** a section that only lists tools you already have, or links that have gone stale — cross-check with other UK directories and confirm each linked source is still live.

## Gotchas & OpSec
- This is a directory, not a lookup — it returns *where to look*, not subject data. Run the actual query on the linked source.
- UK-specific: not useful for non-UK subjects. Some linked registries charge per record or require registration.
- Portal links can age; verify a linked tool is live before relying on it.

## Overlaps ("do both")
- Pairs with global people-search and company tools — UK-OSINT sharpens coverage on British-specific registries those miss (electoral roll, Land Registry, Companies House), while global tools cover diaspora and cross-border leads.

## Trust & verifiability
`trust: trusted` — an authoritative, long-standing curation by a recognized UK practitioner. The portal's guidance is reliable; judge each *linked* source on its own merits and confirm data at the primary registry.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | uk-osint |
| category | public-records |
| selectorsIn → selectorsOut | name, address, phone → address, employer-org |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
