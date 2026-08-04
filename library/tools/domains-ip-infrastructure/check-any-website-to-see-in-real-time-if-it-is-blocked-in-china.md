---
id: check-any-website-to-see-in-real-time-if-it-is-blocked-in-china
name: Check if a Website is Blocked in China (vpnMentor)
description: Use when you have a `domain` and want to know if it's reachable from mainland China — returns a real-time accessible/blocked verdict tested from Chinese nodes.
url: https://www.vpnmentor.com/tools/test-the-great-china-firewall/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Checking in real time whether a site is censored by China's Great Firewall.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free web tool from vpnMentor; no account.
opsec: passive
opsecNote: The test is run from vpnMentor's China-side nodes against the target domain — not from your IP — so your own location isn't exposed to the site. You do submit the domain of interest to vpnMentor, so avoid checking domains that would reveal a sensitive lead.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A convenience tool by vpnMentor (a VPN-review publisher); results reflect a point-in-time check from their vantage points, and GFW behaviour varies by region/time.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Great Firewall of China test
- vpnMentor China block checker
tags:
- Domain/IP/Links
- Domain/IP investigation
- censorship
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Check if a Website is Blocked in China (vpnMentor)

> Enter a domain and it tests, in real time from Chinese vantage points, whether the Great Firewall is blocking it — an accessibility signal, not a person lookup.

## When to use
You have a `domain` and want to know whether it is censored in mainland China. Useful for context on a site's reach and audience, for understanding why a China-based source can't see something, or as a data point about how a platform is treated by the GFW. It returns infrastructure/censorship state, not information about any individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.vpnmentor.com/tools/test-the-great-china-firewall/.
2. Enter the target `domain`.
3. Run the check — it probes the site from China-side nodes and reports **accessible** or **blocked**.
4. Re-test over time/other checkers if it matters: GFW blocking varies by province, ISP, and moment, so one verdict is a snapshot.
5. Pivot: a "blocked" result explains gaps in China-sourced coverage; an "accessible" result means China-based OSINT sources could plausibly reach it.

## Inputs → Outputs
- **In:** `domain`
- **Out:** `domain` accessibility verdict (accessible / blocked in China) at test time
- **Empty/negative result looks like:** an inconclusive/timeout result — meaning the checker's node couldn't complete the test, not a definitive "accessible"; retry or use a second GFW checker.

## Gotchas & OpSec
- GFW blocking is inconsistent across regions and time — treat a single verdict as a snapshot, corroborate with another checker for anything important.
- The test runs from vpnMentor's nodes, not yours; that protects your location but means you rely on their vantage point.
- You reveal the domain to vpnMentor — fine for most cases, but consider it before probing a sensitive lead.

## Overlaps ("do both")
- Complements other censorship/reachability checkers — cross-test a domain on a second GFW tool when the result drives a decision.

## Trust & verifiability
`trust: community` — a convenient publisher-run tool; because GFW behaviour is variable, verify a critical verdict with an independent China-reachability check.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | check-any-website-to-see-in-real-time-if-it-is-blocked-in-china |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
