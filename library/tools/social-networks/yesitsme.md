---
id: yesitsme
name: yesitsme
description: Use when you have a `name` plus a partial `email` or `phone` and want to find the matching Instagram account — returns the username/social-profile.
url: https://github.com/blackeko/yesitsme
category: social-networks
path:
- social-networks
bestFor: Reversing a partial (obfuscated) email/phone back to a specific Instagram profile.
selectorsIn:
- name
- email
- phone
selectorsOut:
- username
- social-profile
status: degraded
pricing: free
costNote: Free and open-source. No paid tier; but it depends on third-party services (Instagram, dumpor.com) whose availability comes and goes.
opsec: active
opsecNote: Requires your own Instagram sessionid cookie, so queries run as your (sock-puppet) IG account and Instagram can log the activity — use a burner account, never your real one. It also scrapes dumpor.com and Instagram's recovery hints, which is intrusive; the account owner is not notified but you are actively touching Instagram infrastructure.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: community
trustNote: Open-source tool by blackeko; relies on the Toutatis technique and dumpor.com, both of which break when Instagram changes, so reliability is intermittent.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
invitationOnly: false
aliases:
- yesitsme
- "yes it's me"
tags:
- instagram
- email-to-account
- phone-to-account
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# yesitsme

> Turns "I have a name and the first/last letters of their email" into a concrete Instagram username by matching against IG's obfuscated recovery hints.

## When to use
You know the subject's `name` and a fragment of their contact — the first and last characters of an `email`, or the area code and last digits of a `phone` — and want to identify their Instagram account. yesitsme enumerates usernames tied to that name, pulls each account's obfuscated recovery email/phone, and compares them to your known fragment, ranking candidates by confidence.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/blackeko/yesitsme` and `pip install -r requirements.txt` (Python 3).
2. Grab a **burner** Instagram account's `sessionid` cookie (from browser dev tools while logged into the sock-puppet).
3. Run with the name, the partial email (first + last letter), and/or partial phone (area code + final digits), passing the sessionid.
4. Read the ranked results: **HIGH** = name, email, and phone all consistent; **MEDIUM** = partial; **LOW** = single-field match.
5. Open the top candidate profile to confirm, then pivot the username into cross-platform username search.

## Inputs → Outputs
- **In:** `name` + partial `email` and/or partial `phone`
- **Out:** `username`, `social-profile` (Instagram), ranked by confidence
- **Empty/negative result looks like:** no candidates above LOW, or a tool error if the sessionid expired or dumpor is down — treat as inconclusive, not "no account."

## Gotchas & OpSec
- Human-in-the-loop: you must supply a live IG `sessionid` from a burner account — use of your real account risks flagging/banning.
- OpSec: **active** — queries run under your IG identity; Instagram may rate-limit or challenge the account.
- Fragile: depends on dumpor.com and Instagram's recovery flow; when either changes the tool degrades or breaks. Re-verify before relying on a null result.

## Overlaps ("do both")
- Pairs with `[[account-live-com]]`-style existence oracles and email/phone enrichment — those confirm an address is real; yesitsme ties a real fragment to a *specific* Instagram profile.

## Trust & verifiability
`trust: community` — clever and open source, but built on scraping surfaces that Instagram actively changes, so treat matches as leads and re-test the tool's health each session.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | yesitsme |
| category | social-networks |
| selectorsIn → selectorsOut | name, email, phone → username, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login) |
