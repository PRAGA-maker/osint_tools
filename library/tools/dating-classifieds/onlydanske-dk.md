---
id: onlydanske-dk
name: onlydanske.dk
description: Use when you have a `username` or creator name and want to check whether it maps to a Danish OnlyFans persona — returns the linked `social-profile` (OnlyFans account) and any handle/name variants listed.
url: https://onlydanske.dk/
category: dating-classifieds
path:
- dating-classifieds
bestFor: Resolving a username/creator handle to a Danish adult-creator (OnlyFans) profile and its cross-links.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free directory; it links out to OnlyFans, where the actual content sits behind that platform's own paywalls. Browsing/searching the directory costs nothing.
opsec: passive
opsecNote: Passive — it's a third-party directory that scrapes/links public OnlyFans creator pages; searching it does not notify the creator. It is an adult-content site; use a sock-puppet browser, and never authenticate or subscribe from a real identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: An unaffiliated third-party aggregator of Danish OnlyFans creators (explicitly "ikke tilknyttet onlyfans.com"); listings are user/scrape-sourced and unverified, and creators come and go.
missingPersonsRelevance: medium
coverage:
- dk
auth: none
api: false
localInstall: false
registration: false
aliases:
- onlydanske
- Only Danske
tags:
- onlyfans
- OnlyFans Related Sites
- adult
source: uk-osint
lastVerified: '2026-07-21'
enrichment: full
---

# onlydanske.dk

> A third-party directory of Danish OnlyFans creators — a narrow way to tie a `username`/handle to an adult-creator persona and its cross-platform links.

## When to use
You are tracing a `username` or creator name in the Danish adult-content space and want to know whether it corresponds to an OnlyFans persona. Adult-creator handles are often reused across platforms, so a hit here can connect a handle to a public persona, a profile image (for reverse-image work), and sometimes linked socials — occasionally relevant in missing-persons or exploitation cases, or when disambiguating an alias.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://onlydanske.dk/ in a sock-puppet browser (adult content; treat accordingly).
2. Use the site search or browse the directory for the `username`/creator name.
3. Open the listing: it shows the creator's display name/handle, a thumbnail, and a link out to the actual OnlyFans profile (content stays on OnlyFans).
4. Take the profile image and any listed socials for pivoting; do **not** subscribe or log in.
5. Pivot: the thumbnail feeds `[[face]]`/reverse-image search; a confirmed handle feeds cross-platform username enumeration; the OnlyFans display name may match other social accounts.

## Inputs → Outputs
- **In:** `username` or creator `name`
- **Out:** linked `social-profile` (OnlyFans), confirmed `username`/display-name, thumbnail image
- **Empty/negative result looks like:** no listing for the handle — the creator isn't Danish-listed here, uses a different handle, or has been removed; absence proves nothing about OnlyFans presence generally.

## Gotchas & OpSec
- **Adult-content site**, unaffiliated with OnlyFans — expect scraped/aggregated, unverified listings and NSFW imagery; handle under a sock puppet.
- Handles are frequently reused *and* impersonated across adult platforms; corroborate before asserting identity.
- Listings churn quickly as creators join/leave; a removed listing is not evidence the persona never existed.

## Overlaps ("do both")
- Pairs with reverse-image/face search on the thumbnail and with cross-platform username tools — this only confirms the Danish-OnlyFans link; those extend it to other identities.

## Trust & verifiability
`trust: unverified` — an unaffiliated aggregator with no vetting; a listing is a lead to verify (image match, handle consistency), never proof of identity on its own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | onlydanske-dk |
| category | dating-classifieds |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
