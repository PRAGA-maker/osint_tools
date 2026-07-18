---
id: hunchly-hidden-services-report
name: Hunchly Hidden Services Report
description: Use when you want a daily-updated feed of newly-discovered Tor hidden services to find or monitor onion sites relevant to an investigation — returns `domain` (onion addresses), `associate`.
url: https://darkweb.hunch.ly/
category: dark-web
path:
- dark-web
- discovery
bestFor: A free daily email/list of newly-seen Tor onion services for dark-web discovery and monitoring.
selectorsIn: []
selectorsOut:
- domain
- associate
status: live
pricing: free
costNote: Free — you subscribe with an email and receive a daily report of new hidden services; no paid tier required for the report.
opsec: passive
opsecNote: Receiving the report is passive intelligence — Hunchly crawls and aggregates, so you don't touch onion sites yourself until you choose to. Actually visiting any listed .onion requires Tor and its own strict OpSec (isolated VM, no logins, no downloads).
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Produced by Hunchly, a well-known investigator tooling vendor; the report is a curated crawl output widely used by OSINT/dark-web researchers.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- hunchly
aliases:
- Hunchly Daily Dark Web Report
- Darkweb.hunch.ly
tags:
- dark-web
- tor
- hidden-services
- monitoring
source: arf-seed
lastVerified: '2026-07-18'
enrichment: full
---

# Hunchly Hidden Services Report

> Hunchly's free daily report of newly-discovered Tor onion services — a discovery feed for finding and monitoring dark-web sites without running your own crawler.

## When to use
You need to discover or keep watch on Tor hidden services — new marketplaces, forums, leak sites, or an onion address tied to a case — and you don't want to build a crawler. Hunchly crawls the dark web and emails a daily list of newly-seen .onion services. It's a monitoring/discovery input, not a person-search: you use it to spot relevant onion sites (e.g. a leak site that might post about a subject, or a marketplace to check), then investigate those with proper Tor OpSec. Low direct missing-persons relevance; a specialist dark-web starting point.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://darkweb.hunch.ly/ and subscribe with an email address (use a dedicated/sock-puppet address).
2. Receive the daily report listing newly-discovered hidden-service `domain`s (onion addresses) with titles/snippets.
3. Scan the list for services relevant to your case (a leak site, forum, or marketplace of interest).
4. To investigate a listed site, open it ONLY in a hardened, isolated Tor setup (dedicated VM, no personal logins, no downloads) — the report itself is passive; visiting is not.
5. Pivot: a relevant onion site becomes a monitoring target; linked services/mirrors are `associate` infrastructure leads.

## Inputs → Outputs
- **In:** none (it's a subscription feed; you consume, not query)
- **Out:** `domain` (new .onion service addresses with titles), `associate` (related/mirror services)
- **Empty/negative result looks like:** a report with nothing relevant to your case — normal; most new hidden services won't matter. Value comes from ongoing monitoring, not a single day.

## Gotchas & OpSec
- Human-in-the-loop: requires subscribing with an email (account-login) to receive the report — use a dedicated address.
- OpSec: the report is passive, but ANY visit to a listed .onion demands strict Tor OpSec — never open one in a normal browser or attributable environment.
- It's a discovery firehose: newly-seen ≠ important; expect to filter heavily.

## Overlaps ("do both")
- Pairs with `[[hunchly]]` (the capture tool) and Tor search/index tools — this surfaces *new* services, Ahmia/onion indexes let you search existing ones, and Hunchly captures evidence when you visit. Do both to discover then document.

## Trust & verifiability
`trust: trusted` — produced by Hunchly, an established investigator-tooling vendor; the feed is a reliable curated crawl, though (as with any crawl) it's a sample of the dark web, not a complete index.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hunchly-hidden-services-report |
| category | dark-web |
| selectorsIn → selectorsOut |  → domain, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
