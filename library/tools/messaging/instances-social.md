---
id: instances-social
name: Instances.Social
description: Use when you need to enumerate or pick Mastodon/fediverse servers — returns a searchable list of instances (`domain`s) with size, topic and moderation stats to target a username hunt.
url: https://instances.social/
category: messaging
path:
- messaging
bestFor: Enumerating Mastodon instances by topic/language/size to know where to search for a fediverse user.
selectorsIn:
- domain
selectorsOut:
- domain
- social-profile
status: live
pricing: free
costNote: Free directory; an API is offered (token-based) for programmatic listing. Manual browsing needs no account.
opsec: passive
opsecNote: Browsing the instance directory is passive — you're reading server metadata, not touching any user. Note that unlike centralised networks, checking a handle on a specific Mastodon instance later means querying that instance, whose admins can see requests; use a sock puppet when you move from listing servers to probing accounts.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A well-known community-run directory (by TheKinrar, open source); instance stats are self-reported by servers via the Mastodon API, so counts/topics are indicative, not audited.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- instances.social
- Mastodon instances directory
tags:
- Social Media
- Mastodon
- fediverse
source: cyb-detective
lastVerified: '2026-07-18'
enrichment: full
---

# Instances.Social

> A directory of Mastodon/fediverse instances — the map of "which servers exist" that tells you where to go looking for a fediverse user or community.

## When to use
The fediverse is decentralised: a user like `@alice@example.social` lives on one of thousands of independent servers. When you're hunting a Mastodon handle, investigating a community, or building a sock-puppet, you first need to know **what instances exist** and their character. Instances.Social lets you filter servers by language, topic, size, and moderation policy — useful for narrowing where a themed community or user is likely to be, or for choosing a plausible instance for a research account.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://instances.social/ and use the list / advanced filters (or the wizard).
2. Filter by language, user-count size, and moderation rules (NSFW, spam, advertising) to find instances matching a community's theme or a target's likely home.
3. Note candidate instance `domain`s; open each to browse its public local timeline and "about" (rules, admins).
4. Then search the target handle on those instances, or use the instance's public directory/search.
5. Pivot: an identified instance narrows a fediverse username search; instance admins/rules give context on a community.

## Inputs → Outputs
- **In:** filter criteria (topic/language/size), or a `domain` to look up
- **Out:** a list of instance `domain`s with stats, plus routes to their public `social-profile` timelines
- **Empty/negative result looks like:** filters too narrow return no instances, or a specific server isn't listed (new/private/opted-out) — instances.social only knows servers that expose stats. Absence here doesn't mean the server doesn't exist.

## Gotchas & OpSec
- Human-in-the-loop: none for browsing.
- OpSec: **passive** to list servers; but *probing accounts* on a specific instance queries that server, where admins may see it — switch to a sock puppet before that step.
- Stats are **self-reported** by each server via the Mastodon API and can be inflated, stale, or hidden; treat size/topic as indicative.
- It indexes Mastodon-style instances; other fediverse software (Pleroma, Misskey, Lemmy) may be under-represented.

## Overlaps ("do both")
- Do both with fediverse-wide user search tools and cross-platform username checkers — instances.social tells you *which servers* to search, the user-search tools find the *account* across them.

## Trust & verifiability
`trust: community` — a reputable open-source community directory; the server list is reliable as far as instances self-report, so verify individual instance stats by visiting the server directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | instances-social |
| category | messaging |
| selectorsIn → selectorsOut | domain → domain, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
