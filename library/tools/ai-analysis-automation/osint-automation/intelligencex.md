---
id: intelligencex
name: IntelligenceX
description: Use when you have an `email`, `domain`, `ip-address`, or selector and want it searched across leaks, pastes, darknet and historical web — returns matching breach/leak intelligence.
url: https://intelx.io/
category: ai-analysis-automation
path:
- ai-analysis-automation
- osint-automation
bestFor: Searching a selector across data leaks, breach dumps, pastes, darknet indexes, and archived web/WHOIS in one place.
selectorsIn:
- email
- domain
- ip-address
- name
selectorsOut:
- email
- domain
- password
- name
status: live
pricing: freemium
costNote: Free account gives limited searches with redacted previews; full results, historical data, and API access require paid tiers.
opsec: passive
opsecNote: You query Intelligence X's cached/indexed data, not the subject's infrastructure, so the person is not alerted. Searches run under your account and are logged to it — use an appropriate identity. Handle any exposed credentials/PII you retrieve as sensitive; viewing leaked data can carry legal/ethical constraints depending on jurisdiction and purpose.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Well-known commercial intelligence search engine with a large archive; results are drawn from leaked/third-party data of varying accuracy and age, so corroborate.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
relatedTools:
- intelligence-x-telegram-search
- intelligencex-linkedin-search
- facebook-graph-searcher-intelligencex
- intelligence-x
- intelligence-x-2
- intelligence-x-person-tools
- intelx-io
aliases:
- Intelligence X
- intelx.io
- IntelX
tags:
- leaks
- breach-data
- darknet
- threat-intelligence
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# IntelligenceX

> A search engine over leaks, breaches, pastes, the darknet, and historical web/WHOIS — enter a selector and see where it surfaces in data that mainstream search won't index.

## When to use
You have an `email`, `domain`, `ip-address`, phone, or name and want to know if it appears in data breaches, paste dumps, leaked databases, darknet indexes, or archived web/WHOIS. It's a broad "has this been exposed / where does this appear" pivot — useful for confirming an email is real and in circulation, finding associated breach records, and surfacing leaked context tied to a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register at https://intelx.io/ (a free account gives limited, often redacted, searches).
2. Enter the selector — email, domain, IP, phone, Bitcoin address, or name.
3. Review the result buckets: leaks/breaches, pastes, darknet, web, WHOIS/domain history — each item shows a source and date.
4. Open items (full/unredacted content typically requires a paid tier) and note breach names, associated emails, and any exposed fields.
5. Pivot: associated emails/domains/usernames become new selectors; a breach name tells you what data class may be exposed.

## Inputs → Outputs
- **In:** `email`, `domain`, `ip-address`, `name`, phone, or crypto address
- **Out:** matching leak/breach/paste/darknet items — associated `email`s, `domain`s, exposed `password`-class fields, `name`s, with sources and dates
- **Empty/negative result looks like:** "no results" (or only redacted teasers on the free tier) — the selector isn't in the indexed data, or full results are paywalled; absence isn't proof of no exposure anywhere.

## Gotchas & OpSec
- Free tier heavily **redacts/limits** results; deep use needs a paid plan.
- Leaked data is **third-party, variably accurate, and often old** — corroborate before relying on any field, and never authenticate with exposed credentials.
- Legal/ethical constraints apply to viewing and using breach data — scope your purpose and jurisdiction.

## Overlaps ("do both")
- Do both with Have I Been Pwned and DeHashed: HIBP confirms breach membership cleanly, DeHashed and IntelX expose associated records — together they triangulate an account's exposure.

## Trust & verifiability
`trust: unverified` — a large, well-known commercial intelligence archive. Coverage is broad, but the underlying data is leaked/third-party of varying age and accuracy; treat hits as leads to verify, not facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | intelligencex |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | email, domain, ip-address, name → email, domain, password, name |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
