---
id: distill-io
name: Distill.io
description: Use when you have a `domain`/URL and want to be alerted the moment a page changes — returns change notifications and a diff of what changed.
url: https://distill.io/
category: archives-cache
path:
- archives-cache
bestFor: Monitoring a specific web page (or page region) for changes and getting alerted when it updates.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free tier — 25 local (browser) monitors, 5 cloud monitors, ~6-hour check frequency, 1000 checks/month, 30 email alerts. Paid plans add faster/cloud monitoring.
opsec: active
opsecNote: Local monitors fetch the page from your own browser, so the target site sees your visits on each check; cloud monitors fetch from Distill's servers instead (your IP hidden, but you trust Distill with the URL and any login). For sensitive targets prefer cloud monitors or a sock-puppet profile, and never point a logged-in local monitor at a subject-controlled site.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: community
trustNote: Established commercial change-monitoring service recommended in the Bellingcat toolkit; reliable for detecting changes, but it's a closed third party you entrust with the URLs (and cloud credentials) you monitor.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: true
registration: true
relatedTools: []
aliases:
- Distill Web Monitor
- distill.io
tags:
- bellingcat-toolkit
- archiving
- change-monitoring
source: bellingcat-toolkit
lastVerified: '2026-07-23'
enrichment: full
---

# Distill.io

> A web-page change monitor (browser extension + cloud) that watches a page or a selected region and alerts you — email, push, SMS — the instant it changes.

## When to use
You have a `domain`/URL that matters to a case and want to catch changes as they happen rather than re-checking by hand: a suspect's profile bio, a marketplace listing, a company "team" page, a court-docket or missing-person appeal page. Distill diffs the page on a schedule and pings you when the part you care about moves.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the Distill Web Monitor extension (Chrome/Firefox/Edge/Opera) and create a free account for cloud monitors and cross-device alerts.
2. Open the target page, click the Distill icon, and "Select part of page to monitor" — drag to pick the exact region (a bio, a price, a status line) so you aren't alerted on unrelated churn.
3. Choose local (runs in your browser) or cloud (runs on Distill's servers), set check frequency and alert channel (email/push/SMS).
4. When a change fires, open the alert to see the before/after diff; save/screenshot it immediately since the live page keeps moving.
5. Pivot: a change (new phone in a bio, an edited listing, a removed name) becomes a fresh lead — capture it durably (e.g. with `[[single-file]]`) before it changes again.

## Inputs → Outputs
- **In:** a `domain`/URL (optionally a selected page region)
- **Out:** change alerts with a diff of the monitored region; a running history of when the page changed
- **Empty/negative result looks like:** no alerts over time — the page is static, OR your selector missed the changing element, OR the page requires a login the monitor doesn't have. Re-scope the selection to confirm.

## Gotchas & OpSec
- Human-in-the-loop: an **account/login** is needed for cloud monitors and syncing; local monitors only run while your browser is open.
- Local monitors reveal *your* IP to the target on every check — use cloud monitors or a clean profile for subject-controlled pages.
- Free tier is rate-limited (6-hour minimum, 1000 checks/mo); fast-moving pages may need a paid plan or you'll miss transient changes.

## Overlaps ("do both")
- Pairs with `[[single-file]]` — Distill tells you *when* something changed; SingleFile captures a durable copy of the *before* and *after*. Run both on anything you may need to prove later.

## Trust & verifiability
`trust: community` — a mature, Bellingcat-listed monitoring service. The change detection is dependable; the trust caveat is that you're handing a closed third party the URLs (and, for authenticated cloud monitors, credentials) you watch.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | distill-io |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | yes (account-login) |
