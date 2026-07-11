---
id: cyberbackgroundchecks
name: CyberBackgroundChecks
description: Use when you have a `name`, `phone`, or `address` in the US and want current/past addresses, phone numbers and named relatives for free — returns name, phone, address, associate.
url: https://www.cyberbackgroundchecks.com/
category: people-search
path:
- people-search
bestFor: Free US people-search returning address history, phones and a relatives/associates graph.
selectorsIn:
- name
- phone
- address
selectorsOut:
- name
- phone
- address
- associate
status: live
pricing: free
costNote: The core people-search results — addresses, phones, relatives — are shown for free without an account. Deeper "background report" tiers are upsold to paid partners, but you rarely need them for OSINT pivots.
opsec: passive
opsecNote: Third-party aggregator; querying does not alert the target. The site is Cloudflare-protected and may present a challenge. Only your own IP is exposed, so use a VPN/sock-puppet if you don't want the lookup tied to you. There is a self-serve opt-out/removal form — do not use it, and be aware records may be suppressed by subjects who have opted out.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: Independent commercial data broker aggregating US public records and marketing data; strong for relatives/address history but not authoritative and can be stale or conflate same-name people.
missingPersonsRelevance: high
coverage:
- us
auth: none
api: false
localInstall: false
registration: false
aliases:
- CBC
- CyberBackground
- cyberbackgroundchecks.com
tags:
- people-search
- us-records
- relatives
source: inteltechniques-tools
lastVerified: '2026-07-11'
enrichment: full
---

# CyberBackgroundChecks

> A free US people-search that turns a name, phone, or address into an address history plus a graph of named relatives and associates.

## When to use
You have a US-based `name` (optionally with city/state), a `phone`, or an `address`, and you want to build out the person's contact history and family/associate network without paying. Its relatives-and-associates listing is the standout feature: it is often the fastest free way to enumerate a subject's likely family members and former co-residents to open new lines of inquiry.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.cyberbackgroundchecks.com/ in a clean/sock-puppet browser.
2. Choose the search mode — Name, Phone, or Address — and enter your `selectorsIn`. For names, add a state to reduce collisions.
3. Submit; solve any Cloudflare/captcha challenge manually.
4. Pick the matching record from the candidate list (match on approximate age/city). The detail page shows:
   - Current and historical `address` list.
   - Associated `phone` numbers.
   - **Possible relatives and associates** — each is a clickable named person.
5. Pivot: relatives/associates become new subjects; a phone or address feeds `[[idcrawl]]` and other reverse lookups; corroborate any single-source address before acting on it.

## Inputs → Outputs
- **In:** `name`, `phone`, or `address`
- **Out:** `name`, `phone`, `address`, `associate`
- **Empty/negative result looks like:** "No results found" or a record with an age/city that doesn't match your subject — a same-name mismatch is not a hit.

## Gotchas & OpSec
- Human-in-the-loop: Cloudflare challenge/captcha appears intermittently; solve manually.
- US-only coverage and marketing-data sourcing mean stale addresses and occasional wrong-person merges — verify against a second source.
- Subjects can opt out, so absence is not proof of non-existence.
- Passive toward the target; only your IP is exposed to the broker.

## Overlaps ("do both")
- Pairs with `[[idcrawl]]` — CyberBackgroundChecks is stronger on address history and relatives; IDCrawl is stronger on social profiles. Run both and cross-check the relatives against social connections.

## Trust & verifiability
`trust: community` — a commercial data broker, not an authoritative record source. Its relatives graph is unusually useful but must be corroborated; treat single-source addresses/phones as leads.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cyberbackgroundchecks |
| category | people-search |
| selectorsIn → selectorsOut | name, phone, address → name, phone, address, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
