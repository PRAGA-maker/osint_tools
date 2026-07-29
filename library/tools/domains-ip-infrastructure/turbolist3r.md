---
id: turbolist3r
name: Turbolist3r
description: Use when you have a `domain` and want to enumerate its subdomains plus DNS/CNAME analysis — returns discovered subdomains flagged for possible takeover.
url: https://github.com/alex14324/Turbolist3r
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Passive-plus-DNS subdomain enumeration of a target domain, with automatic CNAME/takeover analysis.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: degraded
pricing: free
costNote: Free, open-source Python tool; a fork of Sublist3r. No account or key for the OSINT sources it queries.
opsec: active
opsecNote: OSINT-source enumeration is passive, but Turbolist3r also resolves discovered names against public DNS — that DNS activity is low-noise but not zero, and any later direct probing of the found hosts touches target infrastructure. Enumerate from a VPN/sock-puppet if the target might watch its logs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A lightly-maintained community fork of the well-known Sublist3r; the underlying technique is standard, but this specific fork has minimal commit history.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- sublist3r
aliases:
- Turbolist3r
tags:
- subdomain-enumeration
- dns
- recon
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Turbolist3r

> A Sublist3r fork that enumerates a domain's subdomains from public OSINT sources and then does automated reverse-DNS/CNAME analysis to flag possible subdomain takeovers.

## When to use
You have a `domain` tied to a subject or an org (a personal site, a business, a service they run) and want to map its attack/footprint surface: what subdomains exist, where they resolve, and whether any CNAME points at an abandoned cloud service (a takeover indicator). In a people-context this is infrastructure mapping — surfacing staging sites, mail hosts, or forgotten subdomains that carry more identifying content than the main page.

## How to use it (`bestInteractionPattern`: cli)
1. Clone: `git clone https://github.com/alex14324/Turbolist3r` and install its Python requirements.
2. Enumerate: `python turbolist3r.py -d example.com` — pulls subdomains from search engines and OSINT sources.
3. Add DNS analysis: use the analysis flags to resolve found names and categorize A vs CNAME records.
4. Save output to a file for the working set; feed discovered hosts into your normal infra tooling.
5. Read the CNAME analysis for takeover candidates (dangling records pointing at cloud providers).

## Inputs → Outputs
- **In:** `domain`
- **Out:** list of sub-`domain`s, their A/`ip-address` and CNAME mappings, takeover flags
- **Empty/negative result looks like:** few or no subdomains — either a small footprint or the OSINT sources are rate-limiting/blocking; cross-check with a maintained enumerator before concluding the surface is small.

## Gotchas & OpSec
- **Lightly maintained fork** (`status: degraded`) — OSINT source APIs drift; if results look thin, use a current tool like a maintained Sublist3r/amass build.
- DNS resolution of discovered names is mildly active; probing the hosts afterward is definitely active — use a VPN/sock-puppet.
- OpSec: **active** overall once DNS/host probing begins.

## Overlaps ("do both")
- Pairs with `[[sublist3r]]` — Turbolist3r extends it with takeover analysis; run a maintained enumerator alongside to cover sources this fork may miss.

## Trust & verifiability
`trust: community` — standard technique, credible lineage (Sublist3r), but a low-activity fork; verify the tool still resolves current sources before relying on completeness.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | turbolist3r |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
