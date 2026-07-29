---
id: abine-blur-app
name: Abine Blur / IronVest
description: Use when you want masked emails/phone/cards to build isolated sock-puppet identities, or to remove your own data from brokers — a privacy/opsec tool, not a target lookup.
url: https://www.abine.com
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Generating masked emails/cards for sock-puppet accounts and opting your own info out of data brokers.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: Blur (now IronVest) offers free masked email plus paid tiers for masked cards/phone and password features; DeleteMe (data-broker removal) is a paid subscription.
opsec: passive
opsecNote: This is defensive tooling for YOUR side — it isolates your investigative identities (masked email/card so a sock-puppet doesn't touch your real details) and removes your own footprint from brokers. It is not aimed at a subject and returns no target data. Treat masked-identity data as sensitive; keep a secure mapping of which mask belongs to which persona.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: community
trustNote: Abine is an established consumer-privacy company; Blur was rebranded to IronVest, and DeleteMe remains its data-removal service — reputable, though you are trusting a vendor with mask/identity data.
missingPersonsRelevance: low
coverage:
- us
auth: account
api: false
localInstall: true
registration: true
relatedTools:
- deleteme
- disconnect
aliases:
- Abine Blur
- IronVest
- Blur
tags:
- privacy
- sock-puppet
- opsec
- data-removal
source: toddington-resources
lastVerified: '2026-07-29'
enrichment: full
---

# Abine Blur / IronVest

> Abine's privacy suite — masked emails/phone/cards (Blur, now IronVest) to compartmentalize sock-puppet identities, plus DeleteMe to scrub your own info from data brokers.

## When to use
Investigator opsec, not subject lookup. Two jobs: (1) **build clean sock-puppet identities** — generate a masked email (and, on paid tiers, a masked card/phone) so an investigative account never carries your real address or payment details, keeping personas isolated from each other and from you; (2) **reduce your own exposure** — DeleteMe files opt-outs to remove your personal listings from people-search/data-broker sites so a subject can't easily turn the tables. It takes no target selector and returns no OSINT data.

## How to use it (`bestInteractionPattern`: browser-extension)
1. From https://www.abine.com, install the Blur/IronVest browser extension and create an account.
2. Generate a **masked email** per persona (free tier) — forwards to a real inbox without exposing it; use it to register sock-puppet accounts.
3. On paid tiers, generate masked cards/phone numbers for signups that demand them.
4. Keep a secure, offline mapping of mask → persona so you don't cross-contaminate identities.
5. Separately, use **DeleteMe** to submit data-broker removals for your own name/address.

## Inputs → Outputs
- **In:** none (you generate masks / submit your own removal info)
- **Out:** none about a subject — masked email/card/phone for your personas; broker opt-out coverage for you
- **Empty/negative result looks like:** N/A — success is a working mask or a filed removal; there is no query result to read.

## Gotchas & OpSec
- **Vendor trust:** you're entrusting Abine with the mask↔real mapping and (for DeleteMe) your PII — acceptable for a reputable vendor, but understand the dependency.
- Blur's rename to IronVest and tier changes mean feature availability shifts — verify the current free vs paid split.
- OpSec: **passive/defensive** — this hardens your side; combine with a hardened browser (`[[disconnect]]`) and separate sessions per persona.

## Overlaps ("do both")
- Pairs with `[[deleteme]]` (Abine's own removal service) and `[[disconnect]]` — masked identities (Blur/IronVest) + broker removal (DeleteMe) + tracker blocking (Disconnect) together form a practical investigator-hygiene stack.

## Trust & verifiability
`trust: community` — a real, established privacy vendor; the tools work as described, but they are closed services holding sensitive mapping/PII, so weigh the vendor dependency.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | abine-blur-app |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | yes (account-login) |
