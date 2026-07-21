---
id: islegitsite
name: IsLegitSite
description: Use when you have a `domain` and want a quick trust/scam assessment of a website — returns reputation, blocklist status, and HTTPS/popularity signals about the domain.
url: https://www.islegitsite.com/
category: search-engines
path:
- search-engines
bestFor: A fast first-pass legitimacy/scam check on a website domain a subject is linked to.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free to use; no account required.
opsec: active
opsecNote: Submitting a domain sends it to IsLegitSite's "Site Trustworthiness API", and their terms state submitted data is shared with security companies. Do NOT submit a domain that would itself reveal your investigation (e.g. a private or target-controlled host) unless you accept it may be logged/shared. Checking well-known public domains is low-risk.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party aggregator that composes reputation, blocklist, and popularity signals; its verdicts are heuristic, not authoritative, and it monetizes via ads/affiliates.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Is Legit Site
- islegitsite.com
tags:
- speciality-search-engines
- scam-check
- website-reputation
source: awesome-osint
lastVerified: '2026-07-21'
enrichment: full
---

# IsLegitSite

> A one-box website legitimacy checker that rolls up reputation, blocklist, HTTPS, and popularity signals into a quick "is this site trustworthy?" verdict.

## When to use
You have a `domain` that appears in an investigation — a site a subject linked to, a store they claim to run, a page in a message or profile — and you want a fast, low-effort read on whether it looks legitimate or scammy before spending time on it. Treat it as a triage signal, not a verdict: it helps you decide whether a domain is worth deeper WHOIS/DNS/infra work.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.islegitsite.com/ and paste the `domain` (or URL) into the "Check Website" box.
2. Read the composite report: online-reputation assessment, blocklist status, HTTPS/connection details, popularity/traffic rank, and any user comments/reviews.
3. Interpret conservatively — a "looks fine" result is not proof of legitimacy, and a "suspicious" result is a reason to dig, not a conclusion.
4. Pivot: hand the domain to authoritative infra tools (WHOIS, DNS history, certificate transparency, hosting lookups) for the real analysis; use IsLegitSite only to prioritize.

## Inputs → Outputs
- **In:** `domain` (or full URL)
- **Out:** `domain` reputation/trust signals — blocklist status, HTTPS, popularity rank, user reviews
- **Empty/negative result looks like:** little or no data for an obscure/new domain (thin popularity and no reviews), which is itself a mild signal but not a judgment. Don't read "no data" as "safe."

## Gotchas & OpSec
- Human-in-the-loop: none.
- Verdicts are heuristic and partly derived from third-party feeds; the site also carries ads/affiliate content, so weigh its output accordingly.
- OpSec: **active** in the sense that submitted domains are shared with security partners per their terms — avoid submitting a domain whose lookup would expose your target or your operation.

## Overlaps ("do both")
- Pairs with authoritative infrastructure tools — WHOIS, DNS/passive-DNS history, and certificate-transparency search — which give you the real ownership/hosting picture that a heuristic scam-checker only gestures at.

## Trust & verifiability
`trust: community` — an unofficial third-party aggregator. Its individual inputs (blocklists, HTTPS, popularity) are real, but the rolled-up "legit or not" score is heuristic. Use it to triage, confirm with primary infrastructure data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | islegitsite |
| category | search-engines |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
