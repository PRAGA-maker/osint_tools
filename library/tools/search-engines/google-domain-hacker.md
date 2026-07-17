---
id: google-domain-hacker
name: Google Domain Hacker
description: Use when you have a `domain` or `name` and want a preset Google dork scoped to a curated site set — returns matching pages, domain and social-profile leads.
url: https://cse.google.com/cse/publicurl?cx=005797772976587943970:ca2hiy6hmri
category: search-engines
path:
- search-engines
bestFor: Running Google-quality queries through a curator-built Programmable Search Engine focused on domain/host discovery, without setting up your own dorks.
selectorsIn:
- domain
- name
selectorsOut:
- domain
- social-profile
status: live
pricing: free
costNote: Free Google Programmable Search Engine (CSE); no account needed to run a query.
opsec: passive
opsecNote: A standard Google-backed search; the query goes to Google, not the subject. Use a private/sock-puppet session for sensitive terms, as with any search engine.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party-configured Google CSE — its scope is defined by an unknown curator and can drift or be edited, so treat coverage as opaque and Google-dependent.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Google CSE domain hacker
tags:
- google-cse
- dorking
- specialty-search
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# Google Domain Hacker

> A preset Google Programmable Search Engine tuned for domain/host discovery — Google's index, narrowed to a curator's chosen scope.

## When to use
You want Google-powered results confined to a specific slice — a domain/host-discovery preset that someone has already configured as a Custom/Programmable Search Engine. Use it when you have a `domain`, `name` or keyword and want a quick scoped dork without building your own `site:`/`inurl:` queries. Because the scope is curator-defined and opaque, treat it as a convenience layer over Google, not a distinct data source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE URL: https://cse.google.com/cse/publicurl?cx=005797772976587943970:ca2hiy6hmri.
2. Enter your query — a `domain`, subject `name`, or keyword; standard Google operators generally work within the CSE scope.
3. Review results as you would Google's, noting which host/`domain` each hit sits on.
4. Open promising pages and extract `domain`/`social-profile` leads.
5. Pivot: re-run the same query on plain Google to compare scope, and feed discovered domains into WHOIS/subdomain tooling.

## Inputs → Outputs
- **In:** `domain`, `name`, or keyword
- **Out:** Google result pages within the CSE scope → `domain` and `social-profile` leads
- **Empty/negative result looks like:** no results — may mean the CSE scope excludes the relevant sites, not that Google has nothing; always cross-check on unrestricted Google.

## Gotchas & OpSec
- The CSE **configuration is opaque and mutable** — you can't see exactly what it includes, and the owner can change or retire it.
- It inherits Google's ranking and any regional filtering; results aren't exhaustive.
- Nothing here beats knowing the underlying dork — if scope matters, build your own `site:` query.

## Overlaps ("do both")
- Pairs with unrestricted Google and other dorking presets — run both to see what the CSE scope is adding or hiding.

## Trust & verifiability
`trust: unverified` — a third-party Google CSE with an unknown, editable scope; the results are real Google hits, but the framing is only as trustworthy as the anonymous curator, so verify on open Google.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-domain-hacker |
| category | search-engines |
| selectorsIn → selectorsOut | domain, name → domain, social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
