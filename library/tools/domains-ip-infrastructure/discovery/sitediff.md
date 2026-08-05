---
id: sitediff
name: Sitediff
description: Use when you have a `domain`/URL and want to detect what changed between two fetches — returns a highlighted diff of content and structural deltas for change-monitoring.
url: https://github.com/digininja/sitediff
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- discovery
bestFor: Comparing two snapshots of a web page/site to spot content and structural changes over time.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source (run locally); no account or key. You supply your own compute.
opsec: active
opsecNote: The tool fetches the target URL directly from wherever you run it, so the site's logs see your IP/user-agent on each pull. For sensitive monitoring, run it from a VPS/proxy or route through a puppet egress; the comparison itself is non-intrusive but the fetch is a real visit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Authored by Robin Wood (digininja), a well-known security-tools developer (CeWL, DVWA); open-source on GitHub with public history, though this is a smaller utility than his flagship projects.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- cewl
aliases:
- digininja sitediff
tags:
- web-monitoring
- change-detection
- cli
source: arf-seed
lastVerified: '2026-08-05'
enrichment: full
---

# Sitediff

> A command-line utility that fetches a page across two points in time and diffs them — a scriptable way to watch a target site for edits.

## When to use
You are monitoring a `domain` or specific URL — a suspect's landing page, a company notice board, a profile page, a leak site — and need to know precisely what changed between visits. Sitediff pulls the content and reports content/structural deltas, so you catch quiet edits (a removed name, a new phone number, an altered date) that a human eyeballing the page would miss.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and set up from https://github.com/digininja/sitediff (Ruby-based; follow the repo's README for dependencies).
2. Run it against a target URL to capture a baseline snapshot.
3. Re-run later (or on a schedule/cron) to fetch again and diff against the baseline.
4. Read the output: highlighted content and structural changes between the two fetches.
5. Pivot: a changed value (new address/phone/name) → feed into the matching selector tool; a structural change → investigate what was added/removed and archive both versions.

## Inputs → Outputs
- **In:** `domain`/URL (fetched at two times, or two saved snapshots)
- **Out:** a diff highlighting content and structural changes on that `domain`
- **Empty/negative result looks like:** an empty/near-empty diff — the page is unchanged, or it renders content via JavaScript the fetcher didn't execute (dynamic pages may need a browser-based monitor instead).

## Gotchas & OpSec
- Interaction is CLI/local — no login, but you manage scheduling and storage of snapshots yourself.
- JS-heavy sites: a simple fetcher may not see client-rendered content; for those, use a headless-browser change-detector.
- OpSec: marked **active** because each run is a real request to the target from your host — proxy it for sensitive monitoring so repeated pulls don't fingerprint you.

## Overlaps ("do both")
- Pairs with hosted change-detection services and RSS readers like [[the-old-reader]] — sitediff is self-hosted and scriptable (full control, your egress); hosted watchers fetch from their own infrastructure and need no local setup.

## Trust & verifiability
`trust: community` — open-source from a reputable security-tools author (digininja); you can read the code and run it yourself, so behavior is auditable, but it is a lightweight utility, not a maintained enterprise product.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sitediff |
