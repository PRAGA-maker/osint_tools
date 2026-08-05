---
id: mkpath
name: MKPATH
description: Use when you have a target domain and a wordlist and want to generate multi-level directory/file path permutations to feed a content brute-forcer — returns candidate paths, not data itself.
url: https://github.com/trickest/mkpath
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Generating multi-level path permutations from a wordlist for directory/file brute-forcing.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free, open-source Go tool from Trickest; no account required.
opsec: active
opsecNote: MKPATH itself only generates a path list locally (passive). But its whole purpose is to feed a brute-forcer (GoBuster/ffuf/Dirbuster) that then hammers the target server with thousands of requests — that phase is loud and logged. Only run the brute-force stage against systems you are authorised to test, from an attributable-to-nobody source.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Published by Trickest, a known security-automation vendor, on GitHub; small, auditable Go source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- mksub
- trickest-inventory
aliases:
- trickest mkpath
tags:
- Domain/IP/Links
- Wordlists generators
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# MKPATH

> A tiny Go helper that expands a wordlist into multi-level path permutations — the ammunition-maker for directory/file brute-forcing a web target.

## When to use
Web-infrastructure recon (authorised) rather than person-finding. You have a `domain`/host and want to discover hidden directories and files (backups, configs, admin panels, exposed docs that may contain identifiers). MKPATH takes a flat wordlist and produces layered path combinations (`a/`, `a/b/`, `a/b/c/`), which you then feed to a content brute-forcer. It builds the path list; it does not make the requests.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `go install github.com/trickest/mkpath@latest` (or clone the repo).
2. Pipe or pass your wordlist and set the depth/levels you want; MKPATH emits the permuted path list.
3. Feed that list into a brute-forcer — GoBuster, ffuf, or Dirbuster — pointed at the authorised target.
4. Review hits (200/301/403) for exposed content.
5. Pivot: any exposed document/config → extract selectors (emails, names, `metadata-exif`) with your normal tooling.

## Inputs → Outputs
- **In:** a `domain`/host + a wordlist
- **Out:** a generated list of candidate paths to probe on that `domain`
- **Empty/negative result looks like:** MKPATH always emits paths (it's a generator); "nothing found" only happens at the brute-force stage when no path resolves — meaning the wordlist/depth missed, not that the site is empty.

## Gotchas & OpSec
- It is a **generator only** — no discovery happens until you run a brute-forcer with its output.
- **Authorisation required:** the downstream brute-force is active, noisy, and logged; scanning systems you don't own is likely illegal.
- Path explosion: deep levels + big wordlists create enormous lists; cap depth to keep the scan tractable.

## Overlaps ("do both")
- Same-family tooling: pair with `[[mksub]]` (subdomain permutations) and `[[trickest-inventory]]` for a fuller Trickest recon pipeline — subdomains → paths → content.

## Trust & verifiability
`trust: community` — it is a small, auditable open-source tool from a reputable vendor; it invents nothing, so trust comes from reading the ~one-file source. The findings depend entirely on your wordlist and the brute-forcer, not on MKPATH.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mkpath |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
