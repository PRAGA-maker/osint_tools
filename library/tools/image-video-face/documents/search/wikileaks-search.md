---
id: wikileaks-search
name: WikiLeaks Search
description: Use when you have a `name`, `email`, `employer-org`, or keyword and want to find mentions in WikiLeaks' published document sets — returns matching leaked cables, emails, and files.
url: https://search.wikileaks.org/advanced
category: image-video-face
path:
- image-video-face
- documents
- search
bestFor: Full-text searching WikiLeaks' published leaks (diplomatic cables, org emails, files) for a person, address, or keyword.
selectorsIn:
- name
- email
- employer-org
selectorsOut:
- name
- email
- employer-org
- document-id
status: live
pricing: free
costNote: Free full-text search of published WikiLeaks collections; no account required.
opsec: active
opsecNote: Simply visiting WikiLeaks and searching can be sensitive in some jurisdictions/workplaces and may be monitored. Use a VPN/Tor and a clean browser; do not run these searches from an attributable corporate or government network if that matters for your situation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: The documents are genuine leaked materials, but they are unverified primary sources with agenda/selection bias; a hit proves a mention, not the truth of the surrounding claims.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- search.wikileaks.org
tags:
- documents
- leaks
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# WikiLeaks Search

> Full-text search across WikiLeaks' published collections — diplomatic cables, corporate/political email dumps, and leaked files — for any name, email, org, or keyword.

## When to use
You have a `name`, `email`, `employer-org`, or distinctive keyword and want to know whether the subject or their organisation appears in leaked document sets. Useful for surfacing correspondence, affiliations, and mentions that never appear in ordinary records — a niche but occasionally decisive lead in investigations. Its missing-person relevance is situational (mainly for subjects tied to organisations/events covered by leaks).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://search.wikileaks.org/advanced from a privacy-hardened browser (VPN/Tor).
2. Enter the `name`/`email`/`employer-org`/keyword; use the advanced fields to scope by collection, date, or exact phrase.
3. Read the results: matching documents with a `document-id`/reference, source collection, and context snippets.
4. Open documents to extract mentioned people, emails, and affiliations — but treat contents as unverified primary material.
5. Pivot: an `email` feeds email-OSINT/breach checks; named associates feed network mapping; a collection/date anchors a timeline.

## Inputs → Outputs
- **In:** `name`, `email`, `employer-org`, or keyword
- **Out:** matching leaked documents (`document-id`), mentioned `name`s/`email`s/orgs, context
- **Empty/negative result looks like:** no hits — the subject simply isn't in the published leaks (the overwhelming majority of people aren't); absence is expected and uninformative.

## Gotchas & OpSec
- OpSec: **active** in the sense that accessing WikiLeaks can itself be flagged in some networks/jurisdictions — route through a VPN/Tor and a clean environment.
- Unverified content: leaked documents carry selection bias and can contain errors or manipulated material; a mention is a lead, not proof.
- Legal sensitivity: handling leaked material may carry restrictions depending on your role/jurisdiction.

## Overlaps ("do both")
- Pairs with email/breach tools and general document search — WikiLeaks covers a specific leaked corpus; combine with broader search to place any mention in context.

## Trust & verifiability
`trust: community` — the corpus is genuine leaked material but unverified and agenda-selected; corroborate anything you rely on against independent sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wikileaks-search |
| category | image-video-face |
| selectorsIn → selectorsOut | name, email → name, email, document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
