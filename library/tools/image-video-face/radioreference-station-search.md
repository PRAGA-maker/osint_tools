---
id: radioreference-station-search
name: RadioReference Station Search
description: Use when you have a `geolocation`/agency or radio call sign and want radio-comms intelligence — returns scanner frequencies, trunked-system data, agency call signs and live audio feeds for an area.
url: http://www.radioreference.com
category: image-video-face
path:
- image-video-face
bestFor: Finding public-safety and other radio frequencies, call signs, and live scanner feeds for a location or agency.
selectorsIn:
- geolocation
- name
selectorsOut:
- geolocation
status: live
pricing: freemium
costNote: Free to browse much of the database and access many live feeds; a paid Premium subscription unlocks the full frequency database and detailed trunked-system data.
opsec: passive
opsecNote: Read-only browsing/listening of a public radio-reference database and audio feeds; no individual is queried or notified. Listening to public-safety feeds is passive intelligence — mind local laws on scanner use and never act on comms in ways that interfere.
humanInLoop: false
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: RadioReference is the largest crowd-sourced radio-communications database (frequencies, trunked systems, live feeds); community-maintained, so freshness and accuracy vary by area.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: true
invitationOnly: false
relatedTools:
- radioreference
- radioreference-communications-wiki
aliases:
- RadioReference
- radioreference.com
tags:
- toddington
- curated-directory
- radio-comms
- scanner-feeds
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# RadioReference Station Search

> The largest crowd-sourced radio-communications database — frequencies, call signs, trunked systems, and live scanner feeds, searchable by location or agency.

## When to use
You want radio-comms intelligence for an area or agency: which frequencies and trunked systems public-safety (police/fire/EMS), aviation, marine, or other services use, their call signs, and whether a **live scanner feed** exists. In a missing-persons or event context, a live feed for the relevant county can provide real-time situational awareness of an active search or incident, and the frequency/call-sign data helps interpret intercepted or referenced comms. (Its category tag is misleading — this is radio, not image/face.)

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.radioreference.com.
2. Browse the database by `geolocation` (country → state/county) or search by agency `name`/call sign.
3. Read the results: frequency lists, trunked-system details, agency call signs, and any live audio feeds for the area.
4. Open a **live feed** to monitor active comms; note full frequency/trunked detail may require Premium.
5. Pivot: a live feed gives real-time context; agency/call-sign data supports interpreting referenced communications.

## Inputs → Outputs
- **In:** `geolocation` (country/state/county) or agency `name`/call sign
- **Out:** frequencies, trunked-system data, call signs, and live scanner feeds tied to that `geolocation`
- **Empty/negative result looks like:** no listed frequencies/feeds for the area — coverage is crowd-sourced and uneven, so a gap means "not catalogued/no feed," not "no radio activity." Many systems are also encrypted and won't have usable audio.

## Gotchas & OpSec
- **Not an image/face tool** despite the harvested category — it's radio-comms reference.
- Full frequency/trunked detail is **paywalled** (Premium); much browsing and many feeds are free.
- Encryption and jurisdiction: many modern public-safety systems are encrypted; and scanner listening/laws vary by country/state — comply with local law.
- OpSec: **passive** — reading/listening to public feeds.

## Overlaps ("do both")
- Complements live-incident OSINT (news, social geolocation) — RadioReference adds the radio-comms layer (frequencies + live audio) to what open sources report about an area.

## Trust & verifiability
`trust: community` — the definitive crowd-sourced radio database, but community-maintained with uneven freshness; verify a frequency/feed is current before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | radioreference-station-search |
| category | image-video-face |
| selectorsIn → selectorsOut | geolocation, name → geolocation |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
