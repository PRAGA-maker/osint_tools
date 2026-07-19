---
id: chatvisualizer-com
name: chatvisualizer.com
description: Use when you already possess a WhatsApp chat export and want visual statistics of it — returns activity patterns and per-participant `name`/`associate` breakdowns (who talks, when, how much).
url: https://chatvisualizer.com
category: messaging
path:
- messaging
bestFor: Turning a WhatsApp chat export you lawfully hold into charts — message volume per participant, active hours, and interaction patterns.
selectorsIn:
- phone
- name
selectorsOut:
- name
- associate
status: live
pricing: free
costNote: Free web service; results delivered by email link. No account.
opsec: passive
opsecNote: Passive toward the chat participants (they get no signal), but you must EMAIL the entire private conversation to a third-party server (robot@chatvisualizer.com) that then processes and stores it. That is a serious data-exposure and consent risk — only use on data you are legally entitled to analyse, prefer a self-hosted analyzer for sensitive material, and never upload chats you cannot lawfully share.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Third-party service with no transparency about data retention; you are handing it a full private chat log, so treat it as untrusted with your data and verify results yourself.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Chatvisualizer
tags:
- Messengers
- WhatsApp
- chat-analysis
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# chatvisualizer.com

> Email a WhatsApp chat export and get back a web page of stats — message counts, timelines, and who dominates the conversation.

## When to use
You already hold a WhatsApp chat export (e.g. from a device you lawfully control, or a chat shared with consent) and want to understand it fast: who the most active participants are, when the conversation peaks (a clue to timezone/routine), and how people cluster — useful for mapping a subject's contacts (`associate`s) and daily pattern.

## How to use it (`bestInteractionPattern`: web-manual)
1. In WhatsApp, open the conversation → contact/group name → "Export Chat" → "Without Media". The exported filename must contain the string "whatsapp".
2. Email that file to `robot@chatvisualizer.com` (works best for chats up to ~20 members).
3. Wait up to five minutes; you receive a link by email (check spam).
4. Open the link and read the visualizations: per-participant volume, hourly/daily activity, and timeline.
5. Pivot: note the most-active `associate`s and active-hour patterns; corroborate identities and timezone with other tools.

## Inputs → Outputs
- **In:** a WhatsApp chat export (contains participant `name`s/`phone`s)
- **Out:** activity charts, per-participant `name`/`associate` statistics, timing patterns
- **Empty/negative result looks like:** no email back means the file name lacked "whatsapp", the export was malformed, or the group was too large — re-export and retry.

## Gotchas & OpSec
- **Privacy first:** you are uploading a full private conversation to an outside server — only do this with data you are legally entitled to process, and prefer an offline/self-hosted analyzer for anything sensitive.
- Only produces aggregate statistics, not new external data about the participants.
- Human-in-the-loop: none beyond the manual export/email step.
- OpSec: passive toward the chat members; the exposure is to the third-party processor, not the target.

## Overlaps ("do both")
- Compare with a self-hosted WhatsApp analyzer for the same export — an offline tool avoids the third-party upload while giving equivalent stats; use this only when convenience outweighs the privacy cost.

## Trust & verifiability
`trust: unverified` — opaque third party handling your private data; treat its charts as a convenience view and confirm any conclusion (identities, timing) independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | chatvisualizer-com |
| category | messaging |
| selectorsIn → selectorsOut | phone, name → name, associate |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
