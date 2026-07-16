---
id: tinder-usernames
name: Tinder Usernames
description: Use when you have a Tinder `username` and want to confirm the profile exists and see its public web card — returns name, photos and basic info when the user enabled web sharing.
url: https://www.gotinder.com/@username
category: username
path:
- username
- specific-sites
bestFor: Confirming a Tinder profile exists and viewing its shared public web card by username.
selectorsIn:
- username
selectorsOut:
- social-profile
- image
- name
status: live
pricing: free
costNote: Free — just load a public URL. No account or app needed to view a shared web profile.
opsec: passive
opsecNote: This is a plain HTTP GET to a public share URL; unlike swiping in the app, it does not notify the target or appear in their likes. It is not "matching" — you're only viewing a page the user chose to make shareable. Use a clean/sock-puppet browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: The URL resolves against Tinder's own web infrastructure, so a returned profile is first-party and authentic; only users who enabled a public web username are reachable this way.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- tinder-com
- social-searcher
- look-by-username-replace-username-in-this-case-mark
- tinder-2
aliases:
- gotinder.com username
- Tinder web profile
tags:
- tinder
- dating
- username
source: arf-seed
lastVerified: '2026-07-14'
enrichment: full
---

# Tinder Usernames

> A username-to-profile check on Tinder: load `gotinder.com/@<username>` to confirm a profile exists and see its public web card — without swiping or matching.

## When to use
You have a candidate Tinder `username` (some users set a shareable web username) and want to confirm it belongs to a real, active profile and see what it exposes — display name, photos, and any bio/basic info the user made public. Useful for tying a handle used elsewhere to a dating presence, corroborating photos, and confirming someone is active on Tinder without any in-app interaction.

## How to use it (`bestInteractionPattern`: web-manual)
1. In a clean/sock-puppet browser, open `https://www.gotinder.com/@<username>` (replace `<username>`).
2. If the user enabled web sharing, the public profile card loads — read the display `name`, photos (`image`), and any shared info.
3. If it doesn't resolve (redirect to the Tinder homepage / app prompt / error), the username isn't a shareable public profile.
4. Save photos for reverse-image/face work; note the display name and any bio details.
5. Pivot: photos feed `[[yandex-images]]`/face search; a matching name/handle correlates to other social accounts.

## Inputs → Outputs
- **In:** `username` (a Tinder web-share handle)
- **Out:** `social-profile` (the Tinder card), `image` (profile photos), `name` (display name), basic bio info
- **Empty/negative result looks like:** the page redirecting to Tinder's generic landing/app-download screen, or an error — meaning no public web profile exists for that handle (the person may still be on Tinder without web sharing enabled). Absence isn't proof of no account.

## Gotchas & OpSec
- Only users who enabled a public web username are viewable this way; most Tinder users aren't, so expect many misses.
- Passive and non-notifying — this is *not* swiping, so it won't surface you to the target; still use a sock-puppet.
- Photos may be reused across dating apps — reverse-image them to find the same person elsewhere (or spot a catfish).

## Overlaps ("do both")
- Pairs with reverse-image/face tools like `[[yandex-images]]` (to trace the profile photos) and cross-account username tools — the Tinder card is a lead; corroborate identity through the images and matching handles.

## Trust & verifiability
`trust: trusted` — it resolves against Tinder's own web endpoint, so a loaded profile is authentic. The limitation is coverage (only web-share-enabled users), not authenticity.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | tinder-usernames |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, image, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
