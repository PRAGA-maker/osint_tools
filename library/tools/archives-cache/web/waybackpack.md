---
id: waybackpack
name: Waybackpack
description: Use when you have a `domain`/URL and want its entire Wayback history offline — downloads every archived snapshot so you can diff a site's past states for removed content.
url: https://github.com/jsvine/waybackpack
category: archives-cache
path:
- archives-cache
- web
bestFor: Bulk-downloading all Internet Archive snapshots of a URL/domain to local disk for offline analysis.
selectorsIn:
- domain
selectorsOut: []
status: live
pricing: free
costNote: Free, open-source Python CLI (`pip install waybackpack`). Uses the Internet Archive's public Wayback API; no key or account.
opsec: passive
opsecNote: You query the Internet Archive, never the target's live site — the site owner is not notified. At scale the archive may rate-limit or log your IP; throttle and use a VPN if the collection is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A widely-used, well-maintained open-source tool (jsvine/waybackpack). It's a faithful downloader — the data's reliability is the Internet Archive's, not the tool's.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- waybackpack
- jsvine/waybackpack
tags:
- wayback-machine
- internet-archive
- cli
- web-archive
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Waybackpack

> A command-line tool that downloads every Wayback Machine snapshot of a URL or domain to disk — so you can read what a page said years ago, even after it was edited or deleted.

## When to use
You have a `domain` or specific URL (a subject's old blog, a company page, a deleted profile) and want its full archived history, not just one snapshot. Instead of clicking through the Wayback UI, waybackpack pulls all captures for offline grepping and diffing — ideal for recovering a bio, contact detail, staff list, or claim that was later scrubbed, and for timelining when content changed.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install waybackpack`.
2. Download all snapshots of a URL to a folder: `waybackpack example.com/about -d ./out`.
3. Narrow by date if needed: `--from-date 2015 --to-date 2019`; list captures without downloading via `--list`.
4. Grep the downloaded tree for names, emails, phones, or removed text; diff consecutive snapshots to find when something changed.
5. Pivot: recovered emails/phones/handles feed the matching selector tools; a "content removed on date X" finding feeds a timeline.

## Inputs → Outputs
- **In:** `domain` or URL (+ optional date range)
- **Out:** a local tree of all archived HTML snapshots and a capture/timestamp list (no personal selectors by itself — you mine the recovered pages)
- **Empty/negative result looks like:** no captures returned — the URL was never archived (robots-blocked, too obscure, or the exact path differs); try the domain root or known sub-paths before concluding nothing was saved.

## Gotchas & OpSec
- Only as complete as the Internet Archive's captures — gaps mean "not archived," not "never existed."
- Large sites produce many files; scope by path/date to avoid huge downloads and rate-limiting.
- Passive; the live target site is never touched.

## Overlaps ("do both")
- Pairs with the Wayback Machine UI and other archive tools in the [[archives-cache]] set — waybackpack is the bulk/offline path for deep diffing, while the web UI is faster for a single quick look.

## Trust & verifiability
`trust: community` — a reputable open-source downloader over authoritative Internet Archive data. What it fetches is exactly what the archive holds; verify a recovered claim against the snapshot's own timestamp.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | waybackpack |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → — |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
