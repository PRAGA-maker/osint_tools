---
id: appsec-fyi-osint-resources
name: appsec.fyi OSINT Resources
description: Use when you want a curated jump-list of OSINT reconnaissance tools and techniques — returns a vetted directory of external resources, not selector lookups.
url: https://appsec.fyi/osint.html
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A hand-curated index (~74 entries) of OSINT recon tools, frameworks, and technique write-ups for attack-surface mapping.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free, public, ad-free resource page; no account or key required.
opsec: passive
opsecNote: You are only reading a static curated list on a third-party site — no target interaction occurs. Standard web hygiene (your IP is logged by the host) applies, but nothing about a subject is queried here.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Maintained by application-security practitioner Carl Sampson as part of a broader AppSec resource library (XSS, SSRF, RCE, etc.); curated by a single named individual, so it reflects one expert's selection rather than an institution.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Open-Source Intelligence Resources (appsec.fyi)
- Carl Sampson OSINT list
tags:
- other-resources
- curated-directory
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# appsec.fyi OSINT Resources

> A single-page, hand-curated index of OSINT reconnaissance tools and technique write-ups, framed for attack-surface mapping — a launchpad, not a lookup engine.

## When to use
You are early in an investigation and want a vetted shortlist of recon tools and methods rather than the raw firehose of a giant awesome-list. The page groups OSINT resources (certificate-transparency subdomain discovery, paste/repo credential hunting, historical-archive asset discovery, internet-scan platforms like Shodan/Censys) with short context on what each is for.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://appsec.fyi/osint.html.
2. Skim the ~74 curated entries; each links out to the actual tool or write-up.
3. Pick the technique class you need (subdomain enumeration, exposed-secret search, historical assets, internet-scan data) and follow the outbound link.
4. Pivot: use it to discover a tool, then return here or to a broader directory when that tool comes up empty.

## Inputs → Outputs
- **In:** none — it is a reading resource, not a selector query
- **Out:** a curated list of external OSINT tools/resources with brief descriptions and links
- **Empty/negative result looks like:** the page is static; "nothing found" is not a state — if a needed category is absent, move to a broader index like [[awesome-osint]]-style directories.

## Gotchas & OpSec
- Human-in-the-loop: none; just read the page.
- OpSec: fully passive — no target is touched. The value is orientation and tool discovery, not data on a person.
- Scope skew: the list is written for bug-bounty/appsec recon, so it leans toward infrastructure and org attack surface rather than people-search; weight accordingly for missing-persons work.

## Overlaps ("do both")
- Pairs with larger curated indexes and this library's own directory tools — appsec.fyi is opinionated and small; a broad awesome-list is exhaustive but noisier. Use this to start, the big lists to be complete.

## Trust & verifiability
`trust: community` — curated by a named practitioner (Carl Sampson) with a public track record in AppSec; reliable as one expert's selection, but it is a personal list, not an authoritative or comprehensive catalog.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | appsec-fyi-osint-resources |
