---
id: free-proxy-world
name: Free Proxy World
description: Use when you want a quick list of free public HTTP/SOCKS proxies filtered by country, anonymity and type — returns proxy `ip-address`:port entries (use with strong caution).
url: https://www.freeproxy.world
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Grabbing a filterable list of free public proxies (by country/anonymity/type) for low-stakes, throwaway browsing.
selectorsIn: []
selectorsOut:
- ip-address
status: live
pricing: free
costNote: Free proxy list; no account.
opsec: passive
opsecNote: Free public proxies are inherently untrustworthy — the operator can log, inject, or MITM your traffic, and many are compromised hosts. NEVER route logins, sensitive queries, or anything over HTTPS you care about through them. For real investigative anonymity use a paid VPN or Tor, not these.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: An aggregator of anonymous public proxies of unknown provenance; neither the list nor the proxies themselves can be trusted, so treat every entry as hostile until proven otherwise.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- freeproxy.world
- Free Proxy World
tags:
- toddington
- curated-directory
- proxy-servers-online-privacy-security-tools
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# Free Proxy World

> A filterable list of free public proxies (HTTP/SOCKS, by country and anonymity level) — handy for a throwaway IP, but public proxies are a security minefield, so use only for low-stakes tasks.

## When to use
You need a disposable IP in a particular country for a low-sensitivity task — checking whether a site geo-blocks content, or viewing something region-restricted — and don't want to burn a "real" egress. Free Proxy World lets you filter public proxies by country, type and claimed anonymity. This is convenience tooling, **not** a way to achieve genuine investigative anonymity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.freeproxy.world.
2. Filter by country, protocol (HTTP/HTTPS/SOCKS) and anonymity level.
3. Copy a proxy `ip-address`:port and configure it in a throwaway browser profile.
4. Expect frequent failures — free proxies die constantly; test and rotate.
5. Pivot: use only for disposable geo-checks; for anything real, switch to a paid VPN or Tor.

## Inputs → Outputs
- **In:** filter criteria (country/type/anonymity) — not a personal selector
- **Out:** a list of proxy `ip-address`:port entries
- **Empty/negative result looks like:** most listed proxies are slow, dead, or refuse connections at any given moment — that's normal for free lists, not a fault of the site.

## Gotchas & OpSec
- **Serious trust warning:** free public proxies can log, tamper with, or intercept your traffic; some are honeypots or compromised machines. Never send credentials, personal accounts, or sensitive queries through them.
- They provide no real anonymity or integrity — do not rely on them for OpSec-critical work.
- Highly unstable: expect constant churn and test before use.

## Overlaps ("do both")
- Compare with a reputable paid VPN, Tor, or `[[mullvad-browser]]` — those are what you use for actual investigative anonymity; a free proxy list is only for disposable, low-stakes geo-checks.

## Trust & verifiability
`trust: unverified` — both the aggregator and the proxies are of unknown provenance; treat every entry as potentially hostile and never trust it with anything you can't afford to expose.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | free-proxy-world |
