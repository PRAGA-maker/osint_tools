---
id: fastmail-usa
name: Fastmail (USA)
description: Use when you need operational sock-puppet email infrastructure (or to interpret an `email` whose domain is Fastmail-hosted) — provides private mailboxes, Masked Email aliases, and custom-domain hosting.
url: https://www.fastmail.com
category: email
path:
- email
bestFor: Standing up a clean, privacy-respecting sock-puppet mailbox (or masked aliases) for investigative account signups.
selectorsIn:
- email
selectorsOut:
- email
status: live
pricing: freemium
costNote: Paid subscription service (tiered, from a few USD/month) with a 30-day no-card free trial. No permanent free tier — budget for it as investigative infrastructure, not a lookup.
opsec: passive
opsecNote: This is infrastructure you control, not a query against a target. Its OSINT value is defensive/operational — creating burner mailboxes that don't leak to ad networks, and Masked Email aliases so each sock-puppet signup gets a unique address. Never register a puppet with details that tie back to you.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
bestInteractionPattern: web-manual
trust: trusted
trustNote: Established (20+ year) independent email provider based in Australia; first-party service, not a scraper. Reputation for privacy and no ad-based data mining.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
relatedTools:
- protonmail
- account-live-com
aliases:
- Fastmail
tags:
- toddington
- curated-directory
- email-addresses
- sock-puppet-infrastructure
source: toddington-resources
lastVerified: '2026-07-14'
enrichment: full
---

# Fastmail (USA)

> A paid, privacy-first email provider used as investigator infrastructure: clean sock-puppet mailboxes and per-signup Masked Email aliases.

## When to use
Two cases. (1) You need a durable, low-attribution mailbox to run sock-puppet accounts for an investigation and want a provider that won't mine or resell the address — Fastmail's Masked Email generates a unique alias per site so a burn doesn't cascade. (2) You are analysing a target's `email` and the domain's MX records point to Fastmail (`*.messagingengine.com`) — that tells you the mailbox is Fastmail-hosted, useful for provider-fingerprinting a custom domain.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.fastmail.com and start the free trial (or a paid plan) from a sock-puppet identity — never your real name/payment if the puppet must stay clean.
2. For per-signup isolation, enable **Masked Email** and generate a fresh alias for each account you register elsewhere.
3. To fingerprint a target address instead, look up the domain's MX records separately; Fastmail-hosted domains resolve to `in1-smtp.messagingengine.com` / `in2-smtp.messagingengine.com`.
4. Pivot: use the puppet mailbox to register on other OSINT platforms, and confirm-existence lookups like `[[account-live-com]]` against the target's own address.

## Inputs → Outputs
- **In:** `email` (a target address to provider-fingerprint) or your own operational need
- **Out:** `email` (controlled sock-puppet mailbox / masked aliases; or the fact that a target domain is Fastmail-hosted)
- **Empty/negative result looks like:** the target domain's MX does not point to Fastmail — it's hosted elsewhere; this tool tells you nothing more about that address.

## Gotchas & OpSec
- Human-in-the-loop: **account-login** and a **partial payment wall** — no permanent free tier, so this is a budgeted operational cost.
- OpSec: **passive** toward any target; the risk is your own — keep the puppet's registration details, payment, and IP disconnected from your real identity.
- This is not a people-search or breach tool; do not expect it to reveal anything about a stranger beyond provider fingerprinting.

## Overlaps ("do both")
- Pairs with `[[protonmail]]` as an alternative privacy-mailbox provider, and with `[[account-live-com]]` — Fastmail supplies the puppet address you then use to run existence checks against targets elsewhere.

## Trust & verifiability
`trust: trusted` — a long-established first-party provider. The trust rating reflects the operator's reputation; it does not imply any investigative data quality, since this is infrastructure rather than a data source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fastmail-usa |
| category | email |
| selectorsIn → selectorsOut | email → email |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
