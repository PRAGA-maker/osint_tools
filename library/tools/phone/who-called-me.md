---
id: who-called-me
name: Who Called Me
description: Use when you have a `phone` number and want community reports about it — returns user comments/ratings flagging spam, scam or the likely caller identity.
url: https://www.whocalledme.com/
category: phone
path:
- phone
bestFor: Crowd-sourced reputation and spam/scam reports for an unknown phone number.
selectorsIn:
- phone
selectorsOut:
- phone
status: live
pricing: freemium
costNote: Free to search and read community reports; monetised by ads, with some deeper-lookup upsells to paid brokers.
opsec: passive
opsecNote: You read a public community database — no call/text reaches the number and the owner isn't notified. You disclose the number to the site; use a sock-puppet browser. Reports are user-submitted opinions, not verified facts.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Crowd-sourced caller-reputation site; useful for spam/scam signal but comments are anonymous and unverified, so attribution is soft.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- WhoCalledMe
- whocalledme.com
tags:
- reverse-phone
- caller-id
- spam-reports
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Who Called Me

> A crowd-sourced caller-reputation board: what have other people said about this number — spam, scam, or a real business/person?

## When to use
You have a `phone` number and want the community's view before you spend on paid attribution: is it a known spam/scam line, a legitimate business, or has anyone named the caller? Good for quickly triaging a number pulled from a missing person's contacts or a message — the comments often identify the source (debt collector, delivery firm, scam) even when brokers can't name an individual.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.whocalledme.com/ in a sock-puppet browser.
2. Enter the `phone` number and search.
3. Read the community reports: a spam/safe rating, number of lookups, and free-text comments where users describe who called and why.
4. Weigh the signal: many consistent "scam/robocall" comments are a strong negative signal; a comment naming a specific business is a lead to verify.
5. Pivot: a named business feeds company records; a "personal number" with no spam reports pushes you toward reverse-phone attribution (`[[whitepages-reverse-phone]]`, `[[thats-them]]`).

## Inputs → Outputs
- **In:** `phone`
- **Out:** community spam/safe rating and free-text `phone` reports/attribution
- **Empty/negative result looks like:** "no reports" — nobody has commented on this number. Common for personal/low-volume numbers; absence of reports is neutral, not proof the number is safe or unused.

## Gotchas & OpSec
- Reports are **anonymous and unverified** — treat comments as leads and sentiment, not fact; scammers and businesses can also post.
- Coverage skews to high-volume (spam/telemarketing) numbers; personal numbers rarely have reports.
- OpSec: **passive**; the site sees your query. Use a sock puppet.

## Overlaps ("do both")
- Pairs with reverse-phone attribution (`[[whitepages-reverse-phone]]`, `[[thats-them]]`, `[[cell-revealer-telephone-number-lookup]]`) and line-type checks (`[[phone-validator-us]]`) — reputation tells you *how the number behaves*, attribution tells you *who owns it*. Do both.

## Trust & verifiability
`trust: community` — a crowd-sourced reputation site; the aggregate spam signal is useful, but individual attributions are unverified. Corroborate any named caller before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | who-called-me |
| category | phone |
| selectorsIn → selectorsOut | phone → phone |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
