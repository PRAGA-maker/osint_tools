---
id: prankshit-com-2
name: prankshit.com
description: Use when you have a screenshot of a `phone`/`username` WhatsApp "chat" and want to know whether it could be fabricated — this is a fake-chat generator, so it tells you what forged evidence looks like.
url: https://prankshit.com/fake-whatsapp-chat-generator.php
category: messaging
path:
- messaging
bestFor: Understanding and recognising fabricated WhatsApp screenshots — a counter-disinformation reference, not a data source.
selectorsIn:
- phone
- username
selectorsOut: []
status: live
pricing: free
costNote: Free browser tool; an optional €2 payment removes the watermark for 2 hours. Everything runs client-side with no account.
opsec: passive
opsecNote: Runs entirely in your browser with no database, so nothing you type is stored server-side. Never use it to fabricate evidence — its only investigative value is defensive, to learn the tells of forged chats.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: A novelty/entertainment site openly marketed as a fake-chat generator; there is no data provenance because it produces no real data.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- prankshit-com
aliases:
- Fake WhatsApp Chat Generator
- prankshit
tags:
- whatsapp
- WhatsApp
- fake-evidence
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# prankshit.com

> A fake WhatsApp chat generator — catalogued here defensively: know it exists so you can recognise when a "WhatsApp screenshot" handed to you is manufactured.

## When to use
Not a lookup tool. Reach for it when someone presents a WhatsApp conversation as evidence (a "message from the missing person," a threat, an alibi) and you need to gauge how easily that screenshot could have been faked. Generating a sample yourself teaches you the artefacts — perfect timestamps, editable read-receipts, arbitrary names/photos, no metadata — that betray a fabrication.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the URL. It is a form, not a search box.
2. Enter an arbitrary `username`/contact name, `phone`, avatar, message text, timestamps and read-receipt state.
3. Render the fake chat and study the result: note how nothing ties it to a real account and how every field is attacker-controlled.
4. Apply that knowledge to the screenshot under review — demand corroboration (device export, server-side records, matching metadata) rather than trusting the image.

## Inputs → Outputs
- **In:** attacker-supplied `phone`/`username` and message content (all fabricated)
- **Out:** none — it produces a synthetic image, not intelligence about any real person
- **Empty/negative result looks like:** n/a; the tool always "succeeds" at making a fake, which is precisely why screenshots alone are weak evidence.

## Gotchas & OpSec
- Do NOT use this to create evidence — that is fabrication and potentially a crime. Its legitimate use is recognition and debunking only.
- A watermark is present unless the €2 removal is bought; a screenshot with no watermark is not proof of authenticity.
- OpSec: passive and client-side; nothing is stored, but nothing produced here is real either.

## Overlaps ("do both")
- Pairs with genuine message-verification approaches (device chat exports, WhatsApp's own forwarded/label metadata) — this shows the forgery side, those show the authentic side.

## Trust & verifiability
`trust: community` — an entertainment site with no data provenance by design. Its value in an investigation is strictly as a demonstration of how untrustworthy standalone chat screenshots are.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | prankshit-com-2 |
| category | messaging |
| selectorsIn → selectorsOut | phone, username → — |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (manual-review) |
