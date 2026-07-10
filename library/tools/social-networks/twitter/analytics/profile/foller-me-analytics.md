---
id: foller-me-analytics
name: Foller.me Analytics
description: Use when you have a Twitter/X `username` and want a quick public-profile analysis — topics, hashtags, mentions and posting patterns — returns a social-profile summary and behavioural signals.
url: https://foller.me/
category: social-networks
path:
- social-networks
- twitter
- analytics
- profile
bestFor: Fast baseline profiling of a public Twitter/X account — follower stats, top topics/hashtags, frequent mentions, and posting-time patterns.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
status: degraded
pricing: free
costNote: Free web tool, no account. Its usefulness now depends on how much Twitter/X still lets third parties read from public profiles.
opsec: passive
opsecNote: Foller.me reads publicly visible profile data through its own interface — you never contact the target account, so it is passive. Standard operator logging applies.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party Twitter/X analytics site of unclear ownership; results depend on X's API access and can be incomplete or stale as those restrictions change.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Foller.me
- foller
tags:
- twitter
- analytics
- profile-analysis
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Foller.me Analytics

> A quick Twitter/X profile analyser — paste a handle and get a one-page read on the account's topics, hashtags, mentions and posting rhythm.

## When to use
You have a Twitter/X `username` and want a fast behavioural snapshot before deep-diving: what the account talks about (topics/hashtags), who it mentions most (`associate` leads), how active it is and when it posts (timezone/routine hints), plus basic follower stats. Good as a first-pass triage to decide whether an account is your subject and what angle to pursue.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://foller.me/ and enter the target Twitter/X `username`.
2. Read the generated report: numbers (followers/following/tweets), topic and hashtag clouds, most-mentioned accounts, and posting-time distribution.
3. Use the most-mentioned accounts as `associate` leads and the posting times as a timezone/routine signal.
4. Cross-check topics/hashtags against what you know of the subject to confirm the account is theirs.
5. Pivot: mentioned accounts feed network mapping; posting-time patterns feed timezone/location inference; confirmed account feeds full Twitter/X OSINT.

## Inputs → Outputs
- **In:** Twitter/X `username`
- **Out:** `social-profile` (analysed profile summary), `associate` (frequently-mentioned accounts)
- **Empty/negative result looks like:** an error, empty report, or "protected/unavailable" — increasingly common as X restricts third-party read access; a blank report reflects API limits, not necessarily an inactive account.

## Gotchas & OpSec
- **Degraded by X's API lockdown:** depth and freshness vary; treat metrics as approximate and re-verify on the live profile.
- Protected/private accounts won't analyse.
- OpSec: passive.

## Overlaps ("do both")
- Pairs with other Twitter/X analytics and advanced-search tools — Foller.me is the quick triage; combine with deeper tools for follower analysis, geolocation and timeline work.

## Trust & verifiability
`trust: unverified` — an opaque third-party analyser dependent on X's access; use it for a fast read and confirm anything important against the actual profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | foller-me-analytics |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
