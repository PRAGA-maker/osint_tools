---
id: telegcrack-com
name: Telegcrack
description: Use when you have a `name`/keyword and want Telegra.ph articles about or by a subject — returns matching telegra.ph posts (a common Telegram publishing surface).
url: https://telegcrack.com/
category: messaging
path:
- messaging
bestFor: Searching Telegra.ph (Telegram's article publisher) by title/keyword to surface posts that don't show up in normal search engines.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free search engine for Telegra.ph content; no account required.
opsec: passive
opsecNote: Searches an index of already-public Telegra.ph pages; the author is not notified and you never touch Telegram directly. Passive. Opening a found telegra.ph page is an ordinary web request.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An independent third-party index of Telegra.ph (billed as "the first Telegra.ph search engine", 15M+ posts); coverage depends on what it has crawled, so absence isn't proof.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Telegcrack
- Telegra.ph search
tags:
- telegram
- telegraph
- messaging-osint
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Telegcrack

> A search engine for Telegra.ph — Telegram's lightweight article publisher — that indexes millions of posts by title, surfacing long-form content normal search engines miss.

## When to use
You're investigating a subject connected to Telegram and want to find Telegra.ph articles by or about them. Telegra.ph is where Telegram users publish anonymous long-form posts (channel notes, dumps, manifestos, "abouts"), and it's poorly indexed by Google. Search a `name`, `username`, handle, org, or distinctive keyword to surface those pages.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://telegcrack.com/ (may briefly 503/rate-limit; retry).
2. Enter the subject's name/username/keyword; it matches Telegra.ph post titles/content.
3. Open promising posts and read for author bylines, linked Telegram channels/@handles, dates, and content.
4. Pivot: a linked @username or channel feeds Telegram-channel search and username enumeration; content/dates anchor a timeline.

## Inputs → Outputs
- **In:** `name`, `username`, or keyword
- **Out:** matching Telegra.ph posts → author handles/`social-profile` and linked channels
- **Empty/negative result looks like:** no posts — the subject may not use Telegra.ph, or the index hasn't crawled the page; try Google `site:telegra.ph` and dedicated Telegram search tools too.

## Gotchas & OpSec
- Coverage is limited to what Telegcrack has indexed — combine with `site:telegra.ph` dorks and other Telegram tools for completeness.
- Telegra.ph posts are anonymous by design; a match ties content to a page, not automatically to a verified person.
- OpSec: passive; nothing reaches Telegram or the author.

## Overlaps ("do both")
- Pairs with `[[lyzem-blog]]` and other Telegram channel/message search tools — this covers the Telegra.ph article surface, those cover channels/groups/messages.

## Trust & verifiability
`trust: community` — an independent index of public Telegra.ph pages; the posts are real, but attribution is only as strong as the bylines/links in the content itself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telegcrack-com |
| category | messaging |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
