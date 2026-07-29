---
id: hexometer-stack-checker
name: Hexometer stack checker
description: Use when you have a `domain` and want to fingerprint the site's technology stack — returns the CMS, frameworks, analytics IDs and third-party services as pivot points.
url: https://hexometer.com/stack-checker
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Enumerating the CMS, JS frameworks, analytics/tracking IDs and hosting services behind a website for infrastructure pivoting.
selectorsIn:
- domain
selectorsOut:
- domain
- employer-org
status: degraded
pricing: freemium
costNote: The standalone "stack checker" page now redirects to Hexomatic (hexomatic.com), where tech-stack discovery runs as a workflow automation. A free Hexomatic account exists but credits/scans are limited on the free tier; heavy or bulk use is paid.
opsec: passive
opsecNote: A single stack lookup is passive against the target — the scan hits the site's public pages once, indistinguishable from a normal visit; route through a VPN if you want to avoid your IP appearing in the target's logs. Building a Hexomatic workflow means your query is stored in a third-party SaaS account, so use a sock-puppet registration.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Hexact Inc. commercial product (Hexometer/Hexomatic); tech detection is reliable but the free "instant checker" branding has been folded into a paywalled automation platform, so treat it as one detector among several.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Hexomatic tech stack discovery
- Hexometer technology lookup
tags:
- Domain/IP/Links
- Website technology look up
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# Hexometer stack checker

> A website technology fingerprinter — now part of Hexomatic — that reveals the CMS, frameworks, analytics IDs and third-party services a domain runs on.

## When to use
You have a `domain` and want to know what it is built on: CMS (WordPress/Shopify/etc.), JavaScript frameworks, CDN, hosting, and — most useful for OSINT — embedded **analytics/tracking IDs** (Google Analytics `UA-`/`G-`, AdSense, Facebook Pixel). A shared tracking ID is a strong link between otherwise unrelated sites owned by the same person or org, which is the real pivot value here.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://hexometer.com/stack-checker — it now redirects to Hexomatic's "Discover tech stack" automation.
2. Sign in with a sock-puppet Hexomatic account (free tier) and enter the target `domain` (or upload a CSV for several).
3. Run the scan and read the detected stack: CMS, front-end libraries, server/hosting, and tracking/analytics identifiers.
4. Note any analytics/pixel IDs — feed those into a reverse-analytics tool to find sibling domains sharing the same ID (the same-owner pivot).
5. Cross-check with a second detector (results and paywall behavior vary) before relying on a single reading.

## Inputs → Outputs
- **In:** `domain`
- **Out:** technology list (CMS/frameworks/hosting), analytics/tracking IDs; those IDs pivot to related `domain`s and sometimes an `employer-org`
- **Empty/negative result looks like:** a bare or generic stack (just a CDN + generic server) with no CMS or tracking IDs — common for static/hardened sites and gives no pivot.

## Gotchas & OpSec
- Human-in-the-loop: the free instant lookup is gone; you must register on Hexomatic, and the free tier is credit-limited.
- OpSec: passive against the target (one page fetch), but your query lives in a third-party SaaS account — use a throwaway registration.
- Detection is heuristic; obfuscated or server-rendered stacks can be under-reported.

## Overlaps ("do both")
- Pairs with reverse-analytics/same-owner tools — this finds the tracking ID, those turn the ID into a list of co-owned domains. Also complements WHOIS and passive-DNS infrastructure lookups.

## Trust & verifiability
`trust: community` — a competent commercial detector, but tech fingerprinting is inherently probabilistic and the free access has been narrowed, so corroborate the stack with an independent tool before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hexometer-stack-checker |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
