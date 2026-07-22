---
id: eumom-ie
name: eumom.ie
description: Use when you have a `username` or `name` and want to trace an Irish parent's pregnancy/parenting forum posts — returns `social-profile` posting history and thread context.
url: https://www.eumom.ie/forums/
category: communities-forums
path:
- communities-forums
bestFor: Surfacing an Irish parent's or expectant mother's forum posts, due-date threads and disclosed life details.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free to read and search; a free account is only needed to post replies or start threads.
opsec: passive
opsecNote: Reading and Google-dorking public threads is passive and leaves no trace with the target. Do NOT register with your real identity or reply to a target's thread — posting is active and visible to the community. Use a sock-puppet account and browser if you must interact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running (est. 2000) Irish parenting community, now under the everymum brand. Content is user-generated self-disclosure, so treat individual claims as leads, not verified fact.
missingPersonsRelevance: medium
coverage:
- ie
auth: none
api: false
localInstall: false
registration: false
aliases:
- everymum
- eumom forums
tags:
- forums
- parenting-community
source: uk-osint
lastVerified: '2026-07-22'
enrichment: full
---

# eumom.ie

> Ireland's largest pregnancy-and-parenting forum (now everymum): a rich vein of self-disclosed life detail from Irish parents and expectant mothers.

## When to use
You have a `username` or a `name` you believe belongs to an Irish parent, a pregnant woman, or someone trying to conceive, and you want to find their forum footprint. Due-date threads, "birth club" groups and parenting Q&A often leak a poster's approximate location (county/hospital), expected/actual due date, number of children, partner details and health context — high-value corroboration for an Irish subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Try the site's own search at https://www.eumom.ie/forums/ for the `username` or a distinctive phrase.
2. In parallel, Google-dork it: `site:eumom.ie "<username>"` and `site:everymum.ie "<username>"` — the site rebranded to everymum, so older content lives on both hosts.
3. Open matching threads and read the surrounding context: due-date/birth-club threads reveal timelines; profile pages list join date and post history.
4. Pivot: a reused `username` feeds cross-platform username tools; a disclosed county + hospital + due date narrows an Irish subject's location and timeline.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `social-profile` (forum profile + post history), reused `username`, plus free-text disclosures (location, due date, family makeup)
- **Empty/negative result looks like:** no forum profile and no dorked hits — the handle was never used here, or posts sit behind a members-only sub-board you cannot see without an account.

## Gotchas & OpSec
- Content is anonymous self-report; poster claims are unverified and screen names are freely chosen — corroborate before trusting.
- Some sub-forums may require a free login to read fully; register only with a sock puppet, never with attributable details.
- Never reply to or DM a target's thread — that is active contact and tips them off.

## Overlaps ("do both")
- Pairs with broad username-enumeration tools: this confirms activity on an *Irish* parenting community specifically, which those cross-platform scanners often miss.

## Trust & verifiability
`trust: community` — an established Irish parenting brand hosting user-generated content. The platform is legitimate; individual posts are self-disclosed and must be treated as leads.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | eumom-ie |
| category | communities-forums |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
