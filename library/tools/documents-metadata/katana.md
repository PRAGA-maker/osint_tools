---
id: katana
name: Katana (dork scanner)
description: Use when you have a Google dork / GHDB query and want it automated over Tor — returns the search-result URLs matching the dork.
url: https://github.com/TebbaaX/Katana
category: documents-metadata
path:
- documents-metadata
bestFor: Automating Google Hacking/Dorking (GHDB) queries from the CLI with Tor support.
selectorsIn:
- domain
selectorsOut:
- domain
status: degraded
pricing: free
costNote: Free and open source (Python). Repo archived (read-only) in 2025 — the author describes it as an old educational project; usable but unmaintained.
opsec: active
opsecNote: Katana automates real Google searches from your host, which Google rate-limits and can CAPTCHA/block for scripted queries; that pattern is attributable to your IP. It supports Tor for exactly this reason — route through it. Dorking a target's own domain is passive toward the target (you query Google, not them), but heavy automated searching risks your search identity, not the subject's.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: cli
trust: community
trustNote: A known but archived, self-described educational dork script. It just wraps Google queries — reliability depends on Google not blocking automated searches, which it increasingly does. Prefer a maintained dorking approach for serious work.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- Katana-ds
- TebbaaX/Katana
tags:
- toddington
- dorks
- google-hacking
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# Katana (dork scanner)

> A small Python CLI that automates Google Hacking/Dorking — feed it GHDB-style dork queries and it runs them (optionally over Tor) and returns matching result URLs. Archived and educational.

## When to use
You want to run Google dorks in bulk — e.g. hunting exposed files, directories, or endpoints tied to a target `domain` — from the command line rather than pasting queries by hand. Katana automates that and can route through Tor. Because it's archived and Google now aggressively blocks scripted searches, treat it as a convenience/learning tool and expect friction.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo and install the Python requirements (repo is read-only/archived, so use the last state).
2. Configure Tor if you want to distribute/anonymise the automated searches (recommended — see OpSec).
3. Provide dork queries (GHDB-style, often scoped with `site:targetdomain.com`) and run; Katana returns the matching result URLs.
4. Expect CAPTCHAs/blocks on volume — solve/slow down, or switch Tor circuits.
5. Pivot: result URLs (`domain`/paths) feed content review and endpoint discovery.

## Inputs → Outputs
- **In:** Google dork queries (often scoped to a target `domain`)
- **Out:** matching search-result URLs (`domain`/paths)
- **Empty/negative result looks like:** no results, or Google returning a CAPTCHA/consent wall — often means you were rate-limited/blocked, not that the dork found nothing. Slow down / rotate Tor and retry, or run the dork manually.

## Gotchas & OpSec
- Human-in-the-loop: automated Google queries trigger **CAPTCHAs**/blocks; this is the main practical limiter.
- **Archived/educational** since 2025 — no fixes; scraping behaviour breaks as Google changes. Prefer a maintained method for real work.
- OpSec: passive toward the target (you query Google), but automated searching exposes *your* search identity — use Tor and go slow.

## Overlaps ("do both")
- Same idea as other dork automators and the manual Google Hacking Database — for anything important, run the key dorks manually or with a maintained tool; use Katana only for quick batches.

## Trust & verifiability
`trust: community` — a well-known but archived, educational script wrapping Google search. Results are only as reliable as un-blocked Google queries allow; verify findings by opening them, and don't depend on it for critical work.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | katana |
| category | documents-metadata |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (captcha) |
