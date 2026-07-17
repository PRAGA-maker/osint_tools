---
id: iknowwhatyoudownload
name: IKnowWhatYouDownload
description: Use when you have an `ip-address` and want any BitTorrent download activity publicly logged against it — returns torrented titles with timestamps and a coarse geolocation for that IP.
url: https://iknowwhatyoudownload.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Checking what torrents an IP address has been observed downloading, with dates and rough location.
selectorsIn:
- ip-address
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free web lookup shows the sample of activity logged for an IP. Bulk/API and full historical access are sold as a paid product, but the basic per-IP page is free.
opsec: passive
opsecNote: You query a third-party database of collected torrent-swarm data; the IP's owner is not contacted or notified. Passive. Use a VPN for your own hygiene. Remember this exposes potentially sensitive personal activity — handle findings responsibly and lawfully.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A specialist service that harvests public BitTorrent DHT/tracker announcements; the data is real observed swarm activity but is sampled, attributed by IP (shared/dynamic IPs cause error), and unverifiable by you.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools: []
aliases:
- I Know What You Download
- iknowwhatyoudownload.com
tags:
- ip
- torrent
- activity
source: inteltechniques-tools
lastVerified: '2026-07-17'
enrichment: full
---

# IKnowWhatYouDownload

> A database of BitTorrent activity keyed by IP — enter an address and see which torrents it was observed sharing, when, plus a rough location for that IP.

## When to use
You have an `ip-address` (from an email header, server log, chat metadata, or a device) and want a behavioral signal: what content, if any, has been publicly logged as downloaded from that IP. BitTorrent is not anonymous — the service collects swarm announcements, so a subject's IP can be tied to specific torrented titles and timestamps. This is a pattern-of-life and interests signal (media, software, region) and a way to correlate an IP to activity windows.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://iknowwhatyoudownload.com/ and enter the `ip-address` (or view your own by just visiting).
2. Read the logged entries: torrent titles, categories, and the date/time each was observed for that IP.
3. Note the coarse `geolocation` the site attributes to the IP.
4. Judge reliability: a residential IP is often dynamic/shared, so activity may belong to a prior lease or another household member.
5. Pivot: the IP → [[search-arin-net]] / RIR Whois for the provider; activity windows → timeline; interests → other platforms.

## Inputs → Outputs
- **In:** `ip-address`
- **Out:** observed torrent titles with timestamps, plus a coarse `geolocation` for the IP
- **Empty/negative result looks like:** "no data" for the IP — either no torrent activity was sampled from it, the IP has since changed hands, or activity was masked by a VPN. Absence is not proof the person doesn't torrent.

## Gotchas & OpSec
- **Attribution is by IP, not person:** dynamic leases, shared/CGNAT, VPNs, and multi-user households all break the IP→individual link. Treat results as leads about an address, not proof about a named person.
- The free view is a **sample**; full/bulk history sits behind the paid API.
- Ethically/legally sensitive: this exposes private behavior — use only within lawful, authorized scope.
- OpSec: **passive** — a database query; the IP owner isn't contacted.

## Overlaps ("do both")
- Pairs with [[search-arin-net]] and IP-geolocation tools — this gives behavior tied to an IP; those give who owns/where the IP is, together characterizing an address.

## Trust & verifiability
`trust: community` — real observed swarm data, but sampled and IP-attributed with no way for you to independently verify a given entry; corroborate before drawing conclusions and never treat an IP hit as identifying a specific individual on its own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | iknowwhatyoudownload |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | ip-address → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
