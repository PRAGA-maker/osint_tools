---
id: dmi-tcat
name: DMI-TCAT
description: Use when you have a Twitter/X `username`, keyword or hashtag and want to capture and analyse a large tweet dataset over time — returns a stored, queryable corpus of tweets, `social-profile` and `associate` interaction graphs.
url: https://github.com/digitalmethodsinitiative/dmi-tcat
category: social-networks
path:
- social-networks
- twitter
- analytics
bestFor: Self-hosted longitudinal capture and analysis of tweets by handle, keyword, or hashtag into a queryable database.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
status: degraded
pricing: free
costNote: Free and open source. The cost is operational — you must run a PHP/MySQL server and, critically, supply Twitter/X API credentials, which are now expensive/restricted under X's paid API tiers.
opsec: active
opsecNote: Collection runs through an authenticated Twitter/X API app tied to a developer account, so your capture is attributable to that account. It does not notify the targets you track, but X sees the app's activity — use a dedicated project account, never your personal one.
humanInLoop: true
humanInLoopReason:
- account-login
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Maintained (until archival in Jan 2025) by the University of Amsterdam's Digital Methods Initiative — a reputable academic group; the code is open and widely used in research, though the repo is now read-only.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: true
invitationOnly: false
relatedTools:
- twitter-x-advanced-search
aliases:
- DMI-TCAT
- Twitter Capture and Analysis Toolset
tags:
- twitter
- analytics
- academic
source: arf-seed
lastVerified: '2026-07-15'
enrichment: full
---

# DMI-TCAT

> The academic standard for longitudinal Twitter capture — stand up a server, point it at handles/keywords, and build a queryable tweet corpus for analysis; now archived and hostage to X's paid API.

## When to use
You need more than a live look at a `username` — you need to *capture over time* and analyse: every tweet from a handle, everyone using a hashtag, or all mentions of a keyword, stored so you can query, export, and map interactions later. For a missing-person or subject investigation this builds a durable record of a person's posting patterns, who they reply to and retweet (`associate` graph), timing/pattern-of-life, and links they share — evidence that would otherwise vanish as the live timeline moves. Reach for it only when you can host a server and afford API access; for a quick current-state look, use manual advanced search instead.

## How to use it (`bestInteractionPattern`: cli)
1. Provision a Linux host (Ubuntu/Debian) or use the Docker image; install per the GitHub README (PHP/MySQL stack).
2. Obtain Twitter/X API credentials from a developer account and configure them in TCAT.
3. Create capture "bins": define them by tracking keywords/hashtags, by following specific `username`s, or by a geo/one-percent stream (subject to what the current API tier allows).
4. Let it collect over hours/days/weeks; the tweets accumulate in MySQL.
5. Use the web interface / query modules to analyse: activity timelines, mention/retweet networks, hashtag co-occurrence, top URLs, and CSV/GEXF exports.
6. Pivot: the interaction network surfaces `associate` handles to investigate; exported URLs/media feed link-analysis and reverse-image; posting times feed timezone/pattern-of-life inference.

## Inputs → Outputs
- **In:** `username`(s), keywords, hashtags to capture (+ API credentials)
- **Out:** a stored tweet corpus, `social-profile` activity data, `associate` interaction graphs, exportable datasets
- **Empty/negative result looks like:** empty bins despite active targets — almost always an API-tier/credential problem (X's current paid API restricts streaming) rather than the subject being inactive; verify the app's access level first.

## Gotchas & OpSec
- Human-in-the-loop: requires **account-login** and an **api-key**; setup and hosting are non-trivial and X's API changes may break capture entirely.
- OpSec: **active** collection under your API app — attributable to that developer account. Targets aren't notified, but isolate the project account; don't tie it to your identity.
- Status **degraded**: the repo was archived in January 2025 and X's API overhaul has broken or throttled much streaming capture — expect to fight the API, and treat it as best for historical/archived datasets or well-funded projects.

## Overlaps ("do both")
- Pairs with `[[twitter-x-advanced-search]]` — advanced search gives you the fast, credential-free current-state look; TCAT is what you use when you need continuous capture, network analysis, and an exportable archive of the same subject.

## Trust & verifiability
`trust: community` — built and maintained by a respected academic group (Digital Methods Initiative) with open, auditable code. Data fidelity depends on your API access; because it stores raw tweets, findings are self-verifiable against the captured records, but corroborate anything derived from a partial/rate-limited capture.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dmi-tcat |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login, api-key) |
