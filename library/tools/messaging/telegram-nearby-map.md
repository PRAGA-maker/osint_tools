---
id: telegram-nearby-map
name: Telegram Nearby Map
description: Use when you have a `geolocation` and want to find Telegram users who enabled "People Nearby" there — returns nearby profiles plotted on a map with a trilaterated distance estimate.
url: https://github.com/tejado/telegram-nearby-map
category: messaging
path:
- messaging
bestFor: Discovering and roughly locating Telegram users who have the "People Nearby" feature switched on around a given point.
selectorsIn:
- geolocation
selectorsOut:
- social-profile
- geolocation
status: degraded
pricing: free
costNote: Free and open-source (Node.js); you supply your own Telegram account and API credentials.
opsec: active
opsecNote: Using Telegram's "People Nearby" makes YOUR account visible to others nearby and requires a logged-in Telegram account tied to a phone number — use a dedicated burner account/number, never your real one. Querying is active on Telegram's side; the accounts you enumerate are self-exposing, but you are participating in the same feature and can be seen back.
humanInLoop: true
humanInLoopReason:
- api-key
- account-login
bestInteractionPattern: docker
trust: community
trustNote: A popular open-source project (tejado) using Telegram's official TDLib and OpenStreetMap. Last substantially updated in 2023; Telegram deliberately coarsened nearby-distance precision, so exact trilateration is degraded.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: true
localInstall: true
registration: true
aliases:
- telegram-nearby-map
- tejado nearby map
tags:
- telegram
- geolocation
- people-nearby
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Telegram Nearby Map

> A self-hosted tool that surfaces Telegram "People Nearby" users on an OpenStreetMap and estimates their position by trilaterating the distance Telegram reports from several vantage points.

## When to use
You have a `geolocation` of interest (an event, a building, an area a subject frequents) and want to know which Telegram users with "People Nearby" enabled are physically around that point — and roughly where. Useful for tying a Telegram handle to a physical area, or for discovering local accounts near a scene. Only finds users who opted into "People Nearby," which is a minority.

## How to use it (`bestInteractionPattern`: docker)
1. Create a **burner** Telegram account and obtain API `api_id`/`api_hash` from my.telegram.org.
2. Clone `https://github.com/tejado/telegram-nearby-map`, supply credentials, and run it (Docker or `npm install && npm start`); open `http://localhost:3000`.
3. Set the map location to your target `geolocation`; the tool queries "People Nearby" and plots users with Telegram's reported distance.
4. Move the query point / repeat from several coordinates to trilaterate a user's approximate position.
5. Pivot: a discovered Telegram `social-profile` feeds username/phone OSINT; the trilaterated `geolocation` corroborates or refines where the subject is.

## Inputs → Outputs
- **In:** `geolocation` (a point to search around) + a logged-in burner Telegram account
- **Out:** nearby Telegram `social-profile`s and an approximate `geolocation` per user
- **Empty/negative result looks like:** few or no users returned — "People Nearby" is off by default so most people never appear, and Telegram now reports coarse distances, so pinpoint trilateration often fails. Absence means "no opted-in users here," not "no one here."

## Gotchas & OpSec
- **Active + self-exposing:** to see nearby users you must enable the same feature, making your burner account visible to them. Never use a personal account/number.
- Telegram intentionally reduced nearby-distance precision, so exact-location trilateration is degraded (hence status `degraded`).
- Requires Telegram API credentials and a local Node.js/Docker install — not a click-and-go web tool.
- Repo is somewhat stale (2023); Telegram API changes may break it — check issues/forks.

## Overlaps ("do both")
- Pairs with phone-number Telegram lookups and username enumerators — this locates opted-in accounts by area, while those resolve a known handle/number into profile detail. Different entry points to the same target.

## Trust & verifiability
`trust: community` — a well-regarded open-source project built on Telegram's official TDLib; the mechanism is legitimate but the results are inherently coarse and the project is not actively maintained, so verify locations independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telegram-nearby-map |
| category | messaging |
| selectorsIn → selectorsOut | geolocation → social-profile, geolocation |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | docker |
| opsec | active |
| human-in-loop | yes (api-key, account-login) |
