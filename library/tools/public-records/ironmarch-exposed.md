---
id: ironmarch-exposed
name: Ironmarch.exposed
description: Use when you have a `username`, `email`, or `name` and want to check whether it appears in the leaked IronMarch neo-fascist forum database — returns member profiles, emails, IPs, and posts.
url: https://www.ironmarch.exposed/
category: public-records
path:
- public-records
bestFor: Searching the 2019 IronMarch forum leak to tie a handle/email to a member account and its posts, contacts, and IPs.
selectorsIn:
- username
- email
- name
selectorsOut:
- email
- ip-address
- username
- associate
- social-profile
status: live
pricing: free
costNote: Free, publicly searchable archive of the leaked dataset; no account.
opsec: passive
opsecNote: Searching the archive is passive — you query a static leak database, and nothing is sent to the person named. Handle the data with care: it is a criminal-adjacent leak involving named individuals; use it for legitimate investigation/journalism, corroborate before attributing, and be aware of the legal/ethical weight of acting on breached personal data.
humanInLoop: false
humanInLoopReason:
- legal-gate
bestInteractionPattern: web-manual
trust: community
trustNote: A community-built searchable front-end to the well-documented 2019 IronMarch database leak; the underlying data is genuine forum data but, like any leak, may contain aliases, spoofed emails, and shared/temporary IPs.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- Iron March Forum Leak
- ironmarch.exposed
tags:
- data-leak
- extremism-research
- public-records
source: osint4all
lastVerified: '2026-07-29'
enrichment: full
---

# Ironmarch.exposed

> A searchable archive of the leaked IronMarch neo-fascist forum: check whether a handle, email, or name belonged to a member, and pull their profile, posts, and connections.

## When to use
A specialised extremism-research resource. When investigating someone's possible ties to the militant neo-fascist IronMarch network (2011–2017) — for journalism, threat assessment, or vetting — and you have a `username`, `email`, or `name` to check against the 2019 leak. A hit links a persona to real posts, registration email, login IPs, and other members they interacted with (`associate`). Not a general people-finder; scoped to this one dataset.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.ironmarch.exposed/ in a clean/sock-puppet session.
2. Search a `username`, `email`, or `name` against the leaked member/user tables.
3. Read the member record: registration `email`, login `ip-address`(es), posts, and referenced/interacting members (`associate`), plus any linked handles (`social-profile`).
4. Corroborate: an email/handle match is a lead, not proof — confirm the same email/handle elsewhere before attributing the account to a real person.
5. Pivot: the registration `email` and reused `username` feed email/username OSINT; login IPs feed geolocation/ASN; named associates map the network.

## Inputs → Outputs
- **In:** `username`, `email`, or `name`
- **Out:** member profile, registration `email`, login `ip-address`, posts, `associate`s, linked handles
- **Empty/negative result looks like:** no matching record — the identifier wasn't in the leak (never a member, used a different handle/email, or joined outside the leak window); not proof of non-involvement.

## Gotchas & OpSec
- **Legal/ethical gate:** this is breached personal data about named individuals; use it for legitimate purposes, corroborate before naming anyone, and follow local law on handling leaked data.
- Leak data can be gamed: spoofed registration emails, shared/VPN IPs, throwaway handles — an IP or email is a lead, not an identity.
- The archive is a mirror of a fixed 2019 dump; it does not update.

## Overlaps ("do both")
- Pairs with email- and username-enumeration tools and breach-aggregators — cross-confirm any IronMarch email/handle in an independent source before attributing it to a real person.

## Trust & verifiability
`trust: community` — a community-maintained front-end to a genuine, widely-reported leak; the raw data is authentic but self-reported forum data, so every attribution needs independent corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ironmarch-exposed |
| category | public-records |
| selectorsIn → selectorsOut | username, email, name → email, ip-address, username, associate, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (legal-gate) |
