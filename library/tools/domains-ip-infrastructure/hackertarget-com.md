---
id: hackertarget-com
name: hackertarget.com
description: Use when you have a `domain` (or a Google Analytics/AdSense ID) and want to find other sites run by the same owner — returns linked domains sharing the tracking code.
url: https://hackertarget.com/reverse-analytics-search/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Reverse Google Analytics / AdSense search to cluster sites owned by the same operator.
selectorsIn:
- domain
selectorsOut:
- domain
- associate
status: live
pricing: freemium
costNote: Free web tool and API, capped at 50 queries/day per IP; paid membership and enterprise plans raise the quota.
opsec: passive
opsecNote: HackerTarget queries its own crawl data, so the target site's logs never see you. Only HackerTarget sees your IP; use a clean IP if the volume matters. Nothing is sent to the domain owner.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running commercial OSINT/attack-surface vendor; results depend on how completely their crawler captured the analytics IDs.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- hacker-target
- hacker-target-reverse-dns
- online-tool-to-extract-links-from-any-web-page
aliases:
- HackerTarget reverse analytics
- reverse Google Analytics search
tags:
- domainsandips
- Domains & IPs
- reverse-analytics
source: uk-osint
lastVerified: '2026-07-17'
enrichment: full
---

# hackertarget.com

> HackerTarget's reverse-analytics search: paste a domain or a Google Analytics/AdSense ID and get back every other site the crawler saw using the same tracking code.

## When to use
You have a `domain` and suspect the same person or company runs a network of related sites. Sites built by one operator frequently share a single Google Analytics (`UA-…`/`G-…`) or AdSense (`pub-…`) account, so reverse-analytics clustering exposes hidden ownership links — the pivot from one shell site to the rest of the portfolio, and from there to the operator's identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://hackertarget.com/reverse-analytics-search/.
2. Enter either the `domain` (e.g. `example.com`) or, if you already have it, the raw tracking ID (`UA-11223344`, `pub-1122334455`).
3. Submit and read the list of associated web properties sharing that identifier.
4. Take each returned `domain` and run it through WHOIS/DNS tools to attribute ownership; recurring registrant emails/names across the cluster are strong `associate` links.
5. For scripted runs, hit `https://api.hackertarget.com/analyticslookup/?q=UA-123456` (same 50/day free cap).

## Inputs → Outputs
- **In:** `domain`, or a Google Analytics / AdSense ID
- **Out:** `domain` (sites sharing the tracker), `associate` (shared-owner inference)
- **Empty/negative result looks like:** an empty list or "no results" — the site has no captured analytics ID, uses a unique one, or HackerTarget's crawl never indexed it. Absence is not proof of no shared ownership.

## Gotchas & OpSec
- Coverage is only as good as HackerTarget's crawl; a site that changed its analytics ID or uses server-side tagging may not link up. Confirm findings with a second reverse-analytics source before asserting common ownership.
- The free tier is 50 queries/day per IP — budget them; the counter is shared with HackerTarget's other free API endpoints.
- OpSec: **passive** — you query HackerTarget, never the target domain, so the subject sees nothing.

## Overlaps ("do both")
- Pairs with `[[hacker-target-reverse-dns]]` and `[[hacker-target]]` — reverse-DNS and hosting clustering catch shared-owner links that analytics IDs miss (and vice versa), so run both angles on the same domain.

## Trust & verifiability
`trust: community` — HackerTarget is an established vendor, but reverse-analytics is inference from crawl data, so treat each linked domain as a lead to verify via WHOIS, not proof of common ownership on its own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hackertarget-com |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
