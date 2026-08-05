---
id: daunt-link
name: daunt.link
description: Use when you have a dark-web service name or want to reach a known onion site and need a verified, current .onion address — a clearnet-accessible, verified directory of Tor links and mirrors.
url: https://daunt.link/
category: dark-web
path:
- dark-web
bestFor: Finding a verified, working onion address (and backup mirrors) for a dark-web market, forum or service, from the clear web.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free clearnet directory; no account. Following the links themselves requires Tor Browser.
opsec: active
opsecNote: Browsing daunt.link's clearnet page is passive, but it deliberately warns you to DISABLE JavaScript, and any link you follow drops you onto Tor hidden services — reachable only through Tor Browser (ideally Tails/VM). Never open an onion link it lists in a normal browser. Treat every listed destination as hostile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Community-run onion directory with a per-link "verify" feature and mirror tracking; it curates addresses but vouches for nothing about the destinations. Onion listings churn — confirm freshness before relying on an address.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Daunt
- daunt.link directory
tags:
- darkweb
- Dark Web Links
source: uk-osint
lastVerified: '2026-08-05'
enrichment: full
---

# daunt.link

> A clearnet-accessible, verified directory of Tor onion sites — the address book you use to find a current, working .onion (plus mirrors) for a dark-web service before you go looking on Tor.

## When to use
You know the name of a dark-web service — a market, forum, exchanger, news site, privacy tool — or have a stale onion address that no longer resolves, and you need the current verified address (and backup mirrors) to reach it. Onion URLs rotate constantly and phishing clones abound; daunt.link maintains verified addresses so you start from a vetted link rather than a search-engine guess.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://daunt.link/ (accessible on the clear web; disable JavaScript as it warns).
2. Browse the categories (Forums, Markets, Shops, Other) or search for the service by name.
3. Use the per-entry "Verify" feature and note the listed mirrors — pick a verified, recently-checked address.
4. Pivot: switch to Tor Browser to open the confirmed onion `domain`; the mirrors give you fallbacks if the primary is down.

## Inputs → Outputs
- **In:** a dark-web service name or a `domain` (onion address you're trying to confirm)
- **Out:** verified `domain` (current onion address) plus mirror addresses and a verification status
- **Empty/negative result looks like:** the service isn't listed, or all its addresses show as unverified/dead — treat unlisted/unverified links as untrusted; cross-check with another onion directory before visiting.

## Gotchas & OpSec
- It's an address book, not a search engine over content — it points you to sites, it doesn't index what's inside them.
- Verification reduces (not eliminates) phishing-clone risk; still confirm the site's own signed mirror list once you arrive.
- Every destination is Tor-only and potentially illegal/malicious content — use a hardened Tor environment and never in a normal browser.

## Overlaps ("do both")
- Pairs with a Tor content search engine (e.g. `[[deep-search]]` / Ahmia): use the search engine to discover which service mentions your subject, then daunt.link to get that service's verified, current address.

## Trust & verifiability
`trust: unverified` — a useful community directory whose verify feature helps, but which cannot warrant the destinations. Confirm any critical address against a second trusted directory and the site's own canonical mirror list.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | daunt-link |
| category | dark-web |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
