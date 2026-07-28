---
id: onion-land
name: Onion Land
description: Use when you have a `username`, `email`, keyword or vendor name and want to find where it appears on Tor/I2P dark-web sites — returns .onion links and dark-web mentions from the clearnet.
url: https://onionland.io/
category: dark-web
path:
- dark-web
bestFor: Searching indexed Tor (.onion) and I2P content by keyword/selector from a normal browser to find dark-web pages mentioning a subject.
selectorsIn:
- username
- email
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free search; no account. Reading the .onion results themselves requires the Tor Browser.
opsec: active
opsecNote: The clearnet search at onionland.io is operated by an unknown third party that sees your queries — search from a sock-puppet/clean session and never enter case-identifying strings you don't want logged. Opening result .onion links requires Tor; do that only in the Tor Browser (ideally on an isolated VM), never in your normal browser, and treat dark-web pages as hostile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party dark-web search index of unknown operator; useful for discovery but results are unranked, noisy, and unverified.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- OnionLand Search
- onionland.io
tags:
- darkweb
- Dark Web Links
- tor-search
source: uk-osint
lastVerified: '2026-07-28'
enrichment: full
---

# Onion Land

> A clearnet-accessible dark-web search engine indexing Tor (.onion) and I2P content — a discovery tool for finding where a handle, address, or keyword surfaces on the dark web.

## When to use
You have a `username`, `email`, vendor name, or keyword tied to a subject and want to check whether it appears on dark-web sites — marketplaces, forums, paste/leak pages, directories. OnionLand lets you run that search from an ordinary browser, returning .onion (and I2P/clearnet) links you can then open in Tor. Use it to discover leads and dark-web mentions; it does not resolve identities on its own.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://onionland.io/ in a sock-puppet/clean browser session.
2. Search a specific selector or keyword (a handle, an email, a vendor alias). Quote exact strings to reduce noise.
3. Scan the results — titles and .onion URLs across Tor/I2P and some clearnet.
4. To read an .onion result, open it in the **Tor Browser** (never your normal browser), ideally on an isolated VM.
5. Pivot: a dark-web mention of a handle/email links to marketplace or forum activity; corroborate before drawing conclusions.

## Inputs → Outputs
- **In:** `username`, `email`, keyword/vendor name
- **Out:** .onion/I2P links and dark-web page mentions (a `social-profile`-style trail on hidden services)
- **Empty/negative result looks like:** few or no results — the index is partial and hidden services churn/rotate; absence is not proof the subject has no dark-web footprint.

## Gotchas & OpSec
- OpSec: **active/high-risk** — the clearnet operator logs your queries, and opening .onion links exposes you to hostile content. Use Tor + a disposable environment; never authenticate or transact.
- Dark-web indexes are noisy and incomplete; many results are dead, scam, or mirror links.
- Never enter sensitive case identifiers into the search box.

## Overlaps ("do both")
- Do both with other dark-web search engines (Ahmia, Tor-native indexes): each indexes a different, partial slice of hidden services, so cross-running a selector catches mentions any single engine misses.

## Trust & verifiability
`trust: unverified` — a third-party dark-web index of unknown operator. Good for discovery; every result must be independently verified, and the index makes no completeness or safety guarantees.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | onion-land |
| category | dark-web |
| selectorsIn → selectorsOut | username, email → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
