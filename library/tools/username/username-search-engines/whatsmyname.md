---
id: whatsmyname
name: WhatsMyName
description: Use when you have a `username` and want to know every site where it exists — returns a list of accounts across hundreds of platforms via response-pattern matching.
url: https://github.com/WebBreacher/WhatsMyName
category: username
path:
- username
- username-search-engines
bestFor: Enumerating where a single username is registered across hundreds of sites using community-maintained detection rules.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free and open-source; the hosted web UI (whatsmyname.app) and the CLI/data are all free, no account.
opsec: active
opsecNote: The check works by sending an HTTP request to each candidate site for that username — so those sites (and any logging in between) see a hit for the target handle from your IP. Run the CLI behind a VPN/sock infrastructure; the hosted web app proxies requests but still relies on live probes. It does not notify the account owner directly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Maintained by Micah Hoffman (WebBreacher) with a large community-curated detection dataset (wmn-data.json); the de-facto standard username-enumeration data source, reused by many other tools.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- WMN
- whatsmyname.app
tags:
- username-check
- username-enumeration
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# WhatsMyName

> The community standard for username enumeration: give it a handle and it checks hundreds of sites for a live account, using a maintained ruleset that many other OSINT tools also consume.

## When to use
You have a `username` (or a promising handle from an email prefix, a gamer tag, a display name) and want to find every platform where it's registered. This is the backbone of username-pivoting: one enumeration turns a single handle into a map of the subject's online presence — forums, social sites, dev platforms, marketplaces — each a place to read for `name`, photos, location, and associates. Reach for it early whenever you have a distinctive username.

## How to use it (`bestInteractionPattern`: cli)
1. Fastest path: open the hosted web UI at **whatsmyname.app**, type the username, and read the found accounts. For scale/automation, clone `https://github.com/WebBreacher/WhatsMyName` and run the CLI (or use its `wmn-data.json` with a tool that ingests it).
2. Enter the target `username`.
3. Read results: each hit is a URL where the handle resolves to a live account.
4. **Verify each hit** — open the profile and confirm it's your subject, not a same-handle stranger.
5. Pivot: each confirmed `social-profile` feeds face/reverse-image, bio-link, and content-analysis steps; distinctive bios/links tie accounts to one person.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` (list of sites where the handle exists)
- **Empty/negative result looks like:** few or no hits — the handle is uncommon online, the person uses different handles per site, or detection rules for their platforms are missing. Not proof of no presence; try handle variants and other enumerators.

## Gotchas & OpSec
- Human-in-the-loop: none required, but **manual verification of each hit is essential** — a common username produces false matches belonging to other people.
- OpSec: **active** — it probes each site live for the handle; use a VPN, especially with the CLI.
- Detection rules can go stale (sites change responses), causing false positives/negatives; the dataset is updated frequently, so pull the latest.

## Overlaps ("do both")
- Overlaps with Sherlock/Maigret and other enumerators that use the same or similar datasets — run more than one, since each covers a slightly different site list and false-positive profile; WhatsMyName's `wmn-data.json` is often the shared source.

## Trust & verifiability
`trust: trusted` — an actively maintained, widely-adopted open-source project whose data underpins much of the ecosystem; the tool is reliable, but individual hits still need human confirmation.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whatsmyname |
| category | username |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
