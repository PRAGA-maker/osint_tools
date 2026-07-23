---
id: google-dashboard-privacy-control-tool
name: Google Dashboard Privacy Control Tool
description: Use when you (the investigator) want to audit and lock down what your own Google account exposes — activity, location history, connected devices — returns a self-review of your account's data footprint.
url: https://myaccount.google.com/dashboard
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Self-audit and hardening of your own Google account before/after conducting online investigations.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free Google service; requires signing in to the account you are auditing.
opsec: passive
opsecNote: This operates only on YOUR OWN Google account — it is a personal OpSec hygiene tool, not a way to query a target. Use it to disable Web & App Activity, Location History, and to review connected devices/apps on the sock-puppet or investigator account you use for OSINT work, so your searches don't leak into a linked identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party Google Account settings surface (the old google.com/dashboard now redirects into myaccount.google.com); not a third-party scraper.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
aliases:
- Google Dashboard
- Google Account activity controls
- myaccount.google.com/dashboard
tags:
- toddington
- curated-directory
- proxy-servers-online-privacy-security-tools
- opsec
source: toddington-resources
lastVerified: '2026-07-23'
enrichment: full
---

# Google Dashboard Privacy Control Tool

> Google's own account-activity dashboard, used as an OpSec self-audit: see (and switch off) everything your investigator/sock-puppet Google account is silently recording.

## When to use
You run searches, translations, Maps look-ups, or YouTube views while logged into a Google account and want to make sure that activity isn't being logged, personalised, or leaking into a real identity. Reach for this to review what a specific account holds — Gmail, YouTube history, Maps timeline, connected third-party apps, signed-in devices — and to turn off Web & App Activity and Location History before working a case. It is a hygiene tool for *your* account, not a lookup against a subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Sign in to the exact Google account you want to audit (ideally your dedicated sock-puppet account, in a clean browser profile) and open https://myaccount.google.com/dashboard.
2. Scan the per-service summary: number of emails, docs, YouTube subscriptions, saved Maps places, connected devices, and third-party apps with access.
3. Go to **Data & privacy → History settings** and pause **Web & App Activity**, **Location History (Timeline)**, and **YouTube History**; delete existing activity if you want a clean slate.
4. Under **Security → Your devices** and **Third-party apps with account access**, revoke anything you don't recognise.
5. Pivot: pair this with a VPN/sock-puppet browser so that even with logging off, your source IP isn't tied back to you.

## Inputs → Outputs
- **In:** your own Google account credentials (no target selector)
- **Out:** a self-review of the account's data footprint plus toggles to disable logging
- **Empty/negative result looks like:** a freshly created sock-puppet account shows little to no activity — that's the desired clean state, not a failure.

## Gotchas & OpSec
- Human-in-the-loop: you must be logged in; expect 2FA prompts on the account.
- OpSec: **passive** with respect to any subject — you are only touching your own account. Do NOT log into a target's account; that is intrusive and likely illegal. The value here is purely defensive: minimise what your investigative persona records and exposes.
- Pausing activity does not scrub server-side logs Google keeps for its own purposes; treat "off" as "not personalised", not "invisible".

## Overlaps ("do both")
- Pairs with `[[vpn]]` — the dashboard stops Google logging your activity to the account; a VPN stops your ISP/IP tying the session to you. Do both for a clean investigative persona.

## Trust & verifiability
`trust: trusted` — this is Google's genuine account-management console, so the controls are authoritative for the account you're signed into.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-dashboard-privacy-control-tool |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
