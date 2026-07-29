---
id: mozilla-http-observatory
name: Mozilla HTTP Observatory
description: Use when you have a `domain` and want to assess a site's HTTP security posture (headers, TLS, cookies) — returns a security grade and configuration findings for that host.
url: https://developer.mozilla.org/en-US/observatory
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Grading a website's HTTP security headers and configuration to profile how a target's infrastructure is set up.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free public scanner run by Mozilla (MDN); no account required.
opsec: active
opsecNote: The scan makes real HTTP requests to the target site to inspect its responses, so the target's server sees a hit from Mozilla's scanner (not directly from you). Mildly active — you are not anonymous to the site if it correlates the scan, but your own IP is not the requester. Avoid scanning if even Mozilla-sourced probing would tip off a sensitive target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Mozilla and hosted on MDN; a reputable, well-documented first-party security scanner.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
aliases:
- HTTP Observatory
- MDN Observatory
tags:
- website-security
- infrastructure
- headers
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# Mozilla HTTP Observatory

> Mozilla's free scanner that grades a site's HTTP security configuration — a quick way to profile how a target's web infrastructure is built and maintained.

## When to use
You have a `domain` and want to understand a site's technical hygiene: which security headers it sets (CSP, HSTS, X-Frame-Options), cookie flags, TLS/redirect behaviour, and an overall grade. This characterises the operator's competence and stack — useful context in an infrastructure investigation, and a lightweight way to compare related sites you suspect share an owner.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://developer.mozilla.org/en-US/observatory.
2. Enter the target `domain` and run the scan.
3. Read the letter grade and the itemised header/configuration findings.
4. For bulk/programmatic use, call the Observatory API.
5. Pivot: a distinctive header/config fingerprint can be compared across other domains to support common-ownership hypotheses; feed the domain into WHOIS/passive-DNS for the rest of the infra picture.

## Inputs → Outputs
- **In:** `domain`
- **Out:** security grade and per-check configuration findings for that `domain`
- **Empty/negative result looks like:** the scan fails to reach the host (offline, blocking scanners, non-HTTP) — a connection error, not a security verdict.

## Gotchas & OpSec
- **Assesses configuration, not content or ownership** — it tells you how the site is secured, not who runs it.
- Mildly active: the scan hits the target's server (from Mozilla's infra). Consider whether any probing is acceptable for a sensitive target.
- Grades reflect header best-practices; a low grade means weak config, not necessarily malicious intent.

## Overlaps ("do both")
- Pair with WHOIS, passive DNS, and TLS/certificate tools — Observatory profiles the HTTP layer while those map ownership and hosting; together they characterise a target's web presence.

## Trust & verifiability
`trust: trusted` — a first-party Mozilla tool on MDN with published methodology; the technical findings are reliable and reproducible.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mozilla-http-observatory |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
