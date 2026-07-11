---
id: aliens-eye
name: Aliens_eye
description: Use when you have a `username` and want to enumerate matching accounts across hundreds of platforms with ML-assisted confidence scoring — returns social-profile links, display names and avatar images.
url: https://github.com/BLINKING-IDIOT/Aliens_eye
category: username
path:
- username
bestFor: Fast, async username enumeration across 800+ sites with Found/Maybe/Not-Found classification and multi-format export.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
- name
- image
status: live
pricing: free
costNote: Free and open source; install via pip. Costs are only your own compute and (optional) proxy/Tor usage.
opsec: active
opsecNote: The tool actively requests hundreds of platforms for the target username, so your IP hits every one of those sites in a burst. Route through Tor/proxies (built-in support) so the enumeration is not traced to you, and never run it from an IP tied to your real identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: An open-source project on GitHub (BLINKING-IDIOT/Aliens_eye); code is public and auditable, but it is a community tool — verify each "Found" hit manually, as automated classifiers produce false positives.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Aliens eye
- aliens_eye
tags:
- Nicknames
- username-enumeration
source: cyb-detective
lastVerified: '2026-07-11'
enrichment: full
---

# Aliens_eye

> A Sherlock-style username hunter with ML on top — it scans 800+ platforms asynchronously and grades each hit Found / Maybe / Not-Found using structural signals rather than a naive title-match.

## When to use
You have a `username`/handle and want to find every platform where it exists, quickly and with a confidence signal so you can triage. Use it early in a pivot from a single username to a full cross-platform footprint; the Found/Maybe grading saves you from manually checking hundreds of raw hits.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install aliens-eye` (optional extras add browser, image, PDF and MCP-server support; a Docker image is also available).
2. Scan a single handle: `aliens_eye username`. Target specific sites with `--site github,reddit`.
3. For deeper work: `aliens_eye username --correlate --domains` clusters profiles and checks for matching domain registrations; `--format all --output results` exports JSON/CSV/HTML/Markdown/PDF and graph formats (GEXF, Mermaid, Maltego).
4. Route through Tor/proxies for OpSec; use watch mode / resumable scans for large or ongoing jobs.
5. Read the output: Found (high confidence), Maybe (needs manual check), Not-Found. Manually verify every Found before asserting it — the account may be a namesake.
6. Pivot: confirmed profiles feed avatar reverse-image search (`[[pimeyes-com]]`), bio text feeds name/email extraction, and the Maltego/graph export feeds link analysis.

## Inputs → Outputs
- **In:** `username` (single or list; optional config and ML model files)
- **Out:** `social-profile` URLs, `username` confirmations, display `name`s, bios, and avatar `image`s — exportable as JSON/CSV/HTML/MD/PDF/graph
- **Empty/negative result looks like:** all sites return Not-Found — the handle is unused on covered platforms, or the target uses different handles per site. Enumeration finds handle reuse, not the person directly.

## Gotchas & OpSec
- **Namesake risk:** a matching username is not a matching person. Different people reuse handles; treat every hit as a candidate to verify, especially common handles.
- False positives/negatives: the ML classifier is heuristic. Site layout changes cause both missed real accounts and spurious Maybes — corroborate.
- OpSec: **active** and noisy — a burst of requests to 800+ sites from one IP is fingerprintable. Use the built-in Tor/proxy routing and a research environment.

## Overlaps ("do both")
- Pairs with mainstream enumerators like `[[sherlock]]` / `[[whatsmyname-web]]` — coverage and freshness differ per tool, so run more than one and union the Found sets.
- Pairs with `[[pimeyes-com]]` — Aliens_eye finds the profiles and their avatars; reverse face search ties the avatars to a single person.

## Trust & verifiability
`trust: community` — an auditable open-source tool. Its confidence scores are a triage aid, not a verdict; the burden of confirming any account belongs to your subject stays with you.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | aliens-eye |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, username, name, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
