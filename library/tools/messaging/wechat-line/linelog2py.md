---
id: linelog2py
name: linelog2py
description: Use when you have an exported LINE chat history file and want it parsed into structured messages for analysis — returns per-message `username` (sender), timestamps, and content for timeline/associate mapping.
url: https://github.com/jyu0414/linelog2py
category: messaging
path:
- messaging
- wechat-line
bestFor: Parsing exported LINE chat logs into structured Message objects (sender, timestamp, type, content) for downstream analysis.
selectorsIn: []
selectorsOut:
- username
- name
status: live
pricing: free
costNote: Free open-source Python library (jyu0414/linelog2py); installable via `pip install linelog2py`.
opsec: passive
opsecNote: Fully passive and offline — it parses chat-export text files locally and never contacts LINE or any server. OpSec risk is entirely in how you lawfully obtained the export (consent, seizure, disclosure); the parsing itself leaks nothing.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: unverified
trustNote: A small open-source library (modest GitHub adoption). It only transforms a file you already possess, so trust risk is low — but audit the code before running it on sensitive evidence.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- LINE chat export parser
tags:
- line
- chat-analysis
- messaging
source: arf-seed
lastVerified: '2026-07-14'
enrichment: full
---

# linelog2py

> A Python library that turns a raw LINE chat-export text file into structured, analyzable `Message` objects — sender, timestamp, type, and content — so you can reconstruct a conversation programmatically.

## When to use
You have a LINE chat history export (lawfully obtained — a subject's or witness's exported log, or evidence disclosed to you) and need to analyze it: who said what and when, who the participants are, and how activity is distributed over time. Parsing the raw export into structured records lets you build a timeline, extract participant display names (`username`/`name`), and spot patterns — far faster than reading a long text dump by hand.

## How to use it (`bestInteractionPattern`: python-lib)
1. Get the export from LINE: in the app, **talk room settings → Other settings → Export Chat History** (language must be English or Japanese for the parser).
2. Install: `pip install linelog2py` (Python 3.7.15+).
3. Parse the file in a script — the library returns a list of `Message` objects, each with `timestamp` (datetime), `username` (sender display name), `content` (lines of text), and `category` (text, sticker, image, video, call, etc.).
4. Analyze: build a per-sender timeline, count message types, extract mentioned names/numbers, or flag calls/media events.
5. Pivot: sender display names feed name/username OSINT; timestamps feed pattern-of-life/timezone inference; mentioned phone numbers or handles feed their own lookups.

## Inputs → Outputs
- **In:** a LINE chat-export `.txt` file (English or Japanese export)
- **Out:** structured messages exposing sender `username`/`name`, timestamps, message type, and content
- **Empty/negative result looks like:** a parse error or empty list — usually a non-English/Japanese export, a corrupted/edited file, or a LINE format change. It cannot recover anything not in the export itself.

## Gotchas & OpSec
- It parses **exports**, not live LINE — it cannot pull a chat you don't already have. Lawful acquisition of the export is the whole ballgame; the tool adds no access.
- Display names in LINE are user-set and can be nicknames — treat sender names as leads, not verified identities.
- Language setting matters: exports must be English or Japanese to parse.
- OpSec: fully offline/passive; audit the code before running on sensitive evidence.

## Overlaps ("do both")
- Pairs with name/username OSINT and phone tools — linelog2py structures the conversation, while those resolve the participants and any contact details surfaced inside the chat. Also pairs with timeline tools for pattern-of-life once you've extracted timestamps.

## Trust & verifiability
`trust: unverified` — a small community library, but it merely transforms a file you already hold, so the risk surface is low. Audit the source before use on real evidence, and verify parsed content against the original export.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | linelog2py |
| category | messaging |
| selectorsIn → selectorsOut |  → username, name |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | no |
