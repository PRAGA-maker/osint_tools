---
id: leaked-cables
name: Leaked Cables
description: Use when you want to search leaked/declassified US diplomatic cables for a name, org or location reference — returns matching cable documents.
url: https://search.wikileaks.org/plusd/
category: image-video-face
path:
- image-video-face
- documents
- search
bestFor: Full-text search of the WikiLeaks Public Library of US Diplomacy (PlusD) — US State Department cables.
input: ''
output: ''
selectorsIn:
- name
- employer-org
- geolocation
selectorsOut:
- document-id
- name
- associate
status: live
pricing: free
costNote: Free public archive.
opsec: passive
opsecNote: Browsing is read-only over the public WikiLeaks search site; no upload of target data. Note WikiLeaks domains may be filtered on some networks — use a clean connection.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: WikiLeaks PlusD is a real, well-documented archive of US diplomatic cables. Marginal for routine missing-persons work; useful only when a subject intersects diplomatic/government records.
missingPersonsRelevance: low
coverage: [global]
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- WikiLeaks PlusD
- Public Library of US Diplomacy
tags:
- documents
- leaks
source: arf-seed
lastVerified: ''
enrichment: full
---

# Leaked Cables

> The WikiLeaks PlusD search interface — full-text search across US State Department diplomatic cables (including Cablegate and Kissinger cables).

## When to use
You have a `name`, `employer-org`, or place (`geolocation`) that plausibly appears in diplomatic, government, or NGO records — e.g. an international case, a subject with consular/government ties, or a named entity from another lead. For most domestic missing-persons cases this archive will return nothing relevant; it is a niche pivot, not a core tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://search.wikileaks.org/plusd/.
2. Enter the search term (`selectorsIn`: name, employer-org, geolocation) and use the date/classification/origin filters to narrow.
3. Open matching cables; read for named individuals, organisations and relationships (`selectorsOut`: document-id, name, associate).
4. Pivot: a named person/org feeds people-search or background work.

## Inputs → Outputs
- **In:** `name`, `employer-org`, `geolocation`
- **Out:** `document-id` (cable references), `name`, `associate` mentions in the text
- **Empty/negative result looks like:** zero matching cables — expected for ordinary private individuals.

## Gotchas & OpSec
- Coverage is diplomatic correspondence only; absence of a hit means nothing about a person's whereabouts.
- WikiLeaks domains are blocked on some corporate/government networks; access from a clean connection.
- OpSec: passive read-only search; no target data is uploaded.

## Overlaps ("do both")
- Pair with broader leak/document search if a subject is tied to government or international NGOs.

## Trust & verifiability
`trust: community` — genuine, citable primary-source archive, but low relevance to typical missing-persons casework; treat any hit as a specialised lead.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | leaked-cables |
| category | image-video-face |
| selectorsIn → selectorsOut | name, employer-org, geolocation → document-id, name, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
