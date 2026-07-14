---
id: social-analyzer-chrome-extension
name: Social Analyzer (Chrome extension)
description: Use when you have a `username` (or name) and want to find and rank matching profiles across many social platforms from the browser — returns candidate social-profile links with confidence ratings.
url: https://chromewebstore.google.com/detail/socialanalyzer-social-sen/efeikkcpimdfpdlmlbjdecnmkknjcfcp
category: username
path:
- username
bestFor: Browser-based hunting of a username/name across many sites with confidence-scored results.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free browser extension. The related open-source Social-Analyzer engine (qeeqbox) is also free.
opsec: passive
opsecNote: The extension checks public profile URLs for the target handle — probes originate from your browser/IP, so run it in a sock-puppet browser/VPN. No target account is contacted or notified. Avoid using a browser logged into your real social accounts.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: browser-extension
trust: community
trustNote: Companion to the well-known open-source Social-Analyzer project (qeeqbox), which searches 1000+ sites with layered detection and confidence scoring. Verify the extension listing's publisher before installing; treat scores as leads, not proof.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- sherlock
- maigret
aliases:
- Social Analyzer
- social-analyzer
tags:
- username-search
- social-analysis
- chrome-extension
source: osintambition-social
lastVerified: '2026-07-14'
enrichment: full
---

# Social Analyzer (Chrome extension)

> A browser-based front-end to the Social-Analyzer approach: search a username/name across many platforms and get confidence-rated profile matches without leaving the browser.

## When to use
You have a `username` (or a `name` to try as handle variants) and want a quick, in-browser sweep for matching profiles with a confidence score attached — useful as a fast triage before committing to a full CLI enumeration. The underlying Social-Analyzer project checks 1000+ sites with layered detection (normal/advanced/OCR) and rates matches 0–100 to cut false positives.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the extension into a sock-puppet Chrome profile (verify the publisher on the Web Store listing first).
2. Enter the target username (or name variants) and run the search.
3. Read the ranked results — profile links with confidence ratings, titles/descriptions.
4. Apply **manual-review**: open high-confidence hits and confirm they're the same person; handle reuse alone isn't identity. Pivot: run the same handle through `[[sherlock]]` / `[[maigret]]` (or the full Social-Analyzer CLI) for exhaustive coverage.

## Inputs → Outputs
- **In:** `username` / `name`
- **Out:** `social-profile` candidate links with confidence scores
- **Empty/negative result looks like:** no scored matches, or only low-confidence hits — the handle may be unused, spelled differently, or on sites the extension doesn't cover; corroborate with a CLI enumerator.

## Gotchas & OpSec
- Human-in-the-loop: **manual-review** — confidence scores are heuristics, not verdicts.
- OpSec: **passive** — probes public URLs from your browser; sandbox/sock-puppet it and keep it out of a browser logged into your real accounts.
- Extension-store listings can change hands; confirm the publisher before installing, and prefer the audited open-source CLI for sensitive work.

## Overlaps ("do both")
- Pairs with `[[sherlock]]` and `[[maigret]]` — the extension is fast in-browser triage; those give deeper, scriptable coverage. Run both and reconcile.

## Trust & verifiability
`trust: community` — tied to a respected open-source project, but a browser extension you must vet before trusting. Treat confidence scores as ranked leads and verify each match manually.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | social-analyzer-chrome-extension |
| category | username |
| selectorsIn → selectorsOut | username, name → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | yes (manual-review) |
