---
id: owlculus
name: Owlculus
description: Use when you're running an investigation and want to organize it — entities, evidence, and OSINT plugins — in one self-hosted case-management platform; returns a structured case with cross-linked entities and findings.
url: https://github.com/be0vlk/owlculus
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Managing an investigation (missing-person or other) — tracking entities/evidence and running OSINT plugins in one web UI.
selectorsIn:
- name
- username
- email
- domain
selectorsOut:
- social-profile
- email
- associate
status: live
pricing: free
costNote: 100% free and open-source (GPL-3.0); self-hosted via Docker. No fees; you provide the infrastructure and any downstream tool/API keys.
opsec: passive
opsecNote: Owlculus itself is a local case-management app — running it is passive. But its plugins make real queries to third-party services from your host, which are active; isolate the deployment and route plugin traffic through a sock-puppet network. Keep case data on encrypted storage you control.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: docker
trust: trusted
trustNote: Actively maintained open-source project (v2.0.2, Sept 2025) and bundled in the Trace Labs OSINT VM; the app is a workflow/orchestration layer, so its "trust" is about tooling reliability, not data provenance.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- be0vlk/owlculus
tags:
- case-management
- docker
- investigation-platform
- web-ui
source: tracelabs-repos
lastVerified: '2026-07-11'
enrichment: full
---

# Owlculus

> A self-hosted OSINT case-management platform — the workbench that holds an investigation together: entities, evidence, collaborators, and built-in OSINT plugins in one web UI.

## When to use
You're running an investigation (a missing-person case, a subject workup) and need to organize it rather than run a single lookup: track people/companies/domains/IPs as entities, file evidence with templates, correlate across cases, and launch OSINT plugins from the UI. Reach for it when a case has enough moving parts that ad-hoc notes stop scaling — it is the container your other tools feed into.

## How to use it (`bestInteractionPattern`: docker)
1. Clone the repo and bring up the Docker stack (compose files are provided; a setup script and Caddy reverse-proxy option exist):
   ```
   git clone https://github.com/be0vlk/owlculus.git
   cd owlculus
   # run the provided setup / docker compose
   ```
2. Open the web UI, create a case (with your report-numbering scheme), and add entities: `name`, `username`, `email`, `domain`, IPs, vehicles.
3. Run built-in OSINT plugins against those entities and attach results as evidence; use the browser extension to capture web content.
4. Use cross-case correlation to spot shared entities/`associate`s across investigations.
5. Pivot: Owlculus is the hub — findings from `[[blackbird]]`, people-search, and image tools all land here as linked evidence.

## Inputs → Outputs
- **In:** case entities — `name`, `username`, `email`, `domain` (+ IPs, vehicles)
- **Out:** a structured case: cross-linked entities, attached evidence, plugin results (`social-profile`s, `email`s, `associate` links)
- **Empty/negative result looks like:** an empty case or a plugin returning nothing — Owlculus organizes but doesn't invent data; sparse results reflect the underlying sources, not the platform.

## Gotchas & OpSec
- Self-hosting: you run and secure it — keep it off public networks and encrypt case data.
- Plugin traffic is active: the app is passive, but plugins hit third-party services from your host; use a sock-puppet network.
- Update regularly (`git pull`) — it's under active development.

## Overlaps ("do both")
- Pairs with essentially every collection tool in this library — enumerators, people-search, image/geolocation — Owlculus is the case layer that captures and correlates what they return, rather than a competitor to them.

## Trust & verifiability
`trust: trusted` — a well-maintained, widely used open-source case platform; reliability is about the tooling. The trustworthiness of any datum still depends on the source plugin that produced it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | owlculus |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | name, username, email, domain → social-profile, email, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | docker |
| opsec | passive |
| human-in-loop | yes |
