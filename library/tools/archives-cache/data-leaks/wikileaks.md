---
id: wikileaks
name: WikiLeaks
description: Use when you have a `name`, org, or topic and want to find them inside WikiLeaks' published leak collections — returns document-id, name, email.
url: https://wikileaks.org/
category: archives-cache
path:
- archives-cache
- data-leaks
bestFor: Full-text searching high-impact leaked document/email collections (diplomatic cables, email dumps) for a person or organization.
selectorsIn:
- name
- employer-org
selectorsOut:
- document-id
- name
- email
status: degraded
pricing: free
costNote: Free to read and search all published material; no account. Some historical collections/search endpoints are intermittently offline.
opsec: active
opsecNote: Reading is technically passive, but accessing published classified/leaked material can carry legal, employment, or policy exposure in some jurisdictions and organizations, and the site may log requests. Use Tor/a sandbox and a sock-puppet; understand your own risk before querying named individuals.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Documents are primary leaked source material (often authentic and verifiable), but WikiLeaks curates selectively and adds partisan framing — verify individual documents, treat commentary skeptically.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- leaked-cables
- dnc-email-database
- macron-campaign-emails
- sony-archives
- gi-files
aliases:
- WikiLeaks
- wikileaks.org
tags:
- data-leaks
- archives
- leaked-documents
source: arf-seed
lastVerified: '2026-07-16'
enrichment: full
---

# WikiLeaks

> Publisher/archive of high-impact leaks: full-text-search collections like the diplomatic cables and email dumps for any name or organization that surfaces in them.

## When to use
You have a `name`, `employer-org`, or topic and want to know whether that person/entity appears in one of WikiLeaks' published corpora — the US diplomatic cables (Cablegate/PlusD), the DNC/Podesta/Macron email dumps, the Sony archives, the GI Files, and others. A hit places the subject in a documented communication or record, and can leak secondary selectors: an `email` address, a job/`employer-org`, associates, or dates. It is a niche corroboration source, not a general person-finder.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://wikileaks.org/ (over Tor/a sandboxed browser). Use the site search, or go directly to a collection's dedicated searchable database (e.g. the Public Library of US Diplomacy / PlusD, or the email-archive search pages).
2. Query the subject's `name`, `email`, or organization. For email dumps, search both the display name and any known address.
3. Read the hit: the document/cable/email text, its date, sender/recipient identities, and reference ID (`document-id`).
4. Pivot: harvested emails/names feed email- and people-OSINT; a cable reference ID is citeable; cross-check the document's authenticity against independent reporting.

## Inputs → Outputs
- **In:** `name`, `employer-org` (or an email/keyword)
- **Out:** matching `document-id`s (cables/emails/files), plus `name`s and `email`s exposed inside them
- **Empty/negative result looks like:** no hits — the subject simply isn't in any published collection (the vast majority of people aren't). Absence says nothing about the person; it only means they're not in these specific leaks. Some searches may also fail due to the site's degraded/offline endpoints.

## Gotchas & OpSec
- Human-in-the-loop: none functionally, but consider the **legal/policy** implications before accessing leaked classified material.
- OpSec: treated as **active** here — attribution and legal exposure risk. Use Tor and a disposable environment; never query from a work/attributable connection.
- Reliability is partial: parts of the site and older search tools are intermittently down (`status: degraded`). Content is curated and framed — verify each document independently.

## Overlaps ("do both")
- Do both with the dedicated collection tools (`[[leaked-cables]]`, `[[dnc-email-database]]`, `[[macron-campaign-emails]]`, `[[sony-archives]]`) — those give purpose-built search UIs over individual dumps that the main site search covers unevenly.

## Trust & verifiability
`trust: community` — primary leaked documents that are frequently authenticatable, but selection and commentary are partisan; cite the underlying document, not WikiLeaks' framing, and corroborate before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wikileaks |
| category | archives-cache |
| selectorsIn → selectorsOut | name, employer-org → document-id, name, email |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
