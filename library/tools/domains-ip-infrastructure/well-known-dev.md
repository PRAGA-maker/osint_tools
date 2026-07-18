---
id: well-known-dev
name: well-known.dev
description: Use when you have a `domain` and want to mine its /.well-known/ files and related infra — returns security.txt contacts, ad networks, IPs, auth config, and cross-domain links.
url: https://well-known.dev/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Searching indexed /.well-known/ resources (security.txt, ads.txt, openid-configuration, trust.txt) across domains for recon and organizational links.
selectorsIn:
- domain
selectorsOut:
- domain
- email
- ip-address
status: live
pricing: free
costNote: Free public search engine over crawled /.well-known/ resources; no account required.
opsec: passive
opsecNote: Passive — you query well-known.dev's own crawled index, not the target's server, so the subject's infrastructure sees no request from you. Fully OpSec-safe for domain recon.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An independent, purpose-built index of /.well-known/ files with transparent per-record scan dates and hashes; findings are checkable by fetching the same file directly.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- well-known.dev search
tags:
- domainsandips
- Domains & IPs
- infrastructure-recon
- security-txt
source: uk-osint
lastVerified: '2026-07-18'
enrichment: full
---

# well-known.dev

> A search engine over the `/.well-known/` files that sites publish — turn a domain into ad-network ties, security contacts, auth providers, and infrastructure links, all without touching the target.

## When to use
You have a `domain` tied to a subject or organization and want to enrich it: who to contact (security.txt), which ad networks monetize it (ads.txt / app-ads.txt — a strong signal of shared ownership across sites), which identity provider it uses (openid-configuration), what server software/version it runs (nodeinfo), and which other domains it declares relationships with (trust.txt). Excellent for pivoting from one domain to an organization's wider footprint, passively.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://well-known.dev/.
2. Query by domain/base-domain, resource type, IP address, or resource-specific fields (ad system, encryption key, software version).
3. Read the indexed records: the parsed contents of each `/.well-known/` file, plus scan date, status, redirects, and content hash.
4. Pivot laterally: a shared ads.txt publisher ID or a common trust.txt link ties multiple domains to the same owner; a security.txt email/PGP key is a contact/`email` selector; recorded IPs feed infrastructure mapping.

## Inputs → Outputs
- **In:** a `domain` (or an IP / resource-field to search by)
- **Out:** parsed `/.well-known/` records — security contacts (`email`), ad-network IDs, auth config, `ip-address`, and cross-`domain` relationships
- **Empty/negative result looks like:** no records for a domain means it publishes no indexed /.well-known/ files (many small sites don't) — try fetching common paths directly before concluding nothing exists.

## Gotchas & OpSec
- Coverage depends on the crawl — a domain absent from the index isn't proof it lacks these files; verify by fetching `https://<domain>/.well-known/security.txt` etc. directly (that step is active).
- ads.txt / trust.txt linkage is a strong but not conclusive ownership signal; corroborate before asserting common control.
- Passive by design: your search never reaches the subject's server.

## Overlaps ("do both")
- Complements WHOIS, passive-DNS, and certificate-transparency tools — those map a domain's registration and hosting, while well-known.dev exposes the declarative, owner-published metadata that ties domains together.

## Trust & verifiability
`trust: community` — an independent index that records a scan date and content hash per entry, so every finding can be reproduced by fetching the same file yourself; the data originates from the sites themselves.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | well-known-dev |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, email, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
