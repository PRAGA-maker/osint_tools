---
id: bluecoat-webpulse
name: Symantec SiteReview (BlueCoat WebPulse)
description: Use when you have a `domain`/URL and want its content category and reputation — returns the WebPulse classification and a route to dispute or check filtering.
url: https://sitereview.bluecoat.com/sitereview.jsp
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- reputation
bestFor: Checking how enterprise web filters categorise a site (e.g. malware, phishing, suspicious, adult) and its WebPulse reputation.
selectorsIn:
- domain
selectorsOut: []
status: live
pricing: free
costNote: Free lookup (a CAPTCHA gates queries); no account required.
opsec: passive
opsecNote: You query Symantec's cloud reputation database, not the target site itself, so nothing is sent to the subject's server. A CAPTCHA appears per lookup.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Symantec/Broadcom's Blue Coat WebPulse — a major enterprise web-filtering database; categorisation is authoritative for "how corporate filters see this site," though a category is a classification, not proof of intent.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- BlueCoat WebPulse
- Symantec SiteReview
- sitereview.bluecoat.com
tags:
- url-reputation
- categorization
- reputation
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# Symantec SiteReview (BlueCoat WebPulse)

> The public lookup for Symantec/Blue Coat's WebPulse database — enter a `domain` and see the content category and reputation that enterprise web filters apply to it.

## When to use
You have a `domain`/URL and want an at-a-glance risk read: how a widely deployed corporate filter classifies it (e.g. Malicious Sources/Malnets, Phishing, Suspicious, Scam/Questionable Legality, Adult, or a benign category). This helps triage a suspicious link, judge whether a site is likely to be blocked in enterprise environments, or corroborate a malware/phishing suspicion — all without touching the target site yourself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://sitereview.bluecoat.com/ and enter the `domain`/URL.
2. Solve the CAPTCHA and submit.
3. Read the returned category (one or two content classifications) and any risk indication.
4. Pivot: cross-check against other reputation engines (VirusTotal, URLhaus, `[[checkshorturl]]`'s aggregated flags) — a category is one signal, not a verdict.

## Inputs → Outputs
- **In:** `domain` / URL
- **Out:** WebPulse content category and reputation classification for the site
- **Empty/negative result looks like:** "Uncategorized" or a generic/benign category — meaning WebPulse hasn't classified it or sees nothing notable, not proof the site is safe; new malicious sites are often uncategorised.

## Gotchas & OpSec
- Human-in-the-loop: a CAPTCHA is required for each lookup.
- OpSec: passive — you query Symantec's database, not the target; the subject's server is never contacted.
- Interpretation: categorisation reflects content classification for filtering, which can be stale or coarse; a "benign" label is not clearance, and disputes/recategorisation exist for a reason.

## Overlaps ("do both")
- Pairs with VirusTotal, URLhaus and other reputation sources because each vendor classifies differently — agreement across them is a far stronger signal than any single category.

## Trust & verifiability
`trust: trusted` — an authoritative enterprise-filtering database; reliable for "how this site is categorised," with the caveat that categories can lag and describe content, not intent — so corroborate for anything load-bearing.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
