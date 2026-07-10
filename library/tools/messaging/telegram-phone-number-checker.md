---
id: telegram-phone-number-checker
name: Telegram Phone Number Checker
description: Use when you have a `phone` number and want to check whether it has a Telegram account — returns account existence plus username/name/ID where the profile exposes them.
url: https://colab.research.google.com/github/bellingcat/open-source-research-notebooks/blob/main/notebooks/bellingcat/telegram-phone-number-checker.ipynb
category: messaging
path:
- messaging
bestFor: Confirming whether a phone number is registered on Telegram and pulling any exposed profile handle/name.
selectorsIn:
- phone
selectorsOut:
- username
- name
- social-profile
status: live
pricing: free
costNote: Free open-source Bellingcat notebook/CLI; you supply your own Telegram API credentials (free from my.telegram.org) and a Telegram account to run it.
opsec: active
opsecNote: This works by importing the number(s) as contacts into YOUR Telegram account and reading what Telegram returns. That is an ACTIVE step — Telegram associates the check with your account, the number's owner could in principle see you as a contact, and bulk/rapid checks risk rate-limits or a ban. Use a dedicated sock-puppet Telegram account and number, check sparingly, and never use your real account.
humanInLoop: true
humanInLoopReason:
- account-login
- api-key
bestInteractionPattern: python-lib
trust: trusted
trustNote: Published by Bellingcat (open-source research notebooks) — a reputable investigative organisation; the code is open and documented, though results depend on Telegram's privacy settings.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
aliases:
- Bellingcat Telegram phone checker
- telegram-phone-number-checker
tags:
- bellingcat-toolkit
- telegram
- phone-to-account
source: bellingcat-toolkit
lastVerified: '2026-07-10'
enrichment: full
---

# Telegram Phone Number Checker

> Bellingcat's notebook that turns a phone number into a Telegram identity check: is this number on Telegram, and what handle/name does it expose?

## When to use
You have a `phone` number and want to know whether it belongs to a Telegram user — and, if the account's privacy allows, capture the username, display name, and ID. A powerful pivot in a missing-person/identity workflow: a phone that resolves to a Telegram profile links a real number to an online identity you can then investigate.

## How to use it (`bestInteractionPattern`: python-lib)
1. Open the Colab notebook (or clone the Bellingcat open-source-research-notebooks repo to run locally).
2. Create Telegram API credentials at my.telegram.org and use a **dedicated sock-puppet Telegram account + number** — never your real one.
3. Provide the target `phone` number(s) in international format.
4. Run the notebook — it imports the number(s) as contacts and reports which are on Telegram, with any exposed `username`/`name`/ID, then (per the script) can clean up the added contacts.
5. Pivot: an exposed username feeds `[[user-searcher]]` and Telegram-native lookups; the profile feeds `[[telemetr-me]]` if they run a channel.

## Inputs → Outputs
- **In:** `phone` (international format)
- **Out:** on-Telegram boolean, plus `username`/`name`/ID (`social-profile`) where the account's privacy exposes them
- **Empty/negative result looks like:** "not on Telegram," or on-Telegram-but-no-details when the user hides their username/name/photo. A hidden profile is common and is not proof the number is unused.

## Gotchas & OpSec
- **This is active.** You add the number to your account's contacts to check it — Telegram ties the action to your account, the owner may see you as a mutual contact, and volume triggers rate-limits/bans. Use a sock-puppet account/number and check sparingly.
- Results depend entirely on the target's privacy settings — many users hide username/name/photo.
- Human-in-the-loop: requires your own API key and an authenticated Telegram session.

## Overlaps ("do both")
- Pairs with `[[telemetr-me]]` and username tools — this maps a phone to a Telegram identity; those enrich the resulting handle/channel. Also cross-check the number on other messengers (WhatsApp/Viber) to build the full messaging footprint.

## Trust & verifiability
`trust: trusted` — an open, documented Bellingcat tool from a reputable investigative body. The existence signal is reliable (it queries Telegram directly), but exposed detail is gated by the subject's privacy settings.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telegram-phone-number-checker |
| category | messaging |
| selectorsIn → selectorsOut | phone → username, name, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | python-lib |
| opsec | active |
| human-in-loop | yes (account-login, api-key) |
