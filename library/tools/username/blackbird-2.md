---
id: blackbird-2
name: Blackbird
description: Use when you have a `username` (or email/name) and want fast enumeration across hundreds of sites with profile metadata — returns `social-profile` links and `name`s. Run the GitHub tool locally; the old Heroku URL is dead.
url: https://blackbird-osint.herokuapp.com
category: username
path:
- username
bestFor: Fast username (and email/name) enumeration across hundreds of sites with a clean UI and extracted profile metadata — a maintained Sherlock/Maigret alternative.
selectorsIn:
- username
- email
- name
selectorsOut:
- social-profile
- name
status: degraded
pricing: free
costNote: Free and open-source (Python, p1ngul1n0/blackbird on GitHub). The listed Heroku demo host is dead (Heroku removed free dynos) — install and run it locally instead.
opsec: passive
opsecNote: Enumeration probes many sites for profile existence from YOUR IP; those sites (and any breach API) can log the requests. Run behind a VPN/puppet. The target account is not directly notified.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Active open-source project (p1ngul1n0/blackbird). Like all URL-enumeration tools it yields false positives; each hit needs manual confirmation. The Heroku-hosted version is defunct — use the repo.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- blackbird-osint
- p1ngul1n0 blackbird
tags:
- username
- enumeration
- python
source: metaosint
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- before-reddit-optimize-a-post
- cheat-sheet-maker
- mmhdan
- osm-finder
- query-server
- redditsearch
- the-favicon-finder
- trending-words-of-reddit
- username-availability-checker
- web-proxy
---

# Blackbird

> A fast, maintained username enumerator across hundreds of sites with a tidy UI and metadata extraction — install the GitHub tool; the old hosted demo is gone.

## When to use
You have a `username` (Blackbird also accepts `email` and `name`) and want a quick, broad map of where that identity exists, with extracted profile details (display name, bio) rather than just raw links. Reach for it early in username work, or as a cross-check against Sherlock/Maigret/`[[gosearch]]` — each tool's site list and detection differ, so running more than one improves coverage.

## How to use it (`bestInteractionPattern`: cli)
1. **Don't use the Heroku URL — it's dead.** Clone the repo: `git clone https://github.com/p1ngul1n0/blackbird` and `pip install -r requirements.txt`.
2. Run: `python blackbird.py --username <name>` (also `--email`, `--username-file` for batches; `--help` for options and the local web UI).
3. Read the output: found profile URLs (`social-profile`) with extracted `name`/metadata where available; export to CSV/PDF.
4. Verify each hit manually — enumeration over-reports unclaimed/placeholder handles.
5. Pivot: confirmed profiles → `[[socid-extractor]]` for hidden IDs; reused handle → real-name/email pivots; per-platform deep dive.

## Inputs → Outputs
- **In:** `username` (or `email`, `name`)
- **Out:** `social-profile` (profile URLs), `name` (extracted display names/bios)
- **Empty/negative result looks like:** few/no hits — the handle isn't widely reused, or sites changed their existence signals. Corroborate with another enumerator before concluding absence.

## Gotchas & OpSec
- **Hosted version defunct:** only the local GitHub tool works now — ignore the Heroku link.
- **False positives:** verify each result; enumeration lists are candidates, not confirmations.
- Site lists drift; keep the repo updated for newer platforms.
- OpSec: **passive** toward the target, noisy toward probed sites — run behind a VPN/puppet.

## Overlaps ("do both")
- Runs alongside `[[gosearch]]`, `[[whatsmyname-python]]`, Sherlock, and Maigret — different coverage, so run several.
- Feed confirmed profiles into `[[socid-extractor]]`.

## Trust & verifiability
`trust: community` — a popular, maintained open-source enumerator, but results need verification; the hosted demo is dead, so confirm you're running the current repo build, and check every hit on the live site.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | blackbird-2 |
| category | username |
| selectorsIn → selectorsOut | username, email, name → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
