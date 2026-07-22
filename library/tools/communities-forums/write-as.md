---
id: write-as
name: Write.as
description: Use when you have a `username` or Write.as blog handle and want to read someone's publicly published writing — returns `social-profile`, `name`.
url: https://write.as/
category: communities-forums
path:
- communities-forums
bestFor: Reading a subject's public long-form/anonymous blog posts and pivoting from a Write.as handle to identity clues.
selectorsIn:
- username
selectorsOut:
- social-profile
- name
status: live
pricing: freemium
costNote: Free tier supports anonymous publishing and reading; Pro (~$6/mo) adds custom domains, RSS and subscriptions. Reading public posts is entirely free.
opsec: passive
opsecNote: Reading a public Write.as blog or the "Read Write.as" feed is passive and invisible to the author. Only logging in, subscribing, or commenting is active — never do that from an attributable account.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Genuine first-party publishing platform (Musing Studio) — the posts it serves are authentic; the limiting factor is authorship, since Write.as is built for anonymous/pseudonymous writing.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- rentry
- justpaste
aliases:
- write.as
- writefreely
tags:
- pastebins
- blogging
- anonymous-publishing
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# Write.as

> A privacy-first, often-anonymous blogging platform — useful as a place a subject may have published long-form writing under a handle you already hold.

## When to use
You have a `username`, Write.as blog slug, or a link to a `write.as/<handle>` post and want to read what the subject has published and mine the prose for identity leaks (locations, first names, employers, recurring aliases). Also useful when a person is known to write anonymously and you are hunting for the platform they used — Write.as, and its self-hosted sibling WriteFreely, is a common choice for pseudonymous journals and manifestos.

## How to use it (`bestInteractionPattern`: web-manual)
1. If you have a blog slug, go directly to `https://write.as/<slug>` or the custom domain; individual posts live at `https://write.as/<random-id>`.
2. To discover posts, browse the public **Read Write.as** feed (https://read.write.as/), which surfaces everything registered writers have chosen to publish publicly.
3. Read the body for OSINT tells: place names, first names, job details, dates, cross-posted links (Mastodon, RSS, custom domain).
4. Pivot: a custom domain in the blog settings feeds WHOIS/domain OSINT; a reused handle feeds username enumeration; a cross-posted Mastodon/social link feeds `social-profile` lookups.

## Inputs → Outputs
- **In:** `username` / blog slug / direct post URL
- **Out:** `social-profile` (the blog and any linked accounts), occasionally `name` or location leaked in the prose
- **Empty/negative result looks like:** a 404 for the slug, or an author who kept everything unlisted — Write.as exposes no global search of private/unlisted posts, so absence here is not proof the person never wrote there.

## Gotchas & OpSec
- Authorship is deliberately anonymous — treat any `name` you extract as a lead to corroborate, never as confirmed identity.
- There is no username-directory search; you must already have a slug or find the post via the Read feed or an external search engine (`site:write.as <term>`).
- Passive to read; do not comment or subscribe from an attributable account.

## Overlaps ("do both")
- Pairs with `[[rentry]]` and `[[justpaste]]` — all are minimalist anonymous publishing/paste hosts favored for one-off posts, so check each when hunting where a subject dropped text under a handle.

## Trust & verifiability
`trust: trusted` — the platform is the genuine first-party host, so the content is authentic; verifiability of *who* wrote it is the limiting factor, not whether the post is real.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | write-as |
| category | communities-forums |
| selectorsIn → selectorsOut | username → social-profile, name |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
