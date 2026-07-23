---
id: bookmarkee-bookmark-organizer
name: Bookmarkee Bookmark Organizer
description: Use when you need a free, account-based place to organize and access investigation links from any device — a personal bookmark manager, not a data-source.
url: https://www.bookmarkee.com
category: documents-metadata
path:
- documents-metadata
bestFor: Keeping a private, cross-device set of links/leads for a case in one dashboard.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Explicitly free — no charge, no ads, no email spam per the site. Requires a registered account.
opsec: passive
opsecNote: This is workflow infrastructure, not a lookup — but you are storing your investigation's links on a third-party server tied to an email/password. Use a dedicated sock-puppet account and never store links that reveal the target or your identity; mark pages private (default), not public.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: Long-standing free consumer bookmark service (500k+ users); it holds whatever links you save, so treat it as untrusted storage.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- Bookmarkee
tags:
- documents-metadata
- workflow
- bookmark-manager
- toddington
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# Bookmarkee Bookmark Organizer

> A free personal bookmark manager — investigator plumbing for keeping case links organised and reachable from any device, not a source of intelligence in itself.

## When to use
You are running an investigation across machines/browsers and want a single private dashboard of the URLs and leads you have gathered. This is a productivity/organisation tool: it does not enrich or resolve any selector, it just stores and retrieves the links you feed it.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.bookmarkee.com and register an account (use a sock-puppet email/password).
2. Add links to your dashboard; keep pages set to private (the default) so only you can see them after login.
3. Access the same set from any device by logging in.
4. Pivot: this is a holding pen — the actual investigative work happens in the source tools you save links to.

## Inputs → Outputs
- **In:** URLs you choose to save (no selector input)
- **Out:** an organised, retrievable list of your saved links (no selector output)
- **Empty/negative result looks like:** nothing — it only ever contains what you put in.

## Gotchas & OpSec
- Human-in-the-loop: requires account creation and login.
- OpSec: your saved links live on a third-party server. Do not store anything that ties you to the target or reveals sensitive case detail; keep pages private, never public.
- No API, no import from selectors — purely manual organisation.

## Overlaps ("do both")
- Overlaps with any local note/link-keeping workflow; there is no OSINT data-source it duplicates. Prefer an offline or self-hosted notes system when case sensitivity is high.

## Trust & verifiability
`trust: unverified` — a consumer convenience service with a large user base but no security guarantees; safe only for non-sensitive link organisation under a throwaway account.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bookmarkee-bookmark-organizer |
| category | documents-metadata |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
