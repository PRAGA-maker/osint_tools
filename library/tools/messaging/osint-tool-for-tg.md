---
id: osint-tool-for-tg
name: TeleOSINT (OSINT-Tool-For-TG)
description: Use when you have a Telegram `username`, `phone`, or user id and want to enumerate the account, its channels, and linked accounts — returns `social-profile`, `username`, and `associate` links.
url: https://github.com/Flintgliboom/OSINT-Tool-For-TG
category: messaging
path:
- messaging
bestFor: Telegram-centric reconnaissance — resolving a username/phone/id to an account, analysing channels, and mapping relationships, with pivots into VK/Instagram/X/GitHub.
selectorsIn:
- username
- phone
selectorsOut:
- social-profile
- username
- associate
status: live
pricing: free
costNote: Free and open-source (MIT). Requires your own Telegram API credentials (api_id/api_hash) and a Telegram account to run.
opsec: active
opsecNote: This authenticates with YOUR Telegram credentials to query Telegram — actions can be logged by Telegram and, for some operations, expose your account to the target. Use a dedicated sock-puppet Telegram account and API key, and route through the tool's built-in Tor/SOCKS5 proxy support. Never use your real account.
humanInLoop: true
humanInLoopReason:
- api-key
- account-login
bestInteractionPattern: cli
trust: community
trustNote: A small but actively maintained community tool (MIT, releases into 2026); accuracy depends on Telegram's API and the target's privacy settings. Vet the code before running with credentials.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: true
relatedTools:
- telegram-phone-number-checker
aliases:
- OSINT-Tool-For-TG
- TeleOSINT
tags:
- telegram
- messaging
- username
- phone
source: gh-topic-osint-framework
lastVerified: '2026-07-17'
enrichment: full
---

# TeleOSINT (OSINT-Tool-For-TG)

> A self-hosted Telegram OSINT tool: resolve a username/phone/id to an account, analyse its channels, map who it interacts with, and pivot to other platforms — anonymised through Tor/SOCKS5.

## When to use
Your lead runs through Telegram: you have a `username`, a `phone` number, or a user id and need to (a) confirm it maps to a Telegram account, (b) profile the channels/groups it runs or joins, and (c) map `associate`s. Telegram can resolve a phone to an account if the target has that number registered and permissive privacy settings — a strong bridge from a `phone` to a `social-profile`. Valuable for messaging-linked missing-persons leads.

## How to use it (`bestInteractionPattern`: cli)
1. Create a **sock-puppet** Telegram account and obtain API credentials (api_id/api_hash) at my.telegram.org.
2. Clone the repo, install requirements (Python 3.10+), and configure your credentials and proxy (enable Tor/SOCKS5).
3. Run a lookup by `username`, `phone`, or id; use channel-analysis and relationship-mapping modes as needed.
4. Export results (multiple formats) and review the account, channels, and linked-platform hits.
5. Pivot: a resolved `username` → username-search tools; `associate`s → their own profiles; cross-platform hits (VK/IG/X/GitHub) → the matching platform tool.

## Inputs → Outputs
- **In:** `username`, `phone`, or Telegram user id
- **Out:** `social-profile` (Telegram account), `username`, `associate` links, channel/group activity, cross-platform matches
- **Empty/negative result looks like:** no account resolves, or phone→account fails — the number isn't on Telegram, or the target restricted "who can find me by number." Not proof they lack Telegram.

## Gotchas & OpSec
- **Active with your credentials:** authenticated queries can be logged and some expose your account. Use a throwaway account + API key only.
- Phone→account resolution depends on the target's privacy settings and often fails — treat a miss as inconclusive.
- Small community tool — read the source before feeding it credentials; keep it updated as Telegram's API shifts.

## Overlaps ("do both")
- Pairs with `[[telegram-phone-number-checker]]` — a lighter phone→Telegram existence check; use it for a quick yes/no, then TeleOSINT for deeper channel/relationship enumeration.

## Trust & verifiability
`trust: community` — an actively maintained but small MIT project. Results are as reliable as Telegram's API returns; verify identities on the account itself and corroborate cross-platform matches.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-tool-for-tg |
| category | messaging |
| selectorsIn → selectorsOut | username, phone → social-profile, username, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key, account-login) |
