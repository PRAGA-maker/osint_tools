---
id: toutatis-2
name: toutatis
description: Use when you have an Instagram `username`/ID and want the obfuscated contact data Instagram holds — returns partially-masked `email` and `phone`, full `name` and account metadata via a Python tool.
url: https://pypi.org/project/toutatis/
category: social-networks
path:
- social-networks
bestFor: Extracting an Instagram account's obfuscated recovery email/phone and profile metadata from a username.
selectorsIn:
- username
selectorsOut:
- email
- phone
- name
status: degraded
pricing: free
costNote: Free, open-source Python tool (pip install toutatis); requires your own Instagram session cookie (sessionid) to run.
opsec: active
opsecNote: Toutatis authenticates with YOUR Instagram sessionid and queries Instagram's own endpoints about the target — so you must run it from a sock-puppet Instagram account, never your real one. Instagram may rate-limit or flag the puppet. The target is not directly notified, but you are touching Instagram's infrastructure under an account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: python-lib
trust: community
trustNote: A well-known open-source OSINT tool (by megadose); it works only as long as Instagram's endpoints allow, so reliability comes and goes with platform changes.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- instadp
- account-live-com
aliases:
- Toutatis
- megadose toutatis
tags:
- instagram
- python-tool
- account-enrichment
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# toutatis

> An open-source Python tool that pulls the obfuscated recovery contact Instagram stores for an account — a masked email and phone from just a username.

## When to use
You have an Instagram `username` (or numeric ID) and want the contact hints Instagram exposes via its account/lookup endpoints: an obfuscated recovery `email` (e.g. `j***@g***.com`) and `phone` (e.g. `+1 ***-***-**89`), the account's full `name`, verification status, and other metadata. Those masks are pivotable leads toward a secondary email/number — valuable for connecting an Instagram persona to a real identity.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install: `pip install toutatis`.
2. Obtain a **sock-puppet** Instagram account's `sessionid` cookie (log in as the puppet, copy the cookie).
3. Run: `toutatis -u <username> -s <sessionid>` (or `-i <id>`).
4. Read the output: obfuscated `email`/`phone`, full `name`, user ID, follower counts, verification/business flags.
5. Pivot: masked recovery contacts feed phone/email OSINT and account-existence oracles like `[[account-live-com]]`; the real name feeds people-search.

## Inputs → Outputs
- **In:** Instagram `username` (or numeric ID) + your puppet `sessionid`
- **Out:** obfuscated `email`, obfuscated `phone`, full `name`, account metadata
- **Empty/negative result looks like:** an error or empty fields — usually Instagram changed its endpoints, the sessionid is invalid/expired, the puppet got rate-limited, or the account has no recovery contact exposed. A failure is often platform-side, not "no data."

## Gotchas & OpSec
- Human-in-the-loop: needs a **puppet Instagram sessionid** (`account-login`) — never use your real account; the puppet may get flagged/limited.
- **Reliability is platform-dependent** (`status: degraded`): Instagram periodically breaks the endpoints toutatis relies on.
- Masks are partial by design — treat revealed characters as leads, not confirmed values.
- OpSec: **active** — you query Instagram under an account.

## Overlaps ("do both")
- Pairs with `[[account-live-com]]` (turn a masked email into an account-existence check) and `[[instadp]]` (grab the avatar) — toutatis leaks the masked recovery contacts, the others help confirm and enrich them.

## Trust & verifiability
`trust: community` — a respected open-source tool, but dependent on Instagram's shifting endpoints; verify any de-masked contact independently before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | toutatis-2 |
| category | social-networks |
| selectorsIn → selectorsOut | username → email, phone, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | python-lib |
| opsec | active |
| human-in-loop | yes (account-login) |
