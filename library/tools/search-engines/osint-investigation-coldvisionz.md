---
id: osint-investigation-coldvisionz
name: osint-investigation (coldvisionz)
description: Use when you want a hand-curated shortlist of go-to OSINT tools organized by task — returns pointers to email, breach, social, and geolocation resources (no selectors of its own).
url: https://github.com/coldvisionz/osint-investigation
category: search-engines
path:
- search-engines
bestFor: A practitioner's short "tools I actually use" reference, grouped by investigation task.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Public GitHub repository; no account or payment required to read.
opsec: passive
opsecNote: Reading a public GitHub README is passive and leaves no trace on any target. The tools it links to have their own OpSec profiles — treat each linked service on its own terms before you run it against a subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Small personal repo (~40 stars) maintained by one investigator; a starting-point index, not an authoritative or exhaustive catalog.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- coldvisionz osint-investigation
- coldvisionz osint list
tags:
- directory
- reference
source: gh-topic-osint-framework
lastVerified: '2026-08-05'
enrichment: full
---

# osint-investigation (coldvisionz)

> A one-investigator "these are the tools I reach for" GitHub list, grouped by task — a quick orientation index, not a comprehensive framework.

## When to use
You are scoping an investigation and want a short, opinionated menu of proven tools rather than a 1,000-entry mega-list. It is useful early, when you hold a selector (an `email`, a `username`, a name) and want to be reminded which category of tool to pivot into next — email lookups (GHunt, Holehe), breach databases (IntelX, Dehashed, HaveIBeenPwned), Telegram bots, Google dorks, and geolocation helpers.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/coldvisionz/osint-investigation and read the README top to bottom once — it is short.
2. Match your current selector to a section (e.g. you hold an `email` → jump to the email/breach links).
3. Open the linked third-party tool in a separate sock-puppet tab and run it there; this repo only points, it does not process anything.
4. Pivot: use it as a checklist so you do not skip an obvious category (breach data, Telegram bots, archive.org).

## Inputs → Outputs
- **In:** none — you bring the selector; the list points you to the right tool
- **Out:** none directly — it yields links/tool names, not data about a subject
- **Empty/negative result looks like:** the section you need is not covered (it is deliberately small) — fall back to a larger curated catalog.

## Gotchas & OpSec
- Human-in-the-loop: none to read the list; each linked tool has its own login/CAPTCHA requirements.
- OpSec: reading the repo is passive. Do not assume the linked tools are passive — breach lookups and account-existence checks can be active or alerting.
- It is a personal list and can go stale; verify a linked tool still works before relying on it.

## Overlaps ("do both")
- Pairs with any large curated index (awesome-osint-style catalogs) — this one is the short "trusted favorites" cut, the big lists are the exhaustive fallback when a category is missing here.

## Trust & verifiability
`trust: community` — a single maintainer's public repo with modest stars; treat it as a helpful pointer, not a vetted or maintained-to-standard catalog.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-investigation-coldvisionz |
| category | search-engines |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
