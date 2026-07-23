---
id: google-safe-browsing-api
name: Google Safe Browsing
description: Use when you have a `domain`/URL and want Google's verdict on whether it's flagged for malware, phishing, or unwanted software — returns a safe/unsafe classification and threat type.
url: https://developers.google.com/safe-browsing/?csw=1
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- reputation
bestFor: Checking whether a URL/domain is on Google's malware/phishing/unwanted-software blocklists.
input: URL or domain
output: Safe/unsafe classification, threat type
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
opsec: passive
opsecNote: You query Google's precomputed threat lists, not the suspect site, so you don't touch the target and it isn't alerted. The Site Status transparency page needs no account; the API needs a Google Cloud key (free for non-commercial — commercial use requires the paid Web Risk API). Use a dedicated Google/Cloud project for the key.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Google service powering browser safe-browsing warnings; authoritative for what Google itself flags.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Safe Browsing
- Google Safe Browsing API
- Transparency Report Site Status
tags:
- url-reputation
- phishing-detection
- malware
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# Google Safe Browsing

> Google's own malware/phishing verdict on a URL — the same blocklist that pops browser warnings, queryable for whether a link in your investigation is known-bad.

## When to use
You have a `domain` or URL — from a suspicious message, a scam profile, a shortened link — and want to know if Google flags it as malware, social-engineering/phishing, or unwanted software. Fast, authoritative triage for whether a link tied to a subject or scam is dangerous and worth treating as hostile infrastructure. For a quick manual check use the Transparency Report; for automation use the API.

## How to use it (`bestInteractionPattern`: web-manual)
1. Manual: open Google's Safe Browsing "Site Status" transparency page and paste the `domain`/URL — no account needed.
2. API: create a Google Cloud project, enable the Safe Browsing API, get a key, and POST the URL to the `threatMatches:find` endpoint.
3. Read the verdict: safe (no match) or unsafe with a threat type (MALWARE, SOCIAL_ENGINEERING, UNWANTED_SOFTWARE) (`selectorsOut`).
4. Pivot: an unsafe verdict marks the domain as hostile infrastructure — cross-check reputation tools and treat linked assets with care.

## Inputs → Outputs
- **In:** `domain` / URL
- **Out:** `domain` reputation — safe/unsafe classification + threat type
- **Empty/negative result looks like:** "no match" / safe — meaning Google hasn't listed it, NOT a guarantee it's benign (new or targeted malicious sites often aren't listed yet).

## Gotchas & OpSec
- Human-in-the-loop: the transparency page is open; the API needs a Google Cloud key (`api-key`), free for non-commercial use.
- OpSec: passive — you query Google's lists, not the target site.
- A clean result is not proof of safety; blocklists lag fresh threats. Commercial use requires the paid Web Risk API, not this one.

## Overlaps ("do both")
- Pairs with VirusTotal, [[threatminer-org]], and URLScan — cross-check a URL across engines, since each flags different threats and Safe Browsing only reflects Google's own lists.

## Trust & verifiability
`trust: trusted` — a first-party Google service, authoritative for what Google flags (it drives real browser warnings). Its verdicts are reliable positives; treat a negative as "not listed," not "confirmed safe."

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-safe-browsing-api |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (api-key) |
