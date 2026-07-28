---
id: talend-api-tester-free-edition
name: Talend API Tester - Free Edition
description: Use when you have an API endpoint on a `domain` and want to hand-craft requests and inspect responses in-browser — returns domain/response data for enrichment pivots.
url: https://chromewebstore.google.com/detail/talend-api-tester-free-ed/aejoelaoggembcahagimdiliamlcdmfm
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Manually probing REST/SOAP/HTTP APIs from the browser — headers, auth, method, body — and reading raw responses.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: freemium
costNote: The Chrome "Free Edition" extension is free for individual manual testing; Talend/Qlik sells a paid Cloud tier for teams and automation, but the free edition needs no account.
opsec: active
opsecNote: This sends real HTTP requests to the target endpoint from your machine, so your IP and request headers hit the target's server logs. Treat as active reconnaissance — route through a VPN/sock-puppet setup and avoid patterns that look like probing or abuse.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: Published by Talend (now part of Qlik), an established data-integration vendor; the extension is the genuine vendor product (formerly Restlet Client).
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
aliases:
- Restlet Client
- Talend Cloud API Tester
tags:
- api
- http-client
- source-code-analysis
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# Talend API Tester - Free Edition

> A visual REST/SOAP/HTTP client that lives in Chrome — build a request by hand, set headers/auth, and read the raw response.

## When to use
You've found an API endpoint on a target `domain` (an undocumented JSON endpoint behind a web app, a public API, a webhook) and you want to poke it manually: change the method, add headers or auth, tweak the body, and read exactly what comes back. It's the pivot tool when a site's data lives behind an API rather than in rendered HTML, and you want to enumerate response fields, spot linked hosts/IDs, or confirm what an endpoint leaks — without writing a script.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install "Talend API Tester - Free Edition" from the Chrome Web Store and open it (it runs as an app tab).
2. Set the HTTP method and the endpoint URL (`domain`/path).
3. Add headers, query params, auth, and a request body as needed; send the request.
4. Inspect the response — status, headers, and body rendered as JSON/XML/HTML/image. Save requests into a project and replay from history.
5. Pivot: fields in the response (other hostnames, user IDs, emails, image URLs, `domain` references) feed the next lookup; import/export as Postman/OpenAPI to share the request.

## Inputs → Outputs
- **In:** an API endpoint on a `domain` (+ method, headers, auth, body)
- **Out:** the raw response — headers and body — from which you extract linked `domain`s, IDs and other enrichment leads
- **Empty/negative result looks like:** 401/403 (auth required), 404 (no such endpoint), or CORS/empty body — that tells you about the endpoint's access model, which is itself intel.

## Gotchas & OpSec
- OpSec: **active** — every request hits the target's servers from your IP with your headers. Use a VPN/sock puppet and don't hammer endpoints (that's abuse and is logged).
- It's a manual client, not a scanner: you drive each request. Great for careful probing, wrong tool for bulk crawling.
- The free edition is browser-local; the paid Cloud tier adds team/automation features you don't need for manual OSINT.

## Overlaps ("do both")
- Complements passive `domains-ip-infrastructure` recon (WHOIS, DNS, certificate tools): those map a domain's surface passively, while Talend API Tester actively interrogates a specific endpoint you found.

## Trust & verifiability
`trust: trusted` — the genuine vendor extension from Talend/Qlik (formerly Restlet Client); it faithfully sends what you specify and shows the real response, so verifiability rests on the endpoint, not the tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | talend-api-tester-free-edition |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | low |
| interaction | browser-extension |
| opsec | active |
| human-in-loop | no |
