---
id: addmecontacts
name: addmeContacts
description: Use when you have a `username`/`name` and want to find messaging-app handles a person has publicly listed to be added — returns linked `social-profile` handles (Snapchat/Skype/WhatsApp/etc.).
url: http://add-me-contacts.com
category: username
path:
- username
bestFor: Searching a self-submitted directory where users post their Snapchat/Skype/WhatsApp/WeChat handles for others to add.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free to browse the listings; no account needed to view.
opsec: passive
opsecNote: Browsing public listings reveals nothing about your subject and alerts no one. Passive — but the site is a low-trust, ad-heavy directory; use a sandboxed/sock-puppet browser and avoid clicking through to contact anyone.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: An anonymous, user-submitted contact-sharing directory with no verification; entries are self-posted and often spam/adult-adjacent, so treat any match as a weak, unconfirmed lead.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- add-me-contacts.com
- Add Me Contacts
tags:
- snapchat
- skype
- username-discovery
source: osintambition-social
lastVerified: '2026-07-16'
enrichment: full
---

# addmeContacts

> A self-submitted directory of messaging-app handles (Snapchat, Skype, WhatsApp, WeChat and more) where users post their usernames to be added — a long-shot source for tying a handle to other platforms.

## When to use
You have a `username` or `name` and are casting a wide net for other accounts a person exposed, and you want to check whether they ever posted their messaging handles to a public "add me" directory. It is a low-yield, low-trust supplement — worth a quick check when you are enumerating a handle across many sites, not a primary source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://add-me-contacts.com in a sandboxed/sock-puppet browser.
2. Browse or search the platform sections (Snapchat, Skype, WhatsApp, WeChat, etc.) for the handle or name.
3. Review any listing that matches.
4. Read the output: self-posted handles/`social-profile` for the various apps, sometimes with a short bio or location note.
5. Pivot: take a matched handle into username-enumeration and the relevant app's own search; corroborate heavily before trusting it.

## Inputs → Outputs
- **In:** `username` / `name`
- **Out:** `social-profile` (self-listed messaging-app handles)
- **Empty/negative result looks like:** no matching listing — the overwhelmingly common case, since only people who opted into such directories appear.

## Gotchas & OpSec
- **Status: degraded / very low signal** — the directory is dominated by spam and adult-solicitation entries, and coverage of any specific person is tiny; expect mostly noise.
- Entirely unverified and self-submitted — a match proves someone *posted* a handle, not that it belongs to your subject.
- OpSec: passive, but the site is untrustworthy — sandbox it, block scripts, and never actually contact a listed account from a real profile.

## Overlaps ("do both")
- Complements proper username-enumeration tools (Sherlock/WhatsMyName-style): those systematically check mainstream platforms; this only catches handles someone deliberately posted to an add-me directory.

## Trust & verifiability
`trust: unverified` — an anonymous, unmoderated contact-sharing site. Any hit is a weak lead to confirm elsewhere, never evidence on its own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | addmecontacts |
| category | username |
| selectorsIn → selectorsOut | username, name → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
