---
id: rentry
name: Rentry
description: Use when you're chasing leaked/dumped data or a subject's posted notes — Rentry is a markdown pastebin where dumps and lists live; search-engine dorks surface them, returning `document-id` content.
url: https://rentry.co/
category: communities-forums
path:
- communities-forums
bestFor: Finding and reading Rentry paste pages (dumps, lists, doxes, notes) that a subject or a leaker has published.
selectorsIn:
- username
- email
selectorsOut:
- document-id
- email
status: live
pricing: free
costNote: Free markdown paste host; no account needed to create or read pastes.
opsec: passive
opsecNote: Reading a Rentry page is passive and anonymous — the author isn't notified. Pastes are unlisted (not directory-searchable on Rentry itself), so you usually reach them via search-engine dorks; opening one leaks nothing about you beyond a normal page visit. Do not edit/append to a paste (that could require the edit code and alters evidence).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Rentry is a legitimate paste host, but its content is anonymous user-generated text — dumps and "doxes" found there are unverified and may be fabricated, outdated, or malicious.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- rentry.co
- rentry.org
tags:
- pastebins
- paste-sites
source: awesome-osint
lastVerified: '2026-07-18'
enrichment: full
---

# Rentry

> A clean markdown pastebin popular for lists, guides and — for OSINT purposes — data dumps and "doxes"; you find the relevant page, then read it critically.

## When to use
You're investigating a leak, a dump, or a subject who publishes notes/lists, and you want to check whether relevant content lives on Rentry. Paste sites are where dumped credentials, compiled personal info, target lists, and how-to notes get posted. Because Rentry pastes are **unlisted** (there's no on-site search of all pastes), you typically discover them by dorking search engines (`site:rentry.co "target name"`), then open and read the paste for `email`s, handles, and other `document-id` content.

## How to use it (`bestInteractionPattern`: web-manual)
1. **Find the paste** via a search engine, since Rentry has no global search: e.g. `site:rentry.co "Firstname Lastname"`, `site:rentry.co "target@email.com"`, or a known Rentry URL/handle.
2. Open the Rentry page and read the markdown content; capture it (screenshot/archive) immediately — pastes can be deleted by their author.
3. Extract selectors: emails, usernames, phone numbers, links, and any claims about the subject.
4. **Verify everything** — treat dump/dox content as unconfirmed allegations until corroborated elsewhere.
5. Pivot: extracted emails/handles feed email/username OSINT; linked pastes/URLs lead to more sources.

## Inputs → Outputs
- **In:** a `username`, `email`, name, or known Rentry URL to search for
- **Out:** paste content (`document-id`) that may contain `email`s, handles, phone numbers, links and claims
- **Empty/negative result looks like:** no indexed Rentry page for the term — nothing has been posted (or it's unindexed/private). Absence isn't proof; also check other paste sites (Pastebin, Ghostbin, etc.).

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: **passive** — reading is anonymous and unseen; don't edit a paste. Archive quickly, as authors can delete.
- **Content is unverified and often malicious/fabricated** — dumps may be stale, fake, or planted. Corroborate before believing any claim, and handle exposed credentials as evidence, never to use.
- No native search: you're reliant on search-engine indexing, which misses recently-posted or noindexed pastes.

## Overlaps ("do both")
- Do both with other paste sites and with `[[google-dork-cheatsheet]]`/`[[google]]` to actually locate the pastes — the dork is how you find the Rentry page, Rentry is where you read it. Archive with `[[full-page-screen-capture-chrome-extension]]`.

## Trust & verifiability
`trust: community` — a legitimate host of anonymous, unverified content; the paste is real but its *claims* are not vouched for — verify independently before relying on anything found here.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | rentry |
| category | communities-forums |
| selectorsIn → selectorsOut | username, email → document-id, email |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
