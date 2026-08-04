---
id: reddit-enhancement-suite-firefox
name: Reddit Enhancement Suite (Firefox)
description: Use when you are working a `username` on Reddit and want persistent per-user tagging, inline history and never-ending browsing — returns an annotated, easier-to-mine view of a subject's Reddit social-profile.
url: https://addons.mozilla.org/enGB/firefox/addon/reddit-enhancement-suite
category: social-networks
path:
- social-networks
bestFor: Power-user Reddit investigation — tag users, expand context and scroll continuously while reviewing a subject's account.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free and open-source browser extension (community-maintained).
opsec: passive
opsecNote: RES only enhances how your browser renders Reddit; it makes no queries beyond your normal browsing and adds no extra observable footprint. Standard sock-puppet hygiene still applies — browse a target's profile from a research browser/account, not your personal one, since Reddit still sees your session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: Long-established, widely used open-source extension listed on Mozilla's official add-ons store.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- RES
- reddit enhancement suite
tags:
- reddit
- browser-enhancement
- firefox
source: osintambition-social
lastVerified: '2026-08-04'
enrichment: full
---

# Reddit Enhancement Suite (Firefox)

> A browser extension that turns Reddit into a power-user surface — user tagging, inline media/context, and never-ending reload — handy when you're combing one account's history.

## When to use
You have a Reddit `username` and are manually reviewing that account's posting history for leads (locations, habits, associates, timelines). RES lets you tag the user with private notes, expand images/links inline, and scroll continuously so you can read a long history without paginating. It's a convenience layer, not a lookup tool.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install from the Mozilla add-ons store (link above) in a Firefox profile you keep for research.
2. Open the subject's profile (`reddit.com/user/<username>`).
3. Use **User Tagger** to attach a private note/colour to the handle so you recognise it across threads; use **Never-Ending Reddit** to load their history in one scroll.
4. Expand inline media/comment context to read posts without leaving the page; use account-history navigation to jump between their subs.
5. Pivot: mentions, subs and image links you surface feed reverse-image and cross-platform username checks.

## Inputs → Outputs
- **In:** `username` (a Reddit account you open in the browser).
- **Out:** an annotated, expanded view of that `social-profile` — tags, inline context, and easier-to-scan history (no new data source; it reorganises what Reddit already shows).
- **Empty/negative result looks like:** nothing new appears — RES doesn't recover deleted/removed content or private accounts; a suspended/empty profile stays empty.

## Gotchas & OpSec
- It adds no data — if the account is deleted, shadow-banned or private, RES can't reveal it; use cache/archive tools for removed content.
- It's a client-side renderer; your tags live only in that browser profile, so export notes elsewhere for a case file.
- Keep it in a dedicated research browser to avoid mixing personal Reddit sessions with investigative browsing.

## Overlaps ("do both")
- Complements scraping/enumeration: use RES to read one account deeply by hand, then a cross-platform tool like `[[slash]]` to check whether the same `username` exists elsewhere.

## Trust & verifiability
`trust: trusted` — an established open-source extension on Mozilla's official store; it only changes presentation, so it introduces no data-quality risk of its own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reddit-enhancement-suite-firefox |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
