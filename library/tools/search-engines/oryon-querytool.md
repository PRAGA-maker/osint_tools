---
id: oryon-querytool
name: Oryon Querytool
description: Use when you have a `name`, `email`, `username`, `phone` or `domain` and want systematic dork-driven searches across dozens of engines/sites — returns candidate `social-profile`, `email` and file/`document-id` hits.
url: https://github.com/oryon-osint/querytool
category: search-engines
path:
- search-engines
bestFor: A Google-Sheets dork generator that fires one selector at many search engines and site-specific queries at once.
selectorsIn:
- name
- email
- username
- phone
- domain
selectorsOut:
- social-profile
- email
- document-id
status: live
pricing: free
costNote: Free, open-source. Requires a (free) Google account to copy the shared Google Sheet into your own Drive.
opsec: passive
opsecNote: The sheet only builds search URLs — it runs no queries itself, so nothing about your target is sent until you click a link. When you do, searches run from your browser/IP against Google et al.; use a research browser/VPN and expect CAPTCHAs on rapid dorking. Copy the sheet with a burner Google account, not your primary one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Community OSINT dorking framework (~300+ stars) built as a Google Sheet; it only assembles standard search-operator URLs, so it's transparent and low-risk to inspect.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- cyber-intelligence-toolkit-oryon
aliases:
- querytool
- oryon
tags:
- google-dorking
- spreadsheet
- search-operators
source: gh-topic-osint-framework
lastVerified: '2026-07-17'
enrichment: full
---

# Oryon Querytool

> A Google Sheet that turns one selector into a wall of ready-to-click dork links across search engines, social sites and file repositories — systematic manual searching without memorising operators.

## When to use
You have a single strong selector — a `name`, `email`, `username`, `phone`, or `domain` — and want to run it exhaustively across many search surfaces (Google/Bing/Yandex/DuckDuckGo, social platforms, paste/file sites, document repositories) without hand-crafting each `site:`/`inurl:`/filetype dork. Querytool pre-builds those queries; you type the term once and get a grid of clickable searches, which is ideal for the broad "cast a wide net" phase of a person or domain investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the repo (https://github.com/oryon-osint/querytool) and follow its link to the shared Google Sheet.
2. Sign in with a (burner) Google account and **File → Make a copy** into your own Drive so you can edit it.
3. Enter your selector in the designated input cell (name / email / username / phone / domain, per the tab).
4. The sheet populates rows of hyperlinks — each is a pre-formed dork against a specific engine or site. Click through them, opening promising ones.
5. Triage results by eye; save hits (profiles, documents, mentions) to your case notes.
6. Pivot: `social-profile`/`email`/document hits feed username, email-verification and metadata tools.

## Inputs → Outputs
- **In:** one of `name`, `email`, `username`, `phone`, `domain`
- **Out:** links that surface candidate `social-profile`s, `email` mentions, and files/`document-id`s across the web
- **Empty/negative result looks like:** the dorks return no meaningful hits — normal for a scrubbed/low-footprint subject. It reflects the search engines' index, not a failure of the tool; vary the selector and try region-specific engines.

## Gotchas & OpSec
- It's a *link generator*, not a scraper — you still click and read each result manually; expect volume.
- Requires copying a Google Sheet (Google login) — use a burner account, not your identity.
- Rapid dorking triggers CAPTCHAs and temporary blocks; pace yourself or rotate.
- Coverage tracks whatever the underlying engines index; a negative isn't proof of absence.

## Overlaps ("do both")
- Pairs with the broader `[[cyber-intelligence-toolkit-oryon]]` suite. Complements automated username tools — Querytool covers search-engine and file-repository angles they don't, while they check platform APIs it can't.

## Trust & verifiability
`trust: community` — an established community dorking framework. Because it only assembles standard search-operator URLs (no data collection, no backend), you can inspect exactly what every link does before clicking, making it low-risk despite the required Google login.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | oryon-querytool |
| category | search-engines |
| selectorsIn → selectorsOut | name, email, username, phone, domain → social-profile, email, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
