---
id: metafilter
name: MetaFilter
description: Use when you have a `username` (or real `name`) and want to surface a long-running community member's post/comment history and interests — returns social-profile and associate/interest leads.
url: http://www.metafilter.com
category: communities-forums
path:
- communities-forums
bestFor: Reading a MetaFilter member's full posting history and the sub-sites (Ask MetaFilter, Projects) they participate in.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Reading and searching are free. Posting requires a one-time $5 signup fee, but no payment is needed to research existing content.
opsec: passive
opsecNote: Browsing public member pages and threads leaks nothing to the subject. Do not create an account to interact with the target; if you must sign up to see anything gated, use a sock-puppet identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A well-established, moderated community weblog since 1999; user-generated content, so treat individual posts as self-reported and unverified.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- ask-metafilter
aliases:
- MeFi
- MetaFilter Community Weblog
tags:
- toddington
- curated-directory
- online-communities-blogs
- forum
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# MetaFilter

> A long-running moderated community weblog whose stable, real-history user profiles make it a good place to read a member's accumulated posts, questions, and interests.

## When to use
You have a `username` (MetaFilter handles are persistent and often reused across the web) or a `name` you think maps to a MetaFilter member, and you want to read their public activity: front-page posts, comments, and especially the personal questions they asked on **Ask MetaFilter** — which frequently reveal location, occupation, relationships, health, or life events. Best treated as a corroboration/interest source rather than a primary locator.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.metafilter.com. Use the site search, or query a search engine with `site:metafilter.com "<username>"` / the person's phrases.
2. Open a member's profile at `metafilter.com/user/<id>` to see join date, self-written bio, linked homepage/social accounts, and activity across the sub-sites (MetaFilter, Ask MetaFilter, Projects, Music, Jobs).
3. Read their **Ask MetaFilter** questions in particular — people disclose granular personal circumstances there when seeking advice.
4. Pivot: a self-linked homepage/social handle in the bio feeds username-search tools; disclosed city/employer/relationship details are corroboration leads.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `social-profile` (member page, self-linked accounts), plus interest/associate/location leads from post content
- **Empty/negative result looks like:** no member page and no `site:metafilter.com` hits — the handle simply isn't active here; MetaFilter is a niche community, so most people have no presence.

## Gotchas & OpSec
- Human-in-the-loop: none for reading; account creation (only needed to post, which you should not do) costs a one-time $5 fee.
- Content is self-reported community chatter — treat personal claims as leads to verify, not facts.
- OpSec: passive. Do not comment or message the subject; that would be active and alerting.

## Overlaps ("do both")
- Pairs with `[[ask-metafilter]]` — the Ask MetaFilter sub-site is where the richest personal disclosures live, so search both the main site and the Ask archive for a given handle.

## Trust & verifiability
`trust: unverified` — MetaFilter is a reputable, heavily-moderated community, but the value here is user-generated posts, which are self-reported. Corroborate any personal detail before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | metafilter |
| category | communities-forums |
| selectorsIn → selectorsOut | username, name → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
