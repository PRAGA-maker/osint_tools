---
id: webhackurls
name: WebHackUrls
description: Use when you have a `domain` and want its historical URLs — pulls a domain's known paths from the Wayback Machine and filters them by extension/keyword.
url: https://github.com/mathis2001/WebHackUrls
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Fast archive-based URL discovery for a domain, filtered to interesting paths (admin, login, .js, .json, backups).
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source (Python) on GitHub; no account or key needed.
opsec: passive
opsecNote: URL discovery itself is passive — it queries the Wayback Machine's archive, not the target's live server, so the target sees nothing. Note the optional screenshot feature DOES visit the discovered URLs live (active) and reveals your IP to the target; skip it or proxy it for a purely passive pass.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A small community Python tool (mathis2001) wrapping the public Wayback Machine index; results are as complete as the archive's crawl coverage, which is uneven.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- cert4recon
aliases:
- WebHackUrls
tags:
- Domain/IP/Links
- Website analyze
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# WebHackUrls

> A quick way to see everything a domain has ever exposed: it pulls the domain's archived URLs from the Wayback Machine and filters them to the paths you care about — no requests to the live target needed.

## When to use
You have a `domain` and want to map its historical attack/content surface — old admin panels, login pages, exposed `.json`/`.xml`/`.pdf` files, deprecated endpoints — without touching the live site. Because it reads the Internet Archive's index, it surfaces URLs that may no longer be linked but were once crawled, which often includes forgotten or sensitive paths.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/mathis2001/WebHackUrls` (Python).
2. Run: `python3 webhackurls.py -d target.com` — add `-k <keyword>` (e.g. `admin`, `login`, `js`, `pdf`) and `-l <limit>` to filter.
3. Read the returned archived URLs; save to a file for the next stage.
4. (Optional, active) use the screenshot feature to preview URLs — this visits them live, so proxy it.
5. Pivot: interesting paths feed manual review or content scraping ([[rextract]]); discovered file URLs feed document/metadata analysis.

## Inputs → Outputs
- **In:** `domain` (+ optional keyword/extension filter)
- **Out:** archived URLs/paths for that `domain`
- **Empty/negative result looks like:** few or no URLs — the domain may be new, lightly crawled by the Archive, or excluded from it; a thin result reflects archive coverage, not necessarily a small site.

## Gotchas & OpSec
- **Archive-based:** results are historical and may include dead or since-fixed paths — a listed URL isn't proof it's still live.
- The core lookup is passive, but the **screenshot option is active** (visits the URLs); keep them separate for OpSec.
- Coverage depends entirely on what the Wayback Machine crawled; combine with other URL sources for completeness.

## Overlaps ("do both")
- Overlaps with other Wayback/URL-collection tools (gau, waybackurls) and pairs with [[cert4recon]] and scrapers like [[rextract]] — this finds the paths, the scraper extracts data from them.

## Trust & verifiability
`trust: community` — a thin, inspectable wrapper over the public Internet Archive index; every returned URL is verifiable directly in the Wayback Machine.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | webhackurls |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
