---
id: buzz-sumo
name: BuzzSumo
description: Use when you have a topic, `domain`, or `name` and want to find their top content, who shared it, and connected authors/journalists — returns `social-profile` and `associate` links via content analysis.
url: http://buzzsumo.com
category: social-networks
path:
- social-networks
bestFor: Finding the most-shared content on a topic/domain and the authors, influencers, and journalists connected to it.
selectorsIn:
- name
- domain
selectorsOut:
- social-profile
- associate
status: live
pricing: freemium
costNote: Paid platform ($199-$999/month); a limited free trial (no card) allows a few searches. Not a free OSINT tool — treat the trial as the only free access.
opsec: passive
opsecNote: Querying content analytics is passive and does not touch the subject. A trial/account requires giving BuzzSumo your details, so register with a sock-puppet identity if you use it; no signal reaches the target.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Established commercial content-intelligence platform; data (shares, authors, journalists) is aggregated and generally reliable for content discovery, but it is a marketing tool, not an identity database.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- socialblade
- talkwalker-social-media-search
- appsumo-content-analyzer
- buzzsumo
aliases:
- Buzz sumo
- buzzsumo.com
tags:
- real-time-search-social-media-search-and-general-social-media-tools
- content-analytics
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# BuzzSumo

> A commercial content-intelligence platform — surface the most-shared content on a topic or domain, and the authors, influencers, and journalists behind and around it.

## When to use
Your subject is a writer, marketer, journalist, or public figure who produces or is associated with online content, or you want to map who amplifies a particular `domain`/topic. BuzzSumo finds top-performing articles, the authors who wrote them, the influencers/journalists connected to them (`associate`), and their linked social profiles. It is a content-and-network tool, not a people-finder — hence low direct missing-persons value, but useful for professional/network mapping.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://buzzsumo.com and start a free trial (no card) or sign in — use a sock-puppet identity.
2. Search a topic, keyword, `domain`, or author `name`.
3. Read results: top content by engagement (Facebook/X/Reddit/YouTube), the authors, and — via the Influencer and Journalist tools — connected people and their `social-profile`s.
4. Use the "who shared" and author views to build a network of `associate` links.
5. Pivot: authors/influencers surfaced here feed name- and username-based OSINT; a subject's own content footprint corroborates their profession and interests.

## Inputs → Outputs
- **In:** topic/keyword, `domain`, or author `name`
- **Out:** top content, author/influencer/journalist `social-profile`s and `associate` connections
- **Empty/negative result looks like:** little or no indexed content for the query — common for private individuals with no publishing footprint; not evidence of anything about the person.

## Gotchas & OpSec
- Human-in-the-loop: it is a **paid** platform; beyond the limited free trial you hit a paywall. Budget accordingly or use the trial deliberately.
- Best for public content producers — it will find nothing on a subject with no online publishing/sharing footprint.
- OpSec: passive toward targets; only your own registration details are exposed to BuzzSumo — use a sock puppet.

## Overlaps ("do both")
- Pairs with `[[talkwalker-social-media-search]]` for broader social listening, and `[[socialblade]]` when the subject is a platform creator rather than a content author.

## Trust & verifiability
`trust: community` — a reputable commercial analytics vendor; its content and engagement data are reliable for discovery, but it aggregates third-party signals and is not an authoritative identity source. Confirm any person link on the underlying platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | buzz-sumo |
| category | social-networks |
| selectorsIn → selectorsOut | name, domain → social-profile, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
