---
id: threads
name: Threads
description: Use when you have an Instagram/`username` or `name` and want the subject's Threads presence — returns their Threads profile, posts and (shared) Instagram identity link.
url: https://www.threads.net
category: social-networks
path:
- social-networks
bestFor: Finding a subject's Threads profile and posts, and leveraging the fact that a Threads handle is the same as the person's Instagram handle.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free Meta platform. Public profiles/posts are viewable on the web without login, but searching people and seeing more generally prompts an Instagram-linked login.
opsec: passive
opsecNote: Viewing public posts is passive and does not notify the subject. Threads accounts are tied to Instagram — if you log in to browse, use a sock-puppet Instagram account and never follow/like the target from it.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Meta platform, so profiles/posts are authoritative. Its tight coupling to Instagram is the key OSINT property — the Threads handle equals the Instagram handle.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- dumpor-instagram-search
aliases:
- Threads.net
- Meta Threads
tags:
- major-social-networks
- instagram
- meta
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Threads

> Meta's text network, welded to Instagram: a subject's Threads handle *is* their Instagram handle, so a hit here confirms the same person across both.

## When to use
You have an Instagram `username` (or a `name`) and want to (a) find the subject's Threads posts and (b) exploit the Instagram↔Threads link. Because Threads accounts are created from Instagram accounts and share the same handle, confirming a Threads profile corroborates an Instagram identity and vice-versa — and Threads users often post different, more text-heavy content (opinions, locations, real-time activity) than they do on Instagram.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to `https://www.threads.net/@<username>` using the subject's known Instagram handle.
2. If the profile exists, read public posts, bio, and linked Instagram profile — public content is viewable without login.
3. To search by `name` or browse more, sign in with a **sock-puppet Instagram** account (Threads login is Instagram-based).
4. Cross-confirm: the same handle existing on both Instagram and Threads strongly ties them to one person.
5. Pivot: feed the handle into Instagram tools like `[[dumpor-instagram-search]]`; mine Threads posts for locations, opinions, and associates.

## Inputs → Outputs
- **In:** `username` (Instagram handle) or `name`
- **Out:** `social-profile` (Threads posts, bio, and the linked Instagram identity)
- **Empty/negative result looks like:** no profile at the handle. The person may have Instagram but never activated Threads, or use a different handle — absence of Threads doesn't negate the Instagram account.

## Gotchas & OpSec
- Handle = Instagram handle: this is the feature to exploit, but a squatted/renamed handle can break the assumption — verify the linked Instagram matches.
- Full search/browsing nudges you to log in via Instagram — use a sock puppet.
- Content is federating to the fediverse (ActivityPub); some posts may also appear on Mastodon-side viewers.
- OpSec: passive when viewing public posts; interacting from a logged-in account is not.

## Overlaps ("do both")
- Pairs with `[[dumpor-instagram-search]]` — Threads confirms the handle and adds text-post content; the Instagram viewer pulls the visual/story side of the same account anonymously.

## Trust & verifiability
`trust: trusted` — first-party Meta platform, so posts and profiles are authoritative. The main caveat is confirming the Threads handle genuinely maps to your subject's Instagram, since handles can be reassigned.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | threads |
</content>
