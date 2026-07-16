---
id: authentic8-com-2
name: authentic8.com
description: Use when a subject may be on Mastodon/the Fediverse and you need to understand instances and federation before searching — returns platform orientation, not profiles.
url: https://www.authentic8.com/blog/introduction-mastodon-osint-practitioners
category: social-networks
path:
- social-networks
bestFor: Orienting on Mastodon/the Fediverse — instances, federation, and how to find where a subject's account lives.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free vendor blog article; no account.
opsec: passive
opsecNote: Reading the article is passive. When you then search Mastodon instances, do so logged out / via a sock account — some instances log profile views.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Published by Authentic8 (makers of Silo), a reputable managed-attribution/OSINT vendor; accurate platform primer, though it is Part 1 and stops before hands-on collection technique.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Authentic8 Mastodon OSINT
- Introduction to Mastodon for OSINT
tags:
- mastodon
- Mastodon Related Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
relatedTools:
- authentic8-com
- authentic8-com-3
---

# authentic8.com

> Authentic8's primer on Mastodon for OSINT practitioners — a background reference on the Fediverse's decentralized structure, useful before you go looking for a subject across independent instances.

## When to use
This is an **orientation reference, not a lookup**. Mastodon isn't one site — it's thousands of independently run instances that federate, so a subject's `username` might live on any of them and their content may or may not be visible from where you look. Read this before searching so you understand instances, federation, and the discovery tools (instances.social, Mastodon.Help, BuiltWith) it names — otherwise a Fediverse search flails.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read https://www.authentic8.com/blog/introduction-mastodon-osint-practitioners for the ActivityPub/instance model and the instance-discovery tools it lists.
2. Use those tools to enumerate candidate instances (by region, topic, or where a known handle resolves).
3. Search the subject's handle/name across candidate instances and via Fediverse search front-ends.
4. Pivot: a found account is a `social-profile`; its posts, follows, and instance choice are leads. Reused handles feed cross-platform username checks.

## Inputs → Outputs
- **In:** the `username`/`name` you're investigating (used to scope the Fediverse search)
- **Out:** platform understanding + tool pointers → Mastodon `social-profile`s when applied
- **Empty/negative result looks like:** N/A — it's an article; the failure mode is searching only one instance and concluding a subject isn't on Mastodon.

## Gotchas & OpSec
- It's Part 1: foundational knowledge, not step-by-step collection. Pair it with actual Fediverse search tools.
- Federation means visibility is partial — an account can exist on an instance your vantage point doesn't fully see; absence from one search is not proof.
- OpSec: **passive** to read; use a sock account when you browse instances.

## Overlaps ("do both")
- Pairs with Fediverse/username search tools and `[[en-wikipedia-org-2]]`-style landscape references — this explains *how Mastodon works*, those help you *find the account*.

## Trust & verifiability
`trust: trusted` — Authentic8 is an established OSINT/managed-attribution vendor and the platform facts are accurate; just remember it teaches orientation, not extraction.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | authentic8-com-2 |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
