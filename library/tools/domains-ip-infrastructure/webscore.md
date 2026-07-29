---
id: webscore
name: WebScore
description: Use when you have a `domain`/URL and want a fast legitimacy read (HTTPS, domain age, Wayback history, Safe Browsing) — returns basic trust signals for the site.
url: https://garvit835.github.io/WebScore/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: A quick, no-login trust/legitimacy check on a suspicious website.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free static web tool hosted on GitHub Pages; no account.
opsec: passive
opsecNote: Passive toward the subject — checks run against third-party services (domain WHOIS/age, Wayback, Google Safe Browsing), not by hitting the target site as the subject. Your query is seen by those upstream services.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Small community project; the authors explicitly call it "basic checks... not a guarantee of a website's safety."
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- webosint
aliases:
- garvit835 WebScore
tags:
- domain-and-ip-research
- website-legitimacy
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# WebScore

> A lightweight website-legitimacy checker that scores a URL on HTTPS, domain age, Wayback history and Google Safe Browsing.

## When to use
You have a `domain`/URL — a link from a scam message, a marketplace listing, a dubious fundraiser — and want a fast first-pass read on whether it looks legitimate. WebScore bundles a few basic signals (does it use HTTPS, how old is the domain, does it have Wayback history, is it flagged by Safe Browsing) into a single report so you can triage before deeper investigation.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://garvit835.github.io/WebScore/.
2. Enter the target website URL and run the scan.
3. Read the report across its criteria: HTTPS, domain age, Wayback Machine presence, Safe Browsing status.
4. Treat it as triage only — a "good" score is not proof of safety, and a young domain isn't proof of fraud.
5. Pivot: a suspicious result feeds a deeper look with `[[webosint]]`/WHOIS and manual Wayback review.

## Inputs → Outputs
- **In:** `domain`/URL
- **Out:** `domain` trust signals — HTTPS, domain age, Wayback history, Safe Browsing flag
- **Empty/negative result looks like:** partial results if an upstream check (e.g. Safe Browsing) is unavailable; a clean score that still warrants human judgement.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive; the checks hit third-party APIs, so those services see the domain you queried.
- It is deliberately "basic" — a small set of signals. Don't treat the score as a verdict; combine with other tools and judgement.

## Overlaps ("do both")
- Pairs with `[[webosint]]` — WebScore for a 10-second legitimacy triage, WEBOSINT for the full WHOIS/DNS/cert/subdomain workup once something looks off.

## Trust & verifiability
`trust: community` — a small community tool that surfaces third-party signals; its authors say it's not a safety guarantee, so verify each signal (WHOIS age, Wayback, Safe Browsing) at its source before concluding.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | webscore |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
