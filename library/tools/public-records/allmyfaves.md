---
id: allmyfaves
name: AllMyFaves
description: Use when you need to discover categorized links to popular sites (social, search, video, shopping) as a visual start-page directory — returns pointers to other sites/tools.
url: https://www.allmyfaves.com/
category: public-records
path:
- public-records
bestFor: A visual categorized directory of popular websites, useful for discovering platforms to check.
selectorsIn: []
selectorsOut:
- domain
status: live
pricing: free
costNote: Free visual bookmark/start-page directory; no account needed to browse.
opsec: passive
opsecNote: Browsing a link directory is passive and reveals nothing about any subject. The sites it points to each carry their own OpSec cost when you actually use them.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A consumer visual bookmark/start-page site, not an OSINT tool; it only curates links to popular websites and does no lookups itself.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- All My Faves
tags:
- toddington
- curated-directory
- reference-sites
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# AllMyFaves

> A visual "start page" directory of popular websites by category — a discovery aid for remembering which platforms exist to check, not a tool that looks anyone up.

## When to use
You want a quick visual reminder of the major sites in a category — social networks, search engines, video platforms, shopping, news — for example when scoping which platforms to run a subject's `username` against. AllMyFaves is a consumer bookmark/start-page directory: it curates logo-linked lists of popular sites. It performs no searches or lookups itself, so its OSINT value is purely as a low-effort discovery/checklist reference. Very low relevance; use it (or any "awesome-OSINT" list) only to jog which platforms to cover.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.allmyfaves.com/.
2. Browse the category tiles (social, search, video, shopping, etc.).
3. Note the platforms relevant to your investigation that you might otherwise forget.
4. Read the output: a set of `domain`s/platforms to go check with your actual selector.
5. Pivot: go run the subject's selector on each relevant platform using the appropriate dedicated tool — that's where the real work happens.

## Inputs → Outputs
- **In:** none (a browsable directory, not a query interface)
- **Out:** `domain` pointers — a checklist of popular platforms to investigate elsewhere
- **Empty/negative result looks like:** the category lacks the niche/regional platform you need — expected; it curates mainstream consumer sites, so use a specialist OSINT directory for depth.

## Gotchas & OpSec
- Human-in-the-loop: none to browse.
- OpSec: passive; the OpSec that matters belongs to the downstream platforms you visit.
- It is not an OSINT tool — do not expect it to return data on a person; it only lists websites.

## Overlaps ("do both")
- Redundant with dedicated OSINT directories (`[[osint-cheat-sheet]]`, OSINT Framework) — those are purpose-built for investigators and far more complete; AllMyFaves is only a generic consumer start page.

## Trust & verifiability
`trust: unverified` — a consumer link directory with no investigative vetting; use it purely for discovery, and rely on the target platforms and proper tools for any actual data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | allmyfaves |
| category | public-records |
| selectorsIn → selectorsOut |  → domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
