---
id: user-name-search-intel-techniques
name: User Name Search - Intel Techniques
description: Use when you have a `username` and want to fan it out across dozens of social/community sites at once — returns candidate `social-profile` links and `name` leads to confirm manually.
url: https://inteltechniques.com/menu.html
category: username
path:
- username
bestFor: Bulk-checking one username against many platforms from a single search console.
selectorsIn:
- username
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: The online search tools are free to use in the browser. Bazzell also sells a downloadable/offline copy of the toolset and books, but the web console requires no payment.
opsec: passive
opsecNote: The tool builds direct query URLs and opens them in your browser — so the sites you open (each platform) see YOUR IP/session, not IntelTechniques. It never touches the target. Open results through a sock-puppet browser/VPN if you don't want each platform tying the lookup to you.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by Michael Bazzell (IntelTechniques), one of the most established names in OSINT. The console just constructs public search URLs; it stores nothing and vouches for no result — you verify each hit.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- whatsmyname-app
- namechk
- sherlock
aliases:
- IntelTechniques Username Tool
- Bazzell username search
tags:
- username
- search-console
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# User Name Search - Intel Techniques

> Michael Bazzell's browser-based username console: type a handle once and it launches direct searches against dozens of platforms and username-checkers, one click each.

## When to use
You have a `username`/handle and want the fastest manual sweep across social networks, forums, gaming, and dedicated username-availability checkers without typing the same string into 40 sites. Ideal early in an identity workup to find where a handle is registered and to gather candidate `social-profile` links you then confirm belong to the same person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the IntelTechniques search tools (from https://inteltechniques.com/menu.html go to the Tools → Usernames page, `tools/Username.html`).
2. Enter the target `username` in the field.
3. Use "Populate All" (or click individual services) to fire the handle at each platform/checker; results open in new tabs.
4. Manually review each tab — a live profile, a "username taken" signal, or a 404 — and keep the ones that plausibly match your subject.
5. Pivot: confirmed profiles feed cross-platform correlation; a display `name` on one profile feeds people-search; combine with `[[whatsmyname-app]]` and `[[sherlock]]` for automated coverage.

## Inputs → Outputs
- **In:** `username`
- **Out:** direct links to candidate `social-profile`s across many sites, plus `name` leads read off those profiles
- **Empty/negative result looks like:** every opened tab shows a 404 or "username available" — the handle isn't registered on those platforms (or is spelled differently). It is not proof the person has no online presence under another handle.

## Gotchas & OpSec
- Human-in-the-loop: **manual review** is the whole point — the tool opens searches, *you* decide which hits are the same person. Same username ≠ same human.
- OpSec: **passive** to the target, but each result page is loaded by your browser directly, so the destination sites see you. Use a compartmentalised/sock-puppet browser and VPN.
- Bazzell periodically restructures the tools pages and offers an offline version; if a page 404s, start from the current Tools menu.

## Overlaps ("do both")
- Pairs with `[[whatsmyname-app]]`, `[[namechk]]`, and `[[sherlock]]` — those automate the enumeration and de-dupe results, while the IntelTechniques console gives you hand control and a broader, curated site list. Run an automated checker for breadth, then this for the sites it misses.

## Trust & verifiability
`trust: trusted` — a long-standing, well-regarded OSINT resource. The console only assembles public search URLs; it makes no claim that a hit is your subject, so every result is a lead to verify, not a confirmation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | user-name-search-intel-techniques |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
