---
id: mytweetalerts
name: MyTweetAlerts
description: Use when you have a `username`, `name` or keyword and want ongoing email alerts whenever matching tweets are posted — returns `social-profile` activity notifications over time.
url: https://www.mytweetalerts.com/
category: social-networks
path:
- social-networks
bestFor: Standing monitoring of Twitter/X for a person, handle or keyword via scheduled email alerts.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: degraded
pricing: freemium
costNote: Freemium with paid tiers; free/low tiers are limited in number of alerts and frequency. Requires registration. Ongoing viability depends on Twitter/X API access, which has tightened — verify it still delivers before relying on it.
opsec: passive
opsecNote: You monitor public tweets via a third-party service; the target is not notified. But you register an account and hand MyTweetAlerts your search criteria and email, so use a dedicated investigative email, not a personal one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running third-party Twitter alerting service (600k+ alerts sent), but dependent on Twitter/X API terms that can change without notice.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- My Tweet Alerts
tags:
- twitter
- monitoring
- alerts
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# MyTweetAlerts

> A Twitter/X monitoring service: define a handle, name or keyword and get email alerts whenever new matching tweets appear — surveillance-over-time rather than a one-shot lookup.

## When to use
You are tracking a subject's Twitter/X `username`, `name` or a keyword (a location, an alias, a case-specific term) and want to be notified of new activity instead of manually re-checking. Useful in ongoing investigations — a missing person, a monitored account, an evolving event — where the value is catching a fresh post the moment it lands.

## How to use it (`bestInteractionPattern`: web-manual)
1. Register at https://www.mytweetalerts.com/ with a dedicated investigative email.
2. Create an alert: specify the account(s), search terms or criteria you want to watch.
3. Choose delivery — email or real-time, and how often.
4. Receive alerts as matching tweets are posted; each links back to the source tweet (`social-profile` activity) for you to capture.
5. Pivot: treat each alerted tweet as a fresh lead — new locations, associates, media to reverse-image, or handles to enumerate.

## Inputs → Outputs
- **In:** `username`, `name`, or keyword criteria
- **Out:** ongoing email/real-time alerts pointing to matching `social-profile` posts
- **Empty/negative result looks like:** no alerts arriving — either the subject isn't posting, the criteria are too narrow, or (importantly) the service's Twitter/X data feed is degraded; confirm by checking the account directly.

## Gotchas & OpSec
- Twitter/X API changes have repeatedly broken third-party tools; verify alerts are actually flowing before trusting silence as "no activity."
- Free tier caps the number/frequency of alerts.
- You give the service your email and search terms — use a sock-puppet address.

## Overlaps ("do both")
- Pairs with direct Twitter/X advanced search and any archive tool — this catches *new* posts going forward; the others cover the existing/back catalogue.

## Trust & verifiability
`trust: community` — an established third-party alerting service, but its output is only as reliable as its current Twitter/X access; status is marked degraded pending confirmation the feed still works.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mytweetalerts |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
