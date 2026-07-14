---
id: whatsthat-github-com
name: whatsthat (github.com)
description: Use when you have access to a WhatsApp Web group chat and want to map member relationship dynamics — returns per-member influence, reply/reaction bias, and activity-time patterns as associate links.
url: https://github.com/markrai/whatsthat
category: messaging
path:
- messaging
bestFor: Analysing who-talks-to-whom and who is central within a WhatsApp group you already have access to.
selectorsIn:
- username
- social-profile
selectorsOut:
- associate
- social-profile
status: live
pricing: free
costNote: Free and open-source (load-unpacked Chrome extension); no account or API key.
opsec: active
opsecNote: This runs inside YOUR logged-in WhatsApp Web session and only sees chats you are already a member of — it does not covertly join or scrape strangers. Data is stored locally and nothing is sent externally. Being present in the group is itself an active footprint; use an investigative WhatsApp account, and remember analysing a group you infiltrated may have legal/ethical limits.
humanInLoop: true
humanInLoopReason:
- account-login
- manual-review
bestInteractionPattern: browser-extension
trust: community
trustNote: Small single-author open-source project (markrai). Code is inspectable; it processes chat data locally in the browser with no external calls.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- whatsapp-web
aliases:
- WhatsThat
- WhatsApp Web analyzer
tags:
- whatsapp
- WhatsApp
- social-network-analysis
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# whatsthat (github.com)

> A local Chrome extension that reads your open WhatsApp Web group chats and surfaces influence, reply/reaction bias, and activity-time patterns between members.

## When to use
You are already a member of (or have lawful investigative access to) a WhatsApp group and want to understand its social graph — who is central, who replies to whom, who gets marginalised, and when each member is active. It converts raw group chatter into `associate` links and behavioural signals, which helps identify a target's closest contacts or the group's real coordinators.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Clone/download the repo: `git clone https://github.com/markrai/whatsthat`.
2. Go to `chrome://extensions`, enable Developer mode, choose **Load unpacked**, and select the folder.
3. Open WhatsApp Web (logged into your investigative account) and browse the target group so the extension can backfill history as WhatsApp loads it.
4. Read the analysis panel: influence scores, reaction/reply bias, temporal activity. Export the data for your case file.
5. Pivot: treat high-reaction pairs as candidate `associate` links, then profile individual members on `[[whatsapp-web]]` directly.

## Inputs → Outputs
- **In:** `username`/`social-profile` (members of a group you can see in WhatsApp Web)
- **Out:** `associate` links (relationship dynamics), `social-profile` behavioural metrics (influence, active hours)
- **Empty/negative result looks like:** thin or empty analysis — WhatsApp hasn't loaded enough history yet; scroll the chat further back to backfill.

## Gotchas & OpSec
- Human-in-the-loop: requires a logged-in WhatsApp Web session (**account-login**) and analyst **manual-review** of the patterns.
- OpSec: **active** — you must be present in the group; your investigative account is visible to other members. Never use your real account.
- Data stays local (no external upload), which is good for OpSec but means results live only in your browser until exported.

## Overlaps ("do both")
- Pairs with `[[whatsapp-web]]` — WhatsThat quantifies the group's internal dynamics, while direct inspection gives you each member's number, display name, and profile photo.

## Trust & verifiability
`trust: community` — a single-author open-source tool; audit the source before loading it into a session with real case data. Its outputs are inferences from message patterns, not ground truth — corroborate before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whatsthat-github-com |
| category | messaging |
| selectorsIn → selectorsOut | username, social-profile → associate, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | yes (account-login) |
