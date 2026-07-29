---
id: url-void
name: URL Void
description: Use when you have a `domain` tied to your subject (a personal site, a link from their profile, a scam contact) and want to know if it is flagged malicious — returns a reputation report plus the hosting `ip-address`.
url: https://www.urlvoid.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- reputation
bestFor: Reputation-checking a domain against 30+ blocklists without visiting it, and pulling its IP/registration basics.
selectorsIn:
- domain
selectorsOut:
- ip-address
- domain
status: live
pricing: free
costNote: Free web lookup; higher-volume/automated use is pushed to the paid sister API (APIVoid).
opsec: passive
opsecNote: You query URLVoid's aggregated blocklist data, not the target site itself, so the subject's server sees nothing. Note URLVoid states submitted URLs are shared with security companies — don't submit a private/unpublished URL you don't want logged.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Run by NoVirusThumbs/APIVoid; a widely-used aggregator, but it re-reports third-party blocklists rather than making original determinations.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- urlvoid
aliases:
- URLVoid
tags:
- domain-reputation
- blocklist-check
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# URL Void

> A safe-to-run reputation aggregator: paste a domain and see whether 30+ blocklists consider it malicious, without ever loading the site.

## When to use
You have a `domain` connected to your subject — a personal or business website, a link posted on their social profile, or a domain used to contact a missing person (a "job offer", a romance-scam site) — and you want to know whether it is a known-bad property (phishing, malware, fraud) before you trust or visit it. It is a triage step, not a people-finder.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.urlvoid.com/.
2. Enter the `domain` (host only, e.g. `example.com` — not a full deep link) and submit.
3. Read the report:
   - **Detections** — how many of the 30+ blocklist engines flag the site, each linking to its own report.
   - **Details** — server `ip-address`, domain age / creation date, and server location.
4. Pivot: take the reported `ip-address` into infrastructure tooling (reverse-IP, ASN lookup), and use the domain age to gauge whether a "company" site is a throwaway created days ago.

## Inputs → Outputs
- **In:** `domain`
- **Out:** `ip-address`, blocklist detection count, domain age, server location
- **Empty/negative result looks like:** all engines "clean"/green and a plausible domain age — meaning *no blocklist flags it*, which is not proof of legitimacy, just absence of known-bad reports.

## Gotchas & OpSec
- Passive: the aggregation is queried, not the target host, so the subject's server is not touched.
- Submitted URLs are shared with security vendors — fine for suspect scam domains, wrong for a sensitive private link.
- A clean result is weak evidence; a fresh registration date on a "established company" is often the more useful signal than the blocklist score.

## Overlaps ("do both")
- Pairs with `[[urlvoid]]` (same provider record) and any WHOIS/reverse-IP tool — URLVoid tells you *reputation*, WHOIS/reverse-IP tell you *who and what else is on that server*.

## Trust & verifiability
`trust: unverified` — URLVoid faithfully re-reports upstream blocklists, but it is a third-party aggregator; confirm any "malicious" verdict against the individual engine reports it links to before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | url-void |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → ip-address, domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
