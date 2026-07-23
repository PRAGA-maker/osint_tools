---
id: greynoise
name: GreyNoise
description: Use when you have an `ip-address` and want to know whether it is internet-wide background scanning noise or a targeted actor — returns classification, actor/tags, and CVE activity.
url: https://greynoise.io/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Triaging whether an IP that touched a target is opportunistic mass-scanner noise or something worth investigating.
selectorsIn:
- ip-address
selectorsOut:
- ip-address
- domain
status: live
pricing: freemium
costNote: Free searches at viz.greynoise.io without login; a free account adds more queries and a limited API. Full API/enterprise features are paid, but basic IP lookups are free.
opsec: passive
opsecNote: You query GreyNoise's sensor data, never the target IP itself, so the owner of that IP is not alerted. Searches are logged to your GreyNoise account if you log in.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Widely respected commercial threat-intelligence provider running a global sensor grid; the classification data is authoritative for "is this IP scanning the internet."
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- pygreynoise
- alienvault-otx
aliases:
- GreyNoise Visualizer
- greynoise.io
- viz.greynoise.io
tags:
- threat-intel
- ip-reputation
- scanner-noise
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# GreyNoise

> The internet's "is this just noise?" oracle: tells you whether an IP is one of the thousands of hosts opportunistically scanning everyone, or something targeted.

## When to use
You have an `ip-address` from a log, an alert, or infrastructure analysis and need to decide whether it matters. GreyNoise continuously observes internet-wide scan/attack traffic via its sensor grid, so a lookup instantly says whether the IP is benign background noise, a known scanner, or classified malicious — plus the actor, tags, ASN/org, and which CVEs it's probing. This is triage/enrichment; missing-persons relevance is low and indirect (vetting infrastructure behind a case).

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://viz.greynoise.io/ (the free Visualizer) — no login needed for basic searches.
2. Enter an `ip-address` (or a GNQL query like `classification:malicious tags:"..."`).
3. Read the result:
   - **Classification** — benign / unknown / malicious.
   - **Actor & tags** — e.g. "Censys", "Mirai", specific CVE exploitation tags.
   - **Metadata** — organisation, ASN, rDNS `domain`, first/last seen, targeted countries.
4. Pivot: a malicious classification with CVE tags feeds vulnerability triage; the rDNS/org feeds further infrastructure mapping. Bulk lookups use the API (free key from your account) or the `[[pygreynoise]]` client.

## Inputs → Outputs
- **In:** `ip-address`
- **Out:** classification (benign/malicious), actor/tags, ASN + org, reverse-DNS `domain`, CVE activity
- **Empty/negative result looks like:** "IP not observed" — GreyNoise's sensors haven't seen this IP scanning; that means it is *not* mass-scanning the internet (possibly targeted, possibly a normal host), NOT that it is safe.

## Gotchas & OpSec
- "Not seen" ≠ clean. GreyNoise answers "is this internet-wide noise?"; a targeted attacker deliberately avoiding broad scanning won't appear.
- Benign classification (e.g. a known research scanner) still means the IP touched you — it just isn't hostile.
- Free tier has query limits; heavy use needs an API key or a paid plan.
- OpSec: passive — you never contact the target IP.

## Overlaps ("do both")
- Pairs with `[[alienvault-otx]]` and other reputation feeds: GreyNoise tells you *whether it's noise*, OTX tells you *what campaign it's tied to*. Automate lookups with `[[pygreynoise]]`.

## Trust & verifiability
`trust: trusted` — a mature, reputable provider whose classifications come from its own global sensor network; the "is this scanning the internet" signal is authoritative, while absence of data must be read carefully.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | greynoise |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | ip-address → ip-address, domain |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
