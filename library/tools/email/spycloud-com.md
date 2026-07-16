---
id: spycloud-com
name: SpyCloud Check Your Exposure
description: Use when you have an `email` on a domain you control/investigate and want to know whether that identity or domain appears in recaptured darknet data — returns a domain-level exposure report (breached credentials, malware-infected users, stolen session cookies).
url: https://spycloud.com/check-your-exposure/
category: email
path:
- email
bestFor: Checking whether a business/domain's identities show up in SpyCloud's recaptured breach & infostealer-malware data.
selectorsIn:
- email
selectorsOut:
- email
- device-id
status: live
pricing: freemium
costNote: The "Check Your Exposure" report is free but scopes results to the DOMAIN of a business email you submit (consumer webmail is typically rejected). Full record-level data and per-person lookups are a paid enterprise product.
opsec: passive
opsecNote: You submit a business email to receive a domain-level report; the report is delivered to that address, so you must control the mailbox. The subject/individual is not contacted. Do not enter a target's address expecting a personal breach dump — the free tool is org-scoped, not a per-email breach checker, and submitting generates a sales lead tied to whatever email you use.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: trusted
trustNote: SpyCloud is a well-known commercial breach/darknet-recapture vendor whose data underpins many enterprise ARP products. The recaptured data is real; the free tool is deliberately limited to summaries to drive sales.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: true
aliases:
- SpyCloud exposure check
- SpyCloud breach exposure
tags:
- Emails
- breach
- infostealer
- darknet
source: cyb-detective
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- spycloud
---

# SpyCloud Check Your Exposure

> A free front-end to SpyCloud's recaptured-breach and infostealer-malware data — it returns a DOMAIN-level exposure summary for a business email you submit, not a personal breach dump.

## When to use
You are investigating an organisation or a domain (an employer, a suspect company, your own infrastructure) and want to know whether identities on that domain appear in SpyCloud's recaptured darknet data: exposed credentials, malware-infected users/devices, and stolen session cookies. Best treated as an org/domain exposure check rather than a per-person email lookup — for the latter, use `[[haveibeenpwned-com]]`-style tools.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://spycloud.com/check-your-exposure/ from a sock-puppet browser.
2. Enter a **business** `email` on the domain you want assessed (free consumer webmail is usually rejected — this is why it's domain-scoped).
3. Submit; a report is generated (~30 seconds) and/or emailed to that address.
4. Read the three exposure categories: exposed credentials, malware-infected users/devices (`device-id`), and stolen session cookies, plus recency.
5. Pivot: a domain with heavy exposure suggests employee `email`s worth checking individually; malware-infected-device signals point at compromised endpoints. For record-level detail you must engage the paid API/product.

## Inputs → Outputs
- **In:** `email` (business, on the domain under investigation)
- **Out:** domain-level counts of exposed `email` identities, malware-infected `device-id`s, session-cookie theft, and recency
- **Empty/negative result looks like:** low/zero exposure counts for the domain, or the form rejecting a non-business address — a zero here means "nothing in SpyCloud's recaptured set for this domain," not that no individual was ever breached.

## Gotchas & OpSec
- This is NOT a "paste any email, see their breaches" tool — the free tier is organisational and summary-level by design.
- Submitting registers a marketing lead; use a controlled mailbox you're happy to expose.
- Record-level data (the actual leaked passwords/PII) is gated behind a paid enterprise contract/API.

## Overlaps ("do both")
- Pairs with `[[haveibeenpwned-com]]` and `[[dehashed-com]]` — HIBP/DeHashed answer "is THIS email in a breach?" per individual, while SpyCloud answers "how exposed is this DOMAIN, including malware and session theft?" Different granularity, run both.

## Trust & verifiability
`trust: trusted` — SpyCloud is an established commercial breach-recapture vendor; the underlying data is genuine and widely used by enterprise security teams. The free report is intentionally coarse to sell the paid product.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | spycloud-com |
| category | email |
| selectorsIn → selectorsOut | email → email, device-id |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
