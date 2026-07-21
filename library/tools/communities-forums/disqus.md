---
id: disqus
name: Disqus
description: Use when you have a Disqus username and want that person's cross-site public comment history — returns social-profile, associate and text leads that can expose location, opinions, and other handles.
url: https://disqus.com
category: communities-forums
path:
- communities-forums
bestFor: Pulling a user's aggregated public comment history across every site that uses Disqus.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free to view public profiles and comment history; no account needed to read.
opsec: passive
opsecNote: Reading a public Disqus profile is anonymous browsing and does not notify the user. Avoid logging in with an attributable account; if you must, use a sock puppet. Note some users set their comment history to private, which you must respect.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Disqus is the genuine, widely-used comment-hosting platform; the profile pages are first-party, so the comment history shown is authentic (subject to the user's privacy setting).
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- disqus.com
tags:
- toddington
- curated-directory
- online-communities-blogs
- comments
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Disqus

> The dominant third-party comment system on news sites and blogs — and, because it aggregates one identity's comments across every host site, a strong pivot from a `username` to a person's opinions, timeline, and other handles.

## When to use
You have a Disqus `username` (or you have seen one comment and want the rest) and need the subject's full public comment footprint. A single Disqus profile collects everything that person posted across thousands of independent sites, so it can reveal recurring topics, a home region or timezone (from posting times and content), linked accounts they mention, and `associate` relationships from reply threads. This is one of the higher-yield community sources for building a picture of a person from a handle.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go directly to the profile: `https://disqus.com/by/<username>/` (this is the canonical public URL).
2. Read the **Comments** tab for the full history, and **Upvotes**/**Followers**/**Following** for network (`associate`) leads.
3. Read comment content and timestamps for self-disclosed location, employer, timezone, and other usernames the person references.
4. If you only have a name or email, search the person's known sites for their Disqus comments, or use the Disqus API/`site:disqus.com` web search to find the handle.
5. Pivot: other handles and named associates feed username-enumeration and people-search tooling.

## Inputs → Outputs
- **In:** `username` (Disqus handle).
- **Out:** `social-profile` (the aggregated profile), comment `text`/history, and `associate` links (followers/following, reply partners).
- **Empty/negative result looks like:** "This user's profile is private" or an empty comments tab — the account exists but has hidden its history; not the same as the handle being unused.

## Gotchas & OpSec
- Human-in-the-loop: none for reading public profiles.
- OpSec: **passive** — anonymous browsing; the target is not alerted. Do not follow/upvote from an attributable account.
- Privacy setting: many users hide their comment history; respect that and treat a private profile as a dead end rather than trying to circumvent it.

## Overlaps ("do both")
- Pairs with username-enumeration tools — those confirm the handle exists on many platforms, while Disqus uniquely gives you the actual comment *content* tied to it.

## Trust & verifiability
`trust: trusted` — first-party Disqus profile pages, so the comment history is authentic. The only caveats are user-set privacy and the usual need to corroborate self-reported details in comments.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | disqus |
| category | communities-forums |
| selectorsIn → selectorsOut | username → social-profile, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
