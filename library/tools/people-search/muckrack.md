---
id: muckrack
name: Muck Rack
description: Use when you have a `name` (or `employer-org`) for a journalist/media figure and want their beat, outlet and social presence — returns `social-profile`, `employer-org` and published work.
url: https://muckrack.com
category: people-search
path:
- people-search
bestFor: Profiling journalists, editors and PR/media professionals — their outlet, beat, bylines and linked social accounts.
selectorsIn:
- name
- employer-org
selectorsOut:
- social-profile
- employer-org
- name
status: live
pricing: freemium
costNote: Public journalist portfolio pages (muckrack.com/<name>) are free to view. The searchable media database and monitoring tools are a paid B2B subscription.
opsec: passive
opsecNote: Viewing a public Muck Rack profile is passive and anonymous. Reaching profiles via a search engine (site:muckrack.com) avoids logging into the platform at all; the paid database requires an account that ties searches to you.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established commercial media-relations platform; journalist profiles are self-claimed and aggregate real bylines/social accounts, so data quality is high for its niche.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- MuckRack
- muckrack.com
tags:
- expert-search
- journalists
- media
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# Muck Rack

> The go-to database of journalists and media people — use a free public profile page to tie a reporter's name to their outlet, beat, bylines and social accounts.

## When to use
Your subject is (or might be) a journalist, editor, columnist, podcaster or PR/comms professional and you have a `name` or the `employer-org` they write for. A Muck Rack profile consolidates a media person's outlet, beat, recent articles, and the social accounts (X/Twitter, LinkedIn, etc.) they've linked — a fast way to confirm identity and open pivots. It is niche (media professionals only), so it's a low-yield check for the general population but high-value when the subject works in or around the press.

## How to use it (`bestInteractionPattern`: web-manual)
1. Try the direct profile URL pattern `https://muckrack.com/<firstname>-<lastname>`, or Google `site:muckrack.com "Full Name"` to land on the public page without logging in.
2. On the profile, read: current outlet/title, beat/topics, list of recent bylines, and the linked social profiles.
3. Follow the linked `social-profile` accounts and bylines to corroborate identity and gather more selectors (contact info, location clues in articles).
4. If you need to search *by beat/outlet/keyword* across all journalists (rather than look up a known name), that's the paid media database — treat it as a human-in-the-loop, budget-gated step, not a free query.
5. Pivot: linked bylines feed article-level OSINT; linked socials feed username/social tooling.

## Inputs → Outputs
- **In:** `name` (best) or `employer-org`
- **Out:** `employer-org` (outlet), beat, byline list, linked `social-profile` accounts, confirmed `name`/title
- **Empty/negative result looks like:** no profile at the guessed URL and no `site:muckrack.com` hit — the person likely isn't a covered media professional (or hasn't claimed a page). That's a strong signal to look in general people-search tools instead.

## Gotchas & OpSec
- Coverage is limited to journalists/media/PR — do not expect a page for an average subject.
- Profiles are partly self-maintained; titles/outlets can be stale. Confirm against a recent byline.
- The rich search (by topic, outlet, region) sits behind a paid subscription; the free angle is direct/public profile lookup via search engines.

## Overlaps ("do both")
- Pairs with general people-search and social-username tools: Muck Rack confirms the *media* identity and links accounts; the others fill in personal selectors it omits.

## Trust & verifiability
`trust: trusted` — a well-known commercial platform used across the PR/journalism industry. Public profiles aggregate genuine, verifiable bylines and self-linked accounts, though (as always with self-claimed data) confirm current employer against a live byline.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | muckrack |
| category | people-search |
| selectorsIn → selectorsOut | name, employer-org → social-profile, employer-org, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
