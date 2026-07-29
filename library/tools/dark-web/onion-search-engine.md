---
id: onion-search-engine
name: Onion Search Engine
description: Use when you have a `username`/`email`/keyword and want to search Tor `.onion` content from the clearnet without running Tor — returns dark-web site/`social-profile` leads.
url: https://onionsearchengine.com/
category: dark-web
path:
- dark-web
bestFor: Clearnet keyword search across indexed Tor hidden services, with a proxy to preview results without a Tor browser.
selectorsIn:
- username
- email
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free to search from the clearnet; no account.
opsec: active
opsecNote: Searching is done on the clearnet, but Onion Search Engine offers a built-in proxy to open .onion results without Tor — using that proxy routes your request (and any content it fetches) through a third party you don't control, which is an OpSec and safety risk. For anything beyond a title/snippet, switch to Tor Browser on an isolated VM. Search from sock-puppet egress.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing community clearnet-to-onion search service; its crawl covers only a slice of Tor and, like all onion indexes, surfaces scam/phishing mirrors, so treat results as leads to verify.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- tor2web-tor-hidden-services-gateway
aliases:
- onionsearchengine.com
tags:
- darkweb
- onion-search
- Dark Web Links
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Onion Search Engine

> A clearnet search engine for Tor hidden services — query .onion content by keyword without first spinning up Tor, then pivot into a hardened Tor session to verify.

## When to use
You want to check whether a `username`, `email`, handle, or keyword appears on Tor hidden services and want a fast clearnet index to find candidate onion pages before committing to a full Tor session. It's a low-friction discovery step: run the search on the clearnet, triage the snippets, then open the promising ones properly in Tor.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://onionsearchengine.com/ from a sock-puppet browser/egress.
2. Search your `username`/`email`/keyword; read the result titles, snippets, and `.onion` addresses.
3. Do NOT rely on its proxy for real work — copy the promising `.onion` addresses and open them in Tor Browser on an isolated VM to verify.
4. Manually screen each hit for phishing mirrors and legality.
5. Pivot: a confirmed forum/market presence feeds breach-data and username-correlation work.

## Inputs → Outputs
- **In:** `username` / `email` / keyword
- **Out:** indexed `.onion` result pages, dark-web `social-profile`/site leads
- **Empty/negative result looks like:** no results — meaning nothing in this index's partial crawl matches, not proof of no dark-web footprint (cross-check another onion index).

## Gotchas & OpSec
- **Proxy risk:** its "open without Tor" proxy sends your traffic through an untrusted third party and can expose you to hostile content — use Tor Browser directly for anything past the snippet.
- Partial coverage + phishing mirrors: a single onion index sees a fraction of Tor and lists scam clones; corroborate across indexes.
- **Active** once you follow results into Tor; keep it in an isolated VM.

## Overlaps ("do both")
- Pairs with `[[tor-link]]` and the osint.me link lists (`[[osint-me-1]]`), and with `[[tor2web-tor-hidden-services-gateway]]` — run several onion indexes to widen coverage and catch clones; use a gateway only as a last resort, preferring native Tor.

## Trust & verifiability
`trust: community` — an established community onion index; fine for discovery, but never authoritative on which onion address is genuine — always verify in Tor.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | onion-search-engine |
