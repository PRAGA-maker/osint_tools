---
id: osintteam-blog-2
name: osintteam.blog
description: Use when you want a curated shortlist of LinkedIn OSINT tools to try against a subject — returns a listicle of tools that surface `social-profile`s, not a lookup itself.
url: https://osintteam.blog/linkedin-osint-tools-for-osint-investigators-55e91e7c3d43
category: social-networks
path:
- social-networks
bestFor: A quick, curated inventory of current LinkedIn OSINT tools and what each is good for.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free Medium-hosted article (The OSINT Team publication); Medium may prompt a sign-in/paywall interstitial after a few free reads.
opsec: passive
opsecNote: Reading the article is passive. The tools it lists vary in OpSec — some require logging into LinkedIn (active, and visible via "who viewed your profile"); apply per-tool caution.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: The OSINT Team is a community Medium publication; a useful curated pointer, but a listicle — verify each named tool is still live and behaves as described.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- The OSINT Team LinkedIn tools
tags:
- linkedin
- LinkedIn & Similar Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
relatedTools:
- osintteam-blog
- osintteam-blog-3
---

# osintteam.blog

> A curated listicle from The OSINT Team of LinkedIn OSINT tools — a fast way to discover which tools to reach for when working a subject on LinkedIn.

## When to use
This is a **discovery reference, not a lookup**. When you need options for LinkedIn work — profile finders, Boolean builders, email-to-profile tools, connection mappers — this article rounds up current picks so you're not reinventing your toolkit each case. Use it to shortlist, then run the actual tools it names.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read https://osintteam.blog/linkedin-osint-tools-for-osint-investigators-55e91e7c3d43 for the tool roundup and each tool's stated use.
2. Pick the ones matching your selector (have a `name`? a company? an email?).
3. Verify each is still live (listicles age) and note its OpSec profile before use.
4. Pivot: run the chosen tools to surface `social-profile`s, then enrich with employment/associate detail.

## Inputs → Outputs
- **In:** the `name`/`username` you're investigating (used to pick tools)
- **Out:** a shortlist of LinkedIn OSINT tools → `social-profile`s when applied
- **Empty/negative result looks like:** N/A — it's an article; the risk is trusting a listed tool that has since died. Confirm before relying.

## Gotchas & OpSec
- Listicles decay — some named tools may be defunct or changed; verify each.
- Medium may interpose a sign-in/paywall after a few reads; use a reader mode or open incognito.
- OpSec: **passive** to read; the listed tools carry their own (often active) OpSec — check per tool.

## Overlaps ("do both")
- Pairs with `[[secjuice-com-3]]` (LinkedIn *methodology*) and `[[linkedprospect]]` (a concrete tool) — this points you to the toolset, those give you the workflow and a working query builder.

## Trust & verifiability
`trust: community` — a helpful community roundup, but a point-in-time listicle; treat it as a starting inventory and independently confirm each tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osintteam-blog-2 |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
