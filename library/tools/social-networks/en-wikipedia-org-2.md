---
id: en-wikipedia-org-2
name: en.wikipedia.org
description: Use when you need an overview of far-right online platforms/ecosystems to decide where to search for an extremist-adjacent subject — returns background and platform names, not profiles.
url: https://en.wikipedia.org/wiki/Far-right_usage_of_the_internet
category: social-networks
path:
- social-networks
bestFor: Mapping the alt-tech / far-right platform landscape to guide where to look for a subject's online presence.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free encyclopedia article; no account.
opsec: passive
opsecNote: Reading a Wikipedia article is invisible to any subject. Background research only.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Wikipedia is community-edited; strong for a landscape overview and platform names, but corroborate specific claims against the cited primary sources.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Far-right usage of the internet
tags:
- rightwingsocialmediasites
- Right Wing Social Media Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# en.wikipedia.org

> Wikipedia's "Far-right usage of the internet" article — a landscape map of the alt-tech platforms, forums, and tactics used by far-right communities, useful for deciding *where* to search when a subject moves off mainstream networks.

## When to use
This is a **strategy primer, not a lookup**. When a subject appears deplatformed from mainstream sites or their trail points to fringe communities, this article names the ecosystem — Gab, BitChute, Telegram channels, imageboards, Odysee, and the recruitment/coordination patterns around them — so you know which platforms to actually go and search. It turns "they're not on Facebook" into a concrete list of next places to look.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read https://en.wikipedia.org/wiki/Far-right_usage_of_the_internet for the platform inventory and behavioral patterns.
2. Build a checklist of named platforms relevant to your subject's region/language.
3. For each, run a targeted search — the platform's own search or a Google `site:` dork with the subject's `username`/`name`.
4. Pivot: any profile found is a `social-profile` to enrich; cross-reference handles across the listed platforms since users often reuse them.

## Inputs → Outputs
- **In:** the `name`/`username` under investigation (used to scope which platforms to check)
- **Out:** a map of platforms and tactics + pointers to primary sources — not a person record
- **Empty/negative result looks like:** N/A — it's an article; the failure mode is treating a contested, community-edited claim as verified.

## Gotchas & OpSec
- OpSec: **passive** — reading Wikipedia is invisible to the subject.
- Community-edited: use for orientation, verify specifics via footnotes. The platform landscape shifts fast, so treat the list as a starting point, not exhaustive.
- Some named platforms host illegal content — apply your legal/ethical guardrails before browsing them directly.

## Overlaps ("do both")
- Pairs with `[[en-wikipedia-org-3]]` (deep-dive on BitChute specifically) — use this to pick platforms and that to understand one in detail, then hunt with `[[google-com-85]]`/site-dorks.

## Trust & verifiability
`trust: community` — Wikipedia's crowd-sourced editing is reliable for a landscape overview but not authoritative on contested specifics; follow the cited sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | en-wikipedia-org-2 |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
