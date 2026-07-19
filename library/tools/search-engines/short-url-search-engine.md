---
id: short-url-search-engine
name: Short URL Search Engine
description: Use when you have a `username`, `name`, or keyword and want to find shortened links (bit.ly, t.co, goo.gl, etc.) referencing it — a Google Custom Search scoped to URL-shortener domains, returning short links you can then expand.
url: https://cse.google.com/cse?cx=017261104271573007538:magh-vr6t6g#gsc.tab=0
category: search-engines
path:
- search-engines
bestFor: Searching across many URL-shortener domains at once to surface shortened links tied to a term or handle.
selectorsIn:
- username
- name
selectorsOut:
- document-id
- social-profile
status: live
pricing: free
costNote: Free Google Custom Search Engine; no account required.
opsec: passive
opsecNote: You search Google's index (restricted to shortener domains), not the target; passive. Beware that actually visiting/expanding a discovered short link may hit a redirect that logs your visit — expand via a preview service, not by clicking, if you need to stay unseen.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party-configured Google Custom Search Engine over a fixed list of URL-shortener domains; results are genuine Google index hits, but coverage depends on the (unmaintained-by-you) domain list baked into the CSE.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- short URL CSE
- shortened link search
tags:
- url-shorteners
- custom-search-engine
- dorking
source: osint4all
lastVerified: '2026-07-19'
enrichment: full
---

# Short URL Search Engine

> A Google Custom Search Engine restricted to URL-shortener domains — search a term, handle, or name and it returns publicly indexed shortened links (bit.ly, t.co, goo.gl, tinyurl, and more) that you can then expand to their real destinations.

## When to use
You have a `username`, `name`, campaign tag, or keyword and want to find shortened links associated with it — for example short links a subject posts under a handle, or shorteners pointing at their content. Because shortened URLs hide their destination, finding and expanding them can reveal a subject's real sites, profiles, or files that a normal search wouldn't connect. It's a niche pivot, not a primary lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE at the URL above.
2. Enter your term — a `username`, `name`, or keyword — and search; results are limited to the shortener domains configured in the engine.
3. For each interesting short link, expand it safely (a URL-unshortener/preview service like unshorten.it or checkshorturl) to see the true destination before deciding to visit.
4. Assess the destination for relevance to the subject.
5. Pivot: expanded destinations feed domain-, social-, and people-search tools; a recurring destination ties multiple short links to one owner.

## Inputs → Outputs
- **In:** `username`, `name`, or keyword
- **Out:** `document-id`/`social-profile` — indexed shortened links and, after expansion, their destination pages
- **Empty/negative result looks like:** few or no hits — shorteners are sparsely indexed and the CSE's domain list is finite, so absence here says little; complement with direct shortener searches and general dorking.

## Gotchas & OpSec
- Human-in-the-loop: none to search; expanding links is a manual, careful step.
- OpSec: the **search** is passive. **Clicking** a discovered short link is active — the redirect (and its destination) can log your IP/UA and, for tracking shorteners, register a click — always expand via a preview service first.
- Coverage limits: results depend on both Google's index of shortener domains and the fixed domain list inside this CSE; it will miss newer or unindexed shorteners.

## Overlaps ("do both")
- Pairs with URL-expander/preview services and with general Google dorking — this CSE finds the short links; the expanders reveal where they go, and broad dorking catches shorteners outside the CSE's list.

## Trust & verifiability
`trust: community` — it is a user-built Google Custom Search Engine; the hits themselves are real Google index results (verifiable by re-searching), but its usefulness is bounded by the specific shortener domains its creator configured, which you can't see or update.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | short-url-search-engine |
| category | search-engines |
| selectorsIn → selectorsOut | username, name → document-id, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
