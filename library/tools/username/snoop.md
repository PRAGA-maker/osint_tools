---
id: snoop
name: Snoop
description: Use when you have a `username` and want to enumerate where it exists across thousands of sites from your own machine — returns a report of accounts/profiles found on 5,400+ websites.
url: https://github.com/snooppr/snoop/blob/master/README.en.md
category: username
path:
- username
bestFor: Local, high-coverage username enumeration across thousands of sites via CLI.
selectorsIn:
- username
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free and open-source; no account or API key. You run it locally, so the only cost is setup.
opsec: passive
opsecNote: Passive toward the subject, but the checks originate from YOUR IP — Snoop connects directly to each site to test the handle. Run it behind a VPN/proxy if you don't want your address hitting hundreds of platforms.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A well-regarded open-source Sherlock-family username tool (5,400+ sites in the full DB); community-maintained, so results depend on the site-list staying current.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- snooppr/snoop
- Snoop Project
tags:
- username-check
- username-enumeration
- cli
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- shotstars
- snoop-2
---

# Snoop

> An open-source, locally-run CLI that hunts a single `username` across 5,400+ websites at once — a high-coverage account-enumeration tool in the Sherlock family, run entirely from your machine.

## When to use
You have a `username` and want the broadest possible sweep of where it's registered, without depending on a third-party web service's uptime or logging. Because it runs locally and covers thousands of sites, it's the tool to reach for when a hosted enumerator (`[[gaddr]]`, `[[360username-com]]`) comes up thin or you want a self-contained, reproducible check on your own infrastructure.

## How to use it (`bestInteractionPattern`: cli)
1. Install: grab the prebuilt Windows/Linux binary from the GitHub releases, or install from source (Python 3.7+); Android works via Termux, macOS is experimental.
2. Run it against the handle, e.g. `snoop <username>` (see the README for flags and the full vs. lite site DB).
3. Let it query each site directly; it flags where the handle resolves to an existing account.
4. Read the report — export as HTML/CSV/TXT — listing each hit's site and profile URL.
5. Open and confirm each `social-profile` (same handle ≠ same person), then pivot into image/bio mining and cross-check with a second enumerator.

## Inputs → Outputs
- **In:** `username`
- **Out:** report of `social-profile` links where the handle exists, plus name/bio hints from those profiles (HTML/CSV/TXT)
- **Empty/negative result looks like:** few or no hits, or many "error/timeout" rows — the latter means sites blocked or rate-limited your requests, not that the handle is absent. Re-run failures behind a proxy before concluding.

## Gotchas & OpSec
- Requires local install (human-in-the-loop setup); it's a CLI, not a click-and-go site.
- Site-detection logic goes stale as platforms change; expect false positives/negatives and verify every hit.
- All requests come from YOUR IP to hundreds of sites — noisy and attributable. Use a VPN/proxy for OpSec.
- Big runs are slow and can trip rate limits; scope the site list when you don't need all 5,400.

## Overlaps ("do both")
- Pairs with hosted enumerators `[[gaddr]]`, `[[360username-com]]`, `[[username-check]]` — run local + hosted, since each covers and misses different platforms.
- Feed confirmed profiles into face/reverse-image tooling and `[[wayback-machine-2]]` for deleted versions.

## Trust & verifiability
`trust: community` — a reputable open-source project, but coverage and accuracy hinge on a community-maintained site list that drifts over time. Treat every reported account as a lead to confirm by opening the profile; treat errors as "unknown," not "absent."

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | snoop |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
