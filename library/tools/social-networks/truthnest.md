---
id: truthnest
name: TruthNest
description: Use when you have an X/Twitter `username` and want deep account analytics (activity patterns, hashtags, mentions, bot-likelihood signals) — returns a behavioural social-profile.
url: https://app.truthnest.com/
category: social-networks
path:
- social-networks
bestFor: Analysing an X/Twitter account's posting behaviour, network, and authenticity signals for verification work.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
status: degraded
pricing: freemium
costNote: Originally free to the fact-checking community; the free tier was revoked after Twitter/X API pricing changes. Now access is gated behind a paid/quote arrangement — contact truthnest@atc.gr. Treat as effectively pay-gated.
opsec: passive
opsecNote: Analysis runs server-side against X's public data; the target is not notified. You must log into TruthNest, so your investigative identity is known to the operator (ATC, a Greek company) — use an investigative account, not your personal one.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Built by Athens Technology Center (ATC) for journalist/fact-checker use. Reputable origin, but reliant on X's API — coverage degraded as X restricted access.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
relatedTools:
- xcancel-nitter-mirror
aliases:
- Truth Nest
- app.truthnest.com
tags:
- twitter
- x
- account-analytics
- verification
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# TruthNest

> A journalist-grade X/Twitter account analyser: posting patterns, top hashtags/mentions, network, and authenticity signals for a single handle.

## When to use
You have an X/Twitter `username` and need more than the raw timeline — when the account posts, what it amplifies, who it mentions most (candidate `associate` links), and whether its behaviour looks automated. Useful for verifying whether an account tied to a subject is genuine, and for mapping who they interact with. Note the free tier is gone, so reach for this only when you have paid access.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log into https://app.truthnest.com/ with an investigative account (access is now paid/quote-based).
2. Enter the target X handle to run an analysis.
3. Read the dashboard: activity-by-hour/day, most-used hashtags, most-mentioned accounts, follower/following signals, automation indicators.
4. Pivot: most-mentioned accounts feed `associate` mapping; if you only need to *read* the timeline without paying, fall back to `[[xcancel-nitter-mirror]]`.

## Inputs → Outputs
- **In:** `username` (X/Twitter handle)
- **Out:** `social-profile` (behavioural analytics), `associate` (frequent-interaction accounts)
- **Empty/negative result looks like:** an error or empty report — the handle is suspended/protected, or X API limits blocked the pull; it does not mean the account is inactive.

## Gotchas & OpSec
- Human-in-the-loop: **account-login** plus a **payment wall** — the once-free service is now pay-gated.
- **Degraded:** X's API restrictions have reduced what these third-party analysers can retrieve; expect partial data.
- OpSec: **passive** toward the target, but the operator sees your account and queries — use an investigative login.

## Overlaps ("do both")
- Pairs with `[[xcancel-nitter-mirror]]` — the Nitter mirror gives you the raw, login-free timeline; TruthNest adds the quantified behavioural layer when you can access it.

## Trust & verifiability
`trust: community` — credible origin (ATC, for fact-checkers) but dependent on X data access that has degraded. Treat analytics as indicative and corroborate any authenticity judgement.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | truthnest |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
