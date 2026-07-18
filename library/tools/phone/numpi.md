---
id: numpi
name: Numpi
description: Use when you have a US `phone` number and want to identify the owner — returns possible name, location, and carrier/line type from a reverse-lookup directory.
url: https://numpi.com/
category: phone
path:
- phone
bestFor: Reverse-lookup of a US phone number to a possible owner name and location.
selectorsIn:
- phone
selectorsOut:
- name
- address
status: live
pricing: freemium
costNote: Basic reverse-lookup surfaces some data free; full owner reports are typically gated behind a paid/upsell step.
opsec: passive
opsecNote: You query Numpi's aggregated directory, not the number's owner — the subject is not called or notified. You disclose the target number to a US data broker; use a clean session and avoid entering numbers you must keep siloed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A commercial US reverse-phone/data-broker aggregator; matches are probabilistic and drawn from mixed public/marketing sources, so treat owner attributions as leads to confirm.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- numpi.com
tags:
- reverse-phone
- people-search
- phone
source: inteltechniques-tools
lastVerified: '2026-07-18'
enrichment: full
---

# Numpi

> A US reverse-phone people-lookup: paste a number and get a candidate owner name, location, and line details from an aggregated directory.

## When to use
You have a US `phone` number and want to attach an identity to it — a candidate owner `name`, general location (`address`/city), and carrier/line type. Useful early in a case for turning an unknown number into a lead, or corroborating that a number ties to a known subject. Treat results as probabilistic, not proof.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://numpi.com/.
2. Enter a valid 10-digit US number and run the lookup.
3. Read the free-tier output: possible owner name, city/region, carrier/line type; deeper "full report" fields are usually an upsell.
4. Don't pay the upsell reflexively — cross-check the free signal against other reverse-lookup sources first.
5. Pivot: a candidate `name` feeds people-search and social tools; carrier/line type informs whether it's mobile/VoIP/landline.

## Inputs → Outputs
- **In:** US `phone` (10-digit)
- **Out:** candidate owner `name`, general `address`/location, carrier/line type
- **Empty/negative result looks like:** "no information" or only carrier/line data — common for mobiles, VoIP, prepaid, or unlisted numbers; absence isn't proof the number is inactive.

## Gotchas & OpSec
- Data-broker attributions are **probabilistic and often stale** — a returned name may be a prior owner or a household member; always corroborate.
- Expect an upsell/paywall for the "full" report; the free layer is what to rely on for quick triage.
- Coverage is **US-only**; foreign numbers won't resolve.
- OpSec: passive; you disclose the number to a broker — use a clean session.

## Overlaps ("do both")
- Pairs with other reverse-phone sources (Truecaller, carrier/HLR lookups) and messenger account-existence checks (run the number across WhatsApp/Telegram) — cross-source agreement is what turns a broker guess into a confident attribution.

## Trust & verifiability
`trust: community` — a commercial aggregator, not an authoritative source. Its value is generating leads fast; every owner attribution needs independent confirmation before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | numpi |
