---
id: duolingosint
name: duolingOSINT
description: Use when you have a `username` or `email` and want to check for a Duolingo account — returns profile data (name, avatar, country, streak, creation date, languages) when the account exists.
url: https://github.com/ajuelosemmanuel/duolingOSINT
category: social-networks
path:
- social-networks
bestFor: Confirming a Duolingo account from a username/email and pulling its public profile fields.
selectorsIn:
- username
- email
selectorsOut:
- name
- social-profile
- geolocation
status: degraded
pricing: free
costNote: Free, open-source Python CLI; no account or API key required from the user.
opsec: passive
opsecNote: Queries Duolingo's public profile endpoints for the target's username/email; the user is not notified. Duolingo may rate-limit or ban the tool's User-Agent, so throttle and run behind a VPN. No login is used.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A small unaffiliated open-source project (~11 commits, unmaintained) wrapping Duolingo's public profile API; the data is Duolingo's own, but the wrapper breaks as endpoints change.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- duolingOSINT
tags:
- Social Media
- Duolingo
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# duolingOSINT

> A CLI that turns a username or email into a Duolingo profile — useful because the email lookup confirms an address is tied to a real Duolingo account and returns display name, country, and activity.

## When to use
You have a `username` or, more valuably, an `email` and want to know whether it maps to a Duolingo account. The email→account check is an existence oracle on a 500M-user platform; a hit confirms the address is real and in use and yields a display `name`, avatar (for reverse-image), self-declared country (`geolocation` clue), account creation date, streak, and the languages the person is learning — small but corroborating pattern-of-life signals.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo (`git clone https://github.com/ajuelosemmanuel/duolingOSINT`) and install its Python requirements.
2. Run with a username (`-u TARGET`) or an email (`-m target@example.com`).
3. Read the returned profile: name, profile picture, account creation date, country, streak, XP, and study languages.
4. If it errors, update the tool's User-Agent / check for a newer fork — Duolingo endpoint/UA changes are the usual cause.
5. Pivot: avatar → reverse-image; display name → people/username search; declared country → geolocation context; confirmed email → other email-existence tools.

## Inputs → Outputs
- **In:** `username` or `email`
- **Out:** Duolingo profile — `name`, avatar (`social-profile`), country (`geolocation`), creation date, streak, languages
- **Empty/negative result looks like:** "user not found" (no such account) or an error/ban (the tool broke against Duolingo's current API or the UA was blocked). Distinguish the two: a clean not-found is a real negative; an error is a tooling failure, not proof of absence.

## Gotchas & OpSec
- **Maintenance/degradation:** the repo is old and largely unmaintained; Duolingo API and User-Agent changes frequently break it. Expect to patch it or find a maintained fork.
- Profile fields are self-declared (country, name), so treat them as leads, not facts.
- OpSec: **passive** — public profile reads; throttle to avoid IP/UA bans, use a VPN.

## Overlaps ("do both")
- Complements broad email/username enumerators — Duolingo is one niche node; use it alongside multi-platform account-existence tools for fuller coverage.

## Trust & verifiability
`trust: community` — an unaffiliated hobby tool over Duolingo's public API; the underlying data is Duolingo's own (reliable when the tool works), but the wrapper's fragility means you should verify a hit and note the tool may be broken on any given day.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | duolingosint |
| category | social-networks |
| selectorsIn → selectorsOut | username, email → name, social-profile, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
