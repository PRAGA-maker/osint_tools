---
id: zehef
name: ZEHEF
description: Use when you have an `email` and want an automated passive OSINT sweep on it — returns paste-site and breach hits, discovered social accounts, and generated address variations, all from a local CLI.
url: https://github.com/N0rz3/Zehef
category: email
path:
- email
bestFor: One-command local email recon — breaches, paste mentions, and social-account discovery for an address.
selectorsIn:
- email
selectorsOut:
- email
- social-profile
status: live
pricing: free
costNote: Free and open-source (GPL-3.0); local Python install, no account or API key required for core checks.
opsec: passive
opsecNote: Passive — it queries public sources (paste sites, HudsonRock, platform signup checks) about the address, not the subject. Checks originate from YOUR IP, so run behind a VPN/proxy for a clean footprint; nothing is sent to the address owner.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A community open-source tool (~1k GitHub stars) by N0rz3; the author notes it is in development and some checks may break as upstream sites change.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Zehef
- N0rz3/Zehef
tags:
- Emails
- email-osint
- cli
source: cyb-detective
lastVerified: '2026-07-10'
enrichment: full
---

# ZEHEF

> An open-source Python CLI that runs a passive OSINT sweep on a single `email` — checking pastes and breaches, discovering linked social accounts, and generating plausible address variations.

## When to use
You have an `email` and want to automate the routine first-pass checks (breach exposure, paste-site mentions, which platforms the address has accounts on) in one command, on your own machine, without feeding the address to a hosted web service. It's the CLI counterpart to hosted email tools like `[[google-account-finder-epieos]]`, good when you want local control and reproducibility.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `git clone https://github.com/N0rz3/Zehef`, then `pip install -r requirements.txt` (needs Python 3.10+).
2. Run: `python3 zehef.py target@example.com`.
3. Let it query its modules: HudsonRock breach/infostealer data, Pastebin/paste mentions, social-account existence checks (Instagram, Spotify, Adobe, X, etc.), and email-variation generation.
4. Read the console output: breach/paste hits and a list of platforms where the address appears registered (`social-profile`).
5. Pivot: confirmed accounts feed username enumeration (`[[snoop]]`); breach exposure feeds credential/leak context; email variations feed re-checks and existence oracles.

## Inputs → Outputs
- **In:** `email`
- **Out:** breach/infostealer exposure, paste-site mentions, discovered `social-profile`s, generated `email` variations
- **Empty/negative result looks like:** modules return no hits (address not in breaches/pastes, no matched accounts). Because it's in development, some empty results may be a broken module rather than a true negative — sanity-check against a second tool.

## Gotchas & OpSec
- Requires local install (Python CLI) — not a click-and-go site.
- The author flags it as in-development: individual checks break when upstream sites change their signup/APIs, producing false negatives. Corroborate misses.
- Requests come from your IP to many platforms — use a VPN/proxy for OpSec.
- Account-existence checks (Holehe-style) are inherently noisy; treat each hit as a lead to confirm.

## Overlaps ("do both")
- Pairs with hosted email OSINT `[[google-account-finder-epieos]]` and deliverability check `[[emailhippo-2]]` — run local + hosted for coverage.
- Feed discovered accounts into `[[snoop]]`/`[[gaddr]]` and breach context into leak databases.

## Trust & verifiability
`trust: community` — a useful open-source utility, but community-maintained and explicitly in development, so module reliability varies. Verify both hits (open the profile) and misses (a null may be a broken check) against independent tools before drawing conclusions.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | zehef |
| category | email |
| selectorsIn → selectorsOut | email → email, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
