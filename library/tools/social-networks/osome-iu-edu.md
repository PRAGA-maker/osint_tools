---
id: osome-iu-edu
name: OSoMe Mastodon Search (Indiana University)
description: Use when you have a `username`, `name` or keyword and want to search across many Mastodon/Fediverse instances at once — returns matching public posts and account profiles.
url: https://osome.iu.edu/tools/mastodon/
category: social-networks
path:
- social-networks
bestFor: Querying public Mastodon content across multiple instances from one dashboard, instead of searching each instance separately.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free academic research tool from Indiana University's Observatory on Social Media (OSoMe); no payment, though heavy/programmatic use may be rate-limited or require contacting OSoMe.
opsec: passive
opsecNote: You are querying an OSoMe-operated index of already-public Mastodon posts, not the target's instance directly, so it is passive and does not notify the subject. As with any hosted tool, OSoMe sees your queries — avoid pasting sensitive selectors you must keep private.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Observatory on Social Media at Indiana University, a well-established academic research center behind Botometer, Hoaxy and related tools.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- OSoMe Mastodon
- Observatory on Social Media Mastodon Search
tags:
- mastodon
- Mastodon Related Sites
- fediverse
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- botometer
- botometer-by-osome
- botslayer
- covaxxy
- network-tool
- trends-tool
---

# OSoMe Mastodon Search (Indiana University)

> An academic dashboard that lets you query public Mastodon content across many instances at once — the practical answer to the Fediverse's lack of global search.

## When to use
The subject may be active on Mastodon/the Fediverse, where there is no single search box and content is scattered across thousands of independent instances. You have a `username` (a handle, possibly reused from Twitter/X), a `name`, or a keyword/topic, and want to find their public posts or account without knowing which instance they're on. Reach for this to locate a Fediverse footprint or track a discussion.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://osome.iu.edu/tools/mastodon/.
2. Enter the query — a `username`/handle, a `name`, or keywords — and run the cross-instance search.
3. Review the matching public posts and the accounts that authored them; note the instance domain in each handle (`@user@instance.social`).
4. Open a matched account on its home instance for its full public profile and post history.
5. Pivot: a confirmed handle feeds `[[sherlock]]`-style username searches on other platforms; the profile bio/links feed further identity work.

## Inputs → Outputs
- **In:** `username` / `name` / keyword
- **Out:** matching public posts, and the `social-profile` + display `name` of the accounts behind them
- **Empty/negative result looks like:** no matches — the subject isn't on the indexed instances, uses a different handle, is on an instance OSoMe doesn't cover, or has a private/limited account; Fediverse coverage is inherently partial, so absence is weak evidence.

## Gotchas & OpSec
- Partial index: OSoMe cannot see every instance (many defederate or block indexing), so a miss never rules out Mastodon presence — also try searching the likely home instance directly.
- Research tool: it is built for study of information spread, so the UI and coverage can change; heavy use may be rate-limited.
- OpSec: passive — you query OSoMe's index of public posts, not the target.

## Overlaps ("do both")
- Pairs with `[[sherlock]]`/username hunters — those check whether the handle exists across platforms; OSoMe surfaces the actual Mastodon posts and instance.
- Pairs with other OSoMe tools (Hoaxy, Botometer) when assessing whether an account is coordinated or automated.

## Trust & verifiability
`trust: trusted` — operated by Indiana University's Observatory on Social Media, a reputable academic center; it indexes genuinely public Fediverse content, so hits are authoritative within its (partial) coverage.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osome-iu-edu |
