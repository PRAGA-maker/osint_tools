---
id: x-com-3
name: x.com
description: Use when you want curated LinkedIn/people-finding OSINT technique tips from the @cyb_detective account — returns pointers to `social-profile` search methods, not a lookup.
url: https://x.com/cyb_detective/status/1891600542872297622
category: social-networks
path:
- social-networks
bestFor: Reading a curated OSINT tip/thread from @cyb_detective on finding people and profiles.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free public post; viewing full threads on X increasingly prompts a login.
opsec: passive
opsecNote: Reading a public tweet is passive; the subject of your investigation is not involved. Do not like/reply/bookmark from an attributable account — those actions are logged and visible.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: '@cyb_detective (Cyber Detective) is a widely-cited OSINT curator, but this is a personal tip — verify each referenced tool/technique independently before relying on it.'
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- cyb_detective tweet
- Cyber Detective OSINT tip
tags:
- linkedin
- LinkedIn & Similar Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
relatedTools:
- help-x-com
- here-19
- here-20
- twitter-search
- twitter-x-advanced-search
- verif-cation-quiz-bot
- x-com
- x-com-4
- x-com-6
---

# x.com

> A specific post from @cyb_detective (Cyber Detective), one of the most-followed OSINT tool curators — a pointer to a technique or tool for finding people, filed here under LinkedIn/profile-search methods.

## When to use
You want a vetted starting point for a profile-search technique rather than a database. @cyb_detective regularly publishes concise tips and tool lists; this post is one of them. Reach for it when you're stuck on how to surface a subject's `social-profile` and want a practitioner's method to try — but treat it as a lead to a technique, not a lookup you run directly.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the post at https://x.com/cyb_detective/status/1891600542872297622. If X gates the full thread behind login, view it in a logged-out/nitter-style reader or use a sock account.
2. Read the technique/tool it describes and any replies (curator threads often have crucial follow-ups and corrections in the comments).
3. Apply the method against your subject; verify the referenced tool is still live and behaves as claimed.
4. Pivot: whatever `social-profile` or `name` the technique surfaces feeds your normal enrichment chain.

## Inputs → Outputs
- **In:** your investigative goal (a `name`/`username` you're trying to resolve)
- **Out:** a documented OSINT technique/tool pointer → potential `social-profile` leads
- **Empty/negative result looks like:** the post is a tip, not a query — "empty" means the technique doesn't fit your case; move to the next method.

## Gotchas & OpSec
- Human-in-the-loop / **account-login**: X frequently requires a login to see full threads and replies. Use a sock account; never engage (like/reply) from an attributable one.
- Single-post sources age: the referenced tool may have died since posting — confirm before trusting.
- It's one curator's opinion, however respected — cross-check the technique.

## Overlaps ("do both")
- Pairs with `[[linkedprospect]]` — this supplies the LinkedIn-search *method*; that supplies the Boolean *string* to execute it.

## Trust & verifiability
`trust: community` — @cyb_detective is a highly regarded OSINT source, but a single tweet is a personal tip; verify the underlying tool/technique yourself before relying on results.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | x-com-3 |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
