---
id: httpie-io
name: HTTPie
description: Use when you have a `domain`/API endpoint and want to probe it by hand — returns raw HTTP responses, headers, and JSON in a readable CLI.
url: https://httpie.io/run
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A human-friendly command-line HTTP client for manually inspecting endpoints, headers, and APIs during investigation.
selectorsIn:
- domain
selectorsOut:
- domain
- ip-address
status: live
pricing: freemium
costNote: The `httpie` CLI is free and open source (BSD). httpie.io also offers a paid hosted API-testing product; the CLI you need for OSINT is free.
opsec: active
opsecNote: Every request goes directly from your machine to the target server, which logs your IP and user-agent. Route through a proxy/VPN and set a neutral user-agent when probing a subject's infrastructure.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: HTTPie is a mainstream, widely-adopted open-source HTTP client; the CLI is well-maintained and auditable.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- httpie
- http command
tags:
- http-client
- api-testing
- cli
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# HTTPie

> A friendlier curl: fire off HTTP requests from the terminal and get colour-formatted headers and JSON back, ideal for poking at a target's endpoints by hand.

## When to use
You're examining a `domain` or a specific API/web endpoint and want to see exactly what it returns — response headers, status codes, redirects, server banners, JSON bodies — without wrestling with curl's syntax. HTTPie is a general-purpose investigative utility for manual HTTP inspection: checking what technology a server runs, probing an undocumented API, following redirects, or grabbing headers that leak infrastructure detail. It's a supporting tool; missing-persons relevance is low and indirect.

## How to use it (`bestInteractionPattern`: cli)
1. Install the CLI: `pip install httpie` (or via your OS package manager). A browser-based runner also exists at httpie.io/run.
2. Make requests:
   ```
   http GET https://example.com            # readable response + headers
   http HEAD https://example.com           # headers only (server, redirects)
   http https://api.example.com/users id==5 Authorization:"Bearer ..."
   ```
   Syntax is `http [METHOD] URL [items]`, where `key==value` are query params and `Key:Value` are headers.
4. Read the colourised headers/body. Pivot: `Server`/`X-Powered-By` headers and redirect `Location`s reveal tech and other `domain`s; resolving the host gives the `ip-address` for further infra work.

## Inputs → Outputs
- **In:** a `domain`/URL (+ optional headers, params, body)
- **Out:** HTTP status, headers (server banners, redirects), body — plus the host's `ip-address` on resolution
- **Empty/negative result looks like:** connection error / timeout / TLS failure — the host is down, blocking you, or geofenced; a 403/429 may mean your IP is blocked rather than the resource being absent.

## Gotchas & OpSec
- It's a generic HTTP tool, not an OSINT-specific one — value is in *how* you use it to inspect infrastructure.
- The paid httpie.io hosted product is separate from the free CLI; you only need the CLI.
- OpSec: **active** — requests reveal your IP/user-agent to the target. Proxy and spoof the user-agent when probing a subject.

## Overlaps ("do both")
- Overlaps with curl/wget (same job, nicer output) and complements header/tech-fingerprint tools (Wappalyzer, WhatWeb) — HTTPie for manual one-off inspection, the fingerprinters for automated tech detection.

## Trust & verifiability
`trust: trusted` — mainstream, well-maintained open-source client; it simply shows you the server's own response, so what you see is authoritative for that request (mind that servers can vary responses by IP/UA).

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | httpie-io |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain → domain, ip-address |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
