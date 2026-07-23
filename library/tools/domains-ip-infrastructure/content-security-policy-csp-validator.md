---
id: content-security-policy-csp-validator
name: Content Security Policy (CSP) Validator
description: Use when you have a `domain` or URL and want to inspect and validate its Content-Security-Policy and other security headers — returns header findings and misconfiguration warnings.
url: https://cspvalidator.org/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Checking a site's CSP and security headers for weaknesses (XSS, clickjacking) and fingerprinting how it is configured.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free web tool; no account required.
opsec: active
opsecNote: Fetching the target URL through the validator issues a real HTTP request to the site from the validator's servers (not your IP), so your address is masked, but the request still appears in the target's logs as validator traffic. You can also paste raw headers instead of a live URL to stay fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open community tool for CSP analysis; parses and grades headers deterministically, so results are reproducible even though the operator is not a formal authority.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- cspvalidator.org
- CSP Validator
tags:
- headers
- csp
- web-security
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# Content Security Policy (CSP) Validator

> A web tool that parses a site's Content-Security-Policy (and related security headers) and flags misconfigurations.

## When to use
You have a `domain` or specific URL and want to understand how the site is hardened — which security headers it sets, whether its CSP is permissive enough to allow XSS or clickjacking, and what that implies about the operator's sophistication. In an OSINT context this is a low-noise way to fingerprint a site's configuration and spot weak or copy-pasted policies that link related properties.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cspvalidator.org/.
2. Enter the target URL (the validator fetches it server-side), or paste the raw `Content-Security-Policy` header text to analyze it without touching the target.
3. Submit and read the parsed directive-by-directive breakdown.
4. Note warnings — `unsafe-inline`, wildcard sources, missing `frame-ancestors`, absent HSTS, etc.
5. Pivot: a distinctive or reused CSP/header fingerprint can tie one `domain` to others run by the same operator.

## Inputs → Outputs
- **In:** `domain`/URL, or pasted header text
- **Out:** parsed CSP directives, security-header findings, and misconfiguration warnings
- **Empty/negative result looks like:** "no CSP present" — many sites set none at all; that's a finding (weak posture), not a tool error.

## Gotchas & OpSec
- Live-URL mode fetches from the validator's servers, so your IP is hidden — but paste raw headers for a fully passive check.
- It grades policy syntax, not runtime behavior; a "valid" CSP can still be bypassable in practice.

## Overlaps ("do both")
- Pairs with broader header/security scanners and TLS-certificate tools — do both to correlate a site's header fingerprint, certificate, and hosting into an operator profile.

## Trust & verifiability
`trust: community` — an open, deterministic parser; findings are reproducible and can be re-checked by reading the headers yourself with `curl -I`.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | content-security-policy-csp-validator |
