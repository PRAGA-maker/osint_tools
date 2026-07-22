---
id: heartbleed-check
name: Heartbleed Check
description: Use when you have a `domain`/host and want to test whether its TLS server is vulnerable to the Heartbleed bug (CVE-2014-0160) — returns a vulnerable/not-vulnerable verdict.
url: https://osint.sh/heartbleed/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: A quick web check of whether a target host's SSL/TLS is still exposed to the Heartbleed memory-leak vulnerability.
selectorsIn:
- domain
selectorsOut: []
status: live
pricing: free
costNote: Free web tool, part of the osint.sh free toolset; no account.
opsec: active
opsecNote: This actively connects to the target host and sends a TLS heartbeat probe — the target's server logs a connection from the scanner (osint.sh), and probing hosts you are not authorised to test may be unlawful. Only test infrastructure you own or are permitted to assess.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: One of the osint.sh free utilities; the verdict is a live technical test and independently reproducible with other Heartbleed checkers.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- osint.sh heartbleed
- Heartbleed test
tags:
- ssl
- vulnerability-check
source: osint4all
lastVerified: '2026-07-22'
enrichment: full
---

# Heartbleed Check

> A one-field web test (from the osint.sh toolset) that probes a host's TLS server for the Heartbleed bug (CVE-2014-0160) and tells you whether it can leak memory.

## When to use
You're assessing the security posture of a host tied to your investigation or your own infrastructure and want to know if its SSL/TLS is still vulnerable to Heartbleed — the 2014 OpenSSL flaw that leaks server memory (keys, session tokens) to an attacker. A positive result is a strong signal of an unpatched, poorly maintained server.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://osint.sh/heartbleed/.
2. Enter the target `domain`/host and run the check.
3. Read the verdict: vulnerable (the server answered the malformed heartbeat) or not vulnerable/patched.
4. Confirm a positive with a second checker before relying on it.
5. Pivot: a vulnerable host suggests an under-maintained target — combine with other osint.sh utilities (DNS, WHOIS, ports) to profile the infrastructure.

## Inputs → Outputs
- **In:** a `domain`/host (TLS server)
- **Out:** a Heartbleed vulnerable / not-vulnerable verdict
- **Empty/negative result looks like:** "not vulnerable" (patched or unaffected), or an error if the host has no TLS service on the tested port — an error is a reachability issue, not a clean bill of health.

## Gotchas & OpSec
- **Active test with legal scope:** it sends a real probe to the target; only test hosts you own or are authorised to assess.
- Heartbleed is largely patched across the internet today, so expect mostly "not vulnerable" — a hit flags a genuinely neglected server.
- OpSec: the connection comes from osint.sh's scanner, but you initiated an active probe — this is not a passive lookup.

## Overlaps ("do both")
- Complements broader SSL/TLS scanners (e.g. SSL Labs, sslyze) and the rest of the osint.sh toolset — those give a full TLS posture, this is a fast single-vuln check.

## Trust & verifiability
`trust: community` — a free single-purpose utility; the result is a reproducible technical test you can confirm against any other Heartbleed checker.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | heartbleed-check |
