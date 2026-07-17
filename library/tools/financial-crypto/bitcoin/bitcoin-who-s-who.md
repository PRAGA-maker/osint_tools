---
id: bitcoin-who-s-who
name: Bitcoin Who's Who
description: Use when you have a `crypto-wallet` (BTC address) and want owner tags, scam reports and linked websites — returns `domain`, `social-profile`, `associate` leads.
url: https://www.bitcoinwhoswho.com/
category: financial-crypto
path:
- financial-crypto
- bitcoin
bestFor: Attributing a Bitcoin address to reported owners, scam reports and websites where it appeared.
selectorsIn:
- crypto-wallet
- name
- email
selectorsOut:
- domain
- social-profile
- associate
status: live
pricing: freemium
costNote: Free address lookups, scam reports and block explorer; account and API (paid tiers) unlock alerts and higher-volume queries.
opsec: passive
opsecNote: Reads public blockchain data plus community-submitted reports; the query is not visible to the wallet owner. If you submit a report or tag, that content is public — do not disclose your investigation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Aggregates public chain data with crowd-sourced scam reports and tags; the crowd-sourced attribution is unverified and can be gamed, so corroborate before relying on it.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- bitcoinwhoswho
aliases:
- BitcoinWhosWho
- Bitcoin Who Is Who
tags:
- bitcoin
- crypto
- scam
- blockchain
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# Bitcoin Who's Who

> A Bitcoin address reputation and attribution service — cross-references a BTC address against scam reports, community tags and the websites where it has appeared.

## When to use
You have a `crypto-wallet` Bitcoin address (or a name/email/URL you suspect is tied to one) and you want to know whether it has been reported for fraud, what owner or entity it has been tagged as, and which websites it has surfaced on. Useful for tying an anonymous address back to a public persona, a scam campaign, or a domain.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.bitcoinwhoswho.com/ and enter the Bitcoin address in the search box (you can also search by name, email, URL, or keyword).
2. Read the address profile: current balance and transaction summary (block-explorer view), any user-submitted scam reports, community tags, and — most useful for OSINT — "websites found" listing pages where the address string appears.
3. Follow the linked `domain`/URLs and any owner tags to build attribution; check report dates and volume to gauge credibility.
4. Optionally set a transaction alert (needs an account) or use the API for bulk checks.
5. Pivot: linked websites feed WHOIS/domain OSINT; owner tags and emails feed people/email search; the address itself feeds a full chain-analysis tool.

## Inputs → Outputs
- **In:** `crypto-wallet` (BTC address), or `name` / `email` / URL / keyword
- **Out:** scam-report status, community tags, transaction/balance summary, linked `domain`s, owner `social-profile`/`associate` leads
- **Empty/negative result looks like:** "no reports found" and no website hits — meaning the address is simply unreported, not that it is safe; a clean record is weak evidence either way.

## Gotchas & OpSec
- Human-in-the-loop: none for lookups; alerts and higher API volume require registration/paid tiers.
- OpSec: **passive** to query. But submitting a report or tag is public and attributable — never post details that reveal you are investigating.
- Attribution is crowd-sourced and unverified; a "scam" tag can be malicious or mistaken. Corroborate any owner claim with independent evidence before acting on it.

## Overlaps ("do both")
- Pairs with `[[bitcoinwhoswho]]` — same service, alternate index entry.
- Combine with a dedicated blockchain-analytics/explorer tool: Bitcoin Who's Who supplies human-attribution and website links, while a chain analyzer traces the money flow.

## Trust & verifiability
`trust: community` — public chain data is authoritative, but the scam reports and owner tags are user-submitted and should be treated as leads to verify, not established facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bitcoin-who-s-who |
| category | financial-crypto |
| selectorsIn → selectorsOut | crypto-wallet, name → domain, social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
