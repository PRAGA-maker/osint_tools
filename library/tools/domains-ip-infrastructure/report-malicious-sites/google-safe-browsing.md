---
id: google-safe-browsing
name: Google Safe Browsing
description: Use when you have a `domain` or URL and want to know whether Google flags it as malware/phishing — returns its safety status, and lets you report a newly-found malicious site.
url: https://safebrowsing.google.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- report-malicious-sites
bestFor: Checking whether a suspect domain/URL is flagged by Google as malware, unwanted software, or phishing before you or a subject visits it.
input: domain or URL
output: safety status (clean / flagged), threat category
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: The Site Status checker and reporting forms are free with no account; the Safe Browsing API is free for developers (with a key and usage limits).
opsec: passive
opsecNote: You query Google's cached reputation data, not the target site, so checking a URL does not touch the target's server or reveal your interest to them. Submitting a report is logged by Google and tied to whatever session/identity you use.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Google service backed by the same threat data that warns 5B+ devices in Chrome; the flagging signal is authoritative, though absence of a flag is not a clean bill of health.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Safe Browsing
- Google Transparency Report Site Status
tags:
- domain-reputation
- malware
- phishing
source: arf-seed
lastVerified: '2026-07-23'
enrichment: full
---

# Google Safe Browsing

> Google's threat-reputation service — check whether a domain/URL is flagged as malware, unwanted software, or phishing, using the same data that powers Chrome's red warning screens.

## When to use
You have a `domain` or full URL — a link a subject shared, a shortener's revealed destination, a site hosting a lure — and you want a fast, passive verdict on whether it's known-malicious before you or anyone touches it. Also use it to *report* a malicious site you've discovered so it gets flagged for everyone.

## How to use it (`bestInteractionPattern`: web-manual)
1. **To check a site:** open Google's Transparency Report Site Status checker (`transparencyreport.google.com/safe-browsing/search`), enter the `domain` or URL, and read the verdict.
2. Interpret the status: "No unsafe content found" (not currently flagged) vs. flagged with a threat category (malware / social engineering / unwanted software).
3. **To report a bad site:** use the Report Phishing (`safebrowsing.google.com/safebrowsing/report_phish/`) or Report Malware pages and submit the URL.
4. **To automate:** register for a Safe Browsing API key and query the Lookup/Update API to batch-check URLs from code.
5. Pivot: a flagged domain is a strong signal to pair with WHOIS, hosting, and passive-DNS lookups to map the malicious infrastructure.

## Inputs → Outputs
- **In:** `domain` or URL (single check via the UI; batches via the API)
- **Out:** safety status + threat category for that `domain`
- **Empty/negative result looks like:** "No unsafe content found" — this means *not currently on Google's list*, NOT proven safe; brand-new or low-traffic malicious sites are often not yet flagged.

## Gotchas & OpSec
- **Absence ≠ safe.** Safe Browsing lags fresh threats; a "clean" result on a suspicious site should still be treated cautiously and cross-checked.
- Checks are passive (you hit Google, not the target), which makes this a safe first look at a hostile URL.
- The API needs a key and has quota limits; the UI checker does not.
- Status can change; re-check if time has passed since your last look.

## Overlaps ("do both")
- Pairs with link-expansion tools like [[bitly-url-shortener-and-link-manager]] (reveal the real destination first, then check it here) and with multi-engine reputation services — Safe Browsing is one authoritative vote, best confirmed against a second scanner for coverage gaps.

## Trust & verifiability
`trust: trusted` — authoritative first-party Google threat data; a positive flag is highly reliable, while a negative result only means "not yet listed," so weight the two asymmetrically.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-safe-browsing |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
