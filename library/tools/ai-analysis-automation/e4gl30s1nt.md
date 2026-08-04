---
id: e4gl30s1nt
name: E4GL30S1NT
description: Use when you have a `username`, `email`, `phone`, `domain` or `image` and want a single CLI toolkit that sweeps 70+ platforms, breach databases and metadata — returns social-profiles, breach hits, carrier/geolocation and extracted identifiers.
url: https://github.com/C0MPL3XDEV/E4GL30S1NT
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: All-in-one CLI recon on a person's selectors — username enumeration, breach lookups, phone/email and image metadata in one toolkit.
selectorsIn:
- username
- email
- phone
- domain
- image
selectorsOut:
- social-profile
- email
- geolocation
status: live
pricing: free
costNote: Free and open-source (GPL-3.0). Some modules (breach lookups like DeHashed/LeakCheck) work better with your own API keys.
opsec: active
opsecNote: It queries many social platforms and breach services live, so your IP hits 70+ sites and several breach APIs per run. Use a VPN/proxy and dedicated research API keys; note it auto-masks PII in output, but the queries themselves are observable to the platforms and breach providers.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Community CLI toolkit (C0MPL3XDEV, ~700 stars); breadth-focused, so verify each hit manually.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- eagleosint
- eagle-osint
tags:
- toolkit
- username-enumeration
- breach-lookup
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# E4GL30S1NT

> A bundled CLI OSINT toolkit ("EagleOSINT") that runs username reconnaissance across 70+ platforms plus email, phone, breach, DNS and image-metadata modules from one interface.

## When to use
You have a person's selector — `username`, `email`, `phone`, `domain`, or an `image` — and want a fast, broad first pass: where the handle exists, whether the email/phone appears in breaches, the phone's carrier, GPS from image EXIF, and basic infrastructure lookups, all stored in one investigation session.

## How to use it (`bestInteractionPattern`: cli)
1. Install (Python 3.11+): Linux one-line installer, or manual `git clone https://github.com/C0MPL3XDEV/E4GL30S1NT` + `uv` setup across platforms.
2. Add API keys for the breach modules (Have I Been Pwned, DeHashed, LeakCheck) to unlock their full output.
3. Run the tool and choose a module for your selector (username sweep, email/phone lookup, breach check, metadata extraction, DNS/WHOIS/IP).
4. Read the structured JSON/CSV output — matched profiles, breach records, carrier/geo data — with PII auto-masked.
5. Pivot: confirmed `social-profile`/`email` hits feed platform-specific and email tools; breach records corroborate identity linkage.

## Inputs → Outputs
- **In:** `username`, `email`, `phone`, `domain`, `ip-address`, or `image`/PDF file.
- **Out:** `social-profile` matches across 70+ sites, breach-exposure records, phone carrier + `geolocation`, image GPS, and DNS/WHOIS data.
- **Empty/negative result looks like:** "not found"/empty modules — common for rare handles or when breach keys are absent; not a definitive negative.

## Gotchas & OpSec
- Human-in-the-loop: breach modules need your own API keys; without them, coverage is limited.
- Enumeration across 70+ sites is noisy and prone to false positives (soft-404s) — verify each hit.
- Handle breach data lawfully and store the masked output; don't over-trust auto-linked identities.

## Overlaps ("do both")
- Overlaps single-purpose enumerators like `[[slash]]` (username breadth) and in-browser `[[intelhub]]`; run E4GL30S1NT for a scripted all-selector sweep, then a dedicated tool for depth on the strongest lead.

## Trust & verifiability
`trust: community` — a community toolkit whose strength is breadth; every hit is a lead to confirm by opening the source, never a vetted identity match.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | e4gl30s1nt |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username, email, phone, domain, image → social-profile, email, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key) |
