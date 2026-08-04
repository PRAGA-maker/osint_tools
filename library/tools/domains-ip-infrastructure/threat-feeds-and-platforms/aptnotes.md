---
id: aptnotes
name: APTnotes
description: Use when you have a `domain`, `ip-address` or threat-actor name and want to check it against a curated public archive of APT campaign reports — returns links to analyst reports mentioning that indicator.
url: https://github.com/aptnotes/data
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- threat-feeds-and-platforms
bestFor: Looking up whether an indicator/domain/actor appears in the public corpus of vendor APT reports.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free and open-source (public GitHub repository of report metadata/links).
opsec: passive
opsecNote: You browse or clone a static public GitHub dataset — no query is sent to any target. Fetching the linked source reports from third-party vendor sites is likewise passive; nothing you do here touches the actor or infrastructure being researched.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-curated index of publicly released APT reports; the index is well-known, but each linked report's authority is the original vendor's.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- apt notes
- aptnotes data
tags:
- threat-intel
- apt-reports
- dataset
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# APTnotes

> A community-maintained, chronological index of publicly released APT (advanced persistent threat) reports, with links and metadata for each.

## When to use
You have a `domain`, `ip-address`, hash, or threat-actor/group name and want to know whether it's already documented in the public APT-reporting corpus — useful for attribution context and for pulling the original vendor write-up that first named an indicator. This is threat-intel/infrastructure research, not people-finding, so relevance to missing-persons work is indirect.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/aptnotes/data (or clone it) — the repo holds a year-by-year index (`APTnotes.csv` / per-year files) of reports with titles, sources and dates.
2. Search the index (GitHub search or grep the CSV) for your indicator, actor name, or keyword.
3. Follow the linked source URL to the original vendor/analyst report.
4. Read the report for the indicators and infrastructure (`domain`/`ip-address`) it documents.
5. Pivot: extracted infrastructure feeds enrichment tools; actor names feed further reading.

## Inputs → Outputs
- **In:** `domain`, `ip-address`, actor name, or keyword to search the index.
- **Out:** links to analyst reports and their metadata; from those reports, documented `domain`/`ip-address` indicators.
- **Empty/negative result looks like:** no matching row in the index — the indicator simply isn't covered in this public corpus; it says nothing about whether the indicator is malicious.

## Gotchas & OpSec
- It's an index of *links*, not a live indicator feed — some linked reports may have moved or been taken down; use web archives if a link is dead.
- Coverage is what analysts chose to publish publicly; absence is not evidence.
- Not people-centric — treat this as context/attribution support rather than a subject-finding tool.

## Overlaps ("do both")
- Complements live enrichment like `[[hostintel-keithjjones-github]]` — APTnotes tells you if an indicator was reported and by whom; the enricher tells you its current state.

## Trust & verifiability
`trust: community` — a respected but volunteer-curated index; verifiability comes from following each entry to its original, named vendor report rather than from the index itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | aptnotes |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
