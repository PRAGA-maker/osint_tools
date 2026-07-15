---
id: agora-pulse
name: Agora Pulse
description: Use when you have a Facebook Page you control/administer and want to benchmark its reach/engagement against similar pages — returns comparative analytics, not target intel.
url: https://barometer.agorapulse.com
category: social-networks
path:
- social-networks
bestFor: Benchmarking the performance of a Facebook Page you administer against thousands of comparable pages.
selectorsIn:
- social-profile
selectorsOut:
- social-profile
status: live
pricing: free
costNote: The Barometer is free but requires a Facebook Login and only analyses Pages your logged-in account administers — it cannot benchmark arbitrary third-party pages.
opsec: active
opsecNote: This requires logging in with a real Facebook account and grants Agorapulse access to your Page data, so it is attributable to whatever account you use — never your real identity. It only reads Pages you already administer, so it is NOT a way to investigate someone else's page; its investigative value is marginal.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Agorapulse is an established social-media-management vendor; the Barometer is a legitimate free marketing analytics tool, not an OSINT/target-research utility.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
relatedTools: []
aliases:
- Agorapulse Barometer
- Facebook Barometer
tags:
- facebook
source: metaosint
lastVerified: '2026-07-15'
enrichment: full
---

# Agora Pulse

> Agorapulse's free Facebook Barometer — a marketing benchmark for Pages *you* administer, of limited use for investigating other people.

## When to use
Reach for this only in the narrow case where you (or a sock-puppet you fully control) administer a Facebook Page and want to see how its reach, engagement and CTR compare against thousands of similar pages. It is a **marketing analytics** tool, not a target-research tool: it cannot pull data on a page you don't manage, so it does not help identify or locate a third party. Included for completeness under Facebook tooling, but for actual investigation of a subject's Facebook presence, use scraping/lookup tools instead.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://barometer.agorapulse.com.
2. Sign in with a Facebook account that administers the Page (use a controlled sock-puppet account, never your real identity).
3. Grant the requested Page-read permissions.
4. Read the heat-map benchmark: fans reached, engagement, viral/organic/paid reach, CTR and negative feedback vs comparable pages.

## Inputs → Outputs
- **In:** a Facebook Page `social-profile` you administer
- **Out:** comparative performance metrics for that Page (`social-profile` analytics)
- **Empty/negative result looks like:** nothing to benchmark if the login administers no Pages — the tool simply has no third-party data to show, which underlines why it isn't an investigative source.

## Gotchas & OpSec
- Hard limitation: it only sees Pages your login controls — it is **not** a way to analyse someone else's page.
- Human-in-the-loop: Facebook account login and permission grant are mandatory.
- OpSec: **active** — you authenticate and share Page data with a third-party vendor; only ever do this from a disposable, non-attributable account.

## Overlaps ("do both")
- For actually researching a *target's* Facebook footprint, ignore this and use dedicated Facebook OSINT/scraping tools; the Barometer only complements your own-page marketing work, not an investigation.

## Trust & verifiability
`trust: community` — a legitimate tool from an established SaaS vendor. The analytics are trustworthy for their intended marketing purpose; they simply aren't intelligence about other people.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | agora-pulse |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
