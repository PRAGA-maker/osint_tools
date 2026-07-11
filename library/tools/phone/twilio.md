---
id: twilio
name: Twilio Lookup
description: Use when you have a `phone` and want carrier, line-type, caller-name (CNAM) and SIM-swap/validity intelligence — returns carrier, line type and often the account holder `name`.
url: https://www.twilio.com/docs/lookup/v2-api
category: phone
path:
- phone
bestFor: Programmatic phone-number intelligence — validity, carrier, line type, caller name (CNAM), SIM-swap signals.
selectorsIn:
- phone
selectorsOut:
- name
- metadata-exif
status: live
pricing: freemium
costNote: Paid API — a Twilio account is required and most Lookup data packages (carrier, caller-name, SIM-swap) are billed per lookup. Basic format validation is free/cheap; enriched fields cost per query.
opsec: passive
opsecNote: Queries Twilio's carrier data, not the subject's device — the target isn't contacted or notified by a Lookup. Your Twilio account is billed and logs the queries, so use a dedicated investigative account.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: api
trust: trusted
trustNote: Twilio is a major, reputable telecom API provider; carrier/line-type data is authoritative, though CNAM caller-name is US-centric and not always populated.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: false
registration: true
aliases:
- Twilio Lookup API
- Twilio phone lookup
tags:
- phone-number-research
- carrier-lookup
- cnam
- sim-swap
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Twilio Lookup

> Twilio's Lookup v2 API: turn a raw `phone` number into structured intelligence — is it valid, which carrier, mobile vs landline vs VoIP, the caller name (CNAM), and SIM-swap risk signals.

## When to use
You have a `phone` number and need to know what it *is* before acting on it: valid and in service? Mobile, landline or VoIP (VoIP hints at a burner/virtual number)? Which carrier and country? Who does CNAM say it belongs to? These answers shape how much weight to give a number and whether it's likely the subject's real personal line.

## How to use it (`bestInteractionPattern`: api)
1. Create a Twilio account and get your Account SID + Auth Token (registration required; enriched packages are billed).
2. Call Lookup v2: `GET https://lookups.twilio.com/v2/PhoneNumbers/+1XXXXXXXXXX?Fields=line_type_intelligence,caller_name,sim_swap` with your credentials.
3. Read the JSON: validity, carrier, `line_type` (mobile/landline/voip), `caller_name` (CNAM), and SIM-swap/last-porting signals where available.
4. Weigh the result: a VoIP line type suggests a virtual/disposable number; a populated CNAM name is a strong (US) identity lead.
5. Pivot: feed a CNAM `name` into people-search; a carrier + region narrows geography; VoIP steers you to virtual-number provider OSINT.

## Inputs → Outputs
- **In:** `phone` (E.164)
- **Out:** validity, carrier, `line_type`, caller `name` (CNAM), SIM-swap/porting `metadata-exif` signals
- **Empty/negative result looks like:** invalid/unreachable number, or enriched fields empty (CNAM unpopulated, especially outside the US) — a valid number with no caller name is common and not a dead end.

## Gotchas & OpSec
- **Paid** — enriched fields (caller-name, line-type, SIM-swap) bill per lookup; budget accordingly.
- CNAM caller-name is US-centric and frequently blank elsewhere.
- Line-type "VoIP" flags virtual/burner numbers — useful signal, not proof of intent.
- Queries are logged/billed to your Twilio account — use a dedicated one.

## Overlaps ("do both")
- Pairs with free number tools ([[phonebooks-com]], reverse-lookup sites) and account-existence checks — Twilio gives authoritative carrier/line-type/CNAM; the others add subscriber name/address and app-registration hits.

## Trust & verifiability
`trust: trusted` — a major telecom provider; carrier/line-type data is authoritative. Caller-name is best-effort (US CNAM), so corroborate a name before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twilio |
| category | phone |
| selectorsIn → selectorsOut | phone → name, metadata-exif |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | api |
| opsec | passive |
| human-in-loop | yes (api-key) |
