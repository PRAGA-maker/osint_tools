---
id: regvk-com
name: regvk.com
description: Use when you have a VKontakte profile or group URL (a vanity `username`) and want its stable numeric ID — returns the VK id you need for deeper VK OSINT lookups.
url: http://regvk.com/id/
category: social-networks
path:
- social-networks
bestFor: Resolving a VK vanity page/group URL to its permanent numeric ID for downstream VK OSINT.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free single-purpose utility; no account or payment.
opsec: passive
opsecNote: The tool queries VK's public data about the page, not the person, and does not notify the subject. It is a Russian-language third-party site — use a clean/sock browser and avoid entering anything but the public profile URL.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Popular Russian utility for VK ID resolution; single-purpose and widely referenced in VK OSINT guides, but unofficial.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
aliases:
- RegVK
- Узнать ID ВКонтакте
tags:
- russiansocialmedia
- Russian Social Media Sites
- vkontakte
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# regvk.com

> A one-trick VK utility: paste a VKontakte page or group URL and it returns the permanent numeric ID hiding behind the vanity name — the key that unlocks the rest of VK OSINT.

## When to use
You have a VK profile or group with a custom vanity URL (e.g. `vk.com/durov`) but need its stable numeric ID (e.g. `id1`). Many VK OSINT techniques, bots, and API/scraper tools key on the numeric ID, not the changeable vanity name; a subject can rename their vanity URL, but the numeric ID never changes. Reach for this at the start of a VK dive to pin the account to an immutable identifier.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://regvk.com/id/ (Russian-language; a browser translator helps).
2. Paste the target VK page or group URL into the input.
3. Submit — it returns the numeric ID for that page/group.
4. Pivot: feed the numeric ID into VK friend-mapping tools, VK OSINT bots (e.g. QuickOSINT-style), or the VK API/scrapers to pull friends, mentions, linked phone hints, and account creation date.

## Inputs → Outputs
- **In:** `username` (VK vanity page/group URL)
- **Out:** `social-profile` (the VK numeric ID / canonical profile reference)
- **Empty/negative result looks like:** an error or no ID — the page is deleted, private, or the URL was malformed. It does NOT confirm the person doesn't have a VK; re-check the URL and try VK's own search.

## Gotchas & OpSec
- Human-in-the-loop: none; it is a single form.
- The site is Russian-language and unofficial — enter only the public profile URL, nothing sensitive.
- The numeric ID is the durable identifier; record it so a later vanity-URL change doesn't lose you the account.
- OpSec: passive; the subject is not notified.

## Overlaps ("do both")
- Pairs with VK friend/network mappers and VK data-scraper tools — this resolves the ID; those consume it to enumerate the subject's VK connections and metadata.

## Trust & verifiability
`trust: community` — a well-known single-purpose utility; the ID it returns is directly checkable against VK itself, so correctness risk is low.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | regvk-com |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
