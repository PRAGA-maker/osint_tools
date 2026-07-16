---
id: redlinecybersecurity-com
name: Redline — Dating a LinkedIn Post (technique)
description: Use when you have a LinkedIn post URL (a `social-profile` activity) and want its exact publish timestamp for a timeline — returns a precise date/time decoded from the post's activity ID.
url: https://www.redlinecybersecurity.com/blog/how-to-get-the-exact-date-of-a-linkedin-post-using-osint-techniques
category: social-networks
path:
- social-networks
bestFor: Recovering the exact publish date/time of a LinkedIn post from its activity ID when the page only shows a fuzzy "3mo" label.
selectorsIn:
- social-profile
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free technique/write-up; no account, no tool purchase — you decode a number from a public URL.
opsec: passive
opsecNote: The decoding is done on a URL/number you already have; you never re-query LinkedIn, so the subject gets no notification. If you first navigate LinkedIn to grab the post URL, do that from a sock-puppet account (LinkedIn shows "who viewed your profile").
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A vendor blog write-up of a widely-documented method; the underlying trick (the Unix timestamp embedded in the activity ID) is deterministic and independently verifiable.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- LinkedIn post exact date
- LinkedIn activity ID timestamp
tags:
- linkedin
- timestamp
- technique
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# Redline — Dating a LinkedIn Post (technique)

> A step-by-step write-up of the classic trick: LinkedIn embeds a Unix timestamp in every post's activity ID, so any public post URL yields its exact publish date/time.

## When to use
You have a LinkedIn post (yours or a target's `social-profile` activity) and the UI only shows a coarse "2w"/"3mo" label, but you need the precise date/time to place the post on a timeline — corroborating when someone was in a place, employed somewhere, or online.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the LinkedIn post and copy its URL — it contains a long numeric activity/URN id, e.g. `.../feed/update/urn:li:activity:7123456789012345678/`.
2. Take that 19-digit activity id and read it as a 64-bit integer; the **first 41 bits** encode the Unix timestamp in **milliseconds** (the same scheme snowflake-style IDs use).
3. Compute it: convert the id to binary, keep the leading 41 bits, convert back to a decimal, and treat that as milliseconds since 1970 (divide by 1000 for a normal Unix time). A public "LinkedIn Post Timestamp" web tool or a one-line script does the arithmetic; the blog walks through both.
4. Read out the exact UTC date/time and slot it into your timeline. Repeat across a profile's posts to reconstruct an activity pattern.

## Inputs → Outputs
- **In:** a LinkedIn post URL / activity id (`social-profile` activity)
- **Out:** the exact publish date/time (UTC) of that post; across many posts, a per-account activity timeline
- **Empty/negative result looks like:** a URL with no `urn:li:activity:` id (e.g. an article or company page share) — the id-based method does not apply; fall back to page metadata or archive snapshots.

## Gotchas & OpSec
- Only the numeric **activity** id carries the timestamp — comment ids and some share formats differ; make sure you decoded the post's own id.
- The value is the *original post* time; edits and reshares are not reflected.
- OpSec: passive — decoding happens offline on a URL you hold, so no LinkedIn notification fires. Grab the URL from a sock-puppet account, since viewing a profile/post can register.

## Overlaps ("do both")
- Pairs with LinkedIn archive/snapshot tools — the timestamp trick gives the exact moment, while an archive confirms the post's original content at that moment.

## Trust & verifiability
`trust: community` — a vendor blog, but the method is deterministic maths on a public identifier and independently reproducible, so the derived timestamp is high-confidence (not a scraped guess).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | redlinecybersecurity-com |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
