---
id: mailtester
name: MailTester
description: Use when you have an email address and want a quick free check of whether it is valid and deliverable — returns SMTP/DNS validation status without sending mail.
url: http://mailtester.com
category: email
path:
- email
bestFor: Free single-address email validity / deliverability checking.
selectorsIn:
- email
selectorsOut:
- email
status: live
pricing: freemium
costNote: Free single-address web check; bulk/API verification is paid (mailtester.com / Mail Tester Pro).
opsec: passive
opsecNote: Performs DNS/MX and SMTP RCPT checks without delivering a message, so the mailbox owner is not alerted. The receiving mail server still logs the probe connection.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: mailtester.com is a long-standing, widely referenced free email validator listed across OSINT framework lists. Established but no independent accuracy benchmark.
missingPersonsRelevance: high
coverage: []
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- mailscrap
- mxtoolbox
aliases: []
tags:
- email-search-email-check
source: awesome-osint
lastVerified: ''
enrichment: full
---

# MailTester

> Classic free email-validity checker — runs DNS/MX and SMTP probes to tell you if an address is real and deliverable.

## When to use
You have a single candidate `email` (from a permutation guess, a profile, or a breach dump) and want to confirm it exists before investing further. Useful for narrowing a permutation list (see `[[metric-sparrow-email-permulator]]`) down to the addresses that actually resolve.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to mailtester.com and enter the `email`.
2. Read the verdict: valid, invalid, or undetermined, plus MX/SMTP detail.
3. For more than a handful of checks, use the paid API rather than the web form (rate limits apply).
4. Pivot: confirmed addresses go to breach-monitoring (`[[monitor-firefox-com]]`) and to profile-discovery tools.

## Inputs → Outputs
- **In:** `email`
- **Out:** validation status for that `email` (valid / invalid / undetermined, with MX/SMTP notes)
- **Empty/negative result looks like:** "invalid" (server rejected the recipient) or "undetermined" (catch-all domain, greylisting, or blocked probe). Catch-all domains will read as valid for any address — do not trust a lone pass.

## Gotchas & OpSec
- Catch-all and anti-validation servers cause false positives/inconclusive results; corroborate with `[[mailscrap]]`.
- Heavy use gets rate-limited or temporarily blocked by both MailTester and target servers.
- Validity ≠ ownership: a deliverable address does not prove a specific person controls it.

## Trust & verifiability
`trust: community` — long-established free validator referenced in multiple curated OSINT lists; reliable for basic checks but unbenchmarked. Behavior described from common validator mechanics.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mailtester |
| category | email |
| selectorsIn → selectorsOut | email → email |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
