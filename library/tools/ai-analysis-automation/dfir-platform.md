---
id: dfir-platform
name: DFIR Platform
description: Use when you have an `email`, `domain` or `ip-address` (or a suspicious message) and want automated enrichment/verdicts — returns IOC reputation, phishing/BEC analysis and exposure signals.
url: https://platform.dfir-lab.ch
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: API-first triage of phishing/BEC and indicator enrichment (IPs, domains, emails) aggregated from many threat-intel sources.
selectorsIn:
- email
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: Free tier ~100 credits/month plus a welcome bonus; no credit card. A no-signup browser playground gives ~10 sandbox credits/week. Higher volume is paid.
opsec: active
opsecNote: Submitting an indicator sends it to a third-party Swiss service and onward to 14+ intel providers, which may log/redistribute it. Do not submit sensitive case indicators you need to keep confidential; use a dedicated API key.
humanInLoop: true
humanInLoopReason:
- account-login
- api-key
bestInteractionPattern: api
trust: community
trustNote: Run by DFIR Lab (Swiss); enrichment is aggregated from external feeds, so verdicts inherit those sources' accuracy and should be corroborated.
missingPersonsRelevance: low
coverage:
- global
auth: api-key
api: true
localInstall: false
registration: true
aliases:
- DFIR Lab Platform
- platform.dfir-lab.ch
tags:
- threat-intelligence
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# DFIR Platform

> An API-first incident-response toolkit that enriches indicators (IPs, domains, emails) and scores phishing/BEC — useful for infrastructure/email triage, tangential to person-finding.

## When to use
You have an `email`, `domain`, or `ip-address` — or a suspicious message — tied to your case (e.g. a scam contact, a phishing lure, an unknown sender) and want a fast automated verdict plus enrichment aggregated from many threat-intel feeds. It answers "is this infrastructure malicious / what is known about it", not "who is this person".

## How to use it (`bestInteractionPattern`: api)
1. Sign up at https://platform.dfir-lab.ch for a free-tier API key (no card), or try the no-signup browser playground for a few sandbox credits.
2. Call the relevant REST endpoint with your indicator (IOC enrichment, phishing analysis, BEC/email investigation, exposure scan).
3. Read the JSON verdict and the per-source enrichment (reputation, related domains/IPs, categories).
4. Pivot the enriched `domain`/`ip-address` into WHOIS, passive DNS, or breach-lookup tools for attribution.

## Inputs → Outputs
- **In:** `email`, `domain`, `ip-address`, or a raw phishing message
- **Out:** IOC reputation/verdict, related `domain`/`ip-address` enrichment
- **Empty/negative result looks like:** "no threat-intel hits / benign" — means nothing malicious is known, not that the indicator is unrelated to your subject.

## Gotchas & OpSec
- Human-in-the-loop: account + API key required for anything beyond the small sandbox.
- OpSec: **active** — your indicator is shared onward to 14+ providers; never submit a confidential case selector you cannot afford to have logged/redistributed.
- Credits are limited on the free tier; batch thoughtfully.

## Overlaps ("do both")
- Complements dedicated WHOIS/passive-DNS and email-breach tools: DFIR Platform gives a fast aggregated verdict, those give the primary records you cite.

## Trust & verifiability
`trust: community` — a legitimate Swiss DFIR service, but verdicts are aggregated from external feeds; corroborate any actioned result against a primary source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dfir-platform |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | email, domain, ip-address → domain, ip-address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | api |
| opsec | active |
| human-in-loop | yes (account-login, api-key) |
