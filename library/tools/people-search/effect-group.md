---
id: effect-group
name: Effect Group (EffectAI)
description: Use when you have a name, email or phone and want an aggregated OSINT profile — returns linked profiles, contact data, breach hits and face/logo image matches.
url: https://effectgroup.io/
category: people-search
path:
- people-search
bestFor: A pay-per-use aggregated people/company search that fuses web data, breach data and image recognition into one report.
selectorsIn:
- name
- email
- phone
- image
selectorsOut:
- social-profile
- email
- phone
- associate
- employer-org
- face
status: live
pricing: freemium
costNote: Pay-per-use with no meaningful free tier — searches start around €9.95 each, billed per query rather than by subscription. Budget before running; results volume/quality varies by selector.
opsec: passive
opsecNote: Searches run against Effect Group's aggregated datasets, not the target's own accounts, so it does not directly alert the subject. You must create an account and pay, so your identity/payment is known to the vendor — use appropriate billing and a sock-puppet where policy allows. Aggregated broker data can be stale or wrong; verify before acting.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial OSINT aggregator marketed to journalists, investigators and due-diligence users; useful breadth, but it is a data broker whose sourcing is opaque, so treat outputs as leads to verify.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Effect Group
- EffectAI
- effectgroup.io
tags:
- people-search
- osint-aggregator
- breach-data
- face-recognition
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# Effect Group (EffectAI)

> A commercial, pay-per-search OSINT aggregator that fuses web data, breach records and image recognition — one query returns a broad (if broker-grade) profile of a person or company.

## When to use
You have a `name`, `email`, `phone` or `image` and want a fast, wide first pass that pulls many sources at once — linked social profiles, contact data, employer/company links, data-breach appearances, and face/logo image matches. Effect Group pitches itself at journalists, lawyers and investigators and claims billions of profiles with 170+ data points. It is a breadth tool: good for surfacing leads quickly, provided you then verify each one against a primary source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://effectgroup.io/ and create an account (registration + payment method required; there is no real free tier).
2. Choose a search type — people search by `name`/`email`/`phone`, company/officer search, or image analysis (face/logo).
3. Run the query (each search is billed, ~€9.95+); review the aggregated report.
4. Extract the concrete selectors — `social-profile`s, `email`/`phone`, `employer-org`, `associate`s, breach hits — and note which source each came from.
5. Pivot: confirm each lead in a first-party source (the actual profile, a registry, a breach-notification tool) before relying on it; feed image matches into a dedicated reverse-face tool for a second opinion.

## Inputs → Outputs
- **In:** `name`, `email`, `phone`, or `image`
- **Out:** `social-profile`, `email`, `phone`, `associate`, `employer-org`, and `face`/logo image matches, plus breach appearances
- **Empty/negative result looks like:** a thin report or no matches — common for people with a light online footprint, or when the aggregator's datasets don't cover the region. A sparse result is not proof of absence; try a different selector.

## Gotchas & OpSec
- **Paid, per-search** — no usable free tier; costs add up, so scope your query before spending.
- It is a **data broker**: sourcing is opaque and records can be stale, merged from the wrong person, or region-limited. Every output is a lead to verify, not a fact.
- Account + payment mean the vendor knows who you are; consider that for sensitive investigations.
- Passive toward the target, but treat breach/PII data within lawful and ethical scope.

## Overlaps ("do both")
- Pairs with free first-party tools (`[[free-public-records-directory-us]]`, platform lookups) to verify — the aggregator finds the lead, the primary source confirms it.
- Complements a dedicated reverse-face engine to independently check its image matches.

## Trust & verifiability
`trust: community` — a commercial aggregator with real breadth but undisclosed sourcing; never treat a hit as confirmed on its own. Corroborate names, contacts and image matches against authoritative sources before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | effect-group |
| category | people-search |
| selectorsIn → selectorsOut | name, email, phone, image → social-profile, email, phone, associate, employer-org, face |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial, account-login) |
