---
id: osrframework-2
name: OSRFramework
description: Use when you have a `username`, `email`, `phone`, or full `name` and want to enumerate accounts and profiles across many platforms from the command line — returns social-profile and email leads.
url: https://pypi.org/project/osrframework/
category: people-search
path:
- people-search
bestFor: Command-line enumeration of a username/email/phone across social networks, forums and services via the i3visio module suite (usufy, mailfy, phonefy, searchfy).
selectorsIn:
- username
- email
- phone
- name
selectorsOut:
- social-profile
- email
status: degraded
pricing: free
costNote: Free and open-source (AGPLv3). No fees; some modules need free API keys for certain data sources.
opsec: passive
opsecNote: Modules like usufy visit each candidate platform to confirm a profile — that traffic originates from your IP. Run from a sock-puppet context/VPN; you never message the target, but you do touch many sites in quick succession.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Well-known open-source suite by i3visio analysts, but effectively unmaintained since 2021 (last PyPI release Nov 2021); several modules break as target sites change.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- sherlock
- maigret
- whatsmyname
aliases:
- osrframework
- i3visio
- usufy
- mailfy
tags:
- username-enumeration
- open-source
- cli
- python
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# OSRFramework

> The i3visio open-source OSINT suite — a bundle of CLI utilities (usufy, mailfy, searchfy, phonefy, domainfy, entify) that enumerate a selector across many platforms at once.

## When to use
You have a `username`, `email`, `phone`, or full `name` and want a scripted, multi-source sweep for accounts and mentions. Reach for it when you want a local, no-account tool you can chain into a pipeline: `usufy` checks a username across social sites, `mailfy` maps an email to services, `searchfy` looks up a full name, `phonefy` a phone. Treat it as a legacy workhorse — powerful in concept, but expect broken modules.

## How to use it (`bestInteractionPattern`: cli)
1. Install into Python: `pip install osrframework` (or from github.com/i3visio/osrframework).
2. Run the relevant module:
   - `usufy -n <username>` — username across platforms
   - `mailfy -m <email>` — email across services
   - `searchfy -q "<full name>"` — name search
   - `phonefy -n <phone>` — phone across sources
3. Read the output table: confirmed profiles/hits with their URLs. Export to CSV/JSON for pivoting.
4. Sanity-check hits — stale platform definitions cause both misses and false positives.
5. Pivot: confirmed `social-profile` URLs feed face/image and content tools.

## Inputs → Outputs
- **In:** `username`, `email`, `phone`, or `name`
- **Out:** `social-profile` (confirmed account URLs), `email` leads, service hits
- **Empty/negative result looks like:** all-"not found" or a stack trace/timeout — often a broken/outdated module rather than a true negative. Cross-check with a maintained tool.

## Gotchas & OpSec
- **Degraded:** unmaintained since 2021; many platform definitions are stale — verify with `[[maigret]]` / `[[sherlock]]` before trusting negatives.
- Runs many outbound requests fast — throttle and use a VPN/sock-puppet to avoid IP flags.
- Some modules expect free API keys; missing keys silently reduce coverage.

## Overlaps ("do both")
- Pairs with `[[maigret]]` and `[[sherlock]]` — modern, maintained username enumerators with far larger, current site lists. Use those as the primary and OSRFramework's `mailfy`/`phonefy` for the email/phone angles they lack.

## Trust & verifiability
`trust: community` — a respected but aging open-source project. Logic is inspectable; reliability has decayed, so corroborate every hit against a current tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osrframework-2 |
| category | people-search |
| selectorsIn → selectorsOut | username, email, phone, name → social-profile, email |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
