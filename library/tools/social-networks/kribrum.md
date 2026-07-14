---
id: kribrum
name: Kribrum
description: Use when you have a `name` or `username` and want to monitor and analyze mentions across Russian-language social media, forums, and Telegram — returns social-profile, associate, and geolocation signals.
url: https://kribrum.io/
category: social-networks
path:
- social-networks
bestFor: Monitoring and analyzing a person's or topic's footprint across Russian-language social media, blogs, forums, YouTube, and Telegram at scale.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- associate
- geolocation
status: live
pricing: freemium
costNote: Enterprise social-listening platform — access is via paid subscription / demo, not an open free search. Expect a sales-gated onboarding.
opsec: passive
opsecNote: Monitoring indexed public posts is passive and does not contact the subject. Access requires a Kribrum account (a Russian vendor); use investigative-context credentials and be mindful of the jurisdiction when handling data.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Established Russian social-media monitoring firm (Kribrum / Ashmanov & Partners) with a dedicated analytics center; reliable within its Russian-language focus, but a commercial closed platform.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- vk-search
- brand24
aliases:
- Крибрум
- Kribrum Pro
tags:
- social-monitoring
- russia
- vk
- telegram
source: awesome-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Kribrum

> A Russian real-time social-media monitoring and analysis platform — strongest where Western tools are weakest: VKontakte, Russian forums, Telegram, and 23-language text analysis.

## When to use
Your subject has a Russian-language footprint — active on VK, Odnoklassniki, Russian forums, Telegram channels, or Russian-language YouTube — and you need to find and analyze mentions at scale. You have a `name`, `username`, or topic and want sentiment, geographic, and network analysis across sources that English-centric monitoring tools miss. Especially valuable for cases touching Russia, the CIS, or Russian diaspora communities.

## How to use it (`bestInteractionPattern`: web-manual)
1. Request access at https://kribrum.io/ (or kribrum.ru / kribrum.com) — this is a paid, account-gated platform, typically via demo/sales.
2. Set up a monitoring object for the `name`/`username`/keyword.
3. Read the analytics: sources and posts mentioning the target, sentiment, geographic breakdown, author network, and timeline.
4. Drill into individual authors/posts as `social-profile` and `associate` leads; note any location signals (`geolocation`).
5. Pivot: surfaced VK/Telegram profiles feed dedicated platform tools; the network map feeds associate analysis.

## Inputs → Outputs
- **In:** `name`, `username`, or keyword/topic
- **Out:** `social-profile` (authors of mentions), `associate` (author network), `geolocation` (geo-analysis), sentiment & source breakdown
- **Empty/negative result looks like:** few or no mentions in the monitored window — the subject may have little Russian-language public activity, not none at all.

## Gotchas & OpSec
- **Access-gated:** commercial subscription with a sales onboarding; no anonymous public search.
- It's a Russian vendor — weigh jurisdiction/data-handling for sensitive cases.
- Strength is Russian-language space; for global English coverage, pair with a Western listening tool.

## Overlaps ("do both")
- Pairs with direct `[[vk-search]]` (targeted VKontakte lookups) and Western monitoring like `[[brand24]]` — Kribrum for Russian-language breadth and analytics, the others for pinpoint profile lookups and non-Russian coverage.

## Trust & verifiability
`trust: community` — a reputable commercial monitoring firm with a strong Russian-language analytics reputation, but a closed platform. Treat surfaced authors as leads and confirm identities on the source network.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kribrum |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, associate, geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
