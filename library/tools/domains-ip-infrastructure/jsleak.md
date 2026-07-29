---
id: jsleak
name: JSLEAK
description: Use when you have a `domain`/URL list and want to mine its JavaScript for secrets, emails, endpoints and links — returns leaked emails, API keys and hidden paths/domains.
url: https://github.com/channyein1337/jsleak
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Fast Go scanner that extracts secrets, emails and links from a target's JavaScript during recon.
selectorsIn:
- domain
- email
selectorsOut:
- domain
- email
- password
status: live
pricing: free
costNote: Free/open-source Go tool; no account or key.
opsec: active
opsecNote: Active — it fetches the target's JS files (and can verify links with live HTTP requests), so requests hit the subject's infrastructure and appear in their logs. Use a research IP/VPN and avoid the status-check flag if you want to stay quiet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: Community single-author Go tool; regex-driven, so results include false positives and depend on the pattern set (borrows from secrets-patterns-db / LinkFinder).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- webosint
aliases:
- jsleak
tags:
- Domain/IP/Links
- Dorks/Pentest/Vulnerabilities
- secrets
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# JSLEAK

> A fast Go CLI that scrapes a site's JavaScript for secrets, emails, endpoints and links during domain recon.

## When to use
You have a `domain`/URL (or a list of them) tied to a subject or organisation and want to surface what its front-end JavaScript exposes — hidden API endpoints, internal paths, email addresses, and accidentally-shipped API keys/tokens. Useful for mapping a target's web infrastructure and occasionally for pulling contact emails out of a site's code.

## How to use it (`bestInteractionPattern`: cli)
1. Install with Go: `go install github.com/channyein1337/jsleak@latest` (or clone and build).
2. Feed URLs via stdin or a file, e.g. `cat urls.txt | jsleak -s -l -k`:
   - `-s` find secrets/emails, `-l` extract links, `-e` complete relative URLs, `-k` check link status codes.
3. Optionally supply a custom YAML regex file to tune what counts as a "secret".
4. Review hits — each is a regex match, so triage for false positives.
5. Pivot: discovered endpoints/subdomains feed further domain mapping; leaked emails feed email-OSINT tools; exposed keys are a sensitivity/severity flag.

## Inputs → Outputs
- **In:** `domain`/URL list (JavaScript sources)
- **Out:** `email` (addresses in code), `password`/secrets (API keys, tokens), `domain` (endpoints, links, paths)
- **Empty/negative result looks like:** no matches (minified/clean JS or a site with little client-side code) — absence of secrets is normal, not a tool failure.

## Gotchas & OpSec
- Human-in-the-loop: none, but you must manually triage regex false positives.
- OpSec: **active** — fetching JS (and `-k` status checks) touches the target's servers; throttle and use a research IP.
- It only sees what's in client-side JS; server-side secrets and non-JS assets are out of scope.

## Overlaps ("do both")
- Pairs with `[[webosint]]` — run WEBOSINT for WHOIS/DNS/subdomain context, then jsleak to mine the JavaScript of the hosts you find.

## Trust & verifiability
`trust: unverified` — a community single-author tool; every hit is a regex match, so confirm any "secret" or email before treating it as real, and never act on an exposed credential.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | jsleak |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, email → domain, email, password |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
