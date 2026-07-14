---
id: maigret
name: Maigret
description: Use when you have a `username` and want a full cross-platform dossier — checks 3000+ sites and scrapes profile data, returning social-profile, name and linked-username leads.
url: https://github.com/soxoj/maigret
category: username
path:
- username
bestFor: Building a username dossier across 3000+ sites, with profile data extraction and pivoting.
selectorsIn:
- username
selectorsOut:
- social-profile
- name
- username
status: live
pricing: free
costNote: Free and open-source (MIT). A commercial tier offers a daily-updated site database and API, but the core CLI is fully free.
opsec: active
opsecNote: Maigret sends requests to thousands of sites from your machine — that traffic is attributable to your IP unless you route it through the built-in proxy/Tor/I2P support. Use those options and a sock-puppet posture; some sites rate-limit or log the probes.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Authored by soxoj, a leading OSINT-username researcher; 35k+ GitHub stars, actively maintained with an auto-updating site database.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- soxoj Maigret
tags:
- username-check
- username
- dossier
source: awesome-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Maigret

> The flagship username enumerator: give it one handle and it checks 3000+ sites, scrapes what each profile exposes, and assembles a pivotable dossier.

## When to use
You have a `username` and want the broadest possible cross-platform footprint plus extracted profile data (display `name`, bio, linked `username`s, avatars, IDs) — not just a taken/not-taken list. This is the default deep username tool: run it early to map where a subject exists online and to surface new handles and names to pivot on.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install maigret` (Python 3.10+), or run the Docker image; an optional web UI exists.
2. Run `maigret <username>`; add `--all-sites`/tags/country filters to widen or narrow, and `--recursive` to chase newly-found handles.
3. Route probes through the proxy/Tor/I2P options for OpSec.
4. Read the reports (HTML/PDF/JSON/CSV): discovered accounts plus extracted names, bios, and linked usernames.
5. Pivot: new `username`s feed a second Maigret pass; a display `name` feeds people-search; confirmed profiles feed `[[social-profiles-finder]]`.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` accounts across 3000+ sites, extracted `name`/bio, linked `username`s, avatars/IDs
- **Empty/negative result looks like:** few hits — meaning the handle is unused on covered sites or the person uses different handles per platform; run `[[username-generation-guide]]` variants and re-check. False positives happen on sites with loose existence checks, so confirm key hits.

## Gotchas & OpSec
- Active probing: without proxy/Tor, the requests trace to your IP; use the built-in anonymity options.
- Site database drifts; keep Maigret updated (it auto-refreshes) to avoid stale false positives/negatives.
- Verify high-value hits by opening the actual profile.

## Overlaps ("do both")
- Upstream/downstream of `[[username-generation-guide]]` (feed it variants) and `[[social-profiles-finder]]` (index-based discovery catches what enumeration misses, and vice versa).

## Trust & verifiability
`trust: trusted` — the leading open-source username tool from a respected author; every discovered account is verifiable by opening it, which you should do for anything you rely on.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | maigret |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, name, username |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
