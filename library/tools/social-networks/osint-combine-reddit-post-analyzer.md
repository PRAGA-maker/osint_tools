---
id: osint-combine-reddit-post-analyzer
name: OSINT Combine Reddit Post Analyzer
description: Use when you have a Reddit post/thread URL (a `social-profile`) and want its comment metadata — returns commenter usernames, timestamps, timezones and sentiment as a downloadable file.
url: https://www.osintcombine.com/free-osint-tools/reddit-post-analyser
category: social-networks
path:
- social-networks
bestFor: Extracting commenter usernames, posting times, inferred timezone and sentiment from a single Reddit thread.
selectorsIn:
- social-profile
- username
selectorsOut:
- username
- social-profile
status: degraded
pricing: free
costNote: Free browser-based tool from OSINT Combine; no account or payment. (The tool has been intermittently unavailable — check before relying on it.)
opsec: passive
opsecNote: You paste a public Reddit post URL into OSINT Combine's site; the analysis runs on already-public thread data and the redditors are not notified. Disclosing which thread you're analyzing to a third-party service is the only leak — use a research browser profile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Made by OSINT Combine, a well-known professional OSINT training/tooling vendor; it parses Reddit's own public data, so outputs are reproducible against the live thread.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Reddit Post Analyser
tags:
- reddit
- post-analysis
- pattern-of-life
source: osintambition-social
lastVerified: '2026-07-19'
enrichment: full
relatedTools:
- facebook-geo
- instagram-explorer
- osint-combine-blog
- osint-combine-tiktok-quick-search
- osint-combine-tools
- osintcombine-com
- osintcombine-com-2
- snapchat-multi-viewer-osint-combine
---

# OSINT Combine Reddit Post Analyzer

> Paste a Reddit thread URL and get a downloadable breakdown of who commented, when, from what apparent timezone, and with what sentiment — a fast pattern-of-life read on a discussion.

## When to use
You have a Reddit post or thread (often reached from a subject's `username` or a topic of interest) and want structured metadata instead of scrolling comments manually: the list of commenters, each comment's timestamp and inferred timezone (a pattern-of-life / geolocation hint), and a rough sentiment ranking. Useful to find who a subject interacts with, to spot the active hours of participants, and to pull a clean username list to pivot on. It works on public thread data — it's an aggregation aid, not a de-anonymizer.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.osintcombine.com/free-osint-tools/reddit-post-analyser (part of OSINT Combine's free-tools hub).
2. Paste the full URL of a public Reddit post/thread and run the analysis.
3. Download/read the output: commenter usernames, comment times, inferred timezones, sentiment.
4. Use the timezone spread and active hours as location/pattern hints; take usernames to a cross-platform check.
5. Pivot: each `username` feeds a Reddit user analyser (e.g. Reveddit) and cross-site handle enumeration.

## Inputs → Outputs
- **In:** `social-profile` (a Reddit thread URL) / `username`
- **Out:** commenter `username`s, timestamps, inferred timezones, sentiment — links to more `social-profile`s
- **Empty/negative result looks like:** the tool errors or returns nothing (it has had outages) — fall back to manual thread reading or an alternative Reddit analyser.

## Gotchas & OpSec
- Human-in-the-loop: none, but the service has been intermittently down; confirm it loads before depending on it.
- Timezone/sentiment are inferred — treat as hints, not facts.
- Deleted/removed comments may not appear; pair with Reveddit to recover removed content.

## Overlaps ("do both")
- Pairs with Reveddit and Reddit user analysers — this profiles one thread's participants, those profile an individual account's full history (including removed posts).

## Trust & verifiability
`trust: trusted` — a reputable OSINT vendor's tool over Reddit's public data; results are checkable against the live thread, though availability is currently unreliable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-combine-reddit-post-analyzer |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile, username → username, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
