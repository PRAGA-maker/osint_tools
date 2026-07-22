---
id: oralyzer
name: Oralyzer
description: Use when you have a `domain`/URL with redirect parameters and want to test for open-redirect flaws — returns which parameters are exploitable.
url: https://github.com/r0075h3ll/Oralyzer
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Probing a target URL for open-redirect vulnerabilities (header/JavaScript/meta-based) and CRLF injection during infrastructure/security assessment.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source (GPL-3.0).
opsec: active
opsecNote: This actively sends crafted requests to the target site to test redirect behaviour — it WILL appear in the target's logs as fuzzing traffic. Only run against systems you are authorised to test; use attributable-safe infrastructure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source security script (800+ GitHub stars, GPL-3.0); code is auditable but it is offensive tooling — use only with authorisation.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Oralyzer open redirect
tags:
- Domain/IP/Links
- open-redirect
- web-security
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
---

# Oralyzer

> A small Python CLI that fuzzes a URL's redirect parameters to find open-redirect and CRLF-injection flaws.

## When to use
You are assessing the security posture of a `domain`/web app you are authorised to test and want to check whether its redirect parameters can be abused to bounce users to an attacker-controlled site (open redirect) or to inject CRLF. This is offensive security tooling, adjacent to OSINT infrastructure work rather than person-finding.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo (`github.com/r0075h3ll/Oralyzer`) and `pip3 install -r requirements.txt`.
2. Run against a target URL with redirect parameters; it can also pull archived URLs from web.archive.org to find likely-vulnerable parameters.
3. Read the output: it flags header-based, JavaScript-based and meta-tag-based redirects and CRLF injection points.
4. Confirm any finding manually before reporting — automated fuzzers produce false positives.
5. Pivot: a confirmed open redirect on a `domain` is a phishing-abuse risk to document.

## Inputs → Outputs
- **In:** a target `domain`/URL (with parameters)
- **Out:** list of exploitable redirect parameters / CRLF points on that `domain`
- **Empty/negative result looks like:** no vulnerable parameters reported — the endpoint appears safe against the tested vectors (not a guarantee of overall security).

## Gotchas & OpSec
- **Active and authorised-use-only:** it sends fuzzing requests that show up in the target's logs; testing systems you don't own may be illegal.
- Expect false positives; verify by hand.
- OpSec: run from infrastructure you're willing to attribute to the engagement.

## Overlaps ("do both")
- Overlaps with broader web-vuln scanners and with archived-URL discovery tools (it uses the Wayback Machine to source candidate parameters).

## Trust & verifiability
`trust: community` — well-known, auditable GPL-3.0 script, but it is offensive tooling; only the presence of a vulnerability it confirms is meaningful, and only against authorised targets.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | oralyzer |
