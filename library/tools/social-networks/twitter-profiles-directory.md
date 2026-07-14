---
id: twitter-profiles-directory
name: Twitter / X Profiles Directory
description: Use when you have a `name` and want to browse X/Twitter's alphabetical public-profile directory to locate an account — returns social-profile leads.
url: https://twitter.com/i/directory/
category: social-networks
path:
- social-networks
bestFor: Locating an X/Twitter account by browsing (or Google-dorking) the platform's alphabetical public directory of profiles.
selectorsIn:
- name
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free platform feature; under X, browsing the directory now generally requires being logged in.
opsec: passive
opsecNote: Browsing the directory does not notify anyone, but X requires a logged-in session — use a sock-puppet X account, and prefer Google site: dorks against the directory to avoid touching X directly.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A genuine X/Twitter platform feature, but coverage/accessibility has degraded under X's login walls; the directory is an index, not a name search, so it's best exploited via search-engine dorks.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
relatedTools:
- twitter-advanced-search
- google-dorks
aliases:
- Twitter directory
- X profiles directory
tags:
- twitter
- x
- directory
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# Twitter / X Profiles Directory

> X/Twitter's own alphabetical index of public profiles — a way to enumerate accounts by name, best mined through search-engine dorks rather than manual browsing.

## When to use
You have a `name` and want to find the person's X/Twitter account when direct search is noisy or rate-limited. The platform maintains an alphabetical directory of public profiles at `/i/directory/`; because it's crawlable-in-principle, the practical OSINT move is to Google-dork it (`site:twitter.com/i/directory "<name>"`) to enumerate candidate accounts. Reach for it as a complement when in-app search buries your target.

## How to use it (`bestInteractionPattern`: web-manual)
1. Best path: run a search-engine dork — `site:twitter.com/i/directory <name>` (or `site:x.com/i/directory`) — to list indexed directory entries without logging into X.
2. Direct path: open https://twitter.com/i/directory/ in a sock-puppet X session and navigate the alphabetical listing (login is now generally required).
3. Read the candidate profiles; match on display name, bio, and location before attributing.
4. Empty result → the target may not appear in the directory (many accounts don't) — fall back to in-app search and other platforms.
5. Pivot: a confirmed handle feeds `[[twitter-advanced-search]]` for the full timeline.

## Inputs → Outputs
- **In:** `name`
- **Out:** `social-profile` (candidate X/Twitter accounts)
- **Empty/negative result looks like:** no directory entries via the dork, or a login wall on the direct page — the directory's public visibility has shrunk under X, so absence here isn't absence on X.

## Gotchas & OpSec
- **Degraded:** X's login walls have reduced the directory's open accessibility; the Google-dork approach is more reliable than manual browsing.
- The directory is an alphabetical index, not a name search box — expect to sift.
- Use a burner X account for any logged-in browsing.

## Overlaps ("do both")
- Pairs with `[[twitter-advanced-search]]` (query the account once found) and `[[google-dorks]]` (the mechanism that makes this directory practically searchable). Do both: dork to enumerate, advanced search to enrich.

## Trust & verifiability
`trust: community` — a real platform feature whose OSINT value now depends on search-engine indexing more than the page itself. Confirm any candidate against the live profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitter-profiles-directory |
| category | social-networks |
| selectorsIn → selectorsOut | name → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
