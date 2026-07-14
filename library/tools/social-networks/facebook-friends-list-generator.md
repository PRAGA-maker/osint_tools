---
id: facebook-friends-list-generator
name: Facebook Friends List Generator
description: Use when you have a Facebook `social-profile` and want to enumerate that person's friends/connections via a browser tool — returns an associate list for network mapping.
url: https://osint.support/chrome-extensions/2019/10/20/facebook-friends-list-generator.html
category: social-networks
path:
- social-networks
bestFor: Extracting and listing a Facebook subject's friends/connections to map their associate network.
selectorsIn:
- social-profile
selectorsOut:
- associate
- social-profile
status: degraded
pricing: free
costNote: Free technique/extension documented on osint.support. Facebook has repeatedly tightened friend-list visibility and blocked scraping approaches, so the specific extension may be broken and the method degraded.
opsec: active
opsecNote: Active and account-bound — the technique runs from a logged-in Facebook session, so use a sock account. Scraping friend data can breach Facebook's terms and risk the account; only friends the target has made visible are obtainable.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: community
trustNote: A community-documented Chrome-extension technique from osint.support (a respected practitioner site). Third-party extensions can break with Facebook changes or go stale/malicious — vet any extension before installing.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: true
relatedTools:
- facebook-directory-users-by-name
- facebook-watch
aliases:
- FB friends list extractor
- osint.support friends list generator
tags:
- facebook
- browser-extension
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# Facebook Friends List Generator

> A community-documented browser technique for enumerating a Facebook subject's friends into a clean associate list for network mapping.

## When to use
You have a confirmed Facebook `social-profile` and want to map the subject's connections — friends are one of the strongest `associate` signals in missing-persons work (who to contact, where the person may be, shared locations). This osint.support write-up documents a Chrome-extension approach to pull and list a target's visible friends rather than scrolling them manually. Only works where the subject has left their friend list visible.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Read the osint.support guide at the URL for the current recommended extension/method and its cautions.
2. From a **sock** Facebook account, install the vetted extension (or apply the documented technique) in your browser.
3. Navigate to the target's profile Friends section and run the generator to collect the visible friends into a list.
4. Read the output: an enumerated `associate` list (names + profile links). Export/save for link analysis.
5. Pivot: each friend `social-profile` feeds profile checks and [[facebook-watch]]; recurring mutual connections highlight the subject's inner circle; names feed people-search.

## Inputs → Outputs
- **In:** `social-profile` (a Facebook profile whose friends are visible)
- **Out:** `associate` (friend list), `social-profile` (each friend's link)
- **Empty/negative result looks like:** an empty or tiny list — usually because the subject hid their friend list (Facebook default is now often "only me/friends"), or the extension is broken by a Facebook change. Not proof they have few friends.

## Gotchas & OpSec
- Facebook actively restricts friend-list visibility and blocks scrapers; this method is frequently degraded — verify the extension still works and isn't malicious before trusting it.
- Human-in-the-loop: requires a logged-in (sock) Facebook session and a local extension install.
- OpSec: **active** — scraping runs under your account and can violate Facebook's terms and get the account flagged/banned. Use a disposable sock account and only collect data the target made visible.

## Overlaps ("do both")
- Pairs with [[facebook-directory-users-by-name]] (to find the profile) and [[facebook-watch]] (to mine their video) — together they build identity, network, and media coverage of one Facebook subject.

## Trust & verifiability
`trust: community` — a technique from a respected practitioner blog, but reliant on third-party extensions that break as Facebook changes. Vet the tool, expect degradation, and confirm the friend list against the live profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facebook-friends-list-generator |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → associate, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | yes (account-login) |
