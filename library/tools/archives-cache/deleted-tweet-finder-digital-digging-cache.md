---
id: deleted-tweet-finder-digital-digging-cache
name: Deleted Tweet Finder (Digital Digging Cache)
description: Use when you have a tweet/`social-profile` URL and want to recover a deleted or edited tweet — returns cached/archived copies from Wayback, Archive.today, Ghostarchive, Google/Bing/Yandex caches.
url: https://cache.digitaldigging.org/
category: archives-cache
path:
- archives-cache
bestFor: One-click fan-out that checks many web caches/archives for a deleted tweet from a single Twitter/X URL.
selectorsIn:
- social-profile
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free tool by Henk van Ess (Digital Digging); no account or payment.
opsec: passive
opsecNote: You query third-party archives (Wayback, Archive.today, Ghostarchive, search-engine caches), never X/Twitter itself, so the account owner gets no signal. The tool builds lookup URLs client-side; using an archive only touches that archive, not the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Built by well-known OSINT trainer Henk van Ess; it orchestrates reputable public archives rather than holding data itself, but some cache sources need manual confirmation.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- ai-search-whisper
- digitaldigging-org
- digitaldigging-org-2
- visualorigins-digitaldigging-org
aliases:
- Digital Digging Cache
- cache.digitaldigging.org
tags:
- twitter
- deleted-tweets
- archive
- cache
source: osintambition-social
lastVerified: '2026-07-19'
enrichment: full
---

# Deleted Tweet Finder (Digital Digging Cache)

> A single-input launcher that checks every major web archive and search-engine cache for a deleted or edited tweet.

## When to use
You have the URL of a tweet that has been deleted, edited, or made inaccessible (or a profile whose posts vanished) and want to recover the original text/media. This tool takes one Twitter/X URL and fans it out across multiple archival services so you don't have to query each by hand.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cache.digitaldigging.org/.
2. Paste the tweet's URL (or the profile URL) into the search field.
3. Pick a service or use the composite option: automated sources include Google Cache, the Wayback Machine, Archive.today, and Ghostarchive; Bing/Yandex/Baidu cache checks are offered but need manual verification.
4. Read the output: each service opens the archived snapshot if one exists. The composite view fires several at once.
5. Pivot: capture the recovered text/media, note timestamps, and feed named accounts/links into further social-graph and archive tools.

## Inputs → Outputs
- **In:** a tweet or profile URL (`social-profile` / `username`)
- **Out:** archived/cached copies of the deleted tweet (recovered `social-profile` content)
- **Empty/negative result looks like:** every service returns no snapshot — the tweet was likely never crawled/archived before deletion; try the account-level Wayback captures or `[[visualorigins-digitaldigging-org]]` next.

## Gotchas & OpSec
- Some listed caches (Bing/Yandex/Baidu) are increasingly unreliable and need a manual look; treat a "no result" from those as inconclusive, not definitive.
- Twitter/X's own changes frequently break third-party access, so coverage of recent tweets is patchy — older tweets archive better.
- Human-in-the-loop: none required, but manual verification of borderline cache hits is wise.
- OpSec: passive — you touch archives, not the target's account.

## Overlaps ("do both")
- Pairs with `[[visualorigins-digitaldigging-org]]` (image/media origin) and `[[digitaldigging-org]]` — same author's toolset; run the cache finder for text, VisualOrigins for the attached media's provenance.

## Trust & verifiability
`trust: community` — a respected practitioner's front-end over public archives; trust flows from the underlying archive (Wayback/Archive.today), so cite the archived snapshot URL, not this launcher.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | deleted-tweet-finder-digital-digging-cache |
| category | archives-cache |
| selectorsIn → selectorsOut | social-profile, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
