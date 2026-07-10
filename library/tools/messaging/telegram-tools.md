---
id: telegram-tools
name: telegram.tools
description: Use when you have a Telegram user/account `device-id` (numeric ID) or bot file ID and want to decode it — returns approximate account-creation date and file `metadata-exif`, not a name/phone lookup.
url: https://telegram.tools/
category: messaging
path:
- messaging
bestFor: Estimating a Telegram account's creation date from its numeric user ID, and decoding Bot API / TDLib file IDs — developer utilities with narrow OSINT use.
selectorsIn:
- device-id
- username
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free and open-source (maintained by the grammY / grammyjs project). No account or key required.
opsec: passive
opsecNote: Everything is computed client-side or against public Telegram infrastructure from an identifier you already have; the target account is not contacted or notified. It does not resolve phone numbers or reveal private profile data.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source utilities by the grammY Telegram-bot framework project; these are developer tools, so the OSINT-relevant output (approximate account age from user ID) is an inference, not an official Telegram field.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- grammY tools
- Telegram account creation date
tags:
- telegram
- messaging
- developer-utility
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# telegram.tools

> A grab-bag of Telegram developer utilities whose one OSINT-relevant trick is estimating an account's age from its numeric user ID — not a username/phone people-lookup.

## When to use
You already have a Telegram numeric user ID (`device-id`, e.g. from another tool that exposed it) and want to gauge roughly **when the account was created** — old accounts vs. throwaway new ones is a useful trust signal when verifying an identity or spotting a burner. Also handy to decode a Bot API / TDLib **file ID** into its metadata. Do **not** reach for this expecting name/phone resolution — it doesn't do that.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://telegram.tools/.
2. Pick the relevant utility — most useful for OSINT is the **account creation date** estimator: paste the target's numeric Telegram user ID.
3. Read the output: an approximate registration date/window for that ID (IDs are roughly sequential, so age is an estimate, not exact).
4. Other utilities: paste a Bot API or TDLib **file ID** to decode its `metadata-exif` (DC, type); test DC connectivity; analyse session strings.
5. Pivot: an "old" account corroborates a long-standing identity; a very new ID next to claims of long history is a red flag → cross-check the handle on other Telegram-OSINT tools.

## Inputs → Outputs
- **In:** `device-id` (numeric Telegram user ID) or a bot file ID; some tools take a `username` only indirectly
- **Out:** `metadata-exif` — approximate account-creation date, file metadata (no name, phone, or profile content)
- **Empty/negative result looks like:** an obviously implausible date, or a decode error on a malformed ID. Because the age estimate is interpolated from ID ranges, treat it as ±a window, not a precise timestamp.

## Gotchas & OpSec
- **Not a lookup engine:** it will not turn a phone number or handle into an identity — the stub's phone/username framing overstates it. Use dedicated Telegram-OSINT tools for that.
- The creation date is an **estimate** from sequential-ID heuristics and can be off, especially at ID-space boundaries.
- OpSec: **passive** — computed from an ID you already hold; no contact with the target.

## Overlaps ("do both")
- Pairs with Telegram username/ID resolvers and channel-search tools — those get you the numeric ID and profile; telegram.tools then dates the account.

## Trust & verifiability
`trust: community` — legitimate open-source developer tooling. The account-age output is a documented heuristic, not an official Telegram field, so use it as corroboration, not proof.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telegram-tools |
| category | messaging |
| selectorsIn → selectorsOut | device-id, username → metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
