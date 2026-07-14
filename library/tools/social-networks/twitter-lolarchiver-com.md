---
id: twitter-lolarchiver-com
name: twitter.lolarchiver.com
description: Use when you have a Twitter/X `username` or user ID and want its history of handle, display-name, bio, location and website changes — returns a timeline of past profile values.
url: https://twitter.lolarchiver.com/
category: social-networks
path:
- social-networks
bestFor: Recovering a Twitter/X account's former usernames, display names, bio locations and websites over time.
selectorsIn:
- username
selectorsOut:
- username
- name
- geolocation
- domain
status: live
pricing: freemium
costNote: Basic history lookups are free; the wider lolarchiver ecosystem gates deeper/bulk features and other platforms behind paid credits.
opsec: passive
opsecNote: You query the archive, not Twitter/X, so the target is not notified. But you are handing the subject's handle to lolarchiver — a third-party doxx-adjacent archive of dubious provenance — which logs your lookups. Use a sock-puppet and treat the operator as untrusted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party scraped archive with no accountability; data may be stale, partial or wrong, and the site's broader ecosystem is associated with doxxing. Corroborate anything it returns.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- spoonbill-io
- memory-lol
aliases:
- lolarchiver twitter
- twitter username history
tags:
- xtwitter
- X / Twitter Related Sites
- username-history
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# twitter.lolarchiver.com

> A historical profile-lookup for Twitter/X: enter a handle or user ID and get past usernames, display names, bios, locations and websites over time.

## When to use
You have a Twitter/X `username` (or numeric user ID) and need what the account *used to be* — prior handles, old display names, former bio text, listed location and website across time. This is the key move when someone has renamed or scrubbed an account: the numeric ID stays constant while the handle changes, and this archive maps the handle history back to it. Excellent for re-linking a person to an account they've since rebranded or abandoned.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://twitter.lolarchiver.com/ in a sock-puppet browser.
2. Enter the Twitter/X `username` or numeric user ID and submit.
3. Read the returned history: username changes, display-name changes, past bios, bio locations and websites, with rough date ranges (coverage runs ~2011–Jan 2023 and again 2026 onward, with a gap between).
4. Note that any given field may be incomplete or absent depending on when the archive sampled the account.
5. Pivot: an old handle feeds username enumeration elsewhere; a past bio location feeds geolocation; a listed website/`domain` feeds domain/WHOIS OSINT.

## Inputs → Outputs
- **In:** `username` or numeric user ID
- **Out:** historical `username`s, display `name`s, bio `geolocation`, listed `domain`/website
- **Empty/negative result looks like:** no history rows or "not found" — the account may be outside the archive's coverage window or never sampled; absence is not proof the account never changed.

## Gotchas & OpSec
- Coverage has a gap (roughly 2023–2025), so recent changes in that window may be missing.
- Provenance is dubious: lolarchiver is a scraped third-party archive tied to a doxxing-adjacent ecosystem. Data can be stale or wrong — corroborate every finding against another source.
- Passive to the target (they aren't notified), but you expose your lookup to an untrusted operator; use a sock-puppet.

## Overlaps ("do both")
- Pairs with `[[memory-lol]]` and `[[spoonbill-io]]` — both track Twitter/X handle/display-name history from more accountable sources; cross-check lolarchiver's output against them before trusting a former handle.

## Trust & verifiability
`trust: unverified` — an anonymous scraped archive with no guarantees on accuracy or ethics. Treat every result as a lead to confirm elsewhere, never as established fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twitter-lolarchiver-com |
| category | social-networks |
| selectorsIn → selectorsOut | username → username, name, geolocation, domain |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
