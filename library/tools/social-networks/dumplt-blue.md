---
id: dumplt-blue
name: DumpItBlue+
description: Use when you have access to a target's `social-profile` (Facebook profile, group, or friends list) and want the connections as a structured file — returns `associate`/`name`/`social-profile`/`image` rows dumped to text.
url: https://chrome.google.com/webstore/detail/dumpitblue%2B/igmgknoioooacbcpcfgjigbaajpelbfe/related
category: social-networks
path:
- social-networks
bestFor: Bulk-extracting a Facebook profile's friends, a group's members, or a thread's commenters into a text file for network analysis.
selectorsIn:
- social-profile
selectorsOut:
- associate
- name
- social-profile
- image
status: live
pricing: free
costNote: Free Chrome extension by arioux (le-tools.com). No paywall; documentation at le-tools.com/DumpItBlueExtensionDoc.html.
opsec: active
opsecNote: This runs inside YOUR logged-in Facebook session and auto-scrolls the target's pages — that IS automation Facebook can detect and act on. Use ONLY a dedicated sock-puppet Facebook account (never a personal/work one), expect the account to be rate-limited or banned, and never let it touch your real identity. Being friends with the target may surface you in their "recently viewed"; prefer a puppet with no relationship to the subject.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: community
trustNote: Long-maintained extension from arioux/le-tools, a known author of DFIR/OSINT utilities; open enough to inspect, but it injects JS into Facebook, so run it in an isolated browser profile.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- DumpItBlue
- DumpItBlue Plus
- le-tools DumpItBlue
tags:
- Social Media
- Facebook
- friend-list
- network-analysis
- browser-extension
source: cyb-detective
lastVerified: '2026-07-15'
enrichment: full
---

# DumpItBlue+

> A Chrome extension that scrapes a Facebook page you're viewing — friends list, group members, messenger contacts, comment threads — into a text file (profile name, URL, image URL, details), turning a manual friends-list crawl into one export for network mapping.

## When to use
You can see a target's Facebook `social-profile`, group, or friends list (public, or visible to your sock-puppet) and you need the connections as *data*, not screenshots — to map a missing person's `associate` network, spot mutual friends across two subjects, or enumerate who's in a closed group. DumpItBlue+ auto-scrolls and dumps the visible entries so you don't hand-copy hundreds of names.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install DumpItBlue+ from the Chrome Web Store into a **dedicated, isolated browser profile** (current store URL: chromewebstore.google.com/detail/dumpitblue+/igmgknoioooacbcpcfgjigbaajpelbfe).
2. Log that browser into a **sock-puppet Facebook account only**. Never your own.
3. Navigate to the target surface — a profile's Friends tab, a group's Members page, or a comment thread.
4. Open DumpItBlue+ and choose the dump (friends / group members / comments). It auto-scrolls to the bottom, expands replies, and writes rows: Profile Name, Profile URL, Profile Image URL, details.
5. Save the `.txt`, import into a spreadsheet or link-analysis tool, and dedupe.
6. Pivot: each `associate` row (name + profile URL + image) becomes its own workup; mutual connections across two dumps are high-value leads.

## Inputs → Outputs
- **In:** `social-profile` (a Facebook profile/group/thread you can view while logged in)
- **Out:** `associate` list, `name`, `social-profile` URLs, `image` (avatar) URLs — as text rows.
- **Empty/negative result looks like:** an empty/partial dump when the friends list is set to private, the group is closed to your puppet, or Facebook throttles the scroll. Partial ≠ complete — note coverage gaps.

## Gotchas & OpSec
- Human-in-the-loop: you must be logged into Facebook (`account-login`); the extension only sees what that account can.
- OpSec: **active** — auto-scrolling is detectable automation. Burner FB account, isolated browser profile, expect bans; keep it entirely separate from any attributable identity.
- Facebook's DOM changes frequently; a dump that suddenly returns garbage or nothing usually means the extension needs an update, not that the data is gone. Re-verify counts against the live page.

## Overlaps ("do both")
- Complements manual profile review — DumpItBlue+ gives you the *breadth* (the whole list, fast) while a human reads individual profiles for depth. Feed extracted avatar `image` URLs into a reverse-image/face pipeline to de-anonymise puppet or alias accounts.

## Trust & verifiability
`trust: community` — a well-known le-tools/arioux utility, still on the Chrome Web Store and documented, but it injects JavaScript into Facebook and depends on FB's shifting layout. Run it isolated, and treat the dump as a snapshot to verify, not ground truth.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dumplt-blue |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile → associate, name, social-profile, image |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | yes (account-login) |
