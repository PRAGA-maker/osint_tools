---
id: scotland-landlord-search
name: Scottish Landlord Register Search
description: Use when you have a Scottish rental-property `address` (postcode) or a landlord registration number and want to find who owns/manages it — returns landlord/agent name, contact address, and local authority.
url: https://www.landlordregistrationscotland.gov.uk/search/start
category: people-search
path:
- people-search
bestFor: Identifying the registered landlord or letting agent of a rental property in Scotland by postcode.
selectorsIn:
- address
- document-id
selectorsOut:
- name
- address
- associate
status: live
pricing: free
costNote: Free official Scottish Government service; no account or payment required.
opsec: passive
opsecNote: Public register lookup; anonymous and server-side, with no notification to the landlord or occupant. No sock puppet required.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Scottish Government / Scottish local authorities; the statutory landlord register.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Scottish Landlord Register
- landlordregistrationscotland.gov.uk
tags:
- address
- property
- scotland
- uk
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# Scottish Landlord Register Search

> Scotland's statutory landlord register: turn a rental-property postcode into the name and contact address of the landlord or letting agent responsible for it.

## When to use
You have the `address` (postcode) of a rental property in Scotland — or a landlord `document-id` registration number — and want to know who owns or manages it. This is a strong lead for locating a person through a property they let, identifying a subject's landlord/letting agent, or verifying a claimed address. It complements England/Wales tools like `[[residential]]` (VOA) that do not cover Scotland or return a responsible-party name.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.landlordregistrationscotland.gov.uk/search/start (service is in beta).
2. Choose a search method:
   - **By property postcode** → returns ownership/management info, the relevant local authority, and a contact address for that property.
   - **By landlord registration number** (`document-id`) → returns registration validity, whom it belongs to, and the associated local authority.
3. Read the result: landlord/agent `name`, contact `address`, and council area.
4. Pivot: the landlord/agent `name` and contact `address` feed people-search and corporate-registry lookups; a letting agent is an `associate` lead toward the actual owner.

## Inputs → Outputs
- **In:** `address` (postcode) OR `document-id` (registration number)
- **Out:** landlord/agent `name`, contact `address`, local authority; plus `associate` links (agent ↔ owner)
- **Empty/negative result looks like:** no registration found — the property may be owner-occupied (not a rental), the postcode wrong, or the landlord non-compliant/unregistered. You cannot search by landlord name.

## Gotchas & OpSec
- Search is **only** by postcode or registration number — there is no name search, so you cannot go person → properties here.
- The contact address is often a letting agent, not the landlord's home; treat it as a routing point, not necessarily a residence.
- Covers Scotland only. OpSec: passive; no notification to anyone.

## Overlaps ("do both")
- Pairs with `[[residential]]` (VOA, England & Wales) for UK-wide coverage — do both, since the two services cover different nations and this one adds a responsible-party name.

## Trust & verifiability
`trust: trusted` — the statutory register maintained by Scottish local authorities via the Scottish Government platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scotland-landlord-search |
| category | people-search |
| selectorsIn → selectorsOut | address, document-id → name, address, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
