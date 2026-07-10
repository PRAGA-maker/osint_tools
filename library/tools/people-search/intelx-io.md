---
id: intelx-io
name: Intelligence X (intelx.io)
description: Use when you have an `email`, `domain`, `ip-address`, `crypto-wallet` or `username` and want breach/dark-web/archive hits — returns leaked records, documents and linked identities.
url: https://intelx.io/
category: people-search
path:
- people-search
bestFor: Searching data leaks, the dark web (Tor/I2P) and a historical web archive by selector to surface breached credentials, leaked documents and linked identities.
selectorsIn:
- email
- username
- name
- domain
- ip-address
- crypto-wallet
selectorsOut:
- email
- name
- social-profile
- document-id
status: live
pricing: freemium
costNote: Free account returns only ~10 results per search (a teaser). Real use needs a paid tier — Researcher starts around €2,500/year, Enterprise far higher. Effectively paywalled for serious work.
opsec: passive
opsecNote: You query IntelX's archive, not the target, so the subject is not notified. Searches are tied to your account, so use a research identity. Treat any breach data found as sensitive and handle it lawfully.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: Well-regarded data-archive/search engine (in the Bellingcat toolkit). Its index is genuine, but leaked data can be stale, mislabeled, or duplicated across dumps — verify before relying.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
relatedTools:
- epieos
aliases:
- IntelX
- Intelligence X
tags:
- bellingcat-toolkit
- people
- breach-data
- darkweb
source: bellingcat-toolkit
lastVerified: '2026-07-10'
enrichment: full
---

# Intelligence X (intelx.io)

> A selector-driven search engine over data leaks, the dark web, and a historical archive: feed it an email/domain/wallet and get breached records and documents back.

## When to use
You have a strong selector — `email`, `domain`, `ip-address`, `crypto-wallet`, `username`, or `name` — and want to know where it appears in data leaks, paste sites, dark-web (.onion/I2P) content, and IntelX's own historical web archive. It's one of the few ways to search the dark web without running Tor yourself, and it preserves snapshots (like a Wayback Machine for leaks), so it surfaces breached credentials, leaked documents (`document-id`), and identity links that regular search misses.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://intelx.io/ and register (free account for limited results; paid tier for real depth).
2. Enter a selector — email, domain, IP, CIDR, Bitcoin address, IPFS hash, username, or name.
3. Review results grouped by bucket (leaks, darknet, web, documents). Open items to see the archived content/snapshot.
4. On the free tier expect ~10 results only — enough to confirm something exists, not to work it fully.
5. Pivot: a leaked secondary `email`/`social-profile` feeds `[[epieos]]`; a leaked document anchors identity; a wallet/domain expands the graph.

## Inputs → Outputs
- **In:** `email`, `username`, `name`, `domain`, `ip-address`, or `crypto-wallet`
- **Out:** `email`, `name`, `social-profile`, leaked `document-id`s and archived snapshots
- **Empty/negative result looks like:** no buckets populated (or only the 10-result teaser is exhausted). Absence can mean "not in a dump IntelX indexed" — not proof the selector was never breached. Cross-check other breach tools.

## Gotchas & OpSec
- **Paywall:** the free tier is a teaser (~10 results); meaningful work requires an expensive subscription.
- Leaked data is often stale, duplicated across dumps, or mislabeled — verify a credential/identity before acting.
- Handle breach data lawfully and ethically; this is sensitive material.
- OpSec: passive toward the target, but searches are logged to your account — use a research identity.

## Overlaps ("do both")
- Pairs with `[[epieos]]` and other breach checkers — IntelX gives archive/dark-web depth and document snapshots; Epieos maps a confirmed email/phone to live accounts. Use IntelX to find leaked selectors, then pivot those into account-mapping tools.

## Trust & verifiability
`trust: community` — a respected, mature archive used across the OSINT industry (Bellingcat toolkit). The index is real, but leaked content quality varies wildly, so treat every hit as a lead and confirm the underlying data before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | intelx-io |
</content>
