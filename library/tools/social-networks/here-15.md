---
id: here-15
name: Here
description: Use when a subject's trail runs into TikTok and you need to know what data TikTok holds and how law enforcement can request it — returns process knowledge, not a lookup.
url: https://www.tiktok.com/legal/law-enforcement?lang=en
category: social-networks
path:
- social-networks
bestFor: Understanding what TikTok account/content data is obtainable and the legal channel to request it.
selectorsIn:
- username
selectorsOut: []
status: live
pricing: free
costNote: Free public legal/policy page.
opsec: passive
opsecNote: Reading TikTok's law-enforcement guidelines reveals nothing about your subject. Purely a reference — no query touches the target.
humanInLoop: true
humanInLoopReason:
- legal-gate
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party TikTok legal documentation; authoritative on TikTok's own retention and disclosure practices.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- TikTok Law Enforcement Guidelines
tags:
- tiktok
- TikTok Related Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# Here

> TikTok's official Law Enforcement Guidelines — the reference that defines what account and content data TikTok retains and the legal process (preservation, subpoena, court order, emergency disclosure) required to obtain it.

## When to use
This is a **reference, not a lookup**. Reach for it when a subject's trail leads to TikTok and you need to know what is realistically obtainable before drafting a preservation letter or, in a life-at-risk missing-persons case, an emergency-disclosure request. It separates what a user has exposed publicly (scrape-able) from account/IP/upload data that only legal process can unlock, so you don't burn effort chasing the un-gettable.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.tiktok.com/legal/law-enforcement?lang=en and read the data-request and emergency-request sections.
2. Note the retention windows and what each request type (preservation vs subpoena vs emergency) yields.
3. For an at-risk case, follow TikTok's law-enforcement request portal via the appropriate LE channel; note the emergency-disclosure route for imminent danger.
4. Pivot: use it to set expectations, then combine public-profile findings with a properly filed request.

## Inputs → Outputs
- **In:** context of the `username`/case (used to decide what to request)
- **Out:** procedural knowledge — retention scope, request types, disclosure routes (no data records)
- **Empty/negative result looks like:** N/A — it's documentation; the failure mode is misjudging what's obtainable without process.

## Gotchas & OpSec
- Human-in-the-loop / **legal-gate**: the data described is released only to verified law enforcement via legal process — not to investigators directly. Do not misrepresent yourself as LE.
- OpSec: **passive** — reading policy pages is invisible to the subject.
- Policy/retention terms change; re-verify current specifics before relying on them.

## Overlaps ("do both")
- Pairs with `[[discord-com-2]]` — the equivalent Discord process page; read both when a case spans multiple platforms so you route each request correctly.

## Trust & verifiability
`trust: trusted` — first-party TikTok legal documentation; authoritative for its own platform's practices.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | here-15 |
| category | social-networks |
| selectorsIn → selectorsOut | username → — |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (legal-gate) |
