---
id: expandurl
name: ExpandURL
description: Use when you have a shortened or suspicious `domain`/link and want its true final destination and redirect chain without clicking it — returns the resolved URL, HTTP hops, page title and a screenshot.
url: https://www.expandurl.net/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Safely unmasking where a bit.ly/t.co/goo.gl-style short link really goes, plus the full redirect chain, before any human clicks it.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free URL expander; no account required. Offers Chrome/Firefox/Edge extensions. Reports 11M+ links checked.
opsec: passive
opsecNote: ExpandURL's servers do the fetching, so the destination site sees ExpandURL's infrastructure, not you or your target — that indirection is the whole point and keeps you passive. Note that you are disclosing the link you're investigating to ExpandURL; don't submit links that themselves leak sensitive case detail.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Independent free service; actively maintained (2026 blog posts, browser extensions) but unaudited. Cross-check any high-stakes verdict against a second unshortener.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- unshorten-it
- redirect-detective
- urlscan-io
aliases:
- expandurl.net
- URL expander
- link unshortener
tags:
- url-expander
- unshortener
- bookmarklet
- link-analysis
source: sinwindie-osint
lastVerified: '2026-07-29'
enrichment: full
---

# ExpandURL

> A free link-unmasker: paste a short/suspicious URL and get its final destination, the full redirect chain with status codes, the page title, and a live screenshot — all without you ever loading the link.

## When to use
Someone in your investigation shared a shortened link (bit.ly, t.co, tinyurl, a tracking redirector) and you need to know where it actually lands — and whether it's a phishing/malware trap — before you or the subject clicks. ExpandURL resolves the whole hop chain server-side and shows you a screenshot of the endpoint, so you learn the destination `domain` and see the page without touching it yourself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.expandurl.net/ and paste the shortened/suspicious URL into the box (or use the bookmarklet form `https://www.expandurl.net/expand?&url=<link>`, or the Chrome/Firefox/Edge extension).
2. Submit; read the results:
   - **Final destination** — the real landing `domain`/URL.
   - **Redirect chain** — every hop with its HTTP status code (spot cloaking/tracking layers).
   - **Page title + description + screenshot** — a preview of the endpoint without loading it locally.
3. Judge safety from the chain and screenshot (unexpected domain, login-lookalike page, mismatched title = red flag).
4. Pivot: feed the resolved `domain` into `[[urlscan-io]]` or a WHOIS/passive-DNS tool for deeper infrastructure analysis, or `[[virustotal]]` for reputation.

## Inputs → Outputs
- **In:** `domain`/URL (a shortened or redirecting link).
- **Out:** final `domain`/URL, full redirect chain with status codes, page title/description, endpoint screenshot.
- **Empty/negative result looks like:** an error or a single-hop "already a direct link" result (nothing to expand), or a dead/timed-out destination (the short link points nowhere).

## Gotchas & OpSec
- Human-in-the-loop: none — it's fully automated.
- OpSec: **passive** — ExpandURL fetches on your behalf, so the destination host never sees your IP. You do reveal the link to ExpandURL; avoid submitting URLs whose query strings embed sensitive tokens or case identifiers.
- A screenshot is a point-in-time render; cloaking pages can show different content to different visitors, so treat the preview as indicative, not definitive.

## Overlaps ("do both")
- Pairs with `[[urlscan-io]]` — urlscan gives a far deeper technical scan (resources loaded, IPs, related domains); ExpandURL is the quick, friendly "where does this go" answer. Run ExpandURL first, urlscan when it looks worth it.
- Overlaps with `[[unshorten-it]]` and `[[redirect-detective]]` — cross-check with a second unshortener when the verdict matters.

## Trust & verifiability
`trust: unverified` — an actively maintained but independent, unaudited service. The redirect chain and status codes are directly observable and easy to sanity-check; for a high-stakes safety call, confirm with a second expander.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | expandurl |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
