---
id: world-channel-television-united-states
name: WORLD Channel (United States)
description: Use when you have a `name` and want US public-TV documentary/social-issue coverage of a subject — returns `social-profile`/mention, program context and named `associate` links.
url: http://worldchannel.org
category: communities-forums
path:
- communities-forums
bestFor: Searching a US public-television documentary/social-issue channel for a person featured, interviewed, or credited.
selectorsIn:
- name
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free public-broadcasting content; no paywall or account needed.
opsec: passive
opsecNote: Reading and dorking a public broadcaster site is passive and invisible to any subject; only the channel's servers log the visit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: A US public-media channel (PBS/WGBH-affiliated) focused on documentary and social-issue programming; credible content, still secondary to primary records.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- WORLD Channel
- worldchannel.org
tags:
- news-media
- documentary
- united-states
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# WORLD Channel (United States)

> A US public-television channel focused on documentaries, non-fiction and social-issue programming — a niche archive where a documentary subject, interviewee or contributor may appear.

## When to use
You have a `name` and a documentary/social-issue angle — the subject may have featured in, been interviewed for, or contributed to non-fiction programming (community stories, social justice, world affairs). WORLD Channel's catalogue and companion articles can confirm such an appearance, giving a date, program context, named associates, and quotes. Narrow in scope; most people won't appear, but for those connected to documentary content it can be a rich, in-depth source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Use the site's search, or Google-dork it: `site:worldchannel.org "<full name>"`.
2. Open matching program/article pages and read for the connection — featured subject, interviewee, or contributor — with date and named associates.
3. Follow to the producing station/series (often PBS/WGBH-affiliated) for fuller credits.
4. Pivot: named `associate`s/interviewees feed relationship mapping; a program appearance feeds broader media and social lookups; credits confirm a production role.

## Inputs → Outputs
- **In:** `name`
- **Out:** `social-profile`/mention, named `associate`s, program context and date
- **Empty/negative result looks like:** no hits — the subject has no footprint here (the common case); disambiguate same-name matches by program context.

## Gotchas & OpSec
- Very niche (documentary/social-issue) — irrelevant for most subjects.
- Same-name collisions; confirm identity from program context.
- Documentary content is edited/interpretive — corroborate specifics with primary records.

## Overlaps ("do both")
- Pairs with `[[pbs-television-united-states]]` and general news search — WORLD adds documentary/social-issue depth; those add breaking and mainstream coverage.

## Trust & verifiability
`trust: trusted` — a public-media channel with documentary standards; credible content, still secondary to anchor against primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | world-channel-television-united-states |
| category | communities-forums |
| selectorsIn → selectorsOut | name → social-profile, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
