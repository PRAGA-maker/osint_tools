---
id: spycloud
name: SpyCloud
description: Use when you have an email or domain and want to know whether it appears in breach and infostealer-malware data — returns exposure confirmation and, on the paid platform, recaptured records.
url: https://spycloud.com/
category: email
path:
- email
bestFor: Checking whether an email/domain is exposed in breach and infostealer (stealer-log) datasets.
selectorsIn:
- email
- domain
selectorsOut:
- email
- password
status: live
pricing: freemium
costNote: Free self-service "check your exposure" tool gives a yes/exposed summary for an email or domain. The detailed recaptured records (plaintext creds, malware-infection detail) sit behind an enterprise, quote-based platform.
opsec: passive
opsecNote: The free check queries SpyCloud's own recaptured-data index, not the target's accounts, so nothing is sent to the data subject. Entering a target address does log it with a commercial vendor — use a work/sock-puppet context and never submit a subject's password to any "check" field.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: SpyCloud is an established commercial breach/infostealer-intelligence vendor; its data is well-regarded in fraud and account-takeover prevention. The free tier only summarises exposure — the substantive records require a paid contract.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: true
relatedTools:
- spycloud-com
aliases:
- Spycloud
tags:
- breach
- infostealer
- email
source: inteltechniques-tools
lastVerified: '2026-07-21'
enrichment: full
---

# SpyCloud

> Commercial breach- and infostealer-intelligence platform with a free exposure check — tells you whether an email or domain shows up in recaptured breach and stealer-malware data.

## When to use
You have an `email` or a `domain` and want to establish whether the subject's credentials have leaked — in a classic data breach or, more valuably, in infostealer/malware logs that also expose device and session detail. A positive exposure signal corroborates that an address is real and in active use, and it points you toward which breach corpora to search next for reused usernames and passwords.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://spycloud.com/ and use the free "check your exposure" tool.
2. Submit the target `email` (or a `domain` for organisation-wide exposure). Never paste a password.
3. Read the result: it summarises whether — and roughly how heavily — that identity/domain appears in SpyCloud's recaptured data.
4. For the underlying records (specific breaches, plaintext or hashed credentials, infostealer infection detail), you need the paid platform or its API — request a demo; there is no free record-level export.
5. Pivot: confirmed exposure feeds a breach-search workflow (reused passwords, linked usernames) and the sibling `[[spycloud-com]]` entry.

## Inputs → Outputs
- **In:** `email` or `domain`.
- **Out:** exposure confirmation (free); on the paid platform, recaptured `email`/username and `password` records plus breach/infostealer metadata.
- **Empty/negative result looks like:** "no exposure found" means the address isn't in SpyCloud's index — not proof it was never breached, only that SpyCloud hasn't recaptured it.

## Gotchas & OpSec
- Human-in-the-loop: **payment-wall-partial** — the free tool is a summary/teaser; the actionable records require an enterprise contract, so plan around that gate.
- OpSec: **passive** — you query SpyCloud's index, not the target's accounts, so there is no target-side alert. Submitting an address does hand it to a commercial vendor; keep it in an appropriate investigative context.
- Never enter a subject's password into any exposure-check field, here or elsewhere — that would leak the very secret you are investigating.

## Overlaps ("do both")
- Pairs with `[[spycloud-com]]` — the same provider; use them together, and cross-check any hit against a second breach source before treating a credential as confirmed.

## Trust & verifiability
`trust: community` — a reputable commercial breach-intelligence vendor whose data underpins many fraud-prevention products. The free tier is reliable but only tells you *whether* an identity is exposed; treat record-level detail as available only under the paid platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | spycloud |
| category | email |
| selectorsIn → selectorsOut | email, domain → email, password |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
