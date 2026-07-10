---
id: ollie-boyd-github-io
name: ollie-boyd.github.io
description: Use when you have a LinkedIn post/activity URL and want the exact time it was published — returns the precise creation timestamp (local + UTC) decoded from the post ID.
url: https://ollie-boyd.github.io/Linkedin-post-timestamp-extractor/
category: social-networks
path:
- social-networks
bestFor: Recovering the exact publication timestamp of a LinkedIn post from its URL/activity ID.
selectorsIn:
- social-profile
selectorsOut:
- metadata-exif
status: live
pricing: free
costNote: Free client-side static web tool hosted on GitHub Pages; no account, no API key.
opsec: passive
opsecNote: The timestamp is decoded locally in your browser from the numeric post ID embedded in the URL — nothing is sent to LinkedIn and the post owner is not notified. You only need the URL, which you can copy without visiting/interacting with the post while logged in.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open, single-purpose community tool that decodes the timestamp deterministically from the LinkedIn snowflake-style ID; verifiable and low-risk, but community-maintained.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- thread-reader
aliases:
- LinkedIn Post Timestamp Extractor
tags:
- linkedin
- LinkedIn & Similar Sites
- timestamp
- metadata
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# ollie-boyd.github.io

> A one-purpose tool that decodes the exact publication time of any LinkedIn post from the numeric ID baked into its URL — LinkedIn only shows fuzzy "3d ago" labels.

## When to use
You have a LinkedIn post or activity URL and need the precise moment it was published (down to the second), not LinkedIn's relative "2w"/"3mo" label. Exact timestamps matter for building timelines, establishing when a subject was demonstrably online/active, corroborating or contradicting an alibi, or ordering events across platforms. The tool exploits the fact that LinkedIn embeds a timestamp inside each post's numeric activity ID.

## How to use it (`bestInteractionPattern`: web-manual)
1. Copy the LinkedIn post URL (the part containing `activity-<big number>` / `urn:li:activity:<number>`). You can grab this without logging in if the post is public.
2. Open https://ollie-boyd.github.io/Linkedin-post-timestamp-extractor/.
3. Paste the URL into the "Get uploaded date" field and submit.
4. Read the output: the exact upload time shown both in a local/readable form and in UTC.
5. Pivot: drop the UTC timestamp into your case timeline; compare against activity on other platforms (e.g. thread timestamps via `[[thread-reader]]`).

## Inputs → Outputs
- **In:** a LinkedIn post/activity URL (`social-profile` carrying the embedded ID)
- **Out:** exact creation timestamp `metadata-exif` — local time and UTC
- **Empty/negative result looks like:** no timestamp returned — usually the URL doesn't contain a valid activity ID (e.g. it's a profile or company URL, or a shortened/redirected link). Resolve to the canonical post URL and retry.

## Gotchas & OpSec
- Only works on URLs that carry the numeric activity/post ID; profile, article, and some share URLs won't parse until expanded to the underlying post.
- The decode is deterministic — the same URL always yields the same time — so results are independently checkable.
- OpSec: **passive** — computation happens in your browser; no request reaches LinkedIn and the subject is never alerted.

## Overlaps ("do both")
- Conceptually pairs with `[[thread-reader]]` and other timestamp/timeline tools — each recovers precise times on a different platform so you can align a subject's cross-platform activity.

## Trust & verifiability
`trust: community` — an open, single-function community tool whose output is deterministic and easy to sanity-check; safe and verifiable, though not an official LinkedIn feature.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ollie-boyd-github-io |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile, metadata → metadata |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
