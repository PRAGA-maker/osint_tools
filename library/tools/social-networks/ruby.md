---
id: ruby
name: RUBY
description: Use when you have a keyword, `name` or `username` and want video content across Rumble, BitChute and YouTube — returns author usernames, channel URLs and video links.
url: https://github.com/jakecreps/ruby
category: social-networks
path:
- social-networks
bestFor: Bulk keyword search of Rumble + BitChute + YouTube at once, exported to CSV for triage.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free, open-source Python script (MIT-style OSINT utility by Jake Creps). No account or API key required to run the basic keyword search.
opsec: passive
opsecNote: The script queries public search/listing pages of the three platforms from your machine — run it behind a VPN so your own IP isn't the one hitting the platforms repeatedly. It does not log you in or contact any target directly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Written by Jake Creps, a well-known OSINT practitioner, and covered by OS2INT; community-maintained open source, so it can break when a platform changes its markup.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- jakecreps/ruby
- Rumble BitChute YouTube scraper
tags:
- Social Media
- Universal
- video-search
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
---

# RUBY

> One command that fans a keyword across Rumble, BitChute and YouTube and dumps every hit — author, username, channel URL, video URL — into a CSV for fast triage.

## When to use
You have a keyword, a `name`, a `username`, or a phrase associated with a subject and want to see whether they (or content about them) appear on video platforms — especially the alt-tech ones (Rumble, BitChute) that general search engines index poorly. RUBY is a triage tool: it collects candidate channels and videos across three platforms in one pass so you can spot a subject's channel or usernames to pivot on.

## How to use it (`bestInteractionPattern`: cli)
1. `git clone https://github.com/jakecreps/ruby` and `cd ruby`.
2. `pip install -r requirements.txt`.
3. Run `python3 ruby.py "<keyword or name>"`.
4. Open the generated `search.csv` — each row has the video author, profile `username`, author/channel URL, and video URL.
5. Pivot: take channel usernames into cross-platform username tools, and open promising channels to enumerate uploads, bios, and links.

## Inputs → Outputs
- **In:** a keyword / `name` / `username` / phrase
- **Out:** CSV of results — author, `username`, channel/author URL (`social-profile`), video URL — across Rumble, BitChute, YouTube
- **Empty/negative result looks like:** an empty or header-only `search.csv`, or errors from one platform while others return rows — a scraped platform may have changed its layout, so a zero result can be a breakage rather than a true "no hits."

## Gotchas & OpSec
- It **scrapes** public search pages, so it is fragile: a platform redesign can silently break one of the three sources. Cross-check a null result by searching that platform manually.
- Results are keyword-matched listings, not identity confirmations — a matching author name is a lead to verify, not proof.
- OpSec: passive but direct-to-platform; run behind a VPN to avoid rate-limiting/blocking of your own IP.

## Overlaps ("do both")
- Pair with native platform search and dedicated YouTube-OSINT tooling — RUBY gives breadth across three sites fast, while per-platform tools give depth (comments, metadata, upload history) on the channels it surfaces.

## Trust & verifiability
`trust: community` — open-source utility from a recognised OSINT author; reliable in spirit but dependent on unofficial scraping, so verify outputs and expect occasional breakage after platform changes.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ruby |
| category | social-networks |
| selectorsIn → selectorsOut | name, username → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
