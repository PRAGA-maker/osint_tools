---
id: windows-defender-security-intelligence-wdsi
name: Windows Defender Security Intelligence (WDSI)
description: Use when you have a suspicious `domain`/URL and want to check Microsoft's threat classification or report it for analysis — returns Microsoft's verdict and a submission record.
url: https://www.microsoft.com/en-us/wdsi
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- report-malicious-sites
bestFor: Reporting a malicious URL to Microsoft and checking how SmartScreen/Defender classifies a site.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free Microsoft service; submitting some sample types or viewing submission history may require a Microsoft account sign-in.
opsec: passive
opsecNote: You submit a URL/sample to Microsoft for analysis — the interaction is with Microsoft, not the target site, so it does not tip off the site's operator. Microsoft logs submissions and ties them to your account if signed in; use an operational account for reporting.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Microsoft security portal (Defender/SmartScreen intelligence); an authoritative source for Microsoft's own classifications.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
relatedTools: []
aliases:
- WDSI
- Microsoft Security Intelligence
tags:
- report-malicious-sites
- threat-intelligence
- microsoft
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# Windows Defender Security Intelligence (WDSI)

> Microsoft's security-intelligence portal — submit a suspected malicious site/file for analysis and see how Defender/SmartScreen classifies it.

## When to use
You have a suspicious `domain`/URL (phishing, malware, scam) and want to (a) report it so Microsoft's SmartScreen/Defender can block it for the wider ecosystem, or (b) understand Microsoft's current classification of it. Primarily a defensive/reporting action within a fraud or malicious-site investigation, and a way to corroborate a site's reputation from a first-party source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.microsoft.com/en-us/wdsi and choose the submission path (URL/site or file sample).
2. Enter the target `domain`/URL and any context; sign in with a Microsoft account if you want to track the case.
3. Submit; Microsoft performs analysis (partly automated, partly **manual review**) and returns/updates a determination.
4. Check the guidance/encyclopedia sections for how a threat family is classified.
5. Pivot: a confirmed-malicious verdict feeds broader threat-intel and hosting/registrar abuse reports.

## Inputs → Outputs
- **In:** `domain`/URL (or file sample)
- **Out:** Microsoft's threat classification for that `domain` and a submission confirmation/case
- **Empty/negative result looks like:** "not detected / clean" — Microsoft hasn't classified it as malicious yet, which is not a guarantee of safety, especially for brand-new sites.

## Gotchas & OpSec
- Determinations can take time and involve **manual review** — not an instant verdict.
- A "clean" result reflects Microsoft's current data only; cross-check with other reputation engines for new threats.
- This is a reporting/lookup channel, not an investigative pivot on people — it returns site verdicts, not ownership.

## Overlaps ("do both")
- Pair with `[[cybergordon]]` and other reputation aggregators and with registrar/host abuse reporting — WDSI gives Microsoft's authoritative verdict and pushes protection; the aggregators give breadth across other vendors.

## Trust & verifiability
`trust: trusted` — a first-party Microsoft portal; its classifications are authoritative for the Defender/SmartScreen ecosystem, though (like any single vendor) not exhaustive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | windows-defender-security-intelligence-wdsi |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
