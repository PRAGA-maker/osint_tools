---
id: mr-holmes
name: Mr.Holmes
description: Use when you have a `username`, `email`, `phone`, or `domain` and want a one-command multi-module sweep — returns `social-profile`, email/service links, phone recon, and a relationship graph.
url: https://github.com/Lucksi/Mr.Holmes
category: people-search
path:
- people-search
bestFor: Quick multi-selector reconnaissance (username, phone, email, domain) from one CLI/GUI, with graphs and maps.
selectorsIn:
- username
- email
- phone
- domain
- name
selectorsOut:
- social-profile
- email
- phone
- domain
status: live
pricing: free
costNote: Free and open-source (Lucksi); runs locally on Linux/Mac/Windows/Termux. Some modules use free public APIs; a WhoIS API key may be needed for full domain data.
opsec: passive
opsecNote: Modules query third-party sites and APIs directly from your host, so those services see your IP. It supports proxy rotation — use it, from a sock-puppet environment. It does not authenticate to or notify targets, but the Google-dorking and profile checks generate ordinary web traffic.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular community OSINT multi-tool maintained by an individual; convenient but its results are only as good as the underlying free modules — verify every hit.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- social-analyzer
- phunter
aliases:
- mr holmes
- mrholmes
tags:
- multi-tool
- username
- phone
- email
source: gh-topic-osint-framework
lastVerified: '2026-07-10'
enrichment: full
---

# Mr.Holmes

> A local Python multi-tool that bundles username, email, phone, and domain reconnaissance behind one CLI/GUI — with Google-dorking, relationship graphs, and Leaflet maps.

## When to use
You have one or more selectors — a `username`, `email`, `phone`, `domain`, or `name` — and want a fast, single-command first pass that touches several modules at once rather than running separate tools. It is a convenience aggregator: good for quickly scoping a target before you commit to deeper, specialist tooling.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/Lucksi/Mr.Holmes` and run the install script for your OS (Linux/Mac bash, Windows batch, or the Termux/proot script on Android).
2. Launch the CLI or GUI (dark/light/high-contrast themes).
3. Pick a module and feed the selector:
   - **Username** → checks social/media platforms for the handle.
   - **Email** → tests which socials/services the address is registered to.
   - **Phone** → PhoneInfoga-style carrier/region recon.
   - **Domain** → WhoIS lookup (may need an API key).
   - **Google Dorks** → images/video/sound searches with date filters.
4. Use the graph/map/PDF export to visualise and save findings; enable proxy rotation for OpSec.
5. Pivot: confirmed handles/emails feed specialist tools; the graph highlights `associate`/`domain` links to chase next.

## Inputs → Outputs
- **In:** `username`, `email`, `phone`, `domain`, or `name`
- **Out:** `social-profile` hits, email→service links, phone recon, `domain` WhoIS, plus graphs/maps/PDF reports
- **Empty/negative result looks like:** a module returns no hits or an API/key error — treat as inconclusive; a single dead module doesn't mean the target is absent.

## Gotchas & OpSec
- Result quality varies sharply by module (it wraps free sources that break or rate-limit); always verify hits against the primary platform.
- Domain module may require a WhoIS API key for complete data.
- Installation pulls many dependencies; run it in a VM/container for hygiene.
- OpSec: passive toward targets, but modules hit third-party services from your IP — enable proxy rotation and use a sock puppet.

## Overlaps ("do both")
- Overlaps with `[[social-analyzer]]` (deeper username enumeration) and `[[phunter]]` (dedicated phone recon) — use Mr.Holmes for the quick multi-selector scope, then the specialists for depth.

## Trust & verifiability
`trust: community` — a well-starred individual-maintained aggregator. It is a convenience layer over free modules, so its output inherits their reliability; independently confirm anything you act on.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | mr-holmes |
| category | people-search |
| selectorsIn → selectorsOut | username, email, phone, domain, name → social-profile, email, phone, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
