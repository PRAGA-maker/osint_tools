---
id: sony-archives
name: Sony Archives
description: Use when a person may appear in the leaked Sony Pictures email corpus — search a name/email/employer-org to surface their messages and contacts.
url: https://wikileaks.org/sony/emails/
category: email
path:
- email
bestFor: Searching the WikiLeaks Sony Pictures email dump for a specific person, address, or organization.
selectorsIn:
- name
- email
- employer-org
selectorsOut:
- email
- name
- associate
- metadata-exif
status: live
pricing: free
costNote: Fully free, public WikiLeaks archive.
opsec: passive
opsecNote: Read-only search of a hosted archive; the subject is not contacted or notified. Note that WikiLeaks access may be logged or geoblocked, so use a sock-puppet connection.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Authentic, widely-reported leaked corpus published by WikiLeaks; scope is narrow (Sony Pictures, ~2014-2015), so relevance is rare but high when present.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- email
- leak
- wikileaks
source: osint4all
lastVerified: ''
enrichment: full
---

# Sony Archives

> WikiLeaks' searchable archive of leaked Sony Pictures emails — a corpus you can query by name, address, or org.

## When to use
A missing or sought person (or a close associate) had a connection to Sony Pictures or the entertainment/media industry circa 2014-2015. Searching by `name`, `email`, or `employer-org` can surface their correspondence, contacts (`associate`), and historical email behavior. Narrow corpus, so this is a targeted check, not a general lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://wikileaks.org/sony/emails/ in a sock-puppet browser session.
2. Use the search box to query a person's `name`, an `email`, or a company/`employer-org`.
3. Read the matched threads: senders/recipients, dates, body text, and attachments.
4. Pivot: extracted `associate` names, alternate `email` addresses, and timeline details feed people-search and timeline reconstruction.

## Inputs → Outputs
- **In:** `name`, `email`, or `employer-org`
- **Out:** matching emails — `name`s, `associate` links, additional `email` addresses, dates/`metadata-exif`
- **Empty/negative result looks like:** zero hits — almost always the case unless the person was inside or corresponding with Sony Pictures in that window.

## Gotchas & OpSec
- Extremely narrow scope: only useful for people tied to this specific leak; expect no results for most subjects.
- OpSec: passive read-only search; the subject is never notified. WikiLeaks may be geoblocked or logged in some networks — use a neutral connection.

## Overlaps ("do both")
- One of many leak/archive corpora; pair with broader breach search engines and other WikiLeaks collections when a media/corporate link is suspected.

## Trust & verifiability
`trust: community` — authentic, heavily-reported leaked dataset hosted by WikiLeaks; content is genuine but its relevance to any given case is rare.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sony-archives |
| category | email |
| selectorsIn → selectorsOut | name, email, employer-org → email, name, associate, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
