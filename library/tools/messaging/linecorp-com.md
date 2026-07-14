---
id: linecorp-com
name: LINE — Responding to Law Enforcement
description: Use when you have a `phone` or `username` tied to a LINE messenger account and need to know what data LINE holds and how (via legal process) it can be obtained — returns the legal-request channel and data-availability reference, not a self-service lookup.
url: https://linecorp.com/en/security/article/35
category: messaging
path:
- messaging
bestFor: Understanding what account data LINE retains and the lawful channel to request it during a LINE-linked investigation.
selectorsIn:
- phone
- username
selectorsOut:
- name
- social-profile
status: live
pricing: free
costNote: Free reference page published by LINE; the underlying data disclosure requires a valid legal request routed through law enforcement, not a purchase.
opsec: passive
opsecNote: Reading LINE's published policy is passive and leaves no trace against the subject. The actual data request is a legal-process action taken by law enforcement, not something an open-source investigator executes directly — never attempt to social-engineer or impersonate a request.
humanInLoop: true
humanInLoopReason:
- legal-gate
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party policy page published by LINE Corporation (now LY Corporation); authoritative on LINE's own data-handling and disclosure practices.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- linecorp-com-transparency
aliases:
- LINE law enforcement guidelines
- LINE data request policy
tags:
- messengerapps
- Messenger Apps
- legal-process
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# LINE — Responding to Law Enforcement

> LINE Corporation's official "Responding to Law Enforcement Agencies" policy — the reference that tells an investigator what LINE data exists and that it is reachable only through lawful legal process.

## When to use
Your subject uses LINE (dominant in Japan, Taiwan, Thailand) and you have a `phone` or LINE `username` but have exhausted open sources. This page is not a lookup tool — it is the map of the legal channel: it states that LINE does not disclose user information to third parties without consent or valid legal process, and frames what a law-enforcement request can obtain. Use it to brief the LE partner on a missing-persons case, or to set realistic expectations about what is and isn't obtainable from LINE via OSINT alone.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read https://linecorp.com/en/security/article/35 to understand LINE's disclosure stance and the categories of data it holds.
2. Recognise the boundary: as an open-source investigator you cannot pull LINE account data yourself — there is no public lookup.
3. If the case warrants it, hand the `phone`/`username` and the legal justification to the law-enforcement agency, who route a formal request through LINE's Legal/Trust & Safety process.
4. Pivot to open sources meanwhile: LINE IDs are sometimes reused as usernames elsewhere — check username tools and the LINE add-by-ID QR flow (do not initiate contact with the target).

## Inputs → Outputs
- **In:** `phone` or `username` (the identifier you'd supply to the legal channel)
- **Out:** (via legal process only) subscriber `name`, registration data, linked `social-profile` — plus, immediately, a clear picture of what is/ isn't obtainable
- **Empty/negative result looks like:** the page confirms nothing is self-service — treat any site claiming to "look up a LINE user by phone" as a scam/malware.

## Gotchas & OpSec
- Human-in-the-loop: this is a **legal-gate**. Actual data disclosure needs valid legal process via law enforcement; never impersonate one.
- This is a policy document, not an API — do not expect a query box.
- Passive to read; the sensitive action lives entirely on the legal side.

## Overlaps ("do both")
- Pairs with LINE's transparency reporting (`[[linecorp-com-transparency]]`) — this page states the *policy*, the transparency report shows the *volume and types* of requests LINE actually fulfils.

## Trust & verifiability
`trust: trusted` — it is LINE's own published policy, authoritative on its data-handling; just remember it documents a channel you access through law enforcement, not directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | linecorp-com |
| category | messaging |
| selectorsIn → selectorsOut | phone, username → name, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (legal-gate) |
