---
id: deaditarchive-netlify-app
name: deaditArchive
description: Use when you have a `username`/topic tied to a banned or purged subreddit and want the removed posts — returns archived content from deleted Reddit communities.
url: https://deaditarchive.netlify.app/
category: social-networks
path:
- social-networks
bestFor: Browsing preserved posts from subreddits that Reddit removed/banned, recovering content no longer live on Reddit.
selectorsIn:
- username
selectorsOut:
- social-profile
- geolocation
status: live
pricing: free
costNote: Free, static archive site; no account or payment.
opsec: passive
opsecNote: Reading a static archive is passive — nothing is queried against Reddit or the subject and no one is notified. The site is hosted on alt-platform infrastructure; use a sock-puppet browser out of caution, but there's no target-side exposure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-run partisan archive of removed subreddits; content is preserved third-party copy — verify against other archives since selection and framing may be biased.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- reddit-timer
- search-it
- api-guesser
- dorksearch-netlify-app
aliases:
- Dead IT Archive
tags:
- reddit
- archive
source: osint4all
lastVerified: '2026-07-16'
enrichment: full
---

# deaditArchive

> A static archive of purged Reddit communities — preserves posts from subreddits Reddit banned or removed, recovering content that's otherwise gone from the live site.

## When to use
Your subject participated in a subreddit that Reddit later banned or quarantined out of existence, and their posts/comments there are no longer reachable via Reddit or normal search. deaditArchive keeps a browsable copy of some of those removed communities — useful for recovering statements, usernames, and self-disclosures from communities that were wiped.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the archive in a sock-puppet browser.
2. Browse to the archived community relevant to your subject (30+ communities, organized by subreddit).
3. Page through preserved posts; use in-page/browser find to search for a `username`, keyword, or name.
4. Read recovered posts for self-disclosed details (location, associates, links).
5. Pivot: a recovered username feeds cross-platform search; content/timing corroborates a subject's affiliation with that community.

## Inputs → Outputs
- **In:** a `username` / community / keyword to look for
- **Out:** archived Reddit posts (`social-profile` activity) that may reveal `geolocation` and personal details
- **Empty/negative result looks like:** the community or user isn't in the archive — it covers only a curated set of removed subreddits, so many users/communities won't appear; try a general Reddit archive (Pushshift-style) instead.

## Gotchas & OpSec
- Partial and partisan: it preserves a self-selected set of communities and may frame them ideologically — treat as a content source, not a neutral record.
- Snapshots are frozen; deleted-then-archived content may be incomplete or edited.
- Cross-verify recovered posts against another archive before relying on a quote.
- OpSec: passive static read.

## Overlaps ("do both")
- Pairs with Pushshift-style Reddit archives and `[[search-it]]` — those cover broad deleted-comment recovery; deaditArchive specifically preserves whole banned communities the others may not retain.

## Trust & verifiability
`trust: community` — a volunteer archive with a viewpoint; the posts are real captures, but confirm anything decisive against an independent Reddit archive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | deaditarchive-netlify-app |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
