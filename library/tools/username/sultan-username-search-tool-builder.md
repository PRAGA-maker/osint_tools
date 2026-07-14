---
id: sultan-username-search-tool-builder
name: SULTAN (Username Search Tool builder)
description: Use when you have a username and want to check it across many platforms at once — returns per-site profile URLs and hit/miss status for the subject's social footprint.
url: https://github.com/sinwindie/OSINT/tree/master/SULTAN
category: username
path:
- username
bestFor: Bulk-checking one username across many platforms to map a person's social footprint, using an editable spreadsheet of sites.
selectorsIn:
- username
selectorsOut:
- username
- social-profile
status: live
pricing: free
costNote: Free and open on GitHub (Sinwindie's OSINT repo); no account. Requires local Python.
opsec: passive
opsecNote: SULTAN queries each target platform directly from your machine to test whether the username exists, so those platforms see requests from your IP — run it behind a VPN/proxy. It does not log into or notify the target's accounts, but high-volume checks can trip rate-limits or bot-detection; the bundled RequestsValidator helps flag false positives.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: community
trustNote: Authored by Sinwindie, a well-known OSINT educator; the repo is popular (thousands of stars) and open-source, so the code is inspectable, though it is a community project, not a maintained product.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- SULTAN
- Sinwindie SULTAN
- username search tool builder
tags:
- username-enumeration
- self-hosted
- python
- sinwindie
source: sinwindie-osint
lastVerified: '2026-07-14'
enrichment: full
---

# SULTAN (Username Search Tool builder)

> Sinwindie's Python username-enumeration framework, driven by an editable spreadsheet of site templates — check one handle across dozens of platforms and tune the site list yourself.

## When to use
You have a `username` and want to find every platform where the subject reused it — the classic first move to map a missing person's or investigation target's social footprint. SULTAN is in the Sherlock/WhatsMyName family, but its distinguishing feature is that the site list lives in an editable `SULTAN_DATA.xlsx`, so you can add niche/regional platforms and adjust match logic without touching code — useful when the mainstream enumerators lack a site you care about.

## How to use it (`bestInteractionPattern`: python-lib)
1. Clone the repo: `git clone https://github.com/sinwindie/OSINT` and enter `OSINT/SULTAN`.
2. Read `Build An OSINT Username Search Tool Using SULTAN.pdf` — it walks through setup and how the spreadsheet drives the checks.
3. Ensure Python and the deps are installed; keep `SULTAN_DATA.xlsx` (the site templates) beside `SULTAN.py`.
4. Run `python SULTAN.py` and supply the target `username`; it iterates the spreadsheet's sites and reports where the handle exists.
5. Use `RequestsValidator.py` to sanity-check results and cut false positives, then open the confirmed profile URLs.
6. Pivot: each confirmed `social-profile` feeds platform-specific tools (photos, posts, associates); consistent bios/avatars across sites strengthen attribution.

## Inputs → Outputs
- **In:** a single `username`
- **Out:** per-site hit/miss plus `social-profile` URLs where the `username` resolves
- **Empty/negative result looks like:** all-miss, or noisy false-positives on sites that return a soft-200 for any handle. Validate hits (RequestsValidator, or open them) — enumerators are notorious for both false negatives (site changed its markup) and false positives.

## Gotchas & OpSec
- Checks hit each platform from your IP — run behind a VPN/proxy, and throttle to avoid rate-limits and bot-detection that cause false negatives.
- The site list can go stale as platforms change their "user not found" responses; keep `SULTAN_DATA.xlsx` updated and cross-check against another enumerator.
- Username reuse is strong but not proof of identity — two accounts sharing a handle can be different people; corroborate with avatar/bio/content.

## Overlaps ("do both")
- Pairs with `[[amazon-usernames]]` and other `site:`-specific dorks — SULTAN finds the platforms, targeted dorks pull the detail each platform buries.
- Run alongside Sherlock/WhatsMyName-style tools — different site lists catch different platforms; union the results.

## Trust & verifiability
`trust: community` — open-source code from a respected OSINT educator, inspectable and widely used, but self-hosted and unmaintained-as-product: always verify individual hits against the live profile rather than trusting the enumerator's status alone.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sultan-username-search-tool-builder |
| category | username |
| selectorsIn → selectorsOut | username → username, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | no |
