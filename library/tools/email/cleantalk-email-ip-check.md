---
id: cleantalk-email-ip-check
name: CleanTalk Email/IP Check
description: Use when you have an `email` or `ip-address` and want its spam/abuse reputation — returns blacklist status and whether it's been seen in spam activity.
url: https://cleantalk.org/
category: email
path:
- email
bestFor: Checking whether an email address or IP appears on spam blacklists / has an abuse history.
selectorsIn:
- email
- ip-address
selectorsOut:
- email
- ip-address
status: live
pricing: freemium
costNote: The email/IP blacklist lookups are free with no account; CleanTalk's anti-spam SaaS and API are paid.
opsec: passive
opsecNote: Passive reputation lookup against CleanTalk's own database — the email/IP owner is never contacted, so no signal reaches the subject. Your query is logged by CleanTalk.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial anti-spam vendor's free lookup; the blacklist reflects CleanTalk's own crowd-sourced spam data, useful as a signal but not an authoritative registry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- CleanTalk
- cleantalk blacklist
tags:
- email
- spam
- blacklist
- ip-reputation
source: inteltechniques-tools
lastVerified: '2026-07-28'
enrichment: full
---

# CleanTalk Email/IP Check

> A free spam-blacklist lookup — check whether an `email` or `ip-address` has a history of spam/abuse in CleanTalk's crowd-sourced database.

## When to use
You have an `email` or `ip-address` and want a quick reputation read: is it a known spammer, has it been flagged in abusive activity, is it on blacklists? Useful for triaging whether a contact address is a throwaway/spam identity, or whether an IP in a log is a known bad actor.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://cleantalk.org/ and find the free "Blacklist check" tool (email/IP/domain).
2. Enter the `email` or `ip-address`.
3. Read the verdict: whether it's blacklisted, the type of activity reported, and how recently.
4. Pivot: a "clean" email is more likely a real personal address worth deeper email-OSINT; a flagged one suggests a disposable/spam identity. Flagged IPs feed infrastructure/abuse analysis.

## Inputs → Outputs
- **In:** `email` or `ip-address`
- **Out:** blacklist status and reported spam/abuse history for that `email`/`ip-address`
- **Empty/negative result looks like:** "not found in blacklists" — no recorded spam activity; not proof the address is legitimate or benign, just that CleanTalk hasn't flagged it.

## Gotchas & OpSec
- Reflects CleanTalk's own crowd-sourced data — an address can be malicious yet unflagged, or flagged due to shared/CGNAT infrastructure.
- IP reputation attaches to the address, not a person; VPN/proxy/shared IPs muddy attribution.
- Deep/bulk use needs the paid API; the free web check is single-lookup.

## Overlaps ("do both")
- Pairs with other email/IP reputation checks (e.g. [[network-entity-reputation-database-nerd]], [[checkip]]) — cross-checking several blacklists gives a more reliable reputation picture than any one source.

## Trust & verifiability
`trust: community` — a vendor-run free lookup backed by crowd-sourced data; a strong signal but not an authoritative ruling — corroborate before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cleantalk-email-ip-check |
| category | email |
| selectorsIn → selectorsOut | email, ip-address → email, ip-address |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
