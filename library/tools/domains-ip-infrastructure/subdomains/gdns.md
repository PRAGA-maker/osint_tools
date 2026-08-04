---
id: gdns
name: gdns (Google DNS-over-HTTPS)
description: Use when you have a `domain` and want scriptable DNS lookups via Google's DoH API — returns resolved records (A, MX, TXT, NS, SPF) as structured data.
url: https://github.com/hrbrmstr/gdns
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- subdomains
bestFor: Programmatic, bulk DNS resolution from R using Google's DNS-over-HTTPS, including SPF parsing helpers.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free and open source (MIT); available on CRAN and GitHub.
opsec: active
opsecNote: Queries resolve through Google's DoH endpoint rather than directly against the target's authoritative servers, which hides your lookups from the target — but Google sees every query. It does not contact the target's own DNS unless you resolve records that only their nameservers answer. Use a disposable environment for sensitive bulk work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Authored by Bob Rudis (hrbrmstr), a well-known security/data-science developer; MIT-licensed and CRAN-published, so the code is auditable and the DNS answers come straight from Google's resolver.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools: []
aliases:
- hrbrmstr/gdns
- Google DNS over HTTPS R package
tags:
- dns
- doh
- r-package
- bulk-lookup
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# gdns (Google DNS-over-HTTPS)

> An R package wrapping Google's DNS-over-HTTPS API — for scripted, bulk DNS resolution when you want answers as structured data instead of clicking through a web form.

## When to use
You have one or many `domain`s and want to resolve their DNS records programmatically — A/AAAA (→ `ip-address`), MX (mail hosts), NS (nameservers), TXT/SPF (mail authorization and infrastructure hints) — as part of a scripted pipeline. Because it goes through Google's DoH resolver, your queries are encrypted and don't hit the target's nameservers directly for cached records, which is quieter than a direct `dig`.

## How to use it (`bestInteractionPattern`: cli)
1. Install R, then the package: `install.packages("gdns")` (CRAN) or `devtools::install_github("hrbrmstr/gdns")`.
2. In an R session, resolve a domain: `query("example.com")` returns the structured response; `dig()` mimics a dig-style call.
3. For many domains at once, use `bulk_query()` with a vector of `domain`s.
4. Use the SPF helpers to parse a domain's SPF record into its authorized senders/IPs.
5. Read the results: A records give `ip-address`es, NS/MX/TXT map the domain's infrastructure. Pivot IPs into reputation/port tools and included SPF domains into further DNS lookups.

## Inputs → Outputs
- **In:** `domain` (single or bulk)
- **Out:** resolved DNS records — `ip-address`es (A/AAAA), MX/NS/TXT records, parsed SPF senders
- **Empty/negative result looks like:** `NXDOMAIN` / empty record set — the domain doesn't exist or doesn't publish that record type; a missing MX/SPF just means no mail configuration, not an error.

## Gotchas & OpSec
- Human-in-the-loop: none, but you need R installed (`localInstall`).
- OpSec: **active** in that Google's resolver sees your queries, but **quieter toward the target** than direct resolution — good when you don't want lookups appearing in the target's DNS logs. Google logs apply; use a disposable environment for large sensitive sweeps.
- It resolves existing records; it is not a subdomain brute-forcer on its own — pair it with a wordlist/CT-log tool to discover subdomains, then resolve them in bulk here.

## Overlaps ("do both")
- Pairs with certificate-transparency and subdomain-enumeration tools — those *discover* hostnames, and gdns *resolves them in bulk* quietly via Google DoH; together they map a domain's live footprint.

## Trust & verifiability
`trust: community` — a reputable developer's MIT-licensed, CRAN-published package; DNS answers originate from Google's public resolver and are trivially verifiable with an independent `dig`.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | gdns |
