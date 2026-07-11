---
id: nicolasconstant-github-io
name: Sengi (Mastodon/Pleroma client)
description: Use when you have a Mastodon/Pleroma `username` or instance handle and want a multi-account desktop/web client to read and monitor fediverse activity — returns social-profile context, associates and post threads.
url: https://nicolasconstant.github.io/sengi/
category: social-networks
path:
- social-networks
bestFor: Monitoring and reading fediverse (Mastodon/Pleroma) accounts and timelines across multiple sock-puppet accounts in one interface.
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
- name
- associate
status: live
pricing: free
costNote: Free and open source (FLOSS); usable as a web app or installed desktop client. No paid tier.
opsec: passive
opsecNote: Reading public fediverse posts is passive. However, following, boosting, or replying from an account is active and visible to the target and their instance admins — keep a research account in read-only discipline and never interact from your real identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: desktop-app
trust: community
trustNote: Open-source client by developer Nicolas Constant, hosted on GitHub Pages; the code is public and auditable, but it is a community project, not an official Mastodon product.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
aliases:
- Sengi
- sengi mastodon client
tags:
- mastodon
- pleroma
- fediverse
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Sengi (Mastodon/Pleroma client)

> A free, multi-account Mastodon and Pleroma client (web or desktop) that lets an investigator watch several fediverse accounts and timelines side by side without app-switching.

## When to use
You are tracking a subject across the fediverse — you have a Mastodon/Pleroma `username`/handle (e.g. `@person@instance.social`) and want a comfortable read/monitor surface: their profile, boosts, replies, threaded context, and who they interact with. Useful when the subject has migrated off mainstream networks to a small instance.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Open the web app at https://nicolasconstant.github.io/sengi/ or install the desktop build (Snap for Linux / GitHub releases).
2. Add one or more **sock-puppet** fediverse accounts (Sengi is multi-account; use research accounts only).
3. Search the target handle, open their profile, and read their timeline; Sengi keeps profiles, threads and hashtags in-context so you can follow a conversation without losing your place.
4. Use the status labels (thread / has-replies / bot / cross-posted) to triage which posts matter.
5. Pivot: replies and boosts surface `associate` links; a cross-post label hints at other networks the subject uses; profile metadata can reveal `name` or external links.

## Inputs → Outputs
- **In:** fediverse `username`/handle or `social-profile` URL
- **Out:** `social-profile` detail, possible real `name`, and `associate` interactions (who they reply to/boost)
- **Empty/negative result looks like:** the handle resolves to no account, or a private/locked account shows only a profile shell with no readable posts — locked accounts require a follow-approval you should not seek from a real identity.

## Gotchas & OpSec
- Human-in-the-loop: Sengi needs at least one fediverse account logged in to function — set up a dedicated research account first.
- OpSec: **reading is passive, interacting is not.** Boosting/following/replying is visible to the target and to instance moderators, who on small instances are attentive. Stay read-only.
- Instance-scoped: what you can see depends on federation between your account's instance and the target's; a defederated or isolated instance may be invisible from your account.

## Overlaps ("do both")
- Pairs with a fediverse account-discovery search (e.g. Mastodon instance search / `[[fedidb]]`-style tools) — those find where the account lives; Sengi is where you read and monitor it.

## Trust & verifiability
`trust: community` — an open-source, auditable client maintained by an independent developer. It faithfully renders fediverse data; it does not add or vouch for the content of the posts themselves.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nicolasconstant-github-io |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → social-profile, name, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | yes (account-login) |
