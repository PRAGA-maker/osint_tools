---
id: cloakquest3r
name: CloakQuest3r
description: Use when you have a `domain` behind Cloudflare/a CDN and want to uncover its real origin `ip-address` — via subdomain scanning, SSL analysis, and IP history.
url: https://github.com/spyboy-productions/CloakQuest3r
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Attempting to reveal the true origin IP of a website hidden behind Cloudflare or another reverse proxy/CDN.
selectorsIn:
- domain
selectorsOut:
- ip-address
- domain
status: live
pricing: free
costNote: Open source (MIT); free to run locally or on Colab/Cloud Shell/Binder.
opsec: active
opsecNote: It probes subdomains and infrastructure related to the target, and following a discovered origin IP means connecting to the target's real server — that traffic can appear in their logs. The project is explicitly authorised-testing only; run from an isolated/sock-puppet environment.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source PoC by spyboy-productions; a best-effort heuristic tool, not a guaranteed de-cloak — results need independent confirmation.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- CloakQuest3r
tags:
- Domain/IP/Links
- Domain/IP investigation
- cloudflare-bypass
source: cyb-detective
lastVerified: '2026-07-23'
relatedTools:
- https-github-com-spyboy-productions-valid8proxy
- r4ven
---

# CloakQuest3r

> A Python recon tool that tries to strip a site's CDN/proxy cover and reveal the real origin IP — by enumerating subdomains, analysing SSL certificates, and checking historical IP records.

## When to use
You have a `domain` that resolves only to Cloudflare (or another reverse proxy/CDN) and you need the origin `ip-address` — the actual server behind the shield — to attribute hosting, map co-located infrastructure, or corroborate who runs a site. CloakQuest3r bundles the common de-cloaking heuristics (subdomains that leak the origin, cert matches, IP history) into one scan.

## How to use it (`bestInteractionPattern`: cli)
1. `git clone` the repo, `pip3 install -r requirements.txt`.
2. Run `python cloakquest3r.py example.com` (or use the Colab/Cloud Shell option to avoid running from your own IP).
3. Read the output: candidate real IP(s), subdomains found, SSL findings, and scan stats.
4. Verify a candidate origin by requesting the site directly on that IP (Host header set) and comparing content — de-cloak heuristics produce false positives.
5. Pivot: a confirmed origin IP feeds reverse-IP, WHOIS/ASN, and hosting-provider lookups.

## Inputs → Outputs
- **In:** `domain`
- **Out:** candidate origin `ip-address`(es), discovered `domain` subdomains, SSL/IP-history clues
- **Empty/negative result looks like:** no origin found — well-configured Cloudflare deployments genuinely can't be de-cloaked this way; a null result is common and not a tool failure.

## Gotchas & OpSec
- OpSec: **active** — subdomain probing and (especially) connecting to a discovered origin touch real infrastructure; use isolation and only with authorisation (the repo stresses this is educational/PoC).
- Heuristic and noisy: always confirm a candidate IP actually serves the target before treating it as the origin.

## Overlaps ("do both")
- Pairs with `[[certificate-search]]`, reverse-IP databases, and Netlas/Shodan-style search — certificate and passive-DNS history often reveal an origin without any active probing; try those first.

## Trust & verifiability
`trust: community` — a useful open-source PoC, but de-cloaking is probabilistic; never report an origin IP without directly verifying it responds as the target.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cloakquest3r |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → ip-address, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
