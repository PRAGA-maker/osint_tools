---
id: telerecon
name: Telerecon
description: Use when you have a Telegram `username`, `phone` or channel and want to scrape and profile that target across Telegram — returns messages, contact selectors, associate network and EXIF/GPS from media.
url: https://github.com/sockysec/Telerecon
category: messaging
path:
- messaging
bestFor: Deep OSINT reconnaissance and profiling of Telegram users and channels.
selectorsIn:
- username
- phone
selectorsOut:
- name
- phone
- email
- associate
- geolocation
- metadata-exif
status: live
pricing: free
costNote: Free and open-source (MIT). Requires your own Telegram account/API credentials to run.
opsec: active
opsecNote: Telerecon authenticates with a Telegram account to scrape, so use a dedicated sock-puppet Telegram account and API keys — never your real one. Joining or querying channels with a burner still leaves that account's footprint; heavy scraping risks the account being flagged/banned.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source Telegram OSINT framework by sockysec, widely referenced in awesome-osint lists; results depend on your account access and Telegram's current API behavior.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: true
registration: false
aliases:
- sockysec Telerecon
tags:
- telegram
- messaging
- profiling
source: awesome-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Telerecon

> A Python framework that turns a Telegram handle or channel into a full profile — scraped messages, extracted selectors, a network of associates, and geodata from media.

## When to use
You have a Telegram `username`, `phone`, or a channel/group and want to go beyond a single-message view: compile a target's message history, extract embedded contact selectors (emails, phone numbers), map who they interact with and forward from, and pull EXIF/GPS out of shared images. Strong for building an associate graph and geolocating a Telegram-active subject.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/sockysec/Telerecon` and install the Python requirements.
2. Provide **sock-puppet** Telegram API credentials (api_id/api_hash) and log in with a burner account — never your real identity.
3. Point it at a target `@username`, phone, or channel URL (or a CSV/TXT list of channels).
4. Run the modules you need: profile metadata, message/media scraping, forward mapping (network discovery), subscriber census, and selector/entity extraction.
5. Read the reports: user metadata (name, bio, phone, UserID, last-seen), extracted emails/phones, interaction network, and image EXIF/GPS.
6. Pivot: extracted `phone`/`email` feed email/phone OSINT; `associate` links feed further Telegram/social mapping; GPS feeds geolocation.

## Inputs → Outputs
- **In:** Telegram `username`, `phone`, or channel/group URL
- **Out:** `name`, `phone`, `email`, `associate` network, `geolocation`/`metadata-exif` from media, activity patterns
- **Empty/negative result looks like:** private account with hidden phone/last-seen, no public messages, or a channel your burner can't access — meaning limited visibility, not that the account is inactive.

## Gotchas & OpSec
- Human-in-the-loop: requires account login; use a dedicated burner + API keys, expect possible rate-limits or bans on aggressive scraping.
- Active footprint: querying/joining channels is attributable to the account you use.
- Some "threat assessment" heuristics it outputs are indicators, not conclusions — treat as leads.

## Overlaps ("do both")
- Complements phone/email OSINT: Telerecon extracts selectors from Telegram activity, which you then resolve with dedicated phone/email tools; associate links pair with broader social-network mapping.

## Trust & verifiability
`trust: community` — well-regarded open-source framework; every scraped datum is verifiable against the live Telegram content it came from, subject to your account's access.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telerecon |
| category | messaging |
| selectorsIn → selectorsOut | username, phone → name, phone, email, associate, geolocation, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login) |
