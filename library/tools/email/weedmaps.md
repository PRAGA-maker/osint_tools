---
id: weedmaps
name: Weedmaps
description: Use cautiously — an unidentified page hosted on a Keybase public folder; its actual function (an OSINT writeup/guide named "WEEDMAPS") could not be confirmed from name or URL.
url: https://bloopbase.keybase.pub/POPPY/WEEDMAPS/index.html
category: email
path:
- email
bestFor: Unconfirmed — appears to be a hosted OSINT note/guide page rather than a queryable tool.
selectorsIn: []
selectorsOut: []
status: unknown
pricing: free
costNote: Static page on a free Keybase public hosting folder; no paywall implied.
opsec: passive
opsecNote: Reading a static hosted page contacts only Keybase's CDN, not any target; but the page's content and intent are unverified.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Hosted on an individual's Keybase public folder (bloopbase.keybase.pub/POPPY/WEEDMAPS) under the name "Weedmaps". Not a recognized OSINT service; function unconfirmed and content may be stale or gone. Verify before relying on it.
missingPersonsRelevance: unknown
coverage: []
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- email
- unverified
source: osint4all
lastVerified: ''
enrichment: full
---

# Weedmaps

> An unidentified page hosted on a personal Keybase public folder. Despite the name, there is no evidence this is the cannabis-dispensary site Weedmaps.com — it appears to be a self-hosted OSINT note or guide, but its actual content and purpose are unconfirmed.

## When to use
Honest answer: unclear. The entry was harvested into the email category from the `osint4all` list, but the URL is a static file on someone's Keybase public storage, not a queryable service. Open it only to inspect what the page actually contains before deciding whether it's useful; do not assume it performs any email lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://bloopbase.keybase.pub/POPPY/WEEDMAPS/index.html and read what is actually there.
2. Determine whether it is a written guide/notes page, a redirect, a link dump, or dead.
3. If it is a methodology writeup, treat it as reference reading; if it is a link collection, follow and evaluate the linked tools individually.
4. Do not feed it selectors expecting a result — there is no confirmed input/output behavior.

## Inputs → Outputs
- **In:** none confirmed
- **Out:** none confirmed
- **Empty/negative result looks like:** a 404/dead Keybase folder, or a static text/HTML page with no interactive function. Either is the expected case until verified otherwise.

## Gotchas & OpSec
- The categorization as an "email" tool is not corroborated by the URL — do not trust the category here.
- Keybase public folders are individually owned and can disappear or change without notice.
- OpSec: passive (you only fetch a static page), but the destination is an untrusted personal host — fetch via sock infrastructure if footprint matters.

## Trust & verifiability
`trust: unverified` — a personally-hosted page of unconfirmed content and purpose, not a recognized tool. No fabricated capabilities are claimed here; the entry is retained only as a pointer to verify manually.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | weedmaps |
| category | email |
| selectorsIn → selectorsOut | (unconfirmed) |
| pricing / cost | free |
| trust | unverified |
| MP relevance | unknown |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
