---
id: urldna
name: urlDNA
description: Use when you have a `domain`/URL and want a safe server-side scan of it — returns screenshot, resolved `ip-address`, TLS/tech details, and a risk verdict without visiting it yourself.
url: https://urldna.io
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- discovery
bestFor: Sandboxed scanning of a suspicious URL/domain to see what it serves without touching it from your own machine.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Free tier with an account for scans and searching public scans; higher volume/API and private scans are paid.
opsec: passive
opsecNote: Passive from your side — urlDNA's infrastructure fetches the target, so your IP doesn't hit it directly (safer for suspicious links). Note that a PUBLIC scan is visible to others (including, potentially, the site operator watching for scans), which can tip off a target; use a private scan when you don't want the lookup exposed.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A urlscan.io-style URL-analysis service; results reflect what the scanner saw at scan time and its own heuristics — treat the verdict as a signal, not a ruling.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- urldna.io
- url DNA
tags:
- url-scanner
- domain-and-ip-research
- discovery
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# urlDNA

> A "DNA test for websites": submit a URL and its servers scan it for you — screenshot, resolved IP, TLS, technologies, and a risk verdict — so you inspect a suspicious link without visiting it.

## When to use
You have a URL or `domain` that might be phishing/malware and you don't want to open it from your own machine, or you want structured intel (IP, TLS cert, tech, redirects, verdict) on a site. Reach for urlDNA to scan it server-side and read what it serves safely. Also useful for *searching existing public scans* to see if others have already analysed a domain and what related infrastructure appeared.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://urldna.io and sign in (free account) to run a scan.
2. Submit the target URL/`domain`; choose a private scan if you don't want the result public.
3. Read the report: rendered screenshot, resolved `ip-address`/ASN, TLS certificate, detected technologies, redirect chain, and the risk verdict.
4. Search the public scan database for the domain/IP to find prior scans and related sites.
5. Pivot: the resolved IP/cert/tech feed infrastructure analysis (`[[technology-lookup]]`, passive-DNS, certificate search) to expand a phishing/malware cluster.

## Inputs → Outputs
- **In:** a URL or `domain`
- **Out:** screenshot, resolved `ip-address`/ASN, TLS cert, detected tech, redirect chain, risk verdict; and links to related `domain`s
- **Empty/negative result looks like:** a site that blocks scanners, is already down, or cloaks for automated visitors returns a thin/benign-looking scan — absence of badness isn't proof of safety.

## Gotchas & OpSec
- Human-in-the-loop: an account/login is required to scan.
- **Public scans are visible** — a target monitoring for scans can be tipped off, and your submitted URL becomes searchable. Use private scans for sensitive work.
- The verdict is heuristic; corroborate with a second scanner and your own judgement.

## Overlaps ("do both")
- Directly comparable to urlscan.io — run both, since coverage and verdicts differ, and one may hold a prior scan the other lacks. Feed extracted IP/cert/tech into `[[technology-lookup]]` and certificate-transparency search to map related infrastructure.

## Trust & verifiability
`trust: community` — a capable URL-analysis service; its verdict and captured artifacts are a strong signal but reflect one scan at one moment, so verify with a second scanner and the underlying IP/cert data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | urldna |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
