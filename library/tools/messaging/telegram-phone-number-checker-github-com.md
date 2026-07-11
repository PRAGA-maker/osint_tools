---
id: telegram-phone-number-checker-github-com
name: telegram phone number checker (github.com)
description: Use when you have a `phone` number and want to know if it's on Telegram — returns whether an account exists plus the linked `username`, display name and profile (`social-profile`) via Telegram's own API.
url: https://github.com/bellingcat/telegram-phone-number-checker
category: messaging
path:
- messaging
bestFor: Checking whether phone numbers are registered on Telegram and pulling the linked account details.
selectorsIn:
- phone
selectorsOut:
- social-profile
- username
- name
status: live
pricing: free
costNote: Free and open-source (Python). Requires your own Telegram API credentials (api_id/api_hash from my.telegram.org) and a logged-in Telegram account to run.
opsec: active
opsecNote: The script adds the target's number to your account's contacts to resolve it via Telegram's API — an ACTIVE operation. It uses YOUR Telegram identity; abusive volume risks your account being flagged/banned, and the added contact can leave traces. Use a dedicated sock-puppet Telegram account and number, keep volume low, and clean up added contacts.
humanInLoop: true
humanInLoopReason:
- api-key
- account-login
bestInteractionPattern: cli
trust: trusted
trustNote: Published by Bellingcat, a leading OSINT organisation. It queries Telegram's official API, so a positive result is authoritative; the technique is documented and maintained openly.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: true
relatedTools:
- telegram-org
- holehe-2
aliases:
- bellingcat telegram-phone-number-checker
- Telegram phone checker
tags:
- telegram
- Telegram
- phone
- account-existence
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# telegram phone number checker (github.com)

> Bellingcat's Python tool that checks a batch of phone numbers against Telegram — telling you which are registered and revealing the username, name, and profile behind each.

## When to use
You have a `phone` number (or a list) and want to know whether it belongs to a Telegram user and, if so, who. Telegram often exposes the display name, `username`, and profile photo for a number you add as a contact — so this bridges a bare phone number to a named `social-profile`, a strong pivot when you have a number but no identity. Especially valuable because Telegram is a primary comms platform in many regions.

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/bellingcat/telegram-phone-number-checker and install its Python dependencies.
2. Create Telegram API credentials at my.telegram.org (`api_id`/`api_hash`) tied to a **sock-puppet** Telegram account/number.
3. Configure the credentials, then run the script against a single number or a list (per the README).
4. Read the output: for each number, whether a Telegram account exists and, where available, the `username`, display `name`, and profile details.
5. Pivot: a recovered `username` feeds username/cross-platform search; the display name feeds people-search; corroborate on `[[telegram-org]]` directly.

## Inputs → Outputs
- **In:** `phone` (single or batch)
- **Out:** account-exists flag → linked `username`, display `name`, `social-profile` (where the user's privacy settings allow)
- **Empty/negative result looks like:** "no Telegram account" for a number, or an account with name/username hidden by privacy settings. Absence means not-on-Telegram (or a very private account), not that the number is invalid.

## Gotchas & OpSec
- Human-in-the-loop: needs your own **API key** and a **logged-in** Telegram account — set up a dedicated sock puppet before running.
- OpSec: **active** — the tool adds numbers to your account's contacts to resolve them via Telegram's API. High volume gets accounts banned and can leave contact-side traces. Keep batches small, use a burner account/number, and remove added contacts afterward.
- What's revealed depends on each target's privacy settings; many users hide their username or name.

## Overlaps ("do both")
- Pairs with `[[telegram-org]]` (manual profile checks) and `[[holehe-2]]` (email→accounts) — this converts a *phone* to a Telegram identity; combine with email- and username-based enumeration to triangulate the same person across selectors.

## Trust & verifiability
`trust: trusted` — a Bellingcat-published tool hitting Telegram's official API, so positive matches are authoritative. Reliability of the *revealed detail* depends on the target's privacy settings, and the method is account-risky, so operate it carefully from a throwaway identity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telegram-phone-number-checker-github-com |
| category | messaging |
| selectorsIn → selectorsOut | phone → social-profile, username, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (api-key, account-login) |
