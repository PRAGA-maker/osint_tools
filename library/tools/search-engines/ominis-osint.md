---
id: ominis-osint
name: Ominis-OSINT
description: Use when you have a `name`, `username` or `email` and want automated Google reconnaissance across many sites — returns social-profile matches and web mentions.
url: https://github.com/AnonCatalyst/Ominis-OSINT
category: search-engines
path:
- search-engines
bestFor: Scripted search-engine reconnaissance — running a name/handle/email through Google and multi-site username checks to collect mentions and profile matches.
selectorsIn:
- name
- username
- email
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free and open-source (pip-installable); no account or API key required.
opsec: active
opsecNote: The tool scrapes Google and probes many site URLs directly, so requests hit search engines and target platforms (not the subject's own accounts). It ships proxy support and user-agent randomization for a reason — run behind a VPN/proxy to avoid IP blocks.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: cli
trust: community
trustNote: Active, reasonably popular open-source project (~500+ stars); results depend on Google scraping, which is brittle and captcha-prone — verify hits manually.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- coeus-osint-toolbox
- webhound-anoncatalyst
aliases:
- Ominis
- AnonCatalyst Ominis-OSINT
tags:
- search-engine
- python
- footprint
source: gh-topic-osint-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Ominis-OSINT

> A Python recon tool that automates Google queries and multi-site username checks to gather web mentions and profile matches for a name, handle or email.

## When to use
You have a `name`, `username` or `email` and want a fast automated first sweep: what does Google surface, and does the handle exist across common sites? Ominis batches the search-engine work — extracting titles/URLs/mentions and running username checks — so it's a good opening recon pass to seed leads you then verify by hand.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install Ominis-OSINT` (or clone and `pip install -r requirements.txt`).
2. Run: `python3 ominis.py` and supply your query (name/username/email); configure country/language/date filters and the site list in `src/urls.txt` as needed.
3. Let it query Google and probe the site list; it reports titles, URLs, HTTP statuses and potential social-profile matches.
4. If Google throws a captcha or rate-limits, slow the run, enable proxies/user-agent rotation, and retry.
5. Pivot: open each candidate `social-profile`/mention to confirm identity, then feed confirmed handles/emails into deeper tools.

## Inputs → Outputs
- **In:** `name`, `username`, or `email`
- **Out:** `social-profile` matches, web mentions (titles/URLs), and username-check results
- **Empty/negative result looks like:** few or no hits — often a captcha/rate-limit blocking the scrape rather than a truly clean subject; re-run with proxies before concluding.

## Gotchas & OpSec
- **Active + brittle:** it scrapes Google, so captchas and IP blocks are common (`captcha`). Use proxies/VPN and expect maintenance breakage when Google changes.
- Results are unranked leads, not verified identities — confirm each on the live page.
- Username matches can collide across different people; corroborate before attributing.

## Overlaps ("do both")
- Pairs with dedicated username tools (Sherlock/Maigret) and email OSINT — Ominis casts a wide search-engine net; those go deep on a single selector.

## Trust & verifiability
`trust: community` — an active open-source project, but its output quality hinges on fragile Google scraping; treat every hit as a lead to verify manually.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ominis-osint |
| category | search-engines |
| selectorsIn → selectorsOut | name, username, email → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (captcha) |
