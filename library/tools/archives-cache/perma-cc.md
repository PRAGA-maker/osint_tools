---
id: perma-cc
name: Perma.cc
description: Use when you have a web page `domain`/URL that is evidence and want a permanent, citable archived snapshot — returns a stable perma-link (`document-id`) that won't rot or be edited.
url: https://perma.cc/
category: archives-cache
path:
- archives-cache
bestFor: Creating tamper-evident, permanent archived snapshots of web pages for evidence preservation and citation.
selectorsIn:
- domain
selectorsOut:
- document-id
status: live
pricing: freemium
costNote: Viewing existing perma-links is free and open to anyone. Creating links is free for users affiliated with participating libraries/courts and for a limited monthly quota; heavier use needs a paid/registrar tier.
opsec: passive
opsecNote: Perma.cc's servers (not your machine) fetch and capture the target page, so the capture request comes from Perma's infrastructure, not your IP. Creating a link ties the snapshot to your Perma account, so use an appropriate account. Viewing a perma-link is anonymous.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Harvard Law School Library Innovation Lab in partnership with a consortium of libraries; a scholarly-grade, tamper-evident web-archiving service.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- perma.cc
- Perma
tags:
- archive
- Archive & Cached Related Sites
- web-archiving
- evidence-preservation
source: uk-osint
lastVerified: '2026-07-21'
enrichment: full
---

# Perma.cc

> Harvard's evidence-grade web archiver: turn a live page that might change or vanish into a permanent, citable snapshot before it's gone.

## When to use
You've found a web page — a social profile, a news article, a listing, a forum post — that matters to a case and could be edited or deleted at any moment. Perma.cc captures a fixed, timestamped snapshot at a stable `perma.cc/XXXX-XXXX` URL you can cite and revisit, so your evidence survives even if the original is taken down. Also use it to *view* perma-links others created.

## How to use it (`bestInteractionPattern`: web-manual)
1. To preserve a page: sign in to https://perma.cc/ (a free account, ideally via a participating library/court), paste the target URL, and create a perma-link.
2. Perma's servers fetch and archive the page (rendered capture + metadata) and issue a permanent `perma.cc/…` link.
3. Record that perma-link as your citable `document-id`; it won't rot or change even if the source does.
4. To view an existing perma-link, just open the `perma.cc/XXXX-XXXX` URL — no account needed.
5. Pivot: capture *before* you interact with or contact anyone tied to the page, so the untouched state is preserved for the record.

## Inputs → Outputs
- **In:** `domain`/URL of a live page to preserve
- **Out:** `document-id` — a permanent perma-link (archived snapshot + capture timestamp)
- **Empty/negative result looks like:** a capture that renders incompletely (heavy-JS or login-gated pages may archive partially or blank) — verify the snapshot actually captured the content you need before relying on it.

## Gotchas & OpSec
- Human-in-the-loop: creating links requires an **account**; free capture quota is limited unless you're affiliated with a partner institution.
- Login-walled or aggressively dynamic pages may not capture fully — check the snapshot, and pair with a full-page screenshot as backup.
- OpSec: **passive** — Perma fetches the page, not you; but capture *before* any outreach so you preserve the pristine state.

## Overlaps ("do both")
- Pairs with the Wayback Machine and archive.today — Perma gives you a tamper-evident, institution-backed capture for citation, while the others give broad, retroactive historical coverage. Archive to all three for redundancy.

## Trust & verifiability
`trust: trusted` — run by the Harvard Law School Library Innovation Lab and a library consortium specifically for reliable, court-citable web preservation. Captures are authoritative snapshots; just confirm each one rendered the content correctly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | perma-cc |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → document-id |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
