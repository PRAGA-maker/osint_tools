---
id: cctv
name: CCTV (Close-Circuit Telegram Vision)
description: Use when you want to triangulate a Telegram user's location via the People Nearby feature — but the feature was disabled in Sept 2024, so the tool no longer works; historically returned geolocation from a username.
url: https://github.com/IvanGlinkin/CCTV
category: messaging
path:
- messaging
bestFor: (Historic) Triangulating the physical location of a Telegram user who had "People Nearby" enabled, to within ~50–100 m.
selectorsIn:
- username
- geolocation
selectorsOut:
- geolocation
- social-profile
status: down
pricing: free
costNote: Free open-source tool (self-hosted Python/JS). No longer functional: Telegram disabled the "People Nearby" feature on 6 Sept 2024, which is the mechanism CCTV relied on. Documented here so investigators don't waste time on a dead technique.
opsec: active
opsecNote: When it worked, it actively probed Telegram's People Nearby from a controlled account with spoofed coordinates — an intrusive, account-attributable operation that Telegram could log and that could tip a savvy target. Requires your own Telegram API credentials, tying activity to that account.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: A well-known tool by Ivan Glinkin that drew wide media coverage for exposing a real Telegram privacy weakness. Legitimate and technique-transparent — but obsolete since Telegram removed the underlying feature.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
invitationOnly: false
deprecated: true
relatedTools:
- telegram-nearby-map
aliases:
- Close-Circuit Telegram Vision
- CCTV telegram
tags:
- telegram
- geolocation
source: awesome-osint
lastVerified: '2026-07-15'
enrichment: full
---

# CCTV (Close-Circuit Telegram Vision)

> A once-famous Telegram geolocation tool — it triangulated "People Nearby" users to ~50–100 m — now **defunct**, because Telegram removed the feature it depended on in September 2024.

## When to use
Historically: to locate a Telegram user who had left the "People Nearby" setting on, by moving a controlled account to several coordinates and triangulating the target's reported distance. **As of Sept 2024 this no longer works** — Telegram disabled People Nearby platform-wide. This entry exists so you recognise the technique, understand why it's dead, and don't burn time trying to run it. If location via Telegram is your goal, pivot to other signals (shared media EXIF, group membership, linked accounts).

## How to use it (`bestInteractionPattern`: cli)
Historic procedure (no longer functional):
1. Clone `github.com/IvanGlinkin/CCTV` and install Python dependencies.
2. Register Telegram API credentials at `my.telegram.org`.
3. Configure location parameters in `config.yaml`.
4. Run `python3 start.py`; it iterated coordinates, read the target's "distance," and triangulated a position into HTML reports.
5. Today step 4 returns nothing — the People Nearby endpoint is gone.

## Inputs → Outputs
- **In:** `username` / target presence + your seed `geolocation`(s)
- **Out:** `geolocation` (triangulated position), `social-profile` (nearby Telegram accounts)
- **Empty/negative result looks like:** **always empty now** — People Nearby is disabled. Even before that, a target who never enabled the setting was invisible; absence never meant they weren't in the area.

## Gotchas & OpSec
- **Obsolete:** the core dependency was removed by Telegram in 2024 — treat as non-working.
- It required the *target* to have opted into People Nearby, which most users never did.
- OpSec: active and intrusive when it worked — attributable to your Telegram API account.

## Overlaps ("do both")
- Historically paired with other Telegram-nearby mappers (same disabled feature — all now defunct).
- For live Telegram location leads today, rely on media EXIF, group/channel membership analysis, and cross-linked accounts instead.

## Trust & verifiability
`trust: community` — a legitimate, well-documented research tool that exposed a genuine privacy flaw; its trust rating is moot now that the feature is gone. Recorded as **down** for situational awareness.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cctv |
| category | messaging |
| selectorsIn → selectorsOut | username, geolocation → geolocation, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key) |
