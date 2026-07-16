---
id: deepfind-me
name: deepfind.me
url: https://www.deepfind.me/tools/social-media/username-search
category: people-search
path:
- people-search
description: Use when you have a `username` (or email/domain) and want to find every account it maps to — returns correlated `social-profile` links across 50+ platforms.
bestFor: Enumerating accounts tied to a single username across social, gaming, dev and content platforms in one report.
selectorsIn:
- username
- email
- domain
selectorsOut:
- social-profile
- username
status: live
pricing: freemium
costNote: Web username search runs free in the browser; higher-volume use, the API, and advanced tools (infostealer/breach lookup, profile analyzer) are gated behind accounts/paid plans.
opsec: passive
opsecNote: The tool queries third-party platforms server-side from DeepFind's own infrastructure, so your IP is not exposed to each checked site. It does not notify the account owner. Treat results as leads and confirm each profile directly before acting.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A cybersecurity vendor's hosted OSINT tool suite (not open-source); results are convenient but you cannot audit how each platform is checked, so verify hits manually.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- DeepFind.Me
- deepfind username search
tags:
- peoplesearch
- People Search Sites
- username-enumeration
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- deepfind-me-2
---

# deepfind.me

> A hosted OSINT suite whose username search fans a single handle out across 50+ social, gaming, dev and content platforms and returns the accounts that exist.

## When to use
You have a `username` (or an email/domain to seed it) and want a fast, broad map of every online account that handle touches. It is a first-pass enumerator: run the handle, get a list of candidate `social-profile` links, then confirm and mine the real ones. Useful early in a trace to convert one selector into many.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.deepfind.me/tools/social-media/username-search.
2. Enter the target `username` (the suite also accepts email/domain in related tools).
3. Run the check and read the report: each platform is flagged account-exists / not-found with a link.
4. Open each positive hit directly to confirm it is the same person (avatar, bio, cross-links) — automated existence checks produce false positives on common handles.
5. Pivot: confirmed profiles feed `[[whatsmyname-app]]`-style cross-checking, avatar reverse-image search, and bio-scraped emails/locations.

## Inputs → Outputs
- **In:** `username` (+ optional `email` / `domain`)
- **Out:** `social-profile` links, confirmed `username` presence per platform
- **Empty/negative result looks like:** all platforms return not-found, or only generic/parked pages — meaning the handle isn't used on the checked sites, not that the person has no online presence under a different name.

## Gotchas & OpSec
- Existence checks over-report on common usernames; every hit needs manual confirmation.
- The most powerful features (breach/infostealer lookup, profile analyzer, API) are gated — the free web check is enumeration only.
- OpSec: queries run from DeepFind's servers, so checked platforms don't see your IP; the tool is passive and does not alert the account owner.

## Overlaps ("do both")
- Pairs with `[[whatsmyname-app]]` and `[[username-search-tool]]` — different site lists catch different platforms, so running more than one enumerator improves recall.

## Trust & verifiability
`trust: community` — a maintained commercial OSINT tool used across the community, but closed-source and hosted, so treat its automated hits as leads to verify rather than confirmed facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | deepfind-me |
| category | people-search |
| selectorsIn → selectorsOut | username, email, domain → social-profile, username |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
