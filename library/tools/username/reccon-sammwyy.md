---
id: reccon-sammwyy
name: Reccon (sammwyy)
description: Use when you have a `username` and want to check it across many sites at once through a browser UI — returns candidate `social-profile` hits.
url: https://github.com/sammwyy/Reccon
category: username
path:
- username
bestFor: A self-hosted, browser-based Sherlock-style username sweep with live results.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, open-source (MIT). Runs locally; no account or API key.
opsec: passive
opsecNote: The tool queries target platforms directly from wherever you run it, so those sites see your server's IP hitting profile URLs. Run it from a VPN/VPS you don't mind burning if you're checking a sensitive handle; it stores no data itself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Small single-author project (~13 stars, few commits) built on the Sherlock dataset; useful but thin and lightly maintained — verify hits manually.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- sherlock
- maigret
- whatsmyname
aliases:
- Reccon
- sammwyy/Reccon
tags:
- username
- web-app
- sherlock
source: gh-topic-osint-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Reccon (sammwyy)

> A local web app that runs a Sherlock-style username enumeration behind a browser UI with real-time results — Sherlock's coverage, a nicer interface.

## When to use
You have a `username`/handle and want a quick visual sweep of which platforms have an account under it, without living in a terminal. Reccon is worth reaching for when you want live, incremental results in a browser (good for demoing or for handing to a less technical teammate). Because it is built on the Sherlock dataset, treat it as a convenience front-end rather than a distinct data source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Clone the repo: `git clone https://github.com/sammwyy/Reccon`.
2. Install deps with [Bun](https://bun.sh): `bun install`.
3. Start it: `bun run dev`, then open `http://localhost:5173` in your browser.
4. Enter the target `username` and watch results populate in real time — each hit is a platform where that handle appears to exist.
5. Click through to confirm each candidate profile by eye (avatar, bio, activity) before trusting it.
6. Pivot: feed confirmed handles/emails into the account-existence and profile-enrichment tools; cross-run with a second engine to catch misses.

## Inputs → Outputs
- **In:** `username`
- **Out:** list of candidate `social-profile` URLs across platforms
- **Empty/negative result looks like:** few or no hits — for a common handle this often means false negatives (sites rate-limiting or template drift), so re-run with `[[sherlock]]` or `[[maigret]]` before concluding the name is unused.

## Gotchas & OpSec
- Thin, lightly-maintained wrapper: its site list can lag upstream Sherlock and produce false positives/negatives. Always eyeball each hit.
- Queries hit target sites from your host IP — use a disposable VPN/VPS for sensitive handles.
- No CAPTCHA/login, but no dedupe of common-word usernames either; expect noise on generic handles.

## Overlaps ("do both")
- Overlaps heavily with `[[sherlock]]` (same underlying dataset) — use Reccon for the UI, but confirm coverage with Sherlock's CLI.
- Pairs with `[[maigret]]` and `[[whatsmyname]]`, which check different/larger site lists and catch profiles Reccon misses.

## Trust & verifiability
`trust: community` — a small hobby project by a single author with limited stars/commits. It is genuine open source, but treat its output as leads to verify, not confirmed accounts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reccon-sammwyy |
| category | username |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
