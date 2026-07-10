---
id: seekr
name: Seekr
description: Use when you have a `username`, `name`, `email` or `phone` and want an all-in-one investigation workspace — returns account discovery, tool recommendations and organized notes.
url: https://github.com/seekr-osint/seekr
category: username
path:
- username
bestFor: A self-hosted OSINT toolkit that combines account discovery, a target database and note-taking in one web interface, with no API keys needed.
selectorsIn:
- username
- name
- email
- phone
selectorsOut:
- social-profile
- email
- associate
status: live
pricing: free
costNote: Free and open-source; runs locally (Windows/Linux/Docker/NixOS). No API keys required for any feature.
opsec: passive
opsecNote: Runs on your own machine, so investigation data and notes stay local rather than in a third-party service. Its account-discovery checks reach out to platforms from your IP — use a proxy/sock-puppet network for sensitive work.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Open-source project (seekr-osint) with an active GitHub presence. It integrates known tools (e.g. phoneinfoga); results are only as good as those underlying checks, so verify hits.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- socialscan
aliases:
- seekr-osint
tags:
- username-check
- osint-toolkit
- self-hosted
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# Seekr

> A self-hosted OSINT workbench: account discovery, a target database, and note-taking behind one sleek local web UI — no API keys, nothing leaves your machine.

## When to use
You want to run a person-focused investigation and *organize* it, not just fire a single lookup. Seekr combines account discovery (does this username/handle exist across platforms), a structured database of targets ("account cards"), a GitHub-to-email lookup, phone intel via integrated phoneinfoga, and a guide that recommends which web tools to use next — all in one self-hosted interface where your notes and findings stay local. Good as the hub you drive an investigation from.

## How to use it (`bestInteractionPattern`: web-manual)
1. Install: download the release binary (Windows/Linux), pull the Docker image, or build from source (Go + TypeScript). No API keys needed.
2. Launch it and open the local web interface in your browser.
3. Create a target and add what you have — `username`, `name`, `email`, `phone` — into the account/database cards.
4. Run account discovery and the integrated tools (e.g. phoneinfoga for a number); use the Guide for recommended next tools.
5. Record findings in the built-in notes; export when done. Pivot: discovered accounts/emails feed platform-specific tools and `[[socialscan]]`.

## Inputs → Outputs
- **In:** `username`, `name`, `email`, or `phone`
- **Out:** discovered `social-profile`s, `email` (e.g. GitHub-to-email), `associate` links, and organized case notes
- **Empty/negative result looks like:** account discovery returns no hits, or an integrated tool errors. Because it wraps other tools, a null result reflects those underlying checks — cross-check important negatives with a dedicated tool.

## Gotchas & OpSec
- Requires local install/hosting — more setup than a web tool, but keeps data private.
- It orchestrates *other* tools; its accuracy inherits their limitations (and their breakage when platforms change).
- Account-discovery requests originate from your IP — proxy them for sensitive targets.
- OpSec: data stays local (a plus); outbound checks are not anonymous by default.

## Overlaps ("do both")
- Pairs with `[[socialscan]]` — Seekr is the organizing workspace and multi-tool hub; socialscan gives high-accuracy endpoint-based username/email existence you can feed into Seekr's account cards.

## Trust & verifiability
`trust: community` — an open-source, actively-developed toolkit. It integrates reputable tools but is only as reliable as they are, so treat discovered accounts/emails as leads and confirm each at the source before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | seekr |
</content>
