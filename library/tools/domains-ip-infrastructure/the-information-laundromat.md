---
id: the-information-laundromat
name: The Information Laundromat
description: Use when you have a `domain` (or article URL/text) and want to find other sites sharing its content or infrastructure — returns linked `domain`s and shared technical `ip-address`/tracker indicators.
url: https://informationlaundromat.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Uncovering networks of sites that republish the same content or share hidden technical fingerprints.
selectorsIn:
- domain
- ip-address
selectorsOut:
- domain
- ip-address
status: live
pricing: free
costNote: Free to use via the web interface; batch searches require a free registration code (email info@securingdemocracy.org).
opsec: passive
opsecNote: Queries run server-side against search engines, GDELT and the tool's own indicators — you never touch the target sites directly, so it is passive from the target's perspective. Your searches are logged by the operator (German Marshall Fund / ASD).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built and maintained by the German Marshall Fund's Alliance for Securing Democracy with the Institute for Strategic Dialogue and University of Amsterdam; a recognised disinformation-research group.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Information Laundromat
- ASD Information Laundromat
tags:
- bellingcat-toolkit
- websites
- disinformation
- infrastructure-analysis
source: bellingcat-toolkit
lastVerified: '2026-07-28'
enrichment: full
---

# The Information Laundromat

> A disinformation-research tool that reveals when separate websites share the same content or the same hidden technical fingerprints (analytics IDs, IPs, trackers).

## When to use
You have a suspicious `domain`, article, or image and want to know which *other* sites are connected to it — either because they repost the same text/image ("information laundering") or because they quietly share infrastructure (a common Google Analytics ID, ad-network code, or `ip-address`). Useful for mapping coordinated site networks around a person, campaign, or narrative.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://informationlaundromat.com.
2. Choose a mode:
   - **Content similarity** — paste a URL, article title, or text snippet; it searches engines + GDELT + plagiarism tools for reposts.
   - **Domain forensics** — enter one or more `domain`s; it extracts and cross-matches technical indicators (Analytics/AdSense IDs, IPs, tracker fingerprints).
   - **Image similarity** — paste an image URL for reverse-image matches.
3. Read the results: a 0–100% match score, a list of similar content/URLs, and a table of shared indicators across domains.
4. Pivot: shared indicators feed WHOIS/passive-DNS tools and reverse-analytics lookups; matched reposts feed source-tracing.

## Inputs → Outputs
- **In:** `domain` / article URL / text snippet / image URL / `ip-address`
- **Out:** linked `domain`s, shared technical indicators (`ip-address`, analytics/tracker IDs), content-match scores
- **Empty/negative result looks like:** no shared indicators found and low content-similarity scores — treat as "no detectable link," not proof of independence (sites can hide indicators).

## Gotchas & OpSec
- Batch/domain-forensics searches need a free registration code from the operator; single lookups work without it.
- Match scores are heuristic — a high content score can just mean both sites syndicated the same wire story; corroborate before claiming coordination.
- Indicator overlaps are strong leads but can be coincidental (shared CDN, shared ad network); verify the specific ID is truly unique.

## Overlaps ("do both")
- Pairs with passive-DNS and reverse-analytics tooling — the Laundromat surfaces the shared IDs/IPs, and those tools expand each indicator into the full set of sites using it.

## Trust & verifiability
`trust: trusted` — maintained by an established disinformation-research consortium (GMF/ASD, ISD, University of Amsterdam); methodology is documented and the operator is accountable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-information-laundromat |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, ip-address → domain, ip-address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
