---
id: secretfinder
name: SecretFinder
description: Use when you have a `domain`/web app and want to scrape its JavaScript for leaked API keys, tokens, endpoints and secrets — returns domain (endpoints) and password (credential/secret) leads.
url: https://github.com/m4ll0k/SecretFinder
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Regex-scanning a site's JavaScript files for exposed API keys, tokens, JWTs, and hidden endpoints.
selectorsIn:
- domain
selectorsOut:
- domain
- password
status: live
pricing: free
costNote: Free, open-source Python tool (m4ll0k). Install via pip/requirements; no account.
opsec: active
opsecNote: ACTIVE — SecretFinder downloads the target's JavaScript from its servers, so your requests appear in the target's logs. Route through a proxy/VPN and only scan sites you're authorized to test. Handle any recovered secrets responsibly; do not use recovered keys/tokens (that would be intrusion, not OSINT).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Well-known open-source recon/bug-bounty tool; regex-based, so expect false positives and misses — every "secret" needs manual confirmation.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- infoga
aliases:
- SecretFinder
tags:
- Domain/IP/Links
- Source Code Analyzes
- secrets-detection
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# SecretFinder

> A Python recon tool that pulls a site's JavaScript and greps it for the things developers accidentally ship — API keys, access tokens, JWTs, and internal endpoints.

## When to use
You're investigating a `domain`/web application tied to a subject or organization and want to surface what its front-end code leaks: hard-coded API keys, cloud credentials, tokens, and hidden/undocumented endpoints. Those leaks map additional infrastructure (endpoints → more hosts/APIs) and reveal the tech and third-party services in use. It's a web-recon/attack-surface tool; the OSINT value is the endpoints and service fingerprints, not misusing any credential you find.

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/m4ll0k/SecretFinder and install requirements (Python).
2. Run against a live site's JS: `python SecretFinder.py -i https://example.com -e` (extract all JS from the page), or point `-i` at a specific `.js` URL/file. Route through a proxy first.
3. Review matches: API keys, tokens, JWTs, and endpoint strings, each with the regex rule that matched.
4. Manually confirm each hit (regex → false positives are common).
5. Pivot: recovered endpoints → new hosts/APIs to map (`[[infoga]]`, subdomain tools); identified third-party services → the vendors the target relies on.

## Inputs → Outputs
- **In:** a `domain`/URL (page or specific JS file)
- **Out:** candidate secrets (API keys, tokens, JWTs → `password`-class credentials) and hidden endpoints (`domain`/URLs)
- **Empty/negative result looks like:** no matches — the JS is clean/minified beyond the patterns, or the site loads scripts you didn't capture; empty ≠ proof nothing leaks (try capturing more JS, or a JS-aware crawler).

## Gotchas & OpSec
- **Active** — downloads JS from the target; your IP is logged. Proxy it and stay in-scope.
- Regex-based: many false positives (and some misses) — verify every finding by hand.
- Never use a recovered credential; that crosses from OSINT into unauthorized access.

## Overlaps ("do both")
- Pairs with `[[infoga]]`, LinkFinder, and subdomain enumeration — SecretFinder finds secrets/endpoints in JS; those expand the surrounding surface.

## Trust & verifiability
`trust: community` — popular open-source tool; results are regex candidates, so confirm each secret/endpoint manually before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | secretfinder |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, password |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
