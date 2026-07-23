---
id: sucuri-sitecheck
name: Sucuri SiteCheck
description: Use when you have a `domain` and want a free remote malware/blacklist scan plus fingerprinting of its CMS and server — returns infection status, blacklist listings and software `metadata-exif`-style tech details.
url: https://sitecheck.sucuri.net/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- reputation
bestFor: Remotely scanning a website for malware/blacklist status and fingerprinting its CMS, plugins and server software.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free remote scanner from Sucuri (GoDaddy); no account for the public SiteCheck scan.
opsec: active
opsecNote: Sucuri's scanner (not you) fetches the target site, so your IP is not exposed — but the target's server logs/WAF will see Sucuri's scanner hit it, so the owner could infer someone ran a check. You remain anonymous to the target; the site does receive a visit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party tool from Sucuri (a GoDaddy-owned web-security firm); the malware and blacklist verdicts come from an established commercial security provider.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- SiteCheck
- sitecheck.sucuri.net
tags:
- reputation
- malware-scanning
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# Sucuri SiteCheck

> Sucuri's free remote website scanner: point it at a `domain` and it reports malware, blacklist status, and a fingerprint of the site's CMS, plugins and server software.

## When to use
You have a `domain` — a suspicious link, a scam site, a compromised page a subject was directed to — and you want a fast, no-install verdict on whether it is infected or blacklisted, plus a read on what it's running (WordPress version, plugins, server headers). The tech fingerprint alone is useful for pivoting: an outdated CMS or a distinctive plugin set helps cluster related sites.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://sitecheck.sucuri.net/.
2. Enter the target `domain`/URL and run the scan.
3. Read the report: malware detected (with the injected code/URLs), blacklist status across vendors, and the "Website Details" software fingerprint (CMS, version, server).
4. Note any injected external `domain`s in the malware findings — those are pivot targets.
5. Pivot: injected/redirect domains feed infra tooling; the CMS/plugin fingerprint helps match this site to others in the same campaign.

## Inputs → Outputs
- **In:** `domain` / URL
- **Out:** infection status + injected `domain`s, multi-vendor blacklist status, CMS/plugin/server fingerprint
- **Empty/negative result looks like:** "No malware detected" and clean blacklists — this reflects a *remote* scan only, so it can miss server-side or gated infections; absence of a finding is not a clean bill of health.

## Gotchas & OpSec
- It's a remote scanner — it sees what an anonymous visitor sees, so backend/authenticated malware and time/geo-gated redirects can be missed.
- OpSec: active toward the target — Sucuri's scanner visits the site, so the owner's logs show a Sucuri hit (not you). You stay anonymous, but the check isn't invisible to the target.
- Blacklist data is refreshed on vendors' schedules; a very fresh malicious domain may still show clean.

## Overlaps ("do both")
- Pairs with a reputation service like `[[norton-safeweb-rating-search]]` and a live URL sandbox — SiteCheck gives you the technical fingerprint and injected-code detail, while reputation/sandbox tools add historical rating and dynamic behavior.

## Trust & verifiability
`trust: trusted` — a first-party scanner from Sucuri (GoDaddy), an established web-security vendor; findings are authoritative for what a remote scan can see, with the caveat that remote-only scans have blind spots.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sucuri-sitecheck |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
