---
id: google-transparency-report
name: Google Transparency Report (Safe Browsing Site Status)
description: Use when you have a `domain`/URL and want Google's safety verdict — returns Safe Browsing status (malware/phishing/unsafe) for the site.
url: https://transparencyreport.google.com/safe-browsing/search
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Checking whether Google's Safe Browsing flags a domain/URL as hosting malware, phishing, or unwanted software.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free Google service, no account. (Note: the Transparency Report's old HTTPS certificate-transparency search was retired in 2022 — use crt.sh for CT logs; the Safe Browsing site-status tool remains live.)
opsec: passive
opsecNote: You query Google's public Safe Browsing status page, not the target site, so the domain owner is not alerted. Only Google sees your query.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Google resource; Safe Browsing is the authoritative dataset behind Chrome/Firefox/Safari malware & phishing warnings.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Safe Browsing Site Status
- Google Safe Browsing
- transparencyreport.google.com
tags:
- safe-browsing
- url-reputation
- phishing-check
source: osint4all
lastVerified: '2026-07-23'
enrichment: full
---

# Google Transparency Report (Safe Browsing Site Status)

> Google's own verdict on a site: does Safe Browsing — the engine behind those red "deceptive site ahead" warnings — currently flag this domain as dangerous?

## When to use
You have a `domain` or URL tied to an investigation (a phishing lure, a suspicious link, a site of interest) and want Google's authoritative safety classification: is it flagged for malware, social-engineering/phishing, or unwanted software? Safe Browsing powers the warnings in Chrome, Firefox, and Safari, so its verdict is high-signal. It's a reputation/triage check; missing-persons relevance is low and indirect (vetting a site connected to a scam or extortion case).

> Note: the Transparency Report also *used to* host an HTTPS certificate-transparency search at `/https/certificates`; Google retired that in 2022. For CT-log lookups use crt.sh instead. This entry covers the still-live **Safe Browsing Site Status** tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://transparencyreport.google.com/safe-browsing/search.
2. Enter the `domain` or full URL and submit.
3. Read the status:
   - **"No unsafe content found"** — Safe Browsing does not currently flag it.
   - **Flagged** — it reports the category (malware, social engineering/phishing, unwanted software) and details.
4. Pivot: a flagged verdict corroborates malicious intent; combine with a sandbox (`[[hybrid-analysis]]`) and passive DNS to map the infrastructure and campaign.

## Inputs → Outputs
- **In:** `domain` or URL
- **Out:** Safe Browsing status (safe / flagged) and the threat category if flagged
- **Empty/negative result looks like:** "no unsafe content found" — Google isn't *currently* flagging it; this is NOT proof of safety (new or narrowly-targeted malicious sites often aren't listed yet, and delistings happen after cleanup).

## Gotchas & OpSec
- A clean verdict is time-sensitive and coverage-limited — absence of a flag ≠ trustworthy site.
- Status reflects Google's current data; a site can be malicious before listing or benign after delisting.
- The certificate-transparency portion of the Transparency Report is retired — don't expect CT data here (use crt.sh).
- OpSec: passive; the target isn't contacted.

## Overlaps ("do both")
- Pairs with VirusTotal's URL scan, `[[alienvault-otx]]`, and sandboxes — cross-check, since each reputation source flags sites the others miss and their timing differs. Use crt.sh for the CT-log lookups this tool no longer provides.

## Trust & verifiability
`trust: trusted` — first-party Google data that drives mainstream browser warnings; authoritative when it flags a site, but a clean result is a not-currently-listed signal, not a guarantee.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-transparency-report |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
