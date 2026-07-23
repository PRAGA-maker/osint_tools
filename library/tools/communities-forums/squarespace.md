---
id: squarespace
name: Squarespace
description: Use when you have a `domain` or `username` and want to confirm a personal/business site is Squarespace-hosted and mine it for owner contact and social links — returns `social-profile` / `email` leads.
url: https://www.squarespace.com
category: communities-forums
path:
- communities-forums
bestFor: Recognising and profiling a Squarespace-built personal or small-business website tied to a subject.
selectorsIn:
- domain
- username
selectorsOut:
- social-profile
- email
status: live
pricing: freemium
costNote: Building a site is paid, but viewing any published Squarespace site is free; you are consuming published pages, not the builder.
opsec: passive
opsecNote: Passive browsing of a public site is unattributable beyond normal web-server logs. Do NOT sign up or use the contact form to probe — that is active and identifiable. Use a clean browser for sensitive targets.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Squarespace is a legitimate hosting platform; the OSINT value is in individual user-built sites, whose accuracy varies by owner and is unverified.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- wappalyzer
- builtwith
aliases:
- SquareSpace
- squarespace.com
tags:
- forums
- website-builder
- hosting
source: metaosint
lastVerified: '2026-07-23'
enrichment: full
---

# Squarespace

> A major website-builder host — recognisable footprints let you confirm a subject's site is Squarespace-built and harvest the owner contact and social links it exposes.

## When to use
You have a `domain` (a subject's personal or small-business site) or a `username`/brand and want to (a) confirm the site is Squarespace-hosted — a signal about how it was built and where else the owner may have footprints — and (b) pull the owner's published contact details: email, phone, social icons, booking/scheduling links. Squarespace sites almost always surface a contact page and linked social profiles that pivot straight to other platforms.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the subject's site (or search `site:squarespace.com <name/brand>` and free `*.squarespace.com` subdomains for un-migrated sites).
2. Confirm the platform: view source for `static1.squarespace.com` assets, `Squarespace` in the HTML, or check via `[[wappalyzer]]` / `[[builtwith]]`.
3. Read the contact/about pages for `email`, phone, and location; note the footer/header social icons (`social-profile` links).
4. Check `robots.txt`/sitemap and hidden pages (e.g. `/config`, unlinked slugs) for extra content.
5. Pivot: linked social profiles feed username-search; a business email/phone feeds people- and company-lookups.

## Inputs → Outputs
- **In:** `domain` or `username`/brand
- **Out:** platform confirmation, owner `email`/phone, linked `social-profile`s, location text
- **Empty/negative result looks like:** the site isn't Squarespace (no Squarespace assets in source), or a bare template with no contact info — try the platform-detection tools and WHOIS instead.

## Gotchas & OpSec
- Custom domains hide the host; you must inspect source or use a tech-detection tool to confirm Squarespace.
- Contact details are owner-published and may be stale or a business front rather than the individual.
- OpSec: passive read only. Never submit the contact form or start a trial to "test" — that alerts the owner and ties the probe to you.

## Overlaps ("do both")
- Pairs with `[[wappalyzer]]` and `[[builtwith]]` — they confirm the Squarespace fingerprint and reveal other tech (analytics IDs, trackers) that can correlate the site with a subject's other properties.

## Trust & verifiability
`trust: community` — Squarespace itself is a reputable host, but the intelligence value lives in individual user-built sites whose content is self-published and therefore unverified; corroborate any lead.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | squarespace |
| category | communities-forums |
| selectorsIn → selectorsOut | domain, username → social-profile, email |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
