---
id: birdwatcher
name: Birdwatcher
description: Use when you have Twitter/X `username`(s) and want to collect and mine their tweets locally — returns stored tweets, `associate` social graphs, `geolocation` (KML) maps and activity heatmaps.
url: https://github.com/michenriksen/birdwatcher
category: social-networks
path:
- social-networks
- twitter
- analytics
bestFor: A self-hosted, Metasploit-style console for collecting a set of Twitter users' tweets into PostgreSQL and generating word clouds, social graphs, geo maps, and time heatmaps.
selectorsIn:
- username
selectorsOut:
- associate
- geolocation
status: degraded
pricing: free
costNote: Free and open source (MIT). Cost is operational — you host PostgreSQL and supply Twitter API credentials, which under X's paid API are now expensive/restricted.
opsec: active
opsecNote: Collection runs through an authenticated Twitter/X API app tied to a developer account, so activity is attributable to that account. Targets aren't notified, but URL-crawling modules make live requests to links in tweets — those can hit attacker/target-controlled servers that log your IP; use a dedicated project account and consider egress isolation.
humanInLoop: true
humanInLoopReason:
- account-login
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Written by Michael Henriksen (author of Aquatone/Gitrob), a well-known security researcher; open-source and MIT-licensed, though the repo is dormant.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: true
invitationOnly: false
relatedTools:
- dmi-tcat
tags:
- twitter
- analytics
source: arf-seed
lastVerified: '2026-07-15'
enrichment: full
---

# Birdwatcher

> A console-driven Twitter data-mining framework — pull a target set's tweets into a local database, then generate word clouds, relationship graphs, geo maps and activity heatmaps to profile them.

## When to use
You have one or more Twitter/X `username`s and want to *analyse* their activity, not just read it: collect up to ~1,000 tweets per user into PostgreSQL and mine them for who they interact with (`associate` social graph), where they post from (geo-enabled tweets exported to KML for Google Earth = `geolocation`), what they talk about (weighted word clouds), and *when* they're active (Punchcard heatmaps → timezone/pattern-of-life). For a subject investigation this turns a timeline into structured intelligence — home timezone, frequented locations, and closest contacts. Reach for it when you can host a DB and have API access; for lighter needs use manual search.

## How to use it (`bestInteractionPattern`: cli)
1. Install Ruby (1.9.3+), PostgreSQL, Graphviz and ImageMagick per the GitHub README.
2. Configure Twitter API credentials in `~/.birdwatcherrc`.
3. Launch the interactive console (Metasploit-style), create a workspace, and add target `username`s.
4. Run collection, then the analysis modules: word cloud, social graph, KML geo-export, Punchcard heatmap, URL crawler.
5. Query the PostgreSQL store with raw SQL or export CSV for custom analysis.
6. Pivot: the social graph surfaces `associate`s to investigate; the KML map narrows physical locations; heatmaps and word clouds inform interview/search strategy.

## Inputs → Outputs
- **In:** Twitter/X `username`(s) (+ API credentials)
- **Out:** stored tweets, `associate` social graphs, `geolocation` KML maps, activity heatmaps, word clouds, extracted URLs/mentions/hashtags
- **Empty/negative result looks like:** collection returns few/no tweets — almost always an API-tier/credential problem under X's paid API, or a protected account, rather than genuine inactivity; verify the app's access level first.

## Gotchas & OpSec
- Human-in-the-loop: requires **account-login** and an **api-key**, plus a non-trivial local stack (Ruby/Postgres/Graphviz/ImageMagick).
- OpSec: **active** — collection is attributable to your API app, and the URL-crawler module makes live outbound requests to links in tweets (which can log your IP). Isolate the project account and egress.
- Status **degraded**: the repo is dormant and built for the pre-lockdown Twitter API — X's API overhaul likely breaks collection; best treated as a reference/architecture or for historical datasets.

## Overlaps ("do both")
- Pairs with `[[dmi-tcat]]` — both are self-hosted Twitter capture/analysis platforms; TCAT excels at continuous keyword/hashtag capture at scale, Birdwatcher at per-user profiling (geo/word-cloud/heatmap). Pick by whether you're tracking a *topic* or profiling *people*.

## Trust & verifiability
`trust: community` — open-source, MIT-licensed, authored by a respected security researcher, so the code is auditable and it stores raw tweets you can verify against. Fidelity depends on your API access; corroborate anything derived from a partial/rate-limited capture.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | birdwatcher |
| category | social-networks |
| selectorsIn → selectorsOut | username → associate, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login, api-key) |
