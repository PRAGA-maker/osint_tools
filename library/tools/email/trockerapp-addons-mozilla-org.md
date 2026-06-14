---
id: trockerapp-addons-mozilla-org
name: trockerapp (addons.mozilla.org)
description: Use when you want to detect and block email tracking pixels and link trackers in your own webmail on Firefox — protects your OpSec; it does not look up people.
url: https://addons.mozilla.org/en-US/firefox/addon/trockerapp/
category: email
path:
- email
bestFor: Firefox add-on that exposes and strips read-receipt tracking pixels and tracked links in Gmail/webmail.
selectorsIn:
- email
selectorsOut:
- metadata
status: live
pricing: free
costNote: Free open-source browser add-on.
opsec: passive
opsecNote: A defensive OpSec tool — it warns when an inbound email contains tracking pixels and blocks them so opening the mail does not leak your read status/IP to the sender. It does not contact or profile any third party.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: community
trustNote: Trocker (trockerapp) is a known open-source anti-email-tracking add-on. It is a privacy/defense tool, not a person-search or IP-trace tool despite the source list's 'Covert IP Trackers' tag.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
relatedTools:
- trocker-chrome-google-com
aliases:
- Trocker
- Trocker Firefox add-on
tags:
- emailtrackers
- email-privacy
- browser-extension
source: uk-osint
lastVerified: ''
enrichment: full
---

# trockerapp (addons.mozilla.org)

> A Firefox add-on that detects and blocks email read-tracking pixels and tracked links — a defensive OpSec tool for the investigator's own inbox, not an investigative lookup.

## When to use
You correspond with subjects/sources from your own webmail in Firefox and want to avoid leaking read receipts, your `ip-address`, or open-times back to senders. Trocker flags inbound emails containing tracking pixels and lets you open them without firing the beacon. It does not take an `email` and return identity data; its value here is protecting your own footprint while running a case.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the Trocker add-on from the addons.mozilla.org URL above.
2. Open your webmail (Gmail/Outlook web) while logged in.
3. Trocker marks emails that contain trackers and blocks the pixels.
4. Pivot: when you must reply to a tracked sender, you now know they instrument their mail — adjust OpSec (sock puppet, no link clicks) accordingly.

## Inputs → Outputs
- **In:** `email` (messages in your own inbox)
- **Out:** `metadata` (tracker present/blocked indicators)
- **Empty/negative result looks like:** no tracker icon — the email has no detected beacon (or uses a method Trocker doesn't recognize).

## Gotchas & OpSec
- Human-in-the-loop: you must be logged into your webmail account.
- It is a personal-defense tool — do not catalog it as a way to trace or identify other people.
- OpSec: improves your OpSec; nothing leaves toward the subject.

## Overlaps ("do both")
- Same tool as [[trocker-chrome-google-com]], which is the Chrome build — pick the one matching your browser.

## Trust & verifiability
`trust: community` — a recognized open-source anti-tracking add-on; reclassified here from the source list's misleading 'Covert IP Trackers' label, since it blocks trackers rather than tracing IPs.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | trockerapp-addons-mozilla-org |
| category | email |
| selectorsIn → selectorsOut | email → metadata |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | yes |
