---
id: tweepsect
name: Tweepsect
description: Use when an old workflow references Tweepsect for Twitter follower-overlap analysis — returns nothing live; the service is defunct, so pivot to a current follower-intersection method.
url: https://tweepsect.com/
category: social-networks
path:
- social-networks
- twitter
- analytics
- profile
bestFor: Recognising a dead follower-overlap tool and switching to a working approach for comparing two accounts' networks.
selectorsIn:
- username
selectorsOut:
- associate
- social-profile
status: down
pricing: free
costNote: Defunct; nothing to pay for or query.
opsec: passive
opsecNote: The endpoint no longer functions, so there is nothing to leak by "using" it. Do not enter credentials anywhere claiming to be Tweepsect.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Historical third-party Twitter analytics site that is no longer operational; retained only as a pointer away from it toward live alternatives.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- tweepsect.com
tags:
- twitter
- analytics
- follower-overlap
- defunct
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Tweepsect

> A defunct Twitter/X follower-overlap analyzer — kept only so an agent recognises the name is dead and redirects to a working way of comparing two accounts' networks.

## When to use
You find Tweepsect cited in an older OSINT playbook for computing the intersection of two Twitter accounts' followers/following (mutuals, shared audiences). It no longer works — the site and its API are down. Use this entry to confirm the dead end and move to a live method rather than hunting for the tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Recognise that `tweepsect.com` is non-functional; do not spend time trying to make it load or trust look-alike clones.
2. To achieve the original goal (whose followers overlap between account A and B), pull each account's follower/following list with a current method — the platform's own API/export, or a scraping tool that still works against X — and compute the set intersection yourself.
3. For a single account's network, an Instagram/Twitter extractor such as `[[osintgram]]` (Instagram) or a live X-network tool covers the enumeration step.
4. Pivot: shared `associate` handles that appear in both networks are the high-value leads to enrich further.

## Inputs → Outputs
- **In:** `username` (historically, two of them to intersect)
- **Out:** intended `associate`/`social-profile` overlap sets — but **none are produced**, because the service is down
- **Empty/negative result looks like:** the site fails to load or returns errors; that is the expected state, not a transient outage.

## Gotchas & OpSec
- The tool is dead — treat any site now serving under that name as untrusted.
- OpSec: passive by default; never enter Twitter/X credentials into a revived clone.
- The follower-intersection *technique* remains valid even though this specific tool is gone.

## Overlaps ("do both")
- The underlying goal overlaps with network-extraction tools; for the analogous Instagram workflow see `[[osintgram]]`, then compute overlaps manually.

## Trust & verifiability
`trust: unverified` — non-operational service; nothing it (or a clone) returns can be relied upon. Verify network overlaps with live data instead.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tweepsect |
| category | social-networks |
| selectorsIn → selectorsOut | username → associate, social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
