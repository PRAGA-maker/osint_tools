---
id: breach-vip
name: breach.vip
description: Use when you have an `email`, `username`, `phone`, `domain`, `ip-address`, or platform ID (Discord/Steam) and want leaked credential records tied to it — returns breach fields.
url: https://breach.vip/
category: email
path:
- email
- email-search
bestFor: Searching aggregated breach dumps by email, username, name, password, phone, domain, IP, or platform ID.
input: Email, username, name, password, phone, domain, IP, Discord ID, Steam ID, or Minecraft UUID
output: Selected fields of matching breached records
selectorsIn:
- email
- username
- name
- phone
- domain
- ip-address
selectorsOut:
- email
- username
- name
- phone
- ip-address
- associate
status: live
pricing: freemium
costNote: Public search interface with API docs; some depth/volume is typically gated (paid/credits or Telegram channel) on breach aggregators like this. Free queries available; confirm current limits on site.
opsec: passive
opsecNote: Queries the operator's aggregated breach corpus; no contact with the target. You disclose the queried selector to breach.vip — never query your own real identifiers; use a research context. Source is leaked data — handle results lawfully and minimise retention.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Anonymous breach-aggregator service with an API and Telegram channel. Powerful for pivoting (wildcards, cross-field search) but the operator is unaccountable; treat records as leads to verify.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- alerts-bar
- ashley-madison-hacked-email-checker
- arkowl-com
aliases:
- breach vip
tags:
- email
- breach-search
- credential-lookup
source: arf-seed
lastVerified: '2026-06-13'
enrichment: full
---

# breach.vip

> A cross-field breach-aggregator: search leaked records by almost any selector — email, username, name, phone, domain, IP, password, even Discord/Steam IDs — with wildcards.

## When to use
You have any one strong selector (`email`, `username`, `phone`, `domain`, `ip-address`, a `name`, a known `password`, or a platform ID) and want to pull the leaked records linked to it — to expand into other identifiers (alternate emails, reused usernames, phone numbers, associates) and confirm an address is real and exposed. Strong, central pivot tool for a missing-persons digital footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://breach.vip/.
2. Pick a field (Email, Username, Name, Password, Phone, Domain, IP Address, Discord ID, Steam ID, Minecraft UUID) and enter the selector; wildcards and case-sensitive filters are supported.
3. Read the returned breached-record fields. Cross-field pivots are the value: e.g. a username that recurs across breaches, or a second email sharing a password hash.
4. For automation, use the documented API.
5. Pivot: new emails → `[[arkowl-com]]`/`[[alerts-bar]]`; usernames → username tools; phones → phone OSINT.

## Inputs → Outputs
- **In:** `email`, `username`, `name`, `phone`, `domain`, `ip-address` (the UI also accepts a known password string and platform IDs)
- **Out:** matching breach record fields — linked `email`/`username`/`name`/`phone`/`ip-address`, leaked passwords, and `associate` links
- **Empty/negative result looks like:** no matching records — the selector isn't in this aggregator's corpus; not proof of no exposure (try `[[alerts-bar]]` or the specific `[[ashley-madison-hacked-email-checker]]`).

## Gotchas & OpSec
- Result depth/volume is often gated (paid/credits or Telegram) on aggregators like this — confirm current free limits.
- OpSec: passive toward the target, but you reveal the queried selector to an anonymous operator — use a sock-puppet context and never your own identifiers.
- Ethics/legality: this is leaked personal data. Use only for lawful, authorised investigation; minimise what you store and how you share it.

## Overlaps ("do both")
- Pairs with `[[alerts-bar]]` (org-level breach monitoring) and the niche `[[ashley-madison-hacked-email-checker]]`; feed discovered emails into `[[arkowl-com]]` for enrichment. Different aggregators hold different dumps — query more than one.

## Trust & verifiability
`trust: unverified` — an anonymous breach-aggregator with no accountable operator; the cross-field search is genuinely powerful, but every record is a lead to corroborate against a primary source before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | breach-vip |
| category | email |
| selectorsIn → selectorsOut | email, username, phone, domain, ip-address → email, username, name, phone, password, associate |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
