---
id: udon
name: udon
description: Use when you have a `domain` and want other sites run by the same owner via a shared Google Analytics/AdSense ID — returns sibling `domain`s linked by tracking code.
url: https://github.com/dhn/udon
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Pivoting from one domain to a network of sites sharing the same Google Analytics/AdSense tracking ID.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source Go tool; it queries free third-party APIs (HackerTarget, OSINT.sh, SpyOnWeb, Site-Overview) that may rate-limit.
opsec: passive
opsecNote: Passive — it queries third-party ID-to-domain databases, never the target's own sites, so the domain owner sees nothing. The lookup services log your queries; route through a clean IP for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A community Go tool (dhn/udon, ~180 stars); its accuracy depends entirely on the third-party ID databases it aggregates, which are incomplete and can be stale.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- spyonweb
- analyzeid
- builtwith
aliases:
- udon
- dhn udon
tags:
- Domain/IP/Links
- Website analyze
- analytics-id
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# udon

> A one-flag CLI that turns a Google Analytics/AdSense ID into a list of every other domain using it — the classic "sites run by the same person" pivot.

## When to use
You have a `domain` tied to a subject and want to find their *other* sites. Many operators reuse one Google Analytics (`UA-…`/`G-…`) or AdSense (`pub-…`) ID across all their properties; udon takes such an ID and asks several ID-to-domain databases which other domains share it — often exposing a hidden network of related sites, aliases, or businesses.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `go install github.com/dhn/udon@latest` (or clone and `go build`).
2. First get the target's tracking ID: view the domain's page source and grep for `UA-`, `G-`, or `pub-` identifiers (or use `[[builtwith]]`).
3. Run: `udon -s UA-33427076` (add `-silent` for domains only, `-json` for machine-readable output).
4. udon queries HackerTarget, OSINT.sh, SpyOnWeb, and Site-Overview and prints the aggregated sibling `domain`s.
5. Pivot: WHOIS each new domain, diff their content/contact pages, and repeat the ID extraction on the new sites to expand the cluster.

## Inputs → Outputs
- **In:** a Google Analytics / AdSense ID (extracted from a `domain`)
- **Out:** other `domain`s sharing that tracking ID
- **Empty/negative result looks like:** no domains returned — the ID isn't in the third-party databases (common for new/obscure IDs), or the APIs rate-limited you; cross-check with SpyOnWeb directly.

## Gotchas & OpSec
- Coverage is only as good as the free databases behind it — absence is not proof; a shared ID also isn't ironclad proof of same ownership (agencies reuse IDs across clients).
- The upstream APIs rate-limit and occasionally change; expect partial results and re-run.
- OpSec: passive; you never touch the target's sites, only third-party ID indexes.

## Overlaps ("do both")
- Pairs with `[[spyonweb]]` and `[[analyzeid]]` (web front ends for the same ID-pivot) and `[[builtwith]]` (to extract the IDs and other fingerprints) — run several, since each database indexes different IDs.

## Trust & verifiability
`trust: community` — an open-source aggregator; the code is transparent but the results come from third-party databases of varying completeness, so corroborate a claimed link (shared ID + matching WHOIS/content) before asserting common ownership.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | udon |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
