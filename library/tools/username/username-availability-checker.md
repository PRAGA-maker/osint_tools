---
id: username-availability-checker
name: Username Availability Checker
description: Use when you have a `username` and want a quick presence check across popular networks — returns which sites the handle exists on, but the hosted demo is likely offline.
url: https://username-check.herokuapp.com/
category: username
path:
- username
bestFor: A minimal, quick handle-presence check across a handful of popular networks — far smaller coverage than WhatsMyName/Maigret.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: degraded
pricing: free
costNote: Free and open-source (manu-chroma on GitHub). The hosted demo runs on a Heroku free dyno, which Heroku discontinued in Nov 2022, so the public URL is frequently or permanently offline; self-host from the repo if needed.
opsec: passive
opsecNote: Checks are made server-side against target sites, so the subject is not contacted directly. If you self-host, your server's IP makes the requests. Nothing sensitive is submitted beyond the handle.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Small community project with limited site coverage; "not found" is weak evidence given how few networks it checks — corroborate with a comprehensive enumerator.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- whatsmyname-python
- instant-username
tags:
- Nicknames
- username-availability
source: cyb-detective
lastVerified: '2026-07-10'
enrichment: full
---

# Username Availability Checker

> A minimal open-source handle-presence checker (manu-chroma) — historically useful for a quick look, but its hosted demo sits on a retired Heroku free dyno, so treat it as degraded and prefer a fuller enumerator.

## When to use
You have a `username` and want a fast, low-effort read on whether it exists on a small set of popular networks. It was designed as a quick check, explicitly acknowledging it is "very far behind Maigret/WhatsMyName" in coverage. Reach for it only for a throwaway first glance; for any real enumeration use a comprehensive tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Try the hosted URL https://username-check.herokuapp.com/ — but expect it to be down (Heroku killed free dynos in Nov 2022).
2. If it loads, enter the `username`; it reports which of its supported sites the handle appears on.
3. If it's offline, clone the GitHub project (`manu-chroma/username-availability-checker`) and run it locally, or skip straight to a maintained tool.
4. Pivot: take any "taken" handles and verify the actual profiles; then run `[[whatsmyname-python]]` for full coverage.

## Inputs → Outputs
- **In:** `username`
- **Out:** per-site presence → the `social-profile` sites where the handle exists
- **Empty/negative result looks like:** the page fails to load (dead dyno) or reports "not found" — the latter is unreliable given the tiny site list, so never treat it as proof of absence.

## Gotchas & OpSec
- The hosted demo is likely **offline**; don't rely on the live URL.
- Coverage is far smaller than modern enumerators, so false "not found" is common.
- OpSec: passive; nothing sensitive leaves your side beyond the handle.

## Overlaps ("do both")
- Superseded by `[[whatsmyname-python]]` and `[[instant-username]]` — those check hundreds of sites and are maintained. Use this only as a quick glance, then confirm with them.

## Trust & verifiability
`trust: unverified` — small, lightly-maintained project on dead hosting; treat results as hints and confirm every hit on the real platform with a comprehensive enumerator.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | username-availability-checker |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, username |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
