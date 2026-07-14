---
id: tumblr-com
name: Tumblr
description: Use when you have a `username` and want to find a subject's Tumblr blog and image posts — returns a `social-profile` and the images/text they post, often more candid than mainstream platforms.
url: http://www.tumblr.com/tagged/image-search
category: image-video-face
path:
- image-video-face
bestFor: Finding a subject's Tumblr blog by handle and mining its image posts, reblogs, and interests.
selectorsIn:
- username
selectorsOut:
- social-profile
- image
status: live
pricing: free
costNote: Free to view public blogs; an account (free) is only needed to interact, which you should avoid.
opsec: passive
opsecNote: Viewing public blog URLs (`<username>.tumblr.com`) is passive and unauthenticated. Do not log in and follow/like — that notifies the blog owner. Note some blogs gate mature content behind a login prompt.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party access to a real, large blogging platform; content is user-generated (self-asserted), but a confirmed blog is authentic.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- tumblr.com
tags:
- reverse-image
- face
- blogging
- social-media
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# Tumblr

> A large blogging/microblogging platform where people post images, interests, and personal writing under a handle — often more candid and less curated than Instagram or Facebook.

## When to use
You have a `username` and want to check for a Tumblr blog. Tumblr users frequently reuse handles and post revealing content — personal photos, art, fandoms, mental-health and identity discussion, location snippets — that they don't put on mainstream networks. It's a strong node in a username sweep, especially for younger subjects and creative communities. (The stub's tag-page URL is just one search surface; the real value is `username` → blog.)

## How to use it (`bestInteractionPattern`: web-manual)
1. Try the blog URL directly: `https://<username>.tumblr.com/`.
2. Use Tumblr's search and tag pages (e.g. `tumblr.com/tagged/<term>`) to find related posts/blogs.
3. Browse the blog's posts, reblogs, and "about" page for images (`image`), interests, associates, and location clues.
4. Do not log in to like/follow; screenshot posts and save permalinks as citations.
5. Pivot: reused handle → cross-platform username tools; posted images → reverse-image/face search; reblog network → `associate`s and communities.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` (the blog), `image` posts, interests, reblog/association network
- **Empty/negative result looks like:** no blog at the handle, a deactivated blog, or a login wall on mature content — none of which prove the person has no Tumblr presence under another handle.

## Gotchas & OpSec
- Handles are reassigned after deletion — confirm the current blog is your subject.
- Mature-content blogs may require a login to view; weigh using a sock puppet vs. staying logged out.
- Content is self-asserted and often performative/fannish — corroborate factual claims.

## Overlaps ("do both")
- Pairs with `[[whatsmyname]]` (flags the Tumblr hit) and reverse-image tools (link its photos outward); check the Wayback Machine for deleted blogs.

## Trust & verifiability
`trust: trusted` — first-party platform access, so a located blog is genuine; treat the *content* as user claims to verify, not established fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tumblr-com |
| category | image-video-face |
| selectorsIn → selectorsOut | username → social-profile, image |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
