---
id: followthatpage
name: FollowThatPage
description: Use when you have a `domain`/URL you want watched and want email alerts on changes — returns a periodic diff of what text was added or removed.
url: https://www.followthatpage.com
category: archives-cache
path:
- archives-cache
bestFor: Free email alerts when a specific web page's text changes, with the added/removed content shown.
selectorsIn:
- domain
selectorsOut:
- document-id
status: live
pricing: freemium
costNote: Free tier monitors a set number of pages at a daily/weekly cadence; more pages and hourly checks require a paid plan.
opsec: active
opsecNote: "FollowThatPage's own servers fetch the target page on a schedule, so the recurring requests come from its infrastructure, not your IP — that shields you, though the target's server sees periodic hits from a known monitoring service (which it may block). You register with an email address; use a sock-puppet email, and remember the monitored content is processed on their servers."
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running free change-monitoring service; simple and reliable for static pages, but (per its own notice) target sites can block it, and it's a third party you trust to fetch pages.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- follow-that-page
aliases:
- Follow That Page
- followthatpage.com
tags:
- web-monitoring
- change-detection
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# FollowThatPage

> A free, no-frills change monitor: give it a page URL and an email, and it emails you the added/removed text whenever that page changes.

## When to use
You have a `domain`/URL to keep an eye on over time — a subject's profile or bio page, an org's staff/notices page, a listing — and want to be told when it changes without checking manually. It's the lightweight, email-based alternative to heavier change-detection SaaS. Monitoring tooling, so low direct missing-persons relevance, though catching an edit to a subject's page can matter.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.followthatpage.com, enter the target `domain`/URL and your (sock-puppet) email, and set the check frequency.
2. Confirm via the email it sends; the page is now monitored.
3. When the page's text changes, you receive an email highlighting the added/removed content.
4. Save each alert (`document-id` = a dated change record) as timeline evidence; pivot on what changed.
5. For pages it can't fetch (login-walled, heavily dynamic), fall back to a rendering-capable monitor.

## Inputs → Outputs
- **In:** `domain`/URL + email
- **Out:** email alerts with text diffs (added/removed), timestamped (`document-id` = change record)
- **Empty/negative result looks like:** no emails — the page text is unchanged, OR the site is blocking FollowThatPage's fetcher (its own docs warn this happens silently); verify occasionally by hand.

## Gotchas & OpSec
- Per its own warning, monitored sites can block the service without notice — a lack of alerts isn't a guarantee of no change.
- It tracks text, not visual/layout changes, and struggles with JS-rendered or login-walled pages.
- Recurring fetches come from FollowThatPage (shields your IP) but are a known signature the target may block.

## Overlaps ("do both")
- Same-purpose sibling [[follow-that-page]] and the richer [[visualping]] — FollowThatPage is the free email-diff option; VisualPing adds visual diffs and dynamic-page handling. Use FollowThatPage for simple text pages, VisualPing when rendering matters.

## Trust & verifiability
`trust: community` — a durable, simple free service; alerts are reliable for static pages, but because a target can silently block it and you're trusting a third party to fetch pages, spot-check critical pages independently and keep your own archives.
