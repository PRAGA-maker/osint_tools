---
id: first-tweet
name: First Tweet
description: Use when you want the earliest tweet mentioning a keyword/link — DEFUNCT (the ctrlq.org/first tool is offline and Twitter's API changes broke it); retained as historical reference.
url: http://ctrlq.org/first/
category: social-networks
path:
- social-networks
bestFor: Historical reference only — the tool is offline; use a live alternative for earliest-tweet discovery.
selectorsIn:
- name
selectorsOut:
- social-profile
status: down
pricing: free
costNote: Was a free web tool; now returns HTTP 404 and is no longer maintained.
opsec: passive
opsecNote: The endpoint is dead (404). Do not rely on any page that loads there; a lapsed/parked domain could be repurposed. Do not enter data expecting a trustworthy result.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Formerly a popular Amit Agarwal (Digital Inspiration/ctrlq.org) utility; now defunct, largely due to Twitter/X API restrictions that removed the free search access it relied on.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
deprecated: true
relatedTools:
- social-searcher
- whopostedwhat-com
aliases:
- ctrlq first tweet
- first tweet finder
tags:
- twitter
- search
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# First Tweet

> A once-popular tool for finding the earliest tweet mentioning a keyword or link — now **defunct**; kept here so agents recognize it and route to a working alternative.

## When to use
Effectively never in live casework — the tool is offline (404) and Twitter/X's API changes removed the free search access it depended on. This entry exists so that when you find "First Tweet" (ctrlq.org/first) referenced in older OSINT guides, you know it no longer works and can pivot immediately. When you want to find the earliest post mentioning a term, use a current alternative instead (see Overlaps).

## How to use it (`bestInteractionPattern`: web-manual)
1. Don't rely on it — the URL returns HTTP 404 and is unmaintained.
2. If a page ever loads there again, treat it as untrusted (a lapsed domain can be repurposed) and enter nothing meaningful.
3. Route earliest-tweet/keyword-timeline discovery to a maintained tool.

## Inputs → Outputs
- **In:** `name`/keyword (historically)
- **Out:** historically the earliest matching tweet; **today: nothing** (404)
- **Empty/negative result looks like:** the expected state — the service is down and returns no usable data.

## Gotchas & OpSec
- Marked `deprecated`/`down`; do not treat any result as evidence.
- Reflects the broader collapse of free Twitter/X search tooling after the API paywall — many similar utilities are also dead.
- OpSec: passive, but the safe posture is to avoid the dead endpoint entirely.

## Overlaps ("do both")
- Superseded for term-over-time search by [[whopostedwhat-com]] (Facebook by date) and [[social-searcher]] (multi-network real-time search) — use those instead of First Tweet.

## Trust & verifiability
`trust: unverified` — a formerly reputable utility that is now defunct with no working endpoint; retained only as a historical marker, not a usable source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | first-tweet |
| category | social-networks |
| selectorsIn → selectorsOut | name → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
