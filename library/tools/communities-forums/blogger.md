---
id: blogger
name: Blogger
description: Use when you have a `name` or `username` and want to find a subject's personal blog or Blogger/Blogspot profile — returns `social-profile`, posts, and linked contact/`email` details.
url: https://www.blogger.com
category: communities-forums
path:
- communities-forums
bestFor: Finding a subject's self-published blog and Blogger profile, which often expose interests, timelines, and contact links.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- email
status: live
pricing: free
costNote: Free Google service; reading public blogs and profiles needs no account (a Google login is only needed to publish).
opsec: passive
opsecNote: Reading public *.blogspot.com blogs and Blogger profiles is passive. Beware that visiting a low-traffic personal blog can appear in the owner's analytics/referrer logs; use a sock-puppet/logged-out session and avoid commenting.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Google; profiles and posts are genuine first-party user content, though the content itself is self-reported by the blogger.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Blogspot
- blogger.com
tags:
- toddington
- curated-directory
- online-communities-blogs
- blogs
source: toddington-resources
lastVerified: '2026-07-20'
---

# Blogger

> Google's blog platform (Blogspot) — a rich source of a subject's self-published writing, interests, and contact links when they keep a personal blog.

## When to use
You have a `name`, `username`, or email handle and want to find whether the subject maintains a personal blog. Blogger/Blogspot blogs are often long-lived, candid, and packed with pivots — interests, locations, photos with `metadata-exif`, timelines of activity, linked social accounts, and sometimes a contact `email`. Older blogs (2005–2015 especially) can survive long after the person has scrubbed newer platforms, making Blogger a good source for a subject's earlier life.

## How to use it (`bestInteractionPattern`: web-manual)
1. The `blogger.com` root redirects to a Google sign-in dashboard — for OSINT you work with the public side instead: individual blogs live at `<name>.blogspot.com` and profiles at `https://www.blogger.com/profile/<numeric-id>`.
2. Guess/confirm handle-based subdomains: try `subjecthandle.blogspot.com`.
3. Dork it: `site:blogspot.com "Full Name"` or `site:blogspot.com "username"` to surface posts and comments.
4. Open the blogger's **Profile** page — it can list real name, location, other blogs they run, interests, and an obfuscated email.
5. Pivot: linked blogs and profile fields feed username-enumeration and email tools; embedded images feed reverse-image/EXIF checks.

## Inputs → Outputs
- **In:** `name`, `username`, or email handle
- **Out:** `social-profile` (Blogger profile + blog), posts/comments, other blogs by the same profile, sometimes a contact `email`
- **Empty/negative result looks like:** no blog under the handle and no dork hits — common, since most people never blogged; absence is weak evidence.

## Gotchas & OpSec
- A Blogger profile ID aggregates *all* blogs that account runs — a strong pivot to find a person's other sites.
- Content is self-reported; a blog can be pseudonymous or abandoned. Corroborate identity before attributing.
- OpSec: reading is passive, but small personal blogs may see your referrer/analytics — stay logged out, never comment.

## Overlaps ("do both")
- Pairs with username-enumeration and general web-search dorking — Blogger is one platform in a footprint sweep; run the same handle across others.

## Trust & verifiability
`trust: trusted` — Blogger is genuine first-party Google infrastructure, so a profile/blog is authentic; the *claims within* a blog are self-reported and need corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | blogger |
| category | communities-forums |
| selectorsIn → selectorsOut | name, username → social-profile, email |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
