---
id: determines-if-website-is-not-comply-with-eu-cookie-law-and-gives-you-insight-about-cookies-installed-from-website-before
name: Determines if website is not comply with EU Cookie Law and gives you insight about cookies installed from website before
description: Use when you have a `domain` and want to see what cookies and trackers it sets before consent — returns the site's cookie/tracker inventory and third-party services.
url: https://www.cookiemetrix.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Auditing a website's cookies and third-party trackers to reveal the services and analytics IDs behind it.
selectorsIn:
- domain
selectorsOut:
- domain
- device-id
status: live
pricing: freemium
costNote: A limited number of scans are free (no signup for a quick check); higher volume and project features require a paid PRO plan.
opsec: passive
opsecNote: CookieMetrix fetches the target site from its own servers, so the scan does not come from your IP and the site owner sees a scanner visit, not you. Prefer this over loading the site yourself when you want to enumerate trackers without a direct visit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Commercial compliance-scanning service; the cookie/tracker inventory it reports is directly observed from the site, so it is factual, though presented for a legal-compliance audience rather than investigators.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- cookiemetrix
- cookie metrix
tags:
- Domain/IP/Links
- Cookies analyze
- trackers
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Determines if website is not comply with EU Cookie Law and gives you insight about cookies installed from website before

> CookieMetrix scans a website and lists every cookie and tracker it drops — a fast way to surface the third-party services, analytics and ad IDs wired into a `domain`.

## When to use
You are attributing or profiling a `domain` and want to know what runs underneath it: which analytics/advertising/tag-manager services it uses, and any tracking identifiers embedded in its cookies. Shared analytics or ad IDs (e.g. the same Google Analytics/AdSense tag across sites) are a classic pivot for linking multiple sites to one operator; CookieMetrix surfaces those cookies without you loading the page yourself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.cookiemetrix.com/.
2. Enter the target `domain`/URL and run a scan.
3. Read the report: the list of cookies set (name, provider, purpose, expiry) and the third-party services/trackers loaded before consent.
4. Note any embedded IDs (`device-id`/tag identifiers such as UA-/G-/pub- codes) — these are the values to cross-reference across other sites.
5. Pivot: feed a shared analytics/ad ID into a reverse-tracker lookup or code-search engine (`[[source-code-search-engine-315-million-domains-indexed-search-by-title-metadata-javascript-files-server-name-locat]]`) to find sibling domains run by the same operator.

## Inputs → Outputs
- **In:** a `domain`/URL
- **Out:** cookie & tracker inventory; third-party services; embedded tracking `device-id`s/tag ids
- **Empty/negative result looks like:** a site that sets no cookies/trackers, or a scan blocked by the free-tier credit limit — for the latter, retry later or use a browser devtools/`site: source` check instead.

## Gotchas & OpSec
- Free tier is credit-limited; heavy use hits a PRO paywall.
- It reports what the site served at scan time; consent-gated or geo-varying tags may differ from what you'd see elsewhere.
- Passive and indirect: the scan originates from CookieMetrix, not you — an advantage when you want tracker data without a direct visit.

## Overlaps ("do both")
- Pairs with a source-code/tracker search engine — CookieMetrix reveals *which* IDs a site uses; a code-search engine finds *other* sites using the same ID, so together they build the operator's footprint.

## Trust & verifiability
`trust: community` — a commercial compliance scanner; the observed cookie/tracker list is factual (directly measured), but it's framed for legal audits, so extract the raw IDs and verify pivots independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | determines-if-website-is-not-comply-with-eu-cookie-law-and-gives-you-insight-about-cookies-installed-from-website-before |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, device-id |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
