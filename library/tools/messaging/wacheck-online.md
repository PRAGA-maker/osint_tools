---
id: wacheck-online
name: WACheck Online
description: Use when you have a `phone` number and want to monitor its WhatsApp online/offline activity to infer a pattern of life and timezone — returns a social-profile presence/activity signal.
url: https://wacheck.online/
category: messaging
path:
- messaging
bestFor: Tracking when a WhatsApp number is online/offline to infer active hours, timezone and routine.
selectorsIn:
- phone
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free checks are heavily rate-limited (one every several seconds, short trial); continuous/logged monitoring is a paid "WA Watcher" subscription.
opsec: passive
opsecNote: It observes the number's WhatsApp online-presence indicator — it does not message the target, so the person is not notified. However, this is intrusive activity-surveillance; use only with proper authorisation, and be aware the service itself sees the numbers you monitor.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: web-manual
trust: unverified
trustNote: A third-party service that exploits WhatsApp's online-presence indicator. It has been described critically in the press as a surveillance tool; treat the data as observational and the operator as untrusted with your query list.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- WA Check
- wacheck.online
- WA Watcher
tags:
- whatsapp
- WhatsApp
- presence-monitoring
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# WACheck Online

> Turns WhatsApp's "online" indicator into a monitoring signal — track when a number is active to infer routine, timezone, and periods of activity.

## When to use
You have a `phone` number known to be on WhatsApp and, with proper authorisation, you want behavioural signal rather than identity: when is the person online? Logged over time, the online/offline pattern reveals waking hours, likely timezone, and changes in routine (useful in a missing-person timeline — e.g. the exact point activity stopped). It does not reveal identity or content, only presence.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://wacheck.online/.
2. Select the country and enter the target `phone` number; press check.
3. Read the online/offline status. For a pattern, you must sample repeatedly over time — the free tier throttles this; paid "WA Watcher" logs it continuously.
4. Build a timeline of active windows.
5. Pivot: inferred active hours/timezone corroborate a suspected location; a sudden stop in activity is itself a significant event to timestamp against other evidence.

## Inputs → Outputs
- **In:** `phone` (a WhatsApp number)
- **Out:** WhatsApp presence over time — a `social-profile` activity signal (active windows, timezone inference)
- **Empty/negative result looks like:** the number never shows online — it may not be on WhatsApp, may have "last seen/online" privacy enabled (which hides the indicator), or be inactive; not a reliable single data point.

## Gotchas & OpSec
- **Ethics/authorisation:** this is activity surveillance of an individual — only do it with a lawful basis. The operator also learns which numbers you monitor.
- WhatsApp privacy settings can hide the online indicator, defeating the tool.
- Human-in-the-loop: free tier is rate-limited; meaningful patterns need sustained (paid) sampling.
- Single checks are near-worthless — value comes only from a time series.

## Overlaps ("do both")
- Pairs with a WhatsApp profile-photo/existence check and `[[botim-me]]`/other messaging-presence checks — those confirm the account and pull a photo/name, while WACheck adds the temporal activity dimension.

## Trust & verifiability
`trust: unverified` — a third-party presence-scraper of uncertain longevity and questionable ethics. Treat outputs as raw observations to corroborate, and weigh the privacy/legal implications before using.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wacheck-online |
| category | messaging |
| selectorsIn → selectorsOut | phone → social-profile |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
