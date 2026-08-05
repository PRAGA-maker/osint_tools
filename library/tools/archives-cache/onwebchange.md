---
id: onwebchange
name: OnWebChange
description: Use when you have a web page (domain/URL) you want watched and want alerts on changes — returns diffs and email/webhook notifications when the page updates.
url: https://onwebchange.com
category: archives-cache
path:
- archives-cache
bestFor: Hosted, no-setup monitoring of a specific web page with change notifications.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: Free tier gives basic daily monitoring; paid plans (~€0.89–€8.99/mo) add higher check frequency and more trackers (up to ~100).
opsec: active
opsecNote: Active in effect — OnWebChange's servers repeatedly fetch the target page, but the requests come from their infrastructure, not your IP, which shields you from the watched site. Your account and watch list are held by OnWebChange, so use a sock-puppet registration for sensitive targets.
humanInLoop: false
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running (since 2009) hosted monitoring service; it does what it says, but as a third party it holds your watch list and captured content, so it is a trust/dependency to weigh against self-hosting.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- change-detection
- changedetect
aliases:
- OnWebChange
- onwebchange.com
tags:
- web-monitoring
- change-detection
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# OnWebChange

> A hosted "tell me when this page changes" service: register, add a URL, and get emailed (or webhooked) with a diff whenever the content moves — no server of your own to run.

## When to use
You want standing monitoring of a page tied to your case — a profile, a listing, a news or records page, a competitor/company site — but don't want to self-host. OnWebChange runs the checks from the cloud and alerts you on change, and because the fetches come from its servers, the watched site never sees your IP.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://onwebchange.com and register (use a dedicated identity for sensitive work).
2. Add a tracker: paste the target URL (`domain`/page).
3. Optionally select the specific page element/region to watch, so cosmetic churn doesn't spam you.
4. Choose check frequency (free = basic/daily; paid = more often) and a notification channel (email, mobile, webhook).
5. On each change you receive an alert with a diff; review it to see what changed. Pivot: a new address, listing, or edited detail is a fresh, time-stamped lead.

## Inputs → Outputs
- **In:** a `domain`/URL (plus optional element selection)
- **Out:** change alerts and diffs for that page (`domain` activity signal)
- **Empty/negative result looks like:** no notifications — the page is static within your check interval, or your element selection excluded the changed region. Confirm the tracker is active and check its last-run time before assuming nothing changed.

## Gotchas & OpSec
- It monitors URLs you give it; it does not find pages. Feed it targets from other recon.
- Free-tier check frequency is coarse (daily) — fast-moving pages may change and revert between checks.
- JS-heavy or login-gated pages may not diff meaningfully.
- OpSec: fetches originate from OnWebChange (shielding your IP), but the service holds your watch list — a third-party dependency; self-host if that matters.

## Overlaps ("do both")
- Same job as self-hosted `[[change-detection]]` and `[[changedetect]]`: pick hosted (this — zero setup, IP-shielded) vs self-hosted (full control/privacy). One tracker per target is enough.

## Trust & verifiability
`trust: community` — an established hosted monitor; the diffs are verifiable against the live page, and the main consideration is entrusting your watch list and captured content to a third party.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | onwebchange |
