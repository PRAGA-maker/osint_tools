---
id: telegram-message-analyzer
name: Telegram Message Analyzer
description: Use when you have an exported Telegram chat (HTML) and want a behavioural profile of a `username`/participant — returns activity-by-hour/day patterns, message counts, and word-frequency (a `device-id`/timezone-adjacent lifestyle signal).
url: https://github.com/zqtay/Telegram-Message-Analyzer
category: messaging
path:
- messaging
bestFor: Turning a Telegram chat export into activity-pattern graphs and word-frequency lists to profile when a person is online and what they talk about.
selectorsIn:
- username
selectorsOut:
- physical-description
status: live
pricing: free
costNote: Free, open-source Python script; no account, no API key.
opsec: passive
opsecNote: Fully offline analysis of data you already possess — it never contacts Telegram or the target. All processing is local, so nothing leaks; the only risk is chain-of-custody on the export itself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: A small (~60-star) single-author open-source project; read the short Python source before running, but it is inert local tooling with no network calls.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Telegram-Message-Analyzer
- zqtay Telegram analyzer
tags:
- Messengers
- Telegram
- chat-analysis
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# Telegram Message Analyzer

> A local Python script that turns a Telegram chat export into activity-timing graphs and word-frequency stats — a fast way to infer a person's routine and preoccupations from their own messages.

## When to use
You already hold a Telegram chat export (HTML) involving the subject — from a device you're examining, a cooperating witness, or a group you have access to — and want to profile them: **when** are they active (hour-of-day / day-of-week histograms hint at timezone, work schedule, sleep pattern), **how much** do they message, and **what words** dominate (interests, names, places). Useful for pattern-of-life analysis in a missing-persons or due-diligence context.

## How to use it (`bestInteractionPattern`: cli)
1. In the desktop Telegram app, export the chat as **HTML** (Settings → Export Telegram data, or per-chat export).
2. Clone the repo: `git clone https://github.com/zqtay/Telegram-Message-Analyzer` and read the source.
3. Run the Python script; when prompted, give the path to the exported chat file.
4. It writes a `.txt` report plus graphs/GIF: message count by date and time-of-day, averages, and the most-used words.
5. Pivot: an activity histogram skewed to a consistent set of hours suggests a timezone/`geolocation` band; frequent proper nouns feed name/place lookups; a co-participant's handle feeds username enumeration.

## Inputs → Outputs
- **In:** a Telegram chat export (HTML) tied to a `username`/participant
- **Out:** activity-by-time graphs, per-day message counts, word-frequency list — behavioural signals (mapped here as `physical-description`-style lifestyle profile)
- **Empty/negative result looks like:** a nearly flat histogram / tiny word list — too few messages to profile, or an export that captured only part of the history.

## Gotchas & OpSec
- Requires the **desktop** export (HTML); mobile-only exports won't have the same structure.
- Timestamps reflect the exporter's timezone settings — interpret hour-of-day with that caveat before inferring the subject's location.
- It analyses only what's in the export; deleted messages and other chats are invisible, so absence of a topic proves nothing.
- Inspect the script before running (standard hygiene for any downloaded code), though it makes no network calls.

## Overlaps ("do both")
- Pairs with manual review of the same export and with metadata tools on any exported media — the analyzer gives the timing/word view, media EXIF gives the where/when of individual files.

## Trust & verifiability
`trust: unverified` — community code, not an authoritative source; its output is deterministic arithmetic over your own file, so results are self-verifiable by re-running or spot-checking the export.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telegram-message-analyzer |
| category | messaging |
| selectorsIn → selectorsOut | username → physical-description |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
