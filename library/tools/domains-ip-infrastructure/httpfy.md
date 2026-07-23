---
id: httpfy
name: HTTPFY
description: Use when you have a `domain` (or a list of domains) and want fast HTTP fingerprinting — returns which are live plus status, title, server, content-type, redirect target and body metrics.
url: https://github.com/devXprite/httpfy
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Quickly probing a list of domains to find the live ones and grab their HTTP fingerprints.
selectorsIn:
- domain
selectorsOut:
- domain
- employer-org
status: live
pricing: free
costNote: Free and open source (GPL-3.0); installed locally via npm/Node.js.
opsec: active
opsecNote: HTTPFY makes real HTTP requests to each target domain, so your IP appears in the target's web/server logs. This is active reconnaissance — route it through a VPN/proxy or a disposable VPS if you don't want the probe traced back to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source Node.js utility by an independent developer (devXprite) on GitHub; code is inspectable but not from a major vendor.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- infooze
aliases:
- httpfy
- devXprite/httpfy
tags:
- Domain/IP/Links
- Domain/IP investigation
- http-probe
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# HTTPFY

> A fast Node.js HTTP probe: feed it a list of domains and it tells you which respond and fingerprints each one (status, title, server, redirects, content metrics).

## When to use
You have one domain or a large list of them — subdomains from enumeration, candidate hosts, a scope list — and want to know which are actually serving HTTP and what each looks like at a glance. Reach for HTTPFY to triage a bulk list down to live, interesting hosts before doing deeper work: it surfaces the page title, server banner, content type, and any redirect so you can spot parked pages, login portals, or panels quickly.

## How to use it (`bestInteractionPattern`: cli)
1. Install with Node.js: `npm install -g httpfy` (or clone the repo, `npm install`, and run `node index.js`).
2. Put your domains one-per-line in a file, e.g. `domains.txt`.
3. Run: `httpfy -f domains.txt`.
4. Read the per-domain output: HTTP status code, content length, response time, page title, server name, content type, redirect location, and body line/word counts.
5. Pivot: take the live/interesting hosts and enrich them — WHOIS, certificate search, or a broader recon tool like `[[infooze]]`.

## Inputs → Outputs
- **In:** `domain` (single or a file of many)
- **Out:** live/dead verdict per host plus HTTP fingerprint — title, `employer-org` hint (server banner/hosting), content type, redirect target
- **Empty/negative result looks like:** a domain that times out, refuses connection, or returns no status has no live HTTP service (or is blocking you) — not necessarily "no such domain".

## Gotchas & OpSec
- OpSec: **active** — every probe is a real request that lands in the target's logs with your IP. Use a VPN/proxy or throwaway VPS for anything sensitive.
- Rate/volume: hammering a large list can trip WAFs or rate limits; pace it.
- It reports what the server *says* (title, banner), which can be spoofed — corroborate before trusting a server header.

## Overlaps ("do both")
- Pairs with `[[infooze]]` — HTTPFY quickly separates live hosts from dead ones; infooze and similar recon suites then dig deeper into the survivors. Run HTTPFY first as the cheap triage pass.

## Trust & verifiability
`trust: community` — an open-source, inspectable Node.js tool from an independent GitHub developer; reliable as a probe, but verify any single header/title before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | httpfy |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
