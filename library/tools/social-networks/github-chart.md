---
id: github-chart
name: GitHub-Chart
description: Use when you have a GitHub `username` and want to profile their activity rhythm — returns a visual of commit timing that hints at timezone, work schedule, and active days.
url: https://chromewebstore.google.com/detail/github-chart/apaldppjjcjgjddfobajdclccgkbkkje
category: social-networks
path:
- social-networks
bestFor: Inferring a GitHub user's timezone and activity pattern from the temporal distribution of their commits.
selectorsIn:
- username
selectorsOut:
- geolocation
- device-id
status: degraded
pricing: free
costNote: Free Chrome extension; verify it is still listed on the Chrome Web Store before relying on it.
opsec: passive
opsecNote: It visualizes public commit-timestamp data already on the user's GitHub page — no interaction with the subject, nothing disclosed. Passive. Any extension gets browser permissions, so use a dedicated research profile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: unverified
trustNote: A third-party Chrome extension by an unknown developer; it derives from public GitHub timestamps you can verify, but timezone inference is probabilistic.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- GitHub Chart extension
tags:
- Social Media
- Github
- browser-extension
- pattern-of-life
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# GitHub-Chart

> A browser extension that charts when a GitHub user commits — turning public timestamps into a pattern-of-life signal for timezone and schedule.

## When to use
You have a GitHub `username` and want behavioral intelligence rather than content: when is this person active? The temporal distribution of commits reveals productivity peaks, active days of the week, and — crucially — a likely timezone, which narrows geographic location and daily routine. Useful for corroborating a claimed location or building a pattern of life around a coder.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "GitHub-Chart" from the Chrome Web Store into a research browser profile (confirm the listing is still live first).
2. Open the subject's GitHub profile page.
3. Read the chart the extension overlays: commit distribution by hour and by weekday.
4. Infer timezone from the "active hours" band (people commit mostly during their waking/working hours) and note weekday-vs-weekend patterns.
5. Pivot: an inferred timezone narrows `geolocation`; the routine corroborates or contradicts a claimed location/lifestyle; combine with commit emails/real names for identity.

## Inputs → Outputs
- **In:** a GitHub `username`
- **Out:** commit-timing visualization → inferred timezone (`geolocation` band), activity routine (a device/behavior signal)
- **Empty/negative result looks like:** a sparse or flat chart — too few commits to infer a pattern, or activity spread across timezones (travel, scheduled/bot commits); treat weak signal as inconclusive, not as a location.

## Gotchas & OpSec
- Timezone inference is probabilistic: commit timestamps use the committer's local git config, which can be wrong, UTC-forced, or spoofed — corroborate, don't conclude.
- Confounders: bots, CI, scheduled commits, and night-owl habits distort the pattern.
- Extension volatility: Chrome Web Store items get delisted — verify availability (status: degraded); use a research profile.
- OpSec: passive (public data only).

## Overlaps ("do both")
- Pairs with GitHub commit-email harvesting and profile OSINT ([[osint-researcher]]) — this reads the *when* (pattern of life), while those read the *who* (identity, network).

## Trust & verifiability
`trust: unverified` — a third-party extension, but it's derived from public, verifiable commit timestamps; the inference layer (timezone) is probabilistic, so treat conclusions as leads to confirm.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | github-chart |
| category | social-networks |
| selectorsIn → selectorsOut | username → geolocation, device-id |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
