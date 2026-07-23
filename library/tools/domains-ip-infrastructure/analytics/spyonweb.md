---
id: spyonweb
name: SpyOnWeb
description: Use when you have a `domain` (or a Google Analytics/AdSense ID, IP or nameserver) and want to find other sites run by the same owner — returns related `domain`s sharing the same tracking/hosting fingerprint.
url: https://www.spyonweb.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- analytics
bestFor: Reverse-lookup by shared Google Analytics/AdSense ID, IP or DNS to uncover a person's or operator's other websites.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: degraded
pricing: free
costNote: Free to query on the web; a paid API tier exists. Availability is intermittent and its index can be stale.
opsec: passive
opsecNote: Fully passive — you query SpyOnWeb's own pre-collected index, not the target's sites, so nothing touches the subject's infrastructure and no one is notified. Confirm any surfaced link by viewing the shared Analytics/AdSense ID in the pages' source yourself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-standing reverse-analytics tool widely cited in OSINT guides; its database is periodically updated and can lag, so treat matches as leads to verify.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- SpyOnWeb
- spyonweb.com
tags:
- reverse-analytics
- adsense
- google-analytics
- domain-correlation
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# SpyOnWeb

> A reverse-lookup tool that links websites sharing the same Google Analytics ID, AdSense publisher ID, IP address or nameserver — a classic way to find "who else does this person own".

## When to use
You have a `domain` tied to a subject and suspect they run other sites. Personal and small-business sites frequently reuse the same Google Analytics or AdSense ID across every property. SpyOnWeb indexes those identifiers, so feeding one domain (or the raw `UA-`/`pub-` ID, IP, or nameserver) can surface a cluster of sibling sites operated by the same person — a strong pivot for mapping someone's online footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.spyonweb.com/ (retry if it's temporarily unavailable — the service is intermittent).
2. Enter the `domain`, or a Google Analytics ID (`UA-...`/`G-...`), AdSense publisher ID (`pub-...`), IP, or nameserver.
3. Read the returned list of connected domains grouped by the shared identifier.
4. Verify: open each candidate site and confirm the same Analytics/AdSense ID appears in its page source before treating the link as real.
5. Pivot: confirmed sibling domains feed WHOIS/registrant lookups and further footprint mapping.

## Inputs → Outputs
- **In:** `domain` (or Analytics/AdSense ID, `ip-address`, nameserver)
- **Out:** related `domain`s (and the shared `ip-address`/identifier)
- **Empty/negative result looks like:** no connections found — the site may use a unique/no analytics ID, or SpyOnWeb's index hasn't crawled it; cross-check with another reverse-analytics tool.

## Gotchas & OpSec
- **Stale/intermittent:** the index can lag and the site is sometimes down — retry and cross-check.
- **False links:** shared IPs (e.g. big shared hosting) can group unrelated sites; a shared *Analytics/AdSense* ID is far stronger evidence than a shared IP.
- Always confirm the shared ID in the live page source before asserting common ownership.

## Overlaps ("do both")
- Pairs with other reverse-analytics services (HackerTarget reverse analytics, Analyzeid, DNSlytics) — indexes differ, so run more than one and take the union; confirm overlaps in page source.

## Trust & verifiability
`trust: community` — a well-known but unofficial index; matches are leads. The underlying signal (a shared tracking ID) is independently verifiable by reading each site's HTML.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | spyonweb |
