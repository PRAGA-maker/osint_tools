---
id: phoneinfoga-demo
name: PhoneInfoga (demo)
description: Use when you have a `phone` and want automated number reconnaissance — returns country/carrier/line-type plus search-engine footprints (profiles, leaks, ads) tied to the number.
url: https://demo.phoneinfoga.crvx.fr
category: phone
path:
- phone
bestFor: Scanning a phone number for its carrier/line-type and surfacing where it appears online (social profiles, classified ads, breaches) via search-engine dorks.
selectorsIn:
- phone
selectorsOut:
- name
- social-profile
- geolocation
status: live
pricing: free
costNote: Free and open-source (self-host the CLI/web from sundowndev/phoneinfoga). The public demo instance is a convenience and may be down or rate-limited.
opsec: passive
opsecNote: Number-plan lookups are passive. The search-engine/dork footprinting queries Google/Bing/DuckDuckGo, not the subject — but heavy dorking from your IP can trip captchas and is attributable; self-host and use a proxy for sensitive work rather than the shared demo.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: PhoneInfoga is a widely-used, well-maintained open-source phone-OSINT framework (sundowndev). The demo is a third-party hosted instance; results depend on which scanners are configured.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- emobiletracker-com
aliases:
- PhoneInfoga
- phoneinfoga demo
tags:
- phone
- phone-recon
- osint-framework
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# PhoneInfoga (demo)

> The go-to open-source phone reconnaissance framework: identify a number's carrier and line-type, then dork the web for everywhere that number shows up.

## When to use
You have a `phone` and want more than a carrier lookup: PhoneInfoga first validates the number and reports country, area, carrier and line-type (mobile/landline/VoIP), then runs search-engine reconnaissance (Google/Bing/DuckDuckGo dorks) to find the number in social profiles, classified ads, pastebins, and data-breach mentions. It's the standard tool for turning a bare number into online footprints and a candidate owner.

## How to use it (`bestInteractionPattern`: web-manual)
1. Use the demo at https://demo.phoneinfoga.crvx.fr for a quick try, or (recommended for real work) self-host from `github.com/sundowndev/phoneinfoga` via CLI/Docker.
2. Enter the `phone` in full international format.
3. Read the local scan: country, carrier, line-type, validity.
4. Run the footprint scanners: they generate dork links / query engines to surface the number online (you may need to solve a Google captcha to proceed).
5. Pivot: a discovered `social-profile`/`name` feeds account and people-search tools; carrier/region context narrows follow-up.

## Inputs → Outputs
- **In:** `phone`
- **Out:** carrier/line-type + `geolocation` (country/area), and `name`/`social-profile` footprints found via search engines
- **Empty/negative result looks like:** valid carrier data but no online footprints. Many private numbers simply aren't posted anywhere indexable — an empty footprint result means "not found via dorks," not that the owner has no presence.

## Gotchas & OpSec
- The demo instance may be offline, outdated, or rate-limited — self-host for reliable, current scanners.
- Footprinting depends on search-engine dorks and can hit captchas (`GOOGLE_ABUSE_EXEMPTION`); solve manually.
- It does NOT geolocate a live phone or "hack" it — carrier/region only.
- OpSec: local lookup is passive; dorking from your IP is attributable — proxy it and prefer self-hosting for sensitive cases.

## Overlaps ("do both")
- Pairs with `[[emobiletracker-com]]` — both give carrier/region, but PhoneInfoga adds the search-engine footprinting layer that finds where the number appears online. Run PhoneInfoga for depth, the lighter tool for a fast sanity check.

## Trust & verifiability
`trust: community` — PhoneInfoga is a reputable, actively-maintained open-source framework. The carrier/line-type data is reliable; the search-engine footprints are leads to confirm, and the *demo* instance's freshness is not guaranteed — self-host for authoritative results.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | phoneinfoga-demo |
</content>
