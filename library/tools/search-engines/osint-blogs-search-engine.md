---
id: osint-blogs-search-engine
name: OSINT Blogs Search Engine
description: Use when you have a `name`, `username`, tool, or technique and want to search a curated set of OSINT blogs and practitioner writeups at once — returns document-id, social-profile.
url: https://cse.google.com/cse?cx=fd4729049350a76d0
category: search-engines
path:
- search-engines
bestFor: Searching a curated collection of OSINT blogs and practitioner writeups in a single query.
selectorsIn:
- name
- username
selectorsOut:
- document-id
- social-profile
status: live
pricing: free
costNote: Free Google Custom Search Engine; no account required.
opsec: passive
opsecNote: Passive — it's a Google-powered search, so queries go to Google, not to any subject. Use a sock-puppet/logged-out Google session if the query pattern itself is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-built Google Custom Search Engine; its coverage is only the sites the curator added and can drift as blogs move, rename, or close.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
aliases:
- OSINT blogs CSE
tags:
- search
- osint-blogs
- google-cse
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# OSINT Blogs Search Engine

> A Google Custom Search Engine scoped to a curated list of OSINT blogs and practitioner sites — search across the community's collective writeups in one box.

## When to use
You're stuck on a technique, tool, or target type and want to see **how other investigators have handled it** — or you're searching a `name`/`username`/handle that a practitioner may have written up in a case study. Instead of guessing which blog covered it, this CSE queries the whole curated set at once and returns the relevant posts (`document-id`) and any profiles/handles they mention.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE at https://cse.google.com/cse?cx=fd4729049350a76d0.
2. Enter your query — a technique ("reverse image face"), a tool name, or a specific `name`/`username`.
3. Read the results, which are limited to the OSINT blogs in the CSE's site list.
4. Refine with Google operators (quotes, `-`, phrase matching) as you would in normal Google.
5. Pivot: a writeup often names the exact tool/step to use next, or surfaces a `social-profile`/handle tied to your subject that a practitioner documented.

## Inputs → Outputs
- **In:** `name`, `username`, tool, or technique keywords
- **Out:** blog posts / writeups (`document-id`) and any `social-profile`s/handles referenced in them
- **Empty/negative result looks like:** no hits — the topic isn't covered by the blogs in this particular CSE (try a normal Google search or a different OSINT CSE); it's not evidence the topic is undocumented.

## Gotchas & OpSec
- It's just Google under the hood, scoped to a fixed site list; **coverage is whatever the curator configured** and silently decays as sites go offline.
- No login, no CAPTCHA in normal use.
- For sensitive query strings, search from a sock-puppet Google session so the pattern isn't tied to your main account.

## Overlaps ("do both")
- Pairs with a plain Google search and with other OSINT link collections — the CSE is narrow-but-relevant, while open Google is broad; run both when a curated search comes up empty.

## Trust & verifiability
`trust: community` — a hobbyist-maintained CSE; the *engine* is Google (reliable), but the *scope* is an opaque curated list, so treat coverage as partial and unversioned.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-blogs-search-engine |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → document-id, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
