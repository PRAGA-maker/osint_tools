---
id: find-my-facebook-id-3
name: Find my Facebook ID
description: Use when you have a Facebook profile URL/`username` and want its stable numeric user ID — returns the numeric ID that anchors the profile against vanity-name changes.
url: https://findmyfbid.com
category: social-networks
path:
- social-networks
bestFor: Resolving a Facebook profile URL or vanity name to its permanent numeric user ID.
selectorsIn:
- username
- social-profile
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free single-purpose web tool. Widely reported operational, but the .com domain intermittently failed to resolve at verification; several mirrors exist as fallbacks.
opsec: passive
opsecNote: You paste a public profile URL into a third-party site; the target is not notified. Passive, but the resolver only works if the target profile allows search-engine linking, so results reflect the subject's privacy settings.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A small third-party utility (one of many near-identical FBID resolvers); it only echoes Facebook's own numeric ID, so correctness is easy to spot-check, but the specific domain's uptime is unreliable.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- findmyfbid
- findmyfbid.com
- Facebook numeric ID lookup
tags:
- facebook
- facebook-id
source: metaosint
lastVerified: '2026-07-14'
enrichment: full
---

# Find my Facebook ID

> A one-field utility that turns a Facebook profile URL or vanity name into its permanent numeric user ID — the stable key that survives display-name and vanity-URL changes.

## When to use
You have a Facebook `username`/vanity URL or profile link and need the underlying **numeric ID**. That numeric ID is the durable anchor for a Facebook subject: it lets you re-find the profile after they change their vanity name, construct direct-ID URLs, and cross-reference the account in scrapers and graph-search tools that key on ID rather than name.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://findmyfbid.com. If the domain fails to load, use a mirror (e.g. lookup-id.com, findmyfbid.me, commentpicker.com's finder) — they do the same job.
2. Paste the target's Facebook profile URL (or vanity name).
3. Read the returned numeric `social-profile` ID.
4. Verify by loading `facebook.com/<numeric-id>` and confirming it opens the same profile.
5. Pivot: the numeric ID feeds Facebook graph-search techniques, scrapers, and re-identification after a vanity-name change.

## Inputs → Outputs
- **In:** Facebook profile URL or vanity `username`
- **Out:** the profile's permanent numeric ID (`social-profile`)
- **Empty/negative result looks like:** an error or no ID — usually because the profile disallows search-engine linking, the URL is wrong, or the account is restricted; try a mirror or the raw profile source before concluding.

## Gotchas & OpSec
- Reliability: the specific `.com` domain is flaky; keep mirrors handy and cross-check the ID by loading it directly.
- Depends on the target's "allow search engines to link to your profile" setting; privacy-locked profiles may not resolve.
- Numerous near-identical clones exist — prefer whichever currently resolves and always verify the ID against Facebook itself.

## Overlaps ("do both")
- Feeds Facebook scraping/graph tools and `[[social-profiles-finder]]`: resolve the numeric ID here, then use it as the stable key everywhere the vanity name would break.

## Trust & verifiability
`trust: unverified` — a minor third-party utility, but its output is Facebook's own numeric ID, so you can (and should) confirm each result by opening `facebook.com/<id>` directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | find-my-facebook-id-3 |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
