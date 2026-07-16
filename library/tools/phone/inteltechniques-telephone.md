---
id: inteltechniques-telephone
name: IntelTechniques Telephone
description: Use when you have a `phone` number and want to fan it across many phone-OSINT sources at once via Michael Bazzell's search-form tool — returns `name`, `address`, `social-profile`, carrier leads from the linked services.
url: https://inteltechniques.com/tools/Telephone.html
category: phone
path:
- phone
bestFor: A consolidated set of phone-number search forms that push one number to many reverse-lookup, carrier, and social sources.
selectorsIn:
- phone
selectorsOut:
- name
- address
- social-profile
status: live
pricing: free
costNote: Free to use; maintained by Michael Bazzell as a companion to the OSINT Techniques book (tools last updated Nov 2024). Some destination services it links to have their own paywalls.
opsec: passive
opsecNote: The tool only builds and submits queries — it doesn't contact the target. But each form hands your number to a third-party service that logs it (and some, like carrier/HLR or messaging apps, can be more intrusive). Run from a sock-puppet browser/IP and be deliberate about which forms you fire.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Created by Michael Bazzell (former FBI, widely respected OSINT author); the tool itself is authoritative as a query launcher, though result quality depends on the third-party sources.
missingPersonsRelevance: high
coverage:
- global
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- IntelTechniques phone search tool
- Bazzell telephone tool
tags:
- phone
- osint-framework
- reverse-phone-lookup
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- email-assumptions
- email-search-tool-by-inteltechniques
- google-document-dorks-inteltechniques-method
- instagram-search-inteltechniques-method
- instagram-tool-inteltechniques-com
- inteltechniques-business-search-tool
- inteltechniques-facebook
- inteltechniques-osint
- inteltechniques-tools-search-engines-suite
- inteltechniques-twitter
- user-name-search-intel-techniques
---

# IntelTechniques Telephone

> Michael Bazzell's phone-number search console — one field that launches the same number across dozens of reverse-lookup, carrier, and social-search sources.

## When to use
You have a `phone` number and want to sweep it across many phone-OSINT services efficiently, without hand-typing each site. It's the phone module of the well-regarded IntelTechniques search-tools suite — a strong, structured starting point for reverse-phone work before you commit to any single (often paywalled) source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://inteltechniques.com/tools/Telephone.html (part of the broader tool suite at inteltechniques.com/tools/).
2. Enter the target `phone` number once.
3. Use the individual buttons to launch that number into specific sources (reverse-lookup sites, carrier lookups, messaging-app checks, social searches), or the "submit all" style options.
4. Work through the results, noting which sources return a `name`/`address`/`social-profile`.
5. Pivot: confirmed name/address → people-search; carrier/line type → `[[numverify-api]]`; a linked account → email/social OSINT.

## Inputs → Outputs
- **In:** `phone` number
- **Out:** `name`, `address`, `social-profile`, carrier/line-type leads aggregated from the launched sources
- **Empty/negative result looks like:** destination sites return nothing or paywalled teasers — common for mobiles/VoIP. A blank/broken form usually means a linked third-party site changed, not that the number is invalid.

## Gotchas & OpSec
- It's a launcher — it inherits the coverage, paywalls, and reliability of whatever sources it points at.
- Some forms (carrier/HLR, app-presence checks) are more intrusive than a passive lookup — choose deliberately.
- Passive toward the target, but every downstream site logs your number; use a sock puppet.

## Overlaps ("do both")
- Pairs with `[[numverify-api]]` (validation/carrier) and `[[thatsthem-phone-search]]` (US owner data) — IntelTechniques routes you to many sources fast, those give deeper single-purpose results.

## Trust & verifiability
`trust: trusted` — a respected, maintained OSINT resource; the launcher is reliable, but verify each result at its source since the underlying data is third-party.
