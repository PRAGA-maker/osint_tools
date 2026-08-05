---
id: lfitester
name: LFITester
description: Use when you have a `domain`/URL and are authorised to test it for Local File Inclusion — returns detected LFI vulnerabilities and (optionally) proof-of-concept file reads.
url: https://github.com/kostas-pa/LFITester
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Detecting (and, with authorisation, exploiting) Local File Inclusion vulnerabilities on a target web app.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Open source under GPL-3.0; free Python 3 CLI.
opsec: active
opsecNote: This sends crafted attack payloads directly to the target server, which are logged and may trigger WAF/IDS alerts. Its autopwn/RCE features are genuinely intrusive. Only run against systems you have explicit written authorisation to test; route through controlled infrastructure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: An open-source offensive-security script; auditable, but an attack tool — use only within an authorised engagement and expect false positives to need manual confirmation.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- LFITester
tags:
- Domain/IP/Links
- Dorks/Pentest/Vulnerabilities
- lfi
- web-app-testing
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# LFITester

> A Python CLI that automates finding — and, on request, exploiting — Local File Inclusion flaws in a web app: path traversal, PHP-filter reads, and log/session/wrapper-based RCE.

## When to use
Strictly an authorised-testing tool. When you are assessing infrastructure tied to an investigation (a subject's own server, an org you are permitted to test) and need to know whether it leaks local files via LFI, LFITester probes candidate parameters and reports which are exploitable. It targets infrastructure, not people, and its intrusive modes require explicit permission.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/kostas-pa/LFITester` and install (Python 3).
2. Point it at a target URL/parameter (single or batch), optionally supplying cookies, headers, credentials, or a Burp packet; it can crawl to find candidate endpoints.
3. Run detection first: it reports parameters vulnerable to path traversal / PHP-filter inclusion.
4. Only with authorisation, escalate to exploitation modes (log poisoning, session/wrapper RCE, autopwn reverse shell) — these are real attacks.
5. Pivot: a confirmed LFI (e.g. reading `/etc/passwd`, config files) feeds deeper infrastructure/identity findings within the engagement scope.

## Inputs → Outputs
- **In:** target `domain`/URL and parameters (plus optional auth/headers)
- **Out:** LFI detection results and, in exploit mode, retrieved file contents or a shell
- **Empty/negative result looks like:** no vulnerable parameter found — either the app is not LFI-vulnerable or the injection point/bypass was missed; confirm manually before concluding it is clean.

## Gotchas & OpSec
- Human-in-the-loop: none in automation, but you must scope targets and choose whether to run exploitation.
- OpSec: **active and loud** — payloads hit the target's logs and may trip WAF/IDS. The autopwn/RCE features cross from testing into intrusion; use only under written authorisation.
- Automated detection yields false positives/negatives — verify each finding by hand.

## Overlaps ("do both")
- Pairs with broader recon like [[ashok]] and content-discovery tools — those map the app's surface and parameters, LFITester tests a specific class of flaw on that surface; do both within an authorised assessment.

## Trust & verifiability
`trust: community` — open source and auditable, but an offensive tool whose results (especially detection) need manual confirmation. Its ethical/legal use is bounded entirely by having authorisation for the target.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lfitester |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
