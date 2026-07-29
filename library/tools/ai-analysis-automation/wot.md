---
id: wot
name: WOT (Web of Trust)
description: Use when you have a `domain` and want a quick reputation/safety read on it — returns a community + ML trust score flagging phishing, malware, or scam sites.
url: https://www.mywot.com
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A fast reputation check on a website's trustworthiness before visiting or citing it.
selectorsIn:
- domain
selectorsOut: []
status: live
pricing: freemium
costNote: Free website checks and the browser extension; premium tiers add extra protection features.
opsec: passive
opsecNote: Looking up a domain's reputation queries WOT's dataset, not the target site — the site owner isn't notified. The browser extension, however, sees the URLs you visit and sends them to WOT for rating; if that telemetry is a concern, use the website's manual lookup instead of the always-on extension.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: WOT ratings blend community reviews with ML/blacklists; useful as a heuristic, but community scoring can be gamed and has drawn past privacy criticism over its extension's data handling.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- getlinkinfo
- urlscan-io
- web-of-trust
aliases:
- WOT
- Web of Trust
- mywot
tags:
- website-reputation
- safety
- domain
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# WOT (Web of Trust)

> A crowd-plus-ML website reputation service — get a quick trust/safety read on a domain (phishing, malware, scam flags) before you visit or rely on it.

## When to use
You have a `domain` and want a fast heuristic on whether it's trustworthy — is it a known phishing/scam/malware host, or generally reputable? Handy when triaging a link tied to a subject (a site in their bio, a shop, a sketchy landing page) to decide how much caution a visit warrants and whether to trust content there. It's a reputation heuristic, not evidence — it returns a score, not facts about a person.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Manual: open https://www.mywot.com and enter the `domain` to see its reputation score and category flags.
2. Or install the WOT browser extension (Chrome/Firefox/Edge/etc.) for inline safety icons next to search results and on sites as you browse.
3. Read the verdict: overall trust level plus flags (phishing, malware, scam, adult, etc.) and any community reviews.
4. Treat a bad score as a caution flag — inspect the site in a sandbox (`[[urlscan-io]]`) rather than a real browser.
5. Prefer the manual lookup if you don't want the extension reporting your browsing to WOT.

## Inputs → Outputs
- **In:** `domain`
- **Out:** reputation/trust score + category flags (phishing/malware/scam/etc.), community reviews
- **Empty/negative result looks like:** "no rating" for low-traffic/new domains — absence of a score is not a clean bill; fall back to an active scan.

## Gotchas & OpSec
- **Heuristic, not proof:** community scoring can be manipulated; a good or missing score doesn't guarantee safety.
- **Extension privacy:** the add-on transmits visited URLs to WOT (a point of past criticism) — use the website lookup if that telemetry concerns you.
- OpSec: **passive** for manual lookups; the extension is a mild self-leak.

## Overlaps ("do both")
- Pairs with `[[getlinkinfo]]` and `[[urlscan-io]]` — WOT gives a reputation *opinion*; GetLinkInfo reveals where a link goes; urlscan.io does the deep sandboxed analysis. Use WOT as a first-glance flag, then a scanner for anything questionable.

## Trust & verifiability
`trust: community` — a real, widely-used service, but its score is a crowd/ML heuristic that can be gamed; corroborate a verdict with an active scanner before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wot |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain →  |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
