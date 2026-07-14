---
id: h8mail-2
name: h8mail
description: Use when you have an `email` (or a bulk list) and want to find associated breaches, leaked passwords and correlated addresses — a CLI tool querying breach services and local leak dumps.
url: https://pypi.org/project/h8mail/
category: email
path:
- email
bestFor: Bulk email breach hunting from the command line — correlating an address with leaks, passwords and related emails via APIs or local dumps.
selectorsIn:
- email
selectorsOut:
- email
- document-id
status: live
pricing: freemium
costNote: The tool is free/open-source (pip install h8mail). Its best data sources are API keys you supply (some paid, e.g. premium breach services); it also runs offline against local BreachCompilation/Collection#1 dumps you already hold.
opsec: passive
opsecNote: Passive to the target — queries go to breach APIs and your local files, never to the subject. But you transmit the target's email to whatever third-party services you enable; use a dedicated key/environment and mind each provider's logging. Handle recovered credentials lawfully.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A widely used open-source OSINT tool (khast3x/h8mail). Reliable as software, but breach coverage depends on which services/dumps you connect; last major release was 2.5.6 (2022), so some integrations may need updating.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
relatedTools:
- my-cse-for-search-in-48-pastebin-sites
aliases:
- h8mail
- khast3x h8mail
tags:
- breach
- leaks
- cli
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# h8mail

> A command-line email OSINT and breach-hunting tool — feed it an address (or thousands) and it correlates breaches, leaked passwords and related emails from APIs and local dumps.

## When to use
You have a subject's `email` (or a list of them) and want their breach footprint: which leaks they appear in, any exposed passwords, and correlated/adjacent email addresses that widen the identity graph. h8mail shines for bulk, scriptable work and for searching large offline leak datasets you already possess. Recovered passwords and reused-credential patterns are strong pivots for account access-history and for linking a person across services.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install h8mail` (Python 3).
2. Configure API keys in a config file for the breach/recon services you have (premium services give the richest hits); or point it at local dump files.
3. Run against a target: `h8mail -t target@example.com` — or a file of emails with `-t targets.txt`, and local dumps with `-lb`/`-sk`. Output goes to CSV.
4. Read the output: per-email breach hits, any leaked passwords, and newly discovered related emails (h8mail tracks these during a run).
5. Pivot: leaked passwords/usernames feed cross-service account checks; correlated emails feed further email/username OSINT and pastebin sweeps like [[my-cse-for-search-in-48-pastebin-sites]].

## Inputs → Outputs
- **In:** `email` (single or bulk list)
- **Out:** `email` (correlated addresses), `document-id` (breach names/identifiers), leaked credentials
- **Empty/negative result looks like:** no breach hits — meaning the address isn't in the sources you queried (or you have no keys/dumps enabled), NOT proof the email was never leaked. Coverage is only as good as your configured sources.

## Gotchas & OpSec
- Value is gated by the API keys and local dumps you provide; with no sources, results are thin — this drives the `freemium`/`api-key` rating.
- Recovered passwords are sensitive: store and handle lawfully; never use them to access accounts.
- OpSec: passive to the target, but each enabled service receives the queried email — use dedicated keys and review provider logging.

## Overlaps ("do both")
- Pairs with [[my-cse-for-search-in-48-pastebin-sites]] and web breach-lookup services — h8mail automates structured breach APIs and offline dumps; the pastebin CSE catches ad-hoc pastes those miss. Run both for coverage.

## Trust & verifiability
`trust: community` — a respected open-source tool, but breach data it surfaces is unvetted and can be stale or wrong; confirm any decisive finding (e.g. a password still valid, a correct identity link) independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | h8mail-2 |
| category | email |
| selectorsIn → selectorsOut | email → email, document-id |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
