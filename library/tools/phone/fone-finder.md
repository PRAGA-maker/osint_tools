---
id: fone-finder
name: Fone Finder
description: Historical reference only — the classic NPA-NXX carrier/location lookup is defunct; the domain now funnels to affiliate people-search, so route to a live phone tool instead.
url: https://www.fonefinder.net/
category: phone
path:
- phone
bestFor: Historical reference only — legacy phone-prefix-to-carrier/location lookup, no longer reliable.
selectorsIn:
- phone
selectorsOut:
- geolocation
status: down
pricing: freemium
costNote: The original free NPA-NXX lookup is effectively dead; the current page routes to paid affiliate people-search offers rather than serving authoritative prefix data.
opsec: passive
opsecNote: Don't rely on it operationally (flagged defunct in this library). If you do land on the page, treat the "search anybody" boxes as affiliate lead-gen — anything you enter goes to a commercial people-search partner, so use a sock-puppet and don't submit sensitive numbers.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Once a well-known NPA-NXX (area code + exchange) carrier/location reference, but number portability gutted its accuracy and the site has degraded into affiliate people-search; not a dependable source today.
missingPersonsRelevance: high
coverage:
- us
auth: account
api: false
localInstall: false
registration: true
deprecated: true
relatedTools:
- numlookup
- twilio-lookup
- phoneinfoga
aliases:
- FoneFinder
- fonefinder.net
tags:
- phone
- carrier-lookup
- defunct
source: arf-seed
lastVerified: '2026-07-14'
enrichment: full
---

# Fone Finder

> A legacy phone-prefix (NPA-NXX) to carrier/location lookup — now defunct as an authoritative source and degraded into affiliate people-search; kept so an agent recognises it and routes elsewhere.

## When to use
Effectively never, as a live tool. Fone Finder was once the go-to for mapping a North American number's area code + exchange (NPA-NXX) to its carrier and rough geographic location, plus some international prefix data. Two things killed its usefulness: US/Canada number portability broke the prefix→carrier assumption, and the site has since shifted toward affiliate "search anybody" lead-gen. Recognise the name in old guides, then use a maintained phone tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Don't depend on fonefinder.net for carrier/location — portability makes legacy prefix data unreliable and the current site pushes paid people-search.
2. For carrier/line-type today, use a live number-intelligence API or tool.
3. If you only need the historical geographic *origin* of a prefix (not the current carrier), a modern NPA-NXX reference is more trustworthy than this page.

## Inputs → Outputs
- **In:** `phone` (historically an NPA-NXX prefix)
- **Out:** historically the original carrier and `geolocation` of the prefix; today, mostly affiliate people-search prompts
- **Empty/negative result looks like:** the page redirecting into a paid people-search funnel, or returning prefix data that's wrong due to portability — treat any carrier claim here as unverified.

## Gotchas & OpSec
- `status: down` / `deprecated` — flagged defunct in this library; don't spend a step trying to make it authoritative.
- Number portability means legacy prefix→carrier mappings are frequently wrong for real subscribers.
- The current "search anybody" boxes are affiliate lead-gen — whatever you type goes to a commercial partner.

## Overlaps ("do both")
- Replace with `[[numlookup]]` (current carrier/line-type), `[[twilio-lookup]]` (authoritative programmatic number intelligence), or `[[phoneinfoga]]` (OSINT-oriented number recon) — all maintained where Fone Finder is not.

## Trust & verifiability
`trust: unverified` — historically reputable but now unreliable: portability undermines its core data and the site has degraded into affiliate marketing. Use a modern number-intelligence source instead.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fone-finder |
| category | phone |
| selectorsIn → selectorsOut | phone → geolocation |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
