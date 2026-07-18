---
id: karus
name: karus
description: Use when you have a gaming/dev `username` (Roblox, Steam, Minecraft, GitHub) and want to pull profile data across those platforms from one web UI — returns `social-profile`, `email`, `associate`.
url: https://github.com/phishontop/karus
category: people-search
path:
- people-search
bestFor: Self-hosted web-UI SOCMINT lookups across gaming and developer platforms from a single interface.
selectorsIn:
- username
- email
- domain
selectorsOut:
- social-profile
- email
- associate
status: live
pricing: free
costNote: Free and open-source (MIT-style GitHub project); you host it yourself, so the only cost is your own compute.
opsec: active
opsecNote: Runs on your machine and queries each target platform directly, so those platforms see YOUR IP. Route through a VPN/sock-puppet infrastructure; some modules may hit third-party APIs whose terms you should check.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: python-lib
trust: community
trustNote: Small single-author GitHub project (~tens of stars); functional but unaudited — verify each module and pin the commit you run.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- phishontop/karus
tags:
- web-ui
- multi-tool
- socmint
- self-hosted
source: gh-topic-osint-framework
lastVerified: '2026-07-18'
enrichment: full
---

# karus

> A self-hosted "Swiss-army-knife" SOCMINT web app — point it at a gaming/dev `username` and it fans out across Roblox, Steam, Minecraft, and GitHub from one interface.

## When to use
You have a `username` (or email/domain) and your subject's footprint is on gaming or developer platforms rather than mainstream social media. karus bundles several backend modules — including bloxsint (Roblox) functionality plus Steam, Minecraft, and GitHub — behind a local web UI, so you can check them together instead of visiting each site. Best for younger subjects or hobbyist/dev personas where Roblox/Steam/GitHub handles are the strongest leads.

## How to use it (`bestInteractionPattern`: python-lib)
1. Clone and install:
   ```
   git clone https://github.com/phishontop/karus
   cd karus
   pip install -r requirements.txt
   ```
2. Run the app: `python app.py` — it serves a local web UI on port 58533 (open `http://localhost:58533`).
3. Enter the target `username` (or email/domain) and select the modules to run.
4. Read the output: matched profiles per platform (account age, linked handles, public activity). Some modules may need a free API key — supply it if prompted.
5. Pivot: a confirmed handle on one platform feeds cross-platform username tools; linked friends/followers are `associate` leads.

## Inputs → Outputs
- **In:** `username`, `email`, or `domain`
- **Out:** `social-profile` (per-platform accounts), `email`, `associate` (friends/linked accounts)
- **Empty/negative result looks like:** modules return "not found" across platforms — the handle isn't used there, or a platform changed its API and that module has broken (check the module still works).

## Gotchas & OpSec
- Human-in-the-loop: some modules require you to obtain and paste an API key; expect occasional breakage as target platforms change.
- OpSec: **active** — queries originate from your host and hit the platforms directly. Use a VPN/sock-puppet setup; don't run it from an attributable IP.
- Unaudited code: run in an isolated environment and read what each module does before pointing it at live targets.

## Overlaps ("do both")
- Pairs with general username-search tools — karus gives a one-screen multi-platform sweep (it incorporates bloxsint's Roblox lookups), while dedicated tools go deeper on a single site.

## Trust & verifiability
`trust: community` — a small, single-maintainer open-source project; useful as a convenience aggregator but not authoritative. Verify each module's results against the source platform and pin the commit you run.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | karus |
| category | people-search |
| selectorsIn → selectorsOut | username, email, domain → social-profile, email, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | python-lib |
| opsec | active |
| human-in-loop | yes (api-key) |
