---
id: kalilinuxtutorials-com
name: kalilinuxtutorials.com (WhatsApp OSINT / whatsappbeacon)
description: Use when you have a target's `phone`/WhatsApp `username` and want to monitor their online/offline pattern and pull profile metadata — returns activity timing, profile photo and status text.
url: https://kalilinuxtutorials.com/whatsapp-osint-tool-2/
category: messaging
path:
- messaging
bestFor: Passively logging a WhatsApp contact's online/offline activity pattern and scraping their public profile picture/status.
selectorsIn:
- phone
- username
selectorsOut:
- social-profile
- image
- metadata-exif
status: unknown
pricing: free
costNote: The described tool (whatsappbeacon.py) is a free open-source script; the kalilinuxtutorials.com page is a how-to article, not the tool itself.
opsec: active
opsecNote: This drives WhatsApp Web through Selenium logged in as YOUR (sock-puppet) account, and the target must be in that account's contacts. Repeatedly opening their chat to read presence is an active interaction with WhatsApp's servers; use a burner number/device, never your real account, and note that presence-monitoring of a specific person can be legally sensitive.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: community
trustNote: A hobbyist Selenium script written up on a tutorial blog; brittle against WhatsApp Web UI changes and not an official or vetted product.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: true
registration: true
aliases:
- whatsappbeacon
- WhatsApp OSINT Tool
tags:
- whatsapp
- WhatsApp
- presence-monitoring
- selenium
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# kalilinuxtutorials.com (WhatsApp OSINT / whatsappbeacon)

> A tutorial-blog write-up of **whatsappbeacon.py** — a Selenium script that logs when a WhatsApp contact is online and scrapes their public profile picture and status.

## When to use
You have a `phone` number (or the contact saved) that is on WhatsApp, and you want to infer the subject's daily rhythm — when they are awake, active, likely at a device — plus grab their current profile photo and "about"/status text. Activity-timing can corroborate a time zone or routine, and a fresh profile photo is a face lead. Presence data is one of the few live signals WhatsApp leaks.

## How to use it (`bestInteractionPattern`: cli)
1. From the kalilinuxtutorials.com article, follow the link to the tool's GitHub repo and `git clone` it.
2. Install deps: `pip install -r requirements.txt`; install ChromeDriver/GeckoDriver matching your browser.
3. Add the target number to a **burner** WhatsApp account's contacts and log that account into WhatsApp Web when the script opens the browser.
4. Run e.g. `python3 whatsappbeacon.py --username <contact> --language "en"`; add `-e` to export the online/offline log to Excel.
5. Let it poll; read the timeline of online events plus the scraped photo/status. Pivot: the photo feeds face/reverse-image tools; the activity pattern feeds time-zone inference.

## Inputs → Outputs
- **In:** `phone` / WhatsApp `username` (must be a contact of the logged-in account)
- **Out:** `social-profile` (WhatsApp presence + status), `image` (profile picture), `metadata-exif`-style activity log (online/offline timestamps)
- **Empty/negative result looks like:** never-online (privacy set to hide "last seen"/online), no profile photo, or the script crashing when WhatsApp Web's DOM has changed. Hidden presence ≠ inactive account.

## Gotchas & OpSec
- **Requires your logged-in account** (`account-login` human-in-loop) and the target in contacts — use a dedicated burner number/device, never your real WhatsApp.
- **Active and intrusive:** continuous presence-monitoring of an individual is exactly the misuse the author warns against and can be unlawful in some jurisdictions — have a lawful basis.
- Brittle: WhatsApp Web UI/anti-automation changes routinely break Selenium scripts; expect breakage and verify it still works before relying on it.
- Users can hide "last seen"/online and profile photo — a blank result is often a privacy setting, not absence.

## Overlaps ("do both")
- Pairs with number-to-account checks and other messaging-app presence tools — those confirm the number is on WhatsApp and check other apps; this one adds the timing dimension once you know it is.

## Trust & verifiability
`trust: community` — an educational hobby script surfaced via a tutorial blog, not an official or audited tool. Treat presence timestamps as indicative and corroborate the profile photo/status directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | kalilinuxtutorials-com |
| category | messaging |
| selectorsIn → selectorsOut | phone, username → social-profile, image, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login) |
