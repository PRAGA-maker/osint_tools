---
id: curl-for-osint
name: cURL for OSINT
description: Use when you have a `username`, `email`, `domain`, or `ip-address` and want copy-paste cURL+grep recipes to query OSINT endpoints from the shell — returns scriptable `social-profile` / `email` / `domain` extraction.
url: https://github.com/C3n7ral051nt4g3ncy/cURL_for_OSINT
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A cheat-sheet of cURL + grep one-liners for scriptable, low-footprint OSINT lookups (whois, subdomains, email extraction, IP recon) you can drop straight into an agent pipeline.
selectorsIn:
- username
- email
- domain
- ip-address
selectorsOut:
- social-profile
- email
- domain
status: live
pricing: free
costNote: Free, open reference repository on GitHub. No account; you supply your own shell and any target endpoints' access.
opsec: active
opsecNote: These recipes make YOU the one hitting the target endpoint directly from your shell — that is active and leaks your IP/User-Agent to whatever you query. Route through a VPN/proxy and set a neutral User-Agent; do not run them from an attributable host against a sensitive target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Curated by C3n7ral051nt4g3ncy, a known OSINT-tool author (258★); a documentation/recipe repo, so its value is the techniques, and each recipe is only as reliable as the endpoint it calls.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- masto
- osint-tactical
- prot1ntelligence
- webosint
- whatsmyname-python
aliases:
- cURL_for_OSINT
tags:
- curl
- cheatsheet
- scripting
- recipes
source: gh-topic-intelligence-gathering
lastVerified: '2026-07-17'
enrichment: full
---

# cURL for OSINT

> A recipe book, not an app: cURL + grep one-liners for pulling OSINT data (whois, subdomains, emails, IP recon) straight from the terminal — ideal for scripting passive lookups into an automated pipeline.

## When to use
You want to automate a lookup rather than click a web UI, and you have a `username`, `email`, `domain`, or `ip-address` to feed in. Reach for it when building an agent/shell pipeline that needs lightweight HTTP queries with predictable, greppable output — e.g. extracting emails from a page, enumerating subdomains, or scripting a whois. It teaches the *method*; you adapt the endpoints.

## How to use it (`bestInteractionPattern`: cli)
1. Open the repo: https://github.com/C3n7ral051nt4g3ncy/cURL_for_OSINT and browse the recipe sections (IP recon, whois, email extraction, subdomains, downloads).
2. Copy the relevant one-liner and substitute your selector (domain/IP/etc.).
3. Run it in your shell, piping through the provided `grep`/`awk` to isolate the fields you want.
4. Wrap it in a script/loop to batch many selectors; capture output to a file for the case record.
5. Pivot: extracted `email`/`social-profile`/`domain` → the dedicated enrichment tool for that selector.

## Inputs → Outputs
- **In:** `username`, `email`, `domain`, `ip-address`
- **Out:** scriptable extraction of `social-profile`, `email`, `domain` (and other fields depending on the recipe)
- **Empty/negative result looks like:** an empty grep result or an HTTP error in the response — the endpoint blocked you, changed its output, or has nothing; check the raw cURL response before concluding "no data."

## Gotchas & OpSec
- **Active by nature:** unlike a data broker that serves pre-collected results, these recipes query targets directly from your machine. Proxy/VPN and set a neutral User-Agent.
- Recipes can rot as target sites change markup/endpoints; treat them as a starting template, not guaranteed-working commands.
- Respect rate limits and terms of the endpoints you query.

## Overlaps ("do both")
- Pairs with purpose-built collectors like `[[webosint]]` and `[[whatsmyname-python]]` — those give polished results; cURL recipes fill the gaps where no tool exists or you need a bespoke, scriptable query.

## Trust & verifiability
`trust: community` — a reputable author's documentation repo. The techniques are sound, but each result's reliability is the queried endpoint's; always inspect the raw response.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | curl-for-osint |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username, email, domain, ip-address → social-profile, email, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
