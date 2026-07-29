---
id: evuln
name: eVuln
description: Use when you have a `domain` and want a free scan for injected malware, malicious redirects, or defacement — returns a compromise verdict for the site.
url: http://evuln.com/
category: documents-metadata
path:
- documents-metadata
bestFor: Free malware/defacement scanning of a website and browsing eVuln's advisories on known site compromises.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free online website malware scanner and PHP code scanner plus public security advisories; hands-on malware removal and ongoing monitoring are paid services.
opsec: passive
opsecNote: The scanner fetches the target site from eVuln's servers, so your IP isn't exposed to the target — but you submit the domain to a third-party SaaS that logs it. Fine for passive checks on public sites; don't submit private/unlisted hosts.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A long-running small commercial website-security vendor (malware removal/monitoring) offering free scanner tools; results are a point-in-time signal, not a full audit.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- eVuln malware scanner
tags:
- toddington
- curated-directory
- useful-websites-tools-documents
- website-malware-scan
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# eVuln

> A free website malware/defacement scanner (with public compromise advisories) from a small site-security vendor — check whether a domain is currently serving injected malware.

## When to use
You have a `domain` and want a quick, free read on whether it's compromised — injected malware, malicious iframes/redirects, or defacement — for example vetting a link before engaging, or assessing a subject's site for signs it's been hijacked or is hosting a scam. Use it as one signal in domain triage, not as a full security audit.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open evuln.com and find the free website malware scanner (also a PHP code scanner).
2. Enter the target `domain`/URL and run the scan.
3. Read the verdict: clean, or flagged with the malicious content/redirect it detected.
4. Optionally browse eVuln's advisories/stats pages for reports on known malicious-redirect and defacement patterns.
5. Pivot: a compromise verdict feeds a second reputation scanner and passive-DNS/WHOIS to map who else the campaign touches.

## Inputs → Outputs
- **In:** a `domain` / URL
- **Out:** a malware/defacement verdict for the site (clean vs flagged content/redirects)
- **Empty/negative result looks like:** "no malware detected" — meaning nothing found on the scanned surface right now, not a guarantee of safety (targeted or cloaked injections can evade a single scan).

## Gotchas & OpSec
- Point-in-time, surface-level scan: it inspects what it can fetch, so cloaked or login-gated payloads may be missed. Confirm compromise verdicts with a second scanner (e.g. `[[zscaler-zulu-url-risk-analyzer]]`).
- Its core business is paid removal/monitoring — the free scanner is the OSINT-relevant part; don't expect a full paid-grade audit for free.
- **Passive** (scan runs from eVuln's infra), but the submitted domain is retained by a third party.

## Overlaps ("do both")
- Pairs with `[[zscaler-zulu-url-risk-analyzer]]` and other URL-reputation scanners — cross-checking two engines resolves false positives/negatives on a compromise call.

## Trust & verifiability
`trust: unverified` — a small commercial vendor's free tool; treat a hit as a lead to corroborate and a clean result as non-conclusive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | evuln |
