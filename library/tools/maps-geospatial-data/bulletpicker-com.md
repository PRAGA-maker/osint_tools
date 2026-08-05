---
id: bulletpicker-com
name: BulletPicker
description: Use when you have an `image` of munitions/ordnance and want a reference to identify the type, origin or markings — returns matches from military ammunition guidebooks and manuals.
url: https://www.bulletpicker.com/index.html
category: maps-geospatial-data
path:
- maps-geospatial-data
bestFor: Reference identification of ammunition, projectiles, fuzes and ordnance seen in imagery (conflict/verification OSINT).
selectorsIn:
- image
selectorsOut: []
status: live
pricing: free
costNote: Free reference library; no account. Run by Bulletpicker, LLC (not a government/DoD entity).
opsec: passive
opsecNote: Passive — you browse a public reference library; nothing about your case is transmitted. Standard sock-puppet browsing hygiene applies.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: An independent collection of scanned/reformatted ordnance guidebooks and manuals; a strong reference aid, but the site itself says to verify against other official references and not to treat it as EOD/UXO instruction.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Bulletpicker
- bulletpicker.com
tags:
- ordnance
- munitions
- reference
source: uk-osint
lastVerified: '2026-08-05'
enrichment: full
---

# BulletPicker

> A free reference library of ammunition and ordnance guidebooks — the go-to lookup when you need to identify a munition, projectile, fuze or marking spotted in an image.

## When to use
You're doing conflict, weapons or verification OSINT and have an `image` of ordnance (a shell, cartridge, fuze, grenade, bomblet, or its markings) that you need to identify — type, calibre, country of origin, model. BulletPicker aggregates military ammunition manuals and guidebooks you can browse to match what you're seeing. It is a reference aid for identification research, not EOD/handling guidance.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.bulletpicker.com/ and browse by category (e.g. projectiles, fuzes, small arms, grenades, pyrotechnics).
2. Compare your `image`'s shape, dimensions, colour-coding and stencil/headstamp markings against the reference plates and manuals.
3. Narrow to a candidate type/model and note origin and nomenclature.
4. Cross-verify the identification against another authoritative source before publishing — the site explicitly advises this.

## Inputs → Outputs
- **In:** `image` (a munition/ordnance photo or its markings)
- **Out:** reference identification (type, calibre, origin, nomenclature — no enum selector)
- **Empty/negative result looks like:** no matching plate means the item may be non-standard, improvised, or outside the manuals held here — try specialist databases or expert channels.

## Gotchas & OpSec
- Human-in-the-loop: identification is manual, comparison-driven work requiring care and, ideally, expert confirmation.
- Not authoritative and not handling guidance — never treat it as EOD/UXO instruction; it's for remote identification research only.
- Coverage is broad but not exhaustive; markings and colour codes vary by era and country.

## Overlaps ("do both")
- Pair with reverse-image search and conflict-monitoring/verification tools: those geolocate and source the image, BulletPicker names the ordnance in it.

## Trust & verifiability
`trust: community` — a well-regarded independent reference built from real military manuals; reliable for research leads, but confirm any identification against a second authoritative source as the site itself instructs.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bulletpicker-com |
| category | maps-geospatial-data |
| selectorsIn → selectorsOut | image → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
