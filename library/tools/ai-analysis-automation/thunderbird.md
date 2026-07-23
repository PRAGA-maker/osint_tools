---
id: thunderbird
name: Thunderbird
description: Use when you have an `email` or a raw message and want to read full headers, sources and attachments — returns sender ip-address, metadata-exif and routing detail.
url: https://www.thunderbird.net/en-US/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A free desktop mail client for reading full email headers/source and safely examining messages and attachments.
selectorsIn:
- email
selectorsOut:
- ip-address
- metadata-exif
- email
status: live
pricing: free
costNote: Free and open source (Mozilla). Cross-platform desktop app; no cost or account beyond the mailbox you connect.
opsec: active
opsecNote: Thunderbird is a real mail client — if you connect an account it logs into that mailbox and can send/receive as it. Block remote content (disable auto-loading images) so a message can't beacon your IP/read-receipt back to the sender. For pure header analysis, open a saved .eml offline rather than syncing a live account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Mozilla's flagship open-source email client — mature and auditable. Header data it displays is the raw message source; its evidentiary value depends on the message being genuine (headers can be forged upstream).
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
relatedTools:
- google-forum-search
aliases:
- Mozilla Thunderbird
tags:
- privacy-and-encryption-tools
- email
- header-analysis
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Thunderbird

> Mozilla's free desktop email client — in OSINT, the practical tool for reading a message's full headers and source, examining attachments safely, and working saved `.eml`/`.msg` files offline.

## When to use
You have an email (a live account you're authorised to read, or a saved message file) and need to see beyond the pretty rendering: the full **headers** (Received chain, originating `ip-address`, SPF/DKIM/DMARC results, mailer/software), the raw source, and attachment metadata. Thunderbird makes header inspection and safe message handling easy without a webmail interface leaking your activity.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Install Thunderbird (Windows/macOS/Linux). In settings, **disable remote/auto-loading content** before opening anything sensitive.
2. To analyse a standalone message, open a saved `.eml`/`.msg` file directly — no account needed, fully offline.
3. Open the message → View → Message Source (or the headers panel) to read the full `Received:` chain, originating IP, and authentication results.
4. Examine attachments without opening them in situ; save and analyse (e.g. `metadata-exif` of an attached image) in a controlled environment.
5. Pivot: an originating `ip-address` feeds geolocation/reverse-IP; SPF/DKIM failures flag spoofing; attachment `metadata-exif` feeds document/image analysis.

## Inputs → Outputs
- **In:** an `email` message (live mailbox or saved file)
- **Out:** full headers incl. originating `ip-address`, auth results, mailer software, and attachment `metadata-exif`
- **Empty/negative result looks like:** headers stripped or showing only provider relays (e.g. Gmail hides the true origin IP) — meaning the sender's IP isn't recoverable from this message, not that analysis failed.

## Gotchas & OpSec
- Human-in-the-loop: connecting a live account requires **login** and acts as that mailbox — only do so with authorisation. For third-party messages, prefer offline `.eml` analysis.
- Turn off remote content: an HTML email can otherwise phone home (your IP, a read receipt) to the sender when opened.
- Headers can be forged before they reach the last trusted hop; trust the Received chain only from your provider inward.

## Overlaps ("do both")
- Complements online header analysers (e.g. MXToolbox / Google Header Analyzer) — Thunderbird gives you private, offline access to the raw source; paste that source into an analyser for a quick visual trace.

## Trust & verifiability
`trust: trusted` — Mozilla's open-source client faithfully shows the raw message. The *data* is only as trustworthy as the email itself; corroborate originating IPs and auth results, since upstream headers can be spoofed.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | thunderbird |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | email → ip-address, metadata-exif, email |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | desktop-app |
| opsec | active |
| human-in-loop | yes (account-login) |
