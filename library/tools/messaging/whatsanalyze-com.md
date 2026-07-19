---
id: whatsanalyze-com
name: whatsanalyze.com
description: Use when you have an exported WhatsApp chat file and want message statistics — returns per-participant activity, timelines, word frequency, all processed on-device.
url: https://whatsanalyze.com
category: messaging
path:
- messaging
bestFor: Analysing an exported WhatsApp chat (.txt/.zip) for per-participant message counts, timelines, activity patterns and word clouds — entirely in-browser.
selectorsIn:
- username
selectorsOut:
- associate
status: live
pricing: freemium
costNote: Free hosted tool; open source (GitHub Pages, SpiritFour/whatsanalyze). All processing is client-side in your browser — an optional paid PDF/premium export exists, but core analysis is free.
opsec: passive
opsecNote: Because analysis runs entirely locally in your browser and no chat data is sent to any server, this is safe for sensitive exports. The privacy risk is on your side — you must lawfully possess the exported chat, and the file itself contains participants' phone numbers/names.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source, client-side tool hosted on GitHub Pages; the code is public and no data leaves the device. Not affiliated with WhatsApp/Meta.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- WhatsAnalyze
- WhatsApp Chat Analyzer
tags:
- Messengers
- WhatsApp
- chat-analysis
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# whatsanalyze.com

> A privacy-first, in-browser analyzer that turns an exported WhatsApp chat into statistics — who talks most, when, and about what — with no data ever leaving your device.

## When to use
You already hold an exported WhatsApp chat (a subject's device, a consenting party's phone, or lawfully obtained evidence) and want to extract behavioural signal from it: which participants are most active, activity by hour/day (a rough timeline of when someone was online/reachable), response patterns, and frequently used words/contacts. Useful in missing-persons work for reconstructing a timeline of communication and identifying frequent contacts/`associate`s in a group.

## How to use it (`bestInteractionPattern`: web-manual)
1. Export the chat from WhatsApp ("Export chat" → without media gives a `.txt`; with media a `.zip`). The site's guide covers the steps.
2. Open https://whatsanalyze.com and drop the exported file in — it loads into the browser only; nothing uploads.
3. Read the generated dashboard: per-participant message counts, activity timeline, busiest times, word frequency/cloud.
4. Interpret: peaks/gaps in the timeline mark active vs silent periods; top participants and repeated names/numbers surface key contacts.
5. Pivot: identified frequent contacts/numbers feed phone-OSINT and social-profile lookups.

## Inputs → Outputs
- **In:** exported WhatsApp chat file (`.txt`/`.zip`); participants are the `username`/contact set
- **Out:** message statistics, activity timeline, top participants/`associate`s, word frequency
- **Empty/negative result looks like:** a parse error or empty stats — usually a wrong export format (media-only, unsupported language date format) rather than an empty chat.

## Gotchas & OpSec
- Input quality is everything: statistics only reflect the single exported chat; deleted messages and other chats aren't visible.
- Timestamps follow the exporting phone's locale/timezone — account for that when building a timeline.
- Legal/ethical: only analyse chats you are entitled to; the file contains third parties' numbers and messages.
- OpSec: passive and fully on-device — nothing is sent to a server, so it's safe for sensitive material.

## Overlaps ("do both")
- Complements phone/social lookups — WhatsAnalyze surfaces the key contacts from a chat; those numbers/names then feed identity-resolution tools.

## Trust & verifiability
`trust: community` — an open-source, client-side project with public code and no server-side data handling. The statistics are deterministic from your file; verify any lead (a phone number, a name) against independent sources before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whatsanalyze-com |
| category | messaging |
| selectorsIn → selectorsOut | username → associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
