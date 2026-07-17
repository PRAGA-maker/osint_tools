---
id: webhound-anoncatalyst
name: WebHound (AnonCatalyst)
description: Use when you have a `name` or `username` and want to sweep multiple search engines at once, flagging social/forum/news hits — returns aggregated, categorized web results.
url: https://github.com/AnonCatalyst/WebHound
category: search-engines
path:
- search-engines
bestFor: One command that queries Google, Bing, DuckDuckGo and StartPage together and highlights social/forum/news results for a name or handle.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: Free, open-source Python CLI. No account or API key; it scrapes public search-engine results.
opsec: active
opsecNote: Runs live searches against Google/Bing/DuckDuckGo/StartPage from your IP and multithreads them, so you generate a burst of traffic that can trip CAPTCHAs or rate-limits. Use a sock-puppet IP/proxy and throttle for anything sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Independent open-source project (AnonCatalyst) with modest adoption; it aggregates public search results, so quality equals the engines it scrapes and it can break when they change markup.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
aliases:
- WebHound OSINT
- AnonCatalyst/WebHound
tags:
- search-aggregator
- osint-cli
- username-search
source: gh-topic-osint-resources
lastVerified: '2026-07-17'
enrichment: full
relatedTools:
- coeus-osint-toolbox
- ominis-osint
---

# WebHound (AnonCatalyst)

> A Python command-line search aggregator: fire one query across Google, Bing, DuckDuckGo and StartPage at once, then get results grouped and flagged by social platform, forum, and news source.

## When to use
You have a `name`, `username`, or distinctive phrase and want a fast, multi-engine first pass rather than searching each engine by hand. WebHound runs the query across several engines in parallel and categorises the hits (social profiles, forums, news, communities), surfacing where a handle or name appears so you can triage the promising leads quickly.

## How to use it (`bestInteractionPattern`: cli)
1. `git clone https://github.com/AnonCatalyst/WebHound && cd WebHound`
2. `python3 install.py` (or use the bundled `webhound-venv.py` to run inside a virtualenv).
3. `python3 webhound.py` and enter your query (name/username/phrase).
4. Read the colour-coded output: results grouped by engine and category, with social/forum/news hits highlighted; raw HTML and logs are saved for review.
5. Pivot: confirmed `social-profile`s feed username-enumeration tools; interesting `domain`s feed WHOIS/site analysis.

## Inputs → Outputs
- **In:** `name`, `username`, or keyword query.
- **Out:** aggregated, categorized search results — `social-profile` links, `domain`s, forum/news pages.
- **Empty/negative result looks like:** engines return nothing or only noise — a rare/ambiguous name, or an engine blocked the automated request. Cross-check by searching one engine manually.

## Gotchas & OpSec
- It scrapes search engines, so it breaks when they change layout or serve CAPTCHAs; expect occasional dry runs and check for updates.
- Multithreaded bursts look bot-like — throttle and proxy to avoid IP blocks, especially for sensitive targets.
- Categorization is heuristic; verify each flagged "social profile" actually belongs to your subject.

## Overlaps ("do both")
- Complements dedicated username-enumeration tools — WebHound casts a broad net across engines; feed its hits into deeper per-platform checks.

## Trust & verifiability
`trust: community` — a small independent open-source project that aggregates public engines. Treat it as a lead generator; every result must be verified at its source, since accuracy is only as good as the underlying engines.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | webhound-anoncatalyst |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
