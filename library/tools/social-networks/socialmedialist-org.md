---
id: socialmedialist-org
name: socialmedialist.org
description: Use when you have a `username`/`name` and want a checklist of niche and non-Western social networks to hunt it across — returns a reference directory of ~250 platforms to seed a `social-profile` search.
url: https://socialmedialist.org/social-media-sites.html
category: social-networks
path:
- social-networks
bestFor: A curated, regularly-updated reference list of ~250 social networking sites worldwide to remind you which platforms to check a name/handle against.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- name
status: live
pricing: free
costNote: Free reference site; free for personal/academic use (commercial reuse prohibited). No account, no lookup fee — it is a static list, not a search engine.
opsec: passive
opsecNote: You read a public list of website names; nothing about your target is entered anywhere. The only OpSec that matters is downstream — visit the individual platforms it points you to through a sock puppet.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An independently-maintained directory (running since 2018) of social networks in many languages; accurate as a list, but it is a signpost, not a data source, so it holds no personal data itself.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- namechk
aliases:
- Social Media List
- list of social networking sites
tags:
- gsocialmedia
- General Social Media Sites
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# socialmedialist.org

> A directory, not a search tool — a maintained list of ~250 social networks worldwide (including regional/non-Western ones) to jog your memory about *where* to look for a handle before you look.

## When to use
You are enumerating a `username` or `name` across platforms and want to make sure you're not missing the network the subject actually uses. Automated username checkers cover the mainstream sites, but this list catches the long tail — regional platforms (VK, Odnoklassniki, Weibo, Nairaland), niche communities (Academia.edu, ResearchGate, Wattpad), and emerging apps — that a checker may skip. Use it as a **coverage checklist**: it does not hold any personal data and you cannot search it for a person; you read it to decide which platforms to then query manually.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://socialmedialist.org/social-media-sites.html and browse the categorised list of ~250 networks (updated periodically, available in many languages).
2. Identify platforms relevant to your subject — by region (match the person's country/language), by interest/profession, or simply ones your automated tools didn't cover.
3. For each candidate platform, go to it directly and search/enumerate the subject's `username` or `name`.
4. Record any hit as a `social-profile` lead.
5. Pivot: confirmed profiles feed profile-scraping/enumeration tools; run the handle through a cross-platform checker for the mainstream sites in parallel.

## Inputs → Outputs
- **In:** `username` / `name` (used on the platforms it lists, not on the list itself)
- **Out:** a directory of candidate social networks → downstream `social-profile` / `name` hits when you check them
- **Empty/negative result looks like:** the list itself always "returns" the directory; a negative outcome is checking its platforms and finding no profiles — meaning the subject isn't on the niche networks either, not that the list failed.

## Gotchas & OpSec
- Human-in-the-loop: entirely manual — it points, you search; there is no automation or API.
- OpSec: reading the list is **passive** and untargeted; the exposure is downstream — use a sock-puppet browser/IP when you actually visit and query each platform.
- It is a *list of sites*, so treat MP-relevance as indirect: its value is coverage/completeness, not a direct person lookup.

## Overlaps ("do both")
- Pairs with `[[namechk]]` — the automated checker sweeps the mainstream platforms fast; this list backfills the regional/niche networks the checker omits, so run both to avoid coverage gaps.

## Trust & verifiability
`trust: community` — a long-running independent directory. It is reliable as a *reference* (the sites it names are real), but it stores no personal data, so there is nothing here to fact-check about an individual — verification happens when you visit each platform.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | socialmedialist-org |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
