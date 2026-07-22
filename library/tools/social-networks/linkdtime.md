---
id: linkdtime
name: LinkdTime
description: Use when you have LinkedIn post/comment/activity `social-profile` URLs and want exact timestamps — returns a chronological timeline with precise dates/times.
url: https://github.com/Lucksi/LinkdTime
category: social-networks
path:
- social-networks
bestFor: Extracting the exact date/time behind LinkedIn posts, comments and activity and building a timeline from a list of links.
selectorsIn:
- social-profile
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free and open-source (Python); you run it locally, no account or payment.
opsec: passive
opsecNote: LinkdTime derives timestamps from the LinkedIn activity URN embedded in the link — it does not need to log into or actively hit the target's profile if you already hold the URLs. Collect the source URLs OpSec-safely (LinkedIn views can be visible); the timeline generation itself is offline/local.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Open-source on GitHub (Lucksi/LinkdTime), 100% Python; the timestamp derivation is deterministic from LinkedIn's own activity IDs, so results are verifiable.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- LinkdTime
- Lucksi/LinkdTime
tags:
- linkedin
- timeline
- cli
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
relatedTools:
- mr-holmes
---

# LinkdTime

> Turns LinkedIn activity links into exact timestamps: it decodes the time baked into each post/comment's activity ID and builds a clean chronological timeline.

## When to use
You have one or more LinkedIn `social-profile` activity URLs (a post, comment, reaction, or an "recent activity" export) and need the *precise* date and time — LinkedIn shows fuzzy labels ("2mo ago"), but each activity URN encodes an exact timestamp. Use LinkdTime to pin when a subject posted/engaged, reconstruct their activity pattern, establish presence/last-active windows, or timeline a set of interactions across a case.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `git clone https://github.com/Lucksi/LinkdTime`, ensure Python 3, run `python3 main.py` (tested on Linux).
2. Collect the LinkedIn activity URLs you care about into a `.txt` (one per line) or provide an exported `.html`.
3. Run `timeline filename.txt` with options like `--timezone` (localise), `--autoname`, and `--download` (fetch images).
4. Read the generated timeline of exact timestamps. Pivot: correlate active hours to infer a subject's timezone/location; align posts with real-world events; feed the timeline into your case chronology.

## Inputs → Outputs
- **In:** LinkedIn activity URLs (`social-profile` links) — single or a list
- **Out:** a timeline of exact dates/times per post/comment/activity (with optional images), timezone-adjusted
- **Empty/negative result looks like:** a URL that isn't a decodable activity link (e.g. a bare profile URL) yields no timestamp — supply actual post/comment/activity URLs.

## Gotchas & OpSec
- It timestamps activity you already have URLs for; *finding/collecting* those URLs on LinkedIn is the step with OpSec exposure (profile views can be visible) — do that from a sock-puppet/anonymous session.
- Derivation is only as good as the source links; broken/edited/deleted activity may not resolve.
- Linux-tested; Windows/Mac untested per the repo.

## Overlaps ("do both")
- Pairs with LinkedIn OSINT collection methods and general timeline/graph tools — LinkdTime supplies exact times; those supply the surrounding profile/relationship context.

## Trust & verifiability
`trust: trusted` — open-source and deterministic: timestamps come from LinkedIn's own activity IDs, so a reviewer can re-derive them; verify by spot-checking a known post's time.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | linkdtime |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
