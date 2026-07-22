---
id: free-proxy-list
name: Free Proxy List
description: Use when you need a throwaway `ip-address` proxy to view a target without exposing your own IP — returns a live list of free public proxies (IP, port, country, anonymity).
url: https://free-proxy-list.net
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Grabbing a fresh, disposable public HTTP/HTTPS proxy to add a layer between your real IP and a passive lookup.
selectorsIn: []
selectorsOut:
- ip-address
status: live
pricing: freemium
costNote: The public proxy table (refreshed ~every 10 minutes) is free; premium/faster lists and larger volumes are paid ($9.92–$59.95/month).
opsec: passive
opsecNote: This is your-side tooling — it names no target. But free public proxies are untrusted: operators can log or inject traffic, so never send credentials or authenticated sessions through them. Use only for low-stakes, unauthenticated viewing, and prefer a reputable VPN for anything sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: Aggregates anonymous public proxies of unknown ownership; reliability and honesty of any given proxy cannot be verified.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- free-proxy-list.net
tags:
- proxy
- opsec
- anonymity
source: opsec
lastVerified: '2026-07-22'
enrichment: full
---

# Free Proxy List

> A constantly-refreshed table of free public proxies — a quick source of a throwaway exit IP for your own OpSec, not a lookup on any target.

## When to use
You are about to make a passive, unauthenticated request (open a page, view a public profile) and want to avoid doing it from your real or office IP. Free Proxy List gives you a menu of currently-live public proxies with their country and anonymity level so you can route that one request through a disposable address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://free-proxy-list.net — the table lists IP, port, country, anonymity ("elite/anonymous/transparent"), HTTPS support and last-checked time.
2. Pick an **elite/anonymous** proxy in a plausible country with recent "last checked".
3. Configure it in your browser/sock-puppet profile or scraping tool, or pull the raw list / free API URL for automation.
4. Verify it works and hides your IP (e.g. via a "what is my IP" check) before using it, then discard it after the task.
5. Use it only for the low-stakes fetch — never for logins.

## Inputs → Outputs
- **In:** none (you are not querying a target)
- **Out:** a list of proxy `ip-address`:port entries with country and anonymity metadata
- **Empty/negative result looks like:** most listed proxies failing to connect — free proxies die constantly; expect to try several, and if none work, fall back to a paid proxy/VPN.

## Gotchas & OpSec
- Free public proxies are inherently untrusted — assume the operator can see and log your traffic. HTTPS-only, no credentials, no authenticated sessions.
- They are slow and short-lived; not suitable for sustained or high-volume work.
- For any real operational anonymity, a reputable commercial VPN/proxy beats this.

## Overlaps ("do both")
- Pairs with browser-fingerprint checkers (confirm the proxy actually masks you) and with sock-puppet browser tooling as part of a pre-lookup OpSec setup.

## Trust & verifiability
`trust: unverified` — the site simply aggregates anonymous proxies of unknown provenance; treat every entry as potentially hostile infrastructure.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | free-proxy-list |
