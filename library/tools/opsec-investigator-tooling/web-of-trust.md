---
id: web-of-trust
name: Web of Trust (WOT)
description: Use when you have a `domain` and want a crowd-sourced reputation read — returns community trust/safety ratings for the website.
url: https://www.mywot.com
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A quick crowd-sourced reputation/safety rating for a website, as one signal among several.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free browser extension and website reputation lookup; a paid tier exists for advanced/business features.
opsec: passive
opsecNote: Looking up a rating queries WOT's servers, not the target. Be aware of WOT's own history — the browser extension was found (2016) to collect and sell users' browsing data; if you install the extension, treat it as telemetry-bearing and prefer the website lookup or a sandboxed browser profile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Crowd-sourced ratings can be gamed or sparse, and WOT had a serious 2016 data-privacy scandal; useful as a rough signal, not authoritative.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- wot
aliases:
- WOT
- MyWOT
- mywot.com
tags:
- website-reputation
- crowdsourced
- browser-extension
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# Web of Trust (WOT)

> A crowd-sourced website reputation service: a quick community "is this site safe/trustworthy?" score — handy as a first sniff, but not to be leaned on.

## When to use
You have a `domain` and want a fast, rough reputation read before digging deeper — is this site widely reported as a scam, malware host, or otherwise untrustworthy? WOT aggregates community ratings and its own signals into a trust/safety score, surfaced via a website lookup or a browser extension that annotates search results and sites. It's a low-weight triage signal; missing-persons relevance is low and indirect (a rough first pass on a site tied to a case).

## How to use it (`bestInteractionPattern`: browser-extension)
1. Either look up a `domain` on https://www.mywot.com, or install the WOT browser extension to see ratings inline (see the OpSec caveat before installing).
2. Read the score: an overall trust/safety rating plus category flags and, sometimes, community comments explaining *why* a site is rated poorly.
3. Treat it as one input — a bad WOT score is a prompt to investigate, not a conclusion.
4. Pivot: corroborate with authoritative sources — Google Safe Browsing (`[[google-transparency-report]]`), VirusTotal, `[[alienvault-otx]]` — before acting on the reputation.

## Inputs → Outputs
- **In:** `domain`
- **Out:** crowd-sourced trust/safety rating and category flags for the site
- **Empty/negative result looks like:** no or few ratings — the site is too obscure to have been rated; a missing score says nothing about safety, and a *good* score can be the result of insufficient or manipulated ratings.

## Gotchas & OpSec
- **Reputation, not fact** — ratings are crowd-sourced and gameable; both false-good and false-bad scores occur.
- **Privacy history:** WOT's extension was caught selling users' browsing data in 2016. If you install it, assume it can see your browsing; prefer the web lookup or an isolated browser profile.
- Sparse coverage on niche/new domains.
- OpSec: the lookup itself is passive; the *extension* is a telemetry concern for you, not the target.

## Overlaps ("do both")
- Always pair with authoritative reputation sources — `[[google-transparency-report]]` (Safe Browsing), VirusTotal, `[[alienvault-otx]]` — which give evidence-based verdicts where WOT gives crowd opinion. See also the related `[[wot]]` entry.

## Trust & verifiability
`trust: community` — a crowd-sourced signal with a known privacy scandal and gameable ratings; use it to *flag* sites for scrutiny, never as the basis of a conclusion.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | web-of-trust |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
