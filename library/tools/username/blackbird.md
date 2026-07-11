---
id: blackbird
name: Blackbird
description: Use when you have a `username` or `email` and want to sweep 600+ sites for accounts under that identity — returns a list of matching `social-profile` URLs and optional AI profiling.
url: https://github.com/p1ngul1n0/blackbird
category: username
path:
- username
bestFor: Fast enumeration of accounts across 600+ platforms from a username or email.
selectorsIn:
- username
- email
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free and open-source (self-hosted CLI). Optional AI-profiling features may require your own LLM/API key.
opsec: active
opsecNote: Blackbird makes live requests to each of hundreds of platforms from your host to test account existence — that traffic originates from your IP and can be logged by target sites. Run behind a VPN/sock-puppet IP. It queries the target's username, not the target directly, so the subject is not personally notified.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular, actively maintained community project (~6.9k stars) leveraging the WhatsMyName dataset. Well-regarded but unaudited; false positives/negatives occur as sites change.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- blackbird osint
- p1ngul1n0/blackbird
tags:
- username-check
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Blackbird

> A fast, self-hosted username/email account-enumeration CLI that checks 600+ platforms in one run and can auto-generate a profile from what it finds.

## When to use
You have a `username` (or an `email`) and want to know everywhere that handle has an account — the classic "spread a handle across the internet" step. Blackbird is a Sherlock-style sweeper backed by the community WhatsMyName dataset, so it's a strong first move for turning a single handle into a map of `social-profile`s to investigate.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and install:
   ```
   git clone https://github.com/p1ngul1n0/blackbird.git
   cd blackbird
   pip install -r requirements.txt
   ```
2. Run against a username or email:
   ```
   python blackbird.py --username johndoe
   python blackbird.py --email johndoe@example.com
   ```
3. Read the output: a list of platforms where the identity was found, with profile URLs. Optionally generate an AI profile and export PDF/CSV reports.
4. Verify each hit manually — visit the profile to confirm it's the same person (handles collide).
5. Pivot: confirmed profiles feed name/photo enrichment; a recurring bio/photo across sites strengthens attribution.

## Inputs → Outputs
- **In:** `username` or `email`
- **Out:** list of `social-profile` URLs / platforms, matched `username`, optional AI profile, PDF/CSV report
- **Empty/negative result looks like:** few or no hits — either the handle is unused, is unique to one platform, or site checks broke. Common handles produce many false-positive collisions; rare handles are more reliable.

## Gotchas & OpSec
- False positives/negatives: platform checks drift as sites change their responses — always eyeball each hit.
- Handle collisions: a match under a common username may be a different person; corroborate with photo/bio.
- OpSec: **active** — hundreds of live requests leave your IP; run behind a VPN/sock-puppet network. Keep the site list updated so you're not testing dead endpoints.

## Overlaps ("do both")
- Pairs with other sweepers (Sherlock/WhatsMyName) and with `[[daprofiler]]` — run more than one enumerator because their site lists and detection logic differ, and each catches accounts the others miss.

## Trust & verifiability
`trust: community` — a widely used, actively maintained open-source tool, but unaudited and dependent on volatile site signatures; treat every hit as a lead to verify.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | blackbird |
| category | username |
| selectorsIn → selectorsOut | username, email → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
