---
id: controlc-pastebin
name: ControlC Pastebin
description: Use when you have a paste ID/link or a leaked snippet and want to read or host plain-text content anonymously — a pastebin where dumped data (`email`, `phone`, credentials) often surfaces.
url: https://controlc.com
category: communities-forums
path:
- communities-forums
bestFor: Reading or hosting anonymous text pastes; a site where leaked/dumped personal data is sometimes posted.
selectorsIn:
- username
- email
selectorsOut:
- email
- phone
- username
status: live
pricing: free
costNote: Free to view and create pastes. Registration is optional; paid/registered accounts add features like never-expiring pastes.
opsec: passive
opsecNote: Viewing a paste is passive and does not notify anyone. Creating a paste hosts content publicly — never paste real target data or your own investigative notes there. ControlC has no full-text search, so you generally reach pastes via a direct link found through a search engine or a breach index; treat content as unverified and potentially planted.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running independent pastebin (formerly controlc.com / "anonymous pastebin"); content is user-generated and unvetted, so anything found is a lead to corroborate, not a source of truth.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- controlc
- anonymous pastebin
tags:
- pastebins
- leaks
source: awesome-osint
lastVerified: '2026-07-15'
enrichment: full
---

# ControlC Pastebin

> A free anonymous text-hosting site (a Pastebin alternative) where dumped credentials, contact lists, and dox occasionally appear — worth checking when a selector shows up in paste indexes.

## When to use
You have a paste link or ID (surfaced via a search engine, a breach aggregator, or a dork), or you want to read text someone hosted anonymously. As an OSINT surface, ControlC matters because leaked data — email/password combos, phone lists, personal dumps — is sometimes posted to pastebins. If a target's `email`/`username` turns up in a ControlC paste, it may reveal associated `phone`/`email`/credentials.

## How to use it (`bestInteractionPattern`: web-manual)
1. To read: open the direct paste URL (`https://controlc.com/<id>`) in a sock-puppet browser. There is no reliable on-site full-text search, so find pastes via Google dorks (`site:controlc.com "<selector>"`) or a paste-monitoring/breach index.
2. Read the content; note that pastes can be password-protected or set to expire (1–72h, or never for registered users).
3. To host neutral text yourself: paste content, optionally set a password/expiry, solve the CAPTCHA, and share the link. **Do not** post real target PII or case notes.
4. Pivot: selectors found in a paste (`email`, `phone`, `username`) feed breach-check and people-search tools to corroborate.

## Inputs → Outputs
- **In:** paste ID/link, or a selector you are hunting for across paste indexes
- **Out:** free-text content that may contain `email`, `phone`, `username`, or credential material
- **Empty/negative result looks like:** a 404/expired paste, a password-locked paste you cannot open, or no dork hits — none of which prove the selector was never leaked (it may be on another paste host).

## Gotchas & OpSec
- Human-in-the-loop: a CAPTCHA gates posting; expired/password-locked pastes cannot be read.
- No native search — you depend on external indexing to find relevant pastes.
- OpSec: viewing is passive; **never** host real investigative data here. Content is unverified and can be deliberately planted or fabricated.

## Overlaps ("do both")
- Pairs with `[[pastebin-com]]`-style paste sites and breach indexes — the same leak is often mirrored across multiple hosts, so check several; confirm any credential/PII hit against a breach-lookup tool.

## Trust & verifiability
`trust: community` — an unvetted user-content host; anything found is a raw lead. Corroborate every selector before relying on it, and assume some pastes are fake or stale.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | controlc-pastebin |
