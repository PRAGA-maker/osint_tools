---
id: justpaste
name: JustPaste.it
description: Use when you have a JustPaste.it link (or a paste id) found in a breach, chat, or search hit and want to read the shared rich text/images before it is deleted — returns pasted `document-id` content.
url: https://justpaste.it
category: communities-forums
path:
- communities-forums
bestFor: Reading or capturing anonymous rich-text/image pastes shared via a JustPaste.it link.
selectorsIn:
- username
selectorsOut:
- document-id
- image
status: live
pricing: free
costNote: Free to read and to publish; no account required to post. Launched 2009; supports anonymous pastes with rich text, code, and inline images.
opsec: passive
opsecNote: Reading a paste by URL is passive and anonymous. If you publish a paste you get a private edit key, but content is public to anyone with the link and is not truly private — never post target data or your own notes here.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-established, legitimate paste/text-sharing platform; the site is trustworthy but paste *content* is user-generated and unverified, and it has historically hosted extremist and leaked material.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- hastebin
- rentry
- controlc-pastebin
- dpaste
aliases:
- JustPaste.it
- justpaste.it
- Just Paste
tags:
- pastebins
- paste-sites
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# JustPaste.it

> A popular anonymous rich-text/image pastebin: retrieve the formatted text and embedded images behind a JustPaste.it link found in your investigation.

## When to use
A JustPaste.it URL has surfaced — in a chat, forum post, breach index, Telegram channel, or search result — and you need to read what was shared before it is edited or removed. Because it supports rich text *and* inline images and requires no account, it is heavily used to drop dumps, manifestos, contact lists, and propaganda; the content behind a link can be direct evidence or a strong pivot.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the paste URL directly, e.g. `https://justpaste.it/<id>`.
2. Read the rendered content and note any embedded images (right-click to save/reverse-search them).
3. Capture immediately — full-page screenshot plus save the text and images — because the author holds an edit key and can alter or delete the paste at any time.
4. Pivot: extract selectors from the body (emails, handles, phones, wallets, IPs) and reverse-search embedded images; note the paste id and any author handle referencing it.

## Inputs → Outputs
- **In:** a JustPaste.it id / URL (often shared by a `username` you are tracking)
- **Out:** `document-id` — the rich-text body plus any embedded `image`, and whatever selectors they contain
- **Empty/negative result looks like:** "not found" / 404 — the paste was deleted or expired; try the Wayback Machine or a search cache of the id, as the live content is gone.

## Gotchas & OpSec
- Mutable and deletable: the owner's edit key lets them change or remove content, so archive on first sight.
- Unverified content: a paste claiming to be a subject's data may be fabricated or misattributed — corroborate before relying on it.
- OpSec: reading is passive/anonymous. Never publish target data or notes here; a "private" toggle only hides it from listings, not from anyone with the link.

## Overlaps ("do both")
- Same family as `[[hastebin]]`, `[[rentry]]`, `[[controlc-pastebin]]`, and `[[dpaste]]` — when a lead references "a paste," sweep the paste-site ecosystem, since actors post to whichever host is convenient and often cross-post.

## Trust & verifiability
`trust: community` — the platform is legitimate and long-running, but treat each paste's *content* as unverified and potentially manipulated until independently confirmed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | justpaste |
| category | communities-forums |
| selectorsIn → selectorsOut | username → document-id, image |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
