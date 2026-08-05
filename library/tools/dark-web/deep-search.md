---
id: deep-search
name: Deep Search
description: Use when you have a `name`, `username` or `email` and want to see where it appears across Tor hidden services — searches indexed .onion pages, returns onion links / `social-profile` leads.
url: http://search7tdrcvri22rieiwgi5g46qnwsesvnubqav2xakhezv4hjzkkad.onion/
category: dark-web
path:
- dark-web
bestFor: Keyword/selector search across indexed Tor (.onion) sites to find where a name, handle or email surfaces on the dark web.
selectorsIn:
- name
- username
- email
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free to use; no account. Requires Tor Browser to reach the hidden service.
opsec: active
opsecNote: Reachable only over Tor — never load the onion address in a clearrealm browser or it will leak. Use Tor Browser (ideally on Tails/a VM). Searching a dark-web index is investigative but low-touch; still avoid entering identifiers that tie the query back to you, and treat any linked onion site as hostile (malware/illegal content) — do not click through carelessly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Anonymous-operator Tor search engine; coverage of the onion space is partial and its index freshness is unknown. Onion addresses rotate, so verify the current address (via a trusted dark-web link directory) before relying on this exact URL.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Deep Search onion
tags:
- darkweb
- Dark Web Links
source: uk-osint
lastVerified: '2026-08-05'
enrichment: full
---

# Deep Search

> A search engine over Tor hidden services: enter a term and get back .onion pages that mention it — the dark-web equivalent of a web search, for finding where a selector surfaces off the clear web.

## When to use
You have a `name`, `username`, or `email` that you suspect may appear on the dark web — a leaked-data mention, a forum handle, a marketplace vendor name, a paste — and you want to search indexed Tor sites for it. Deep Search crawls a slice of the .onion space, so it's a starting point for locating hidden-service pages that reference your subject when clear-web search comes up empty.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open Tor Browser (ideally on Tails or an isolated VM). Confirm the current onion address via a trusted dark-web link directory — the address above may have rotated.
2. Load the Deep Search hidden service and enter your term (`name`, `username`, or `email`).
3. Review the returned onion links. Treat every result as untrusted; note the URL and context without necessarily visiting.
4. Pivot: a handle or vendor name found here feeds username/`[[social-profile]]` correlation on the clear web and cross-marketplace searches.

## Inputs → Outputs
- **In:** `name`, `username`, or `email` (as a keyword)
- **Out:** links to .onion pages mentioning the term (`social-profile`/handle leads on hidden services)
- **Empty/negative result looks like:** no indexed onion pages match — the term isn't in Deep Search's (partial) crawl, which is NOT evidence it's absent from the dark web; try other Tor search engines and Ahmia.

## Gotchas & OpSec
- Onion addresses rotate and hidden services go down often — verify the current address and expect intermittent availability (hence `status: degraded`).
- Coverage is a fraction of the onion space; a miss means little. Corroborate across multiple dark-web search engines.
- Results can link to illegal or malicious content — record URLs, don't click through recreationally, and keep everything inside a hardened Tor environment.

## Overlaps ("do both")
- Pairs with other Tor search engines (e.g. Ahmia and additional onion indexers) — each crawls a different slice, so run the same selector through several to widen coverage.

## Trust & verifiability
`trust: unverified` — an anonymous-operator dark-web engine with unknown index freshness. Use it to *find* leads, then verify each onion page's content directly (in a safe environment) rather than trusting the search snippet.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | deep-search |
| category | dark-web |
| selectorsIn → selectorsOut | name, username, email → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
