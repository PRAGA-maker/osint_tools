---
id: scylla
name: Scylla
description: Use when you have a `username`, `phone`, or `name` and want an all-in-one recon sweep from a local CLI — returns social profiles, geolocation, and breach hints (but many data sources are stale).
url: https://github.com/josh0xA/Scylla
category: people-search
path:
- people-search
bestFor: Running a single local Python CLI that fans a username/phone/name across multiple recon sources at once.
selectorsIn:
- username
- phone
- name
selectorsOut:
- social-profile
- geolocation
- email
status: degraded
pricing: free
costNote: Free open-source (Python). Some modules (e.g. Shodan) need your own API key; no paid tier.
opsec: passive
opsecNote: Runs from your own machine and queries third-party APIs/sites; nothing is sent to the target directly. Because it hits many external services, run it from a VPN and expect some modules to leak your IP to those services. Do not rely on its breach/finance checks for anything sensitive.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Open-source tool by Josh Schiavone; explicitly no longer maintained, with many APIs broken — code is inspectable but results are unreliable and partial.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
aliases:
- josh0xA Scylla
- Scylla OSINT
tags:
- people-search
- open-source
- cli
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# Scylla

> A self-hosted Python "kitchen-sink" recon CLI (username, phone, name → social profiles, geolocation, breach hints) — historically useful, but now developer-abandoned with many broken data sources, so treat it as a legacy convenience wrapper.

## When to use
You want to run one local command that sprays a `username`, `phone`, or `name` across several recon sources — social-media profile discovery, geolocation, and leaked-card/breach checks — without wiring up each service by hand. Reach for it only when you already have the environment and understand its outputs are partial: the developer has stated the project is no longer maintained and many of its APIs no longer work, so it is a starting scatter-shot, not an authority.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/josh0xA/Scylla` and install its Python 3.6+ dependencies.
2. Optionally add API keys (e.g. Shodan) for the modules that need them.
3. Run the CLI against your selector: username (finds social profiles across major platforms), phone, or name; use the geolocation and finance/breach modules as available.
4. Read outputs skeptically — cross-check every hit, since dead APIs return empty or wrong results.
5. Pivot: confirmed `social-profile`s feed username tools; a `geolocation` hint feeds mapping; treat breach output as unverified.

## Inputs → Outputs
- **In:** `username` / `phone` / `name`
- **Out:** `social-profile` (username-to-platforms), `geolocation`, `email`/breach hints
- **Empty/negative result looks like:** many modules return nothing or errors — this usually means a **broken/deprecated API**, not that the target is absent. Verify with a currently-maintained equivalent before concluding.

## Gotchas & OpSec
- Human-in-the-loop: some modules need your own **API key**; setup is technical.
- **Maintenance: abandoned.** Expect broken sources and outdated results — hence `status: degraded`. Prefer maintained single-purpose tools for anything you'll rely on.
- OpSec: passive to the target but it queries many third parties; run behind a VPN.

## Overlaps ("do both")
- Overlaps heavily with maintained username-enumeration tools (Sherlock/Maigret-style) and phone tools — use those for the parts Scylla can no longer reach reliably; Scylla's value is only the one-command convenience.

## Trust & verifiability
`trust: community` — open-source and inspectable, but self-declared unmaintained with broken APIs; every result needs independent confirmation with a current tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | scylla |
| category | people-search |
| selectorsIn → selectorsOut | username, phone, name → social-profile, geolocation, email |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
