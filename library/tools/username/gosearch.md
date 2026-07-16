---
id: gosearch
name: GoSearch
description: Use when you have a `username` and want fast enumeration across 300+ sites plus breach/infostealer hits — returns `social-profile` links and exposure signals.
url: https://github.com/ibnaleem/gosearch
category: username
path:
- username
bestFor: Fast CLI username enumeration across 300+ sites with integrated HudsonRock infostealer and breach-directory checks — a quicker Sherlock with exposure data.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free and open-source (Go). Install via `go install` or a release binary; no account. Breach/HudsonRock lookups use public/free endpoints.
opsec: passive
opsecNote: Enumeration probes target sites for profile existence from YOUR IP — high-volume automated requests can be logged by those sites and by any breach API used. Run from a VPN/puppet network; the target is not directly notified.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Active open-source project (ibnaleem/gosearch, thousands of stars). Like all URL-enumeration tools it produces false positives; each hit needs manual confirmation.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- gosearch
tags:
- username
- go
- fast
- breach-check
source: gh-topic-osint-framework
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- instatracker
---

# GoSearch

> A fast Go-based username enumerator across 300+ sites that also folds in breach and infostealer-exposure data — Sherlock-speed with an exposure bonus.

## When to use
You have a `username` and want a quick, broad map of where it exists online plus whether it shows up in breach/infostealer datasets. Reach for GoSearch early in username work when speed matters, or as a cross-check against Sherlock/Maigret (each tool's site list and accuracy differ). The HudsonRock/infostealer integration is the differentiator: it can surface that a handle appears in stealer logs, hinting at a compromised machine tied to the identity.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `go install github.com/ibnaleem/gosearch@latest`, or grab a release binary.
2. Run: `gosearch -u <username>` (see `--help` for flags).
3. Read the output: found profile URLs across sites (`social-profile`), plus any breach-directory / HudsonRock infostealer hits for the username.
4. Verify each profile hit manually — enumeration over-reports (unclaimed/placeholder handles).
5. Pivot: confirmed profiles → per-platform deep dive; breach/infostealer hits → linked emails/passwords context (handle ethically); consistent handle → real-name and email pivots.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` (profile URLs), `username` (confirmed handle presence), breach/infostealer exposure flags
- **Empty/negative result looks like:** few/no hits — the handle isn't widely reused, or sites blocked the probes. Enumeration false-negatives happen when a site changes its "profile exists" signal; corroborate with Maigret/Sherlock.

## Gotchas & OpSec
- **False positives/negatives:** URL enumeration is inherently noisy — confirm each result; don't trust the raw list.
- Site lists drift; a stale build misses newer platforms — keep it updated.
- OpSec: **passive** toward the target but noisy toward the *sites* you probe — run behind a VPN/puppet network.

## Overlaps ("do both")
- Runs alongside `[[whatsmyname-python]]`, Sherlock, and Maigret — different site coverage and detection logic, so run more than one.
- Feed a confirmed profile URL into `[[socid-extractor]]` to pull hidden IDs and pivot further.

## Trust & verifiability
`trust: community` — a popular, maintained open-source enumerator, but results are candidate links needing verification. Confirm every hit on the actual site before attribution.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gosearch |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
