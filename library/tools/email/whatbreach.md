---
id: whatbreach
name: WhatBreach
url: https://github.com/Ekultek/WhatBreach
category: email
path:
- email
description: Use when you have an `email` and want to know which data breaches it appears in — returns breach names, associated pastes and (with keys) downloadable dumps.
bestFor: Enumerating the data breaches and paste leaks tied to an email address from the command line.
selectorsIn:
- email
selectorsOut:
- email
- username
status: degraded
pricing: freemium
costNote: Open-source and free to run, but useful output depends on API keys — HaveIBeenPwned now needs a paid key (~$3.50/mo); some sources it was built against (WeLeakInfo, databases.today) are defunct.
opsec: passive
opsecNote: Querying breach indexes about an email does not contact or notify the owner — it is passive. Note you are sending the target's email to third-party APIs (HIBP, Hunter, emailrep), which log the query against your keys. Use dedicated keys/accounts for sensitive work.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: A genuine open-source OSINT CLI, but lightly maintained and built partly against data sources that have since been seized/shut down, so coverage is degraded versus its original scope.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: false
aliases:
- WhatBreach
- Ekultek/WhatBreach
tags:
- breach
- cli
- open-source
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# WhatBreach

> An open-source Python CLI that maps an email to the data breaches and paste leaks it appears in — useful, but partly degraded as several of its original data sources no longer exist.

## When to use
You have an `email` and want a quick breach footprint: which known breaches contain it, whether it shows up in pastes, and (with the right keys) the ability to pull associated dumps. Good for confirming an address is real and in active use, and for surfacing linked usernames/passwords-reuse leads. Because some backends are dead, treat it as one input alongside a live breach search, not the sole authority.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and install from GitHub (`pip install -r requirements.txt`).
2. Add API keys you have — HaveIBeenPwned (paid), Hunter.io (free), emailrep.io (open); skip defunct ones (WeLeakInfo, databases.today).
3. Run against a target: `python whatbreach.py -e target@example.com` (batch mode and throttling available).
4. Read the output: breach names, paste hits, and downloadable dump/paste references where sources are alive.
5. Pivot: breach-linked `username`s feed enumeration; confirmed exposure feeds `[[snusbase]]`/`[[account-live-com]]` and password-reuse hypotheses.

## Inputs → Outputs
- **In:** `email`
- **Out:** breach names, paste references, linked `username`/`email` artifacts
- **Empty/negative result looks like:** "no breaches found" — which now often reflects dead data sources or a missing HIBP key rather than a genuinely clean email. Cross-check with a live breach engine before concluding.

## Gotchas & OpSec
- **Degraded:** several original sources (WeLeakInfo, databases.today) are defunct; HIBP requires a paid key. Missing results may be tooling gaps, not clean addresses.
- Lightly maintained — expect occasional breakage against changed APIs.
- OpSec: passive toward the subject, but your API keys log the queries; use dedicated keys for sensitive traces.

## Overlaps ("do both")
- Pairs with `[[snusbase]]` and Have I Been Pwned directly — those provide live, maintained breach coverage that fills WhatBreach's dead-source gaps.

## Trust & verifiability
`trust: community` — legitimate, auditable open-source, but abandoned enough that coverage is partial; corroborate any breach claim against a currently-maintained source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whatbreach |
| category | email |
| selectorsIn → selectorsOut | email → email, username |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
