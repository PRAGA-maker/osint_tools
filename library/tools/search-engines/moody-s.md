---
id: moody-s
name: Moody’s
description: Use when you have an `employer-org` (a company or bond issuer) and want its credit standing — returns issuer profiles, credit ratings, and ratings-action history.
url: https://www.moodys.com
category: search-engines
path:
- search-engines
bestFor: Corporate/issuer due diligence — looking up a company's Moody's credit rating and ratings history.
selectorsIn:
- employer-org
selectorsOut:
- employer-org
status: live
pricing: freemium
costNote: Basic issuer/rating pages and ratings news are viewable free (some behind a free registration); full research and analytics require a paid Moody's subscription.
opsec: passive
opsecNote: You look up a public company/issuer's rating — no individual is touched. If you register for the free tier you disclose an email to Moody's; use a sock-puppet email for sensitive research.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Moody's is a primary Nationally Recognized Statistical Rating Organization; its ratings are authoritative first-party financial data.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- Moodys
- moodys.com
- Moody's Ratings
tags:
- toddington
- curated-directory
- specialty-search
- credit-ratings
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Moody’s

> The credit-ratings agency's site — a due-diligence source for a company or bond issuer's credit rating and ratings history, not a people finder.

## When to use
Your subject is a company, financial institution, government, or bond issuer (`employer-org`) and you want its creditworthiness and financial standing: the current Moody's rating, outlook, and the history of upgrades/downgrades. Useful for corporate due diligence and following the money behind an organisation — its direct missing-persons value is low, but it corroborates an entity's legitimacy and financial trajectory.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.moodys.com and search the organisation/issuer by name.
2. Open the issuer page; register for the free tier if prompted (some content is gated).
3. Read the output: issuer profile, current rating and outlook, and rating-action history/press releases.
4. Pivot: rating actions name related entities and dates; the issuer profile ties to filings and corporate registries for deeper org mapping.

## Inputs → Outputs
- **In:** `employer-org` (company / issuer name)
- **Out:** issuer profile, Moody's credit rating + outlook, ratings-action history
- **Empty/negative result looks like:** no issuer found — the entity isn't rated by Moody's (most private/small orgs aren't), or the detail sits behind the paid tier; absence isn't evidence about the entity itself.

## Gotchas & OpSec
- Coverage is **rated issuers only** — large corporates, banks, sovereigns, funds; ordinary private companies and individuals won't appear.
- The most useful analytics are paywalled; the free layer is ratings + news.
- OpSec: passive; a free-tier registration exposes an email — use a sock puppet.

## Overlaps ("do both")
- Pairs with corporate registries (OpenCorporates, SEC EDGAR) and the other rating agencies (S&P, Fitch): registries give ownership/filings, Moody's gives credit standing — combine for a full org picture.

## Trust & verifiability
`trust: trusted` — Moody's is a primary NRSRO; its ratings are authoritative. The limitation is scope and paywalling, not reliability.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | moody-s |
