---
id: muckrock
name: MuckRock
description: Use when you want to file or search US public-records/FOIA requests and released government documents about a `name` or `employer-org` — returns document-id and address leads.
url: https://www.muckrock.com/
category: public-records
path:
- public-records
bestFor: Searching a large archive of released FOIA/public-records documents and filing new records requests to US agencies.
selectorsIn:
- name
- employer-org
selectorsOut:
- document-id
- address
- associate
status: live
pricing: freemium
costNote: Browsing and searching the public archive of completed requests and documents is free. Filing your own requests uses a credit/subscription system (some free requests, then paid bundles).
opsec: active
opsecNote: Searching the archive is passive. FILING a request is active and generally public — your name and the request text usually become part of the public record and go directly to a government agency, so never file under a real identity you want to protect, and understand a request signals your interest to the agency.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: MuckRock is an established non-profit transparency organization; hosted documents are genuine agency releases, and the platform is well regarded among journalists.
missingPersonsRelevance: medium
coverage:
- us
auth: none
api: true
localInstall: false
registration: false
aliases:
- muckrock.com
tags:
- foia
- public-records
- transparency
source: osint4all
lastVerified: '2026-07-16'
enrichment: full
relatedTools:
- state-public-records-laws
---

# MuckRock

> A public-records/FOIA platform: search a large public archive of documents already released by US government agencies, and file your own records requests through the site.

## When to use
Two modes. (1) **Search** the existing archive when your subject, their `employer-org`, or an incident might appear in documents journalists and researchers have already obtained — police records, contracts, correspondence, permits. (2) **File** a new FOIA/state-records request when the record you need isn't public yet. Released documents can contain names, `address`es, `associate`s, and official `document-id`s useful for corroboration.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.muckrock.com/ and use the search to query the archive by name, agency, topic, or keyword.
2. Open matching requests to read the released documents and the agency correspondence trail.
3. To file your own: create an account, choose the agency/jurisdiction, write the request (MuckRock handles delivery and tracking); note requests and responses are typically published.
4. Pivot: names/addresses in documents → people-search and mapping tools; agency + case numbers (`document-id`) → follow-on records requests.

## Inputs → Outputs
- **In:** `name`, `employer-org`, agency, or topic keyword (search); or a new records request (file)
- **Out:** released government documents (`document-id`) containing `address`es, `associate`s, and official identifiers.
- **Empty/negative result looks like:** no archived documents match — the topic hasn't been requested/released here; consider filing your own request or checking a state portal.

## Gotchas & OpSec
- Filing is public by default and goes to a real agency under your account — this is active and attributable; plan identity accordingly.
- FOIA is US-centric and slow; a filed request may take weeks/months and can be denied or redacted.
- Archived documents reflect what was released, often with redactions; absence isn't proof of nonexistence.

## Overlaps ("do both")
- Pairs with `[[state-public-records-laws]]` — MuckRock is the request/archive platform, that reference tells you each state's law, timelines, and what's obtainable.

## Trust & verifiability
`trust: trusted` — a reputable non-profit; hosted documents are authentic agency releases, so the source material is reliable (interpretation and redactions aside).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | muckrock |
| category | public-records |
| selectorsIn → selectorsOut | name, employer-org → document-id, address, associate |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
