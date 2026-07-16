---
id: osint-tactical
name: OSINT Tactical (C3n7ral051nt4g3ncy)
description: Use when you have a `username`, Mastodon handle, or domain and want purpose-built recon tools — returns the developer's OSINT toolset (username enumeration, Mastodon intel, web recon).
url: https://github.com/C3n7ral051nt4g3ncy
category: social-networks
path:
- social-networks
bestFor: A prolific OSINT developer's GitHub with tools for username enumeration, Mastodon intelligence, and web reconnaissance.
selectorsIn:
- username
- name
- domain
selectorsOut:
- social-profile
- name
- email
status: live
pricing: free
costNote: Free open-source repositories on GitHub; some tools are also on PyPI.
opsec: passive
opsecNote: Browsing the GitHub profile is passive. The tools you run from it vary — username enumerators and Mastodon scrapers make requests that hit target platforms; run them from a sock-puppet environment and review each tool's behavior before pointing it at a live subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Maintained by C3n7ral051nt4g3ncy / "OSINT Tactical," a recognized OSINT practitioner (1k+ followers, CTF participant); open-source code is inspectable, though as with any third-party tool, review before running.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- whatsmyname
- sherlock
- masto-python
- curl-for-osint
- masto
- prot1ntelligence
- webosint
- whatsmyname-python
aliases:
- OSINT Tactical
- C3n7ral051nt4g3ncy
- Central Intelligence Agency OSINT
tags:
- mastodon
- Mastodon Related Sites
- username-enumeration
- toolmaker
source: uk-osint
lastVerified: '2026-07-15'
enrichment: full
---

# OSINT Tactical (C3n7ral051nt4g3ncy)

> The GitHub home of a busy OSINT toolmaker — username-recon, Mastodon intelligence, and web-recon utilities you can clone and run.

## When to use
You're holding a `username`, a Mastodon handle, or a `domain` and want purpose-built tooling rather than a web form. This profile hosts several actively useful tools — most notably username enumeration across platforms and Mastodon user/instance intelligence — that fit into a CLI/Python workflow.

## How to use it (`bestInteractionPattern`: cli)
1. Open https://github.com/C3n7ral051nt4g3ncy and scan the pinned/most-starred repos.
2. Pick the tool for your selector:
   - **HandleHawk** / **WhatsMyName-Python** — enumerate a `username` across many sites.
   - **Masto** (also on PyPI) and the **Masto Maltego Transform** — gather intelligence on Mastodon users and instances.
   - **WebOSINT (W3b0s1nt)** — Python web reconnaissance on a `domain`.
3. Clone the repo, install dependencies, and run per its README (most are Python CLIs).
4. Feed your selector and collect the output (found profiles, Mastodon metadata, web-recon findings).
5. Pivot: enumerated `social-profile`s feed cross-platform verification; Mastodon findings feed the `[[mastodon-github-com]]` account-lookup step; web-recon feeds domain/infra tools.

## Inputs → Outputs
- **In:** `username`, `name`, Mastodon handle, or `domain`.
- **Out:** discovered `social-profile`s across platforms, Mastodon user/instance metadata, and web-recon results (subdomains, `email`s, exposed assets).
- **Empty/negative result looks like:** a tool returns no hits — the username isn't registered on the checked sites, or a scraper is rate-limited/blocked. Re-run with updated site lists or from a different IP before concluding.

## Gotchas & OpSec
- These are self-hosted CLI tools: you must install and run them, and you are responsible for reviewing the code before running (standard for any third-party OSINT tool).
- Username enumerators produce false positives (a profile page that exists but isn't your subject) — verify each hit manually.
- Scrapers hitting Mastodon instances or many sites can be rate-limited or trip abuse detection; pace requests and use a sock-puppet environment.

## Overlaps ("do both")
- Pairs with `[[whatsmyname]]` and `[[sherlock]]` — this profile's HandleHawk/WhatsMyName-Python cover similar username-enumeration ground; run more than one because each carries a different site list. Its Masto tools pair with `[[mastodon-github-com]]` for the lookup step.

## Trust & verifiability
`trust: community` — an established practitioner's open-source toolkit. The code is public and inspectable, which is the basis for trust; still review any tool before running it and verify each tool's findings independently.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-tactical |
| category | social-networks |
| selectorsIn → selectorsOut | username, name, domain → social-profile, name, email |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
