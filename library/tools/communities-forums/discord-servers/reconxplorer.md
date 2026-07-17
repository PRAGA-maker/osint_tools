---
id: reconxplorer
name: ReconXplorer
description: Use when you have an `ip-address`, `email`, `phone`, `username` or Discord ID and want quick multi-source recon from one menu-driven CLI — returns `geolocation`, breach/`social-profile` hints and Discord metadata.
url: https://github.com/root7am/ReconXplorer
category: communities-forums
path:
- communities-forums
- discord-servers
bestFor: A menu-driven Python toolkit that runs IP/email/phone/username and Discord (token/server/webhook) lookups from one place.
selectorsIn:
- ip-address
- email
- phone
- username
selectorsOut:
- geolocation
- email
- social-profile
- ip-address
status: live
pricing: free
costNote: Free, open-source (Python). Local install; some modules call third-party APIs that may need their own keys/limits.
opsec: active
opsecNote: Modules make direct queries from your machine to external services (IP geo, breach APIs, Discord). Those services see your IP and may log/rate-limit you; the Discord token/webhook modules touch Discord infrastructure. Run from a research VM/VPN, never feed it credentials you can't burn, and only test Discord tokens/webhooks you're authorised to.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: Small single-author toolkit (~50 stars); it bundles third-party lookups of varying reliability — inspect the source before running and verify every result.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- root7am/ReconXplorer
tags:
- recon
- discord
- multi-input
- cli
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# ReconXplorer

> A menu-driven Python recon toolkit that batches common lookups — IP, email, phone, username, plus Discord token/server/webhook checks — behind one interface.

## When to use
You want to run a quick first-pass across several selectors without stringing together a dozen separate tools. ReconXplorer wraps IP geolocation/ISP, email breach/domain/social checks, phone carrier/location, Instagram profile stats, and URL scanning into one menu, and adds Discord-specific modules (validate/decode a token, pull server metadata, analyse a webhook). It's a convenience aggregator for triage — useful early to see which selectors light up, then confirm findings in dedicated, more authoritative tools.

## How to use it (`bestInteractionPattern`: cli)
1. Clone: `git clone https://github.com/root7am/ReconXplorer`.
2. Install deps (`pip install -r requirements.txt`, or the bundled `install.bat` on Windows) and run `python main.py` (or `run.bat`).
3. From the menu, pick a module and enter the selector (IP, email, phone, username, Discord ID/token/webhook).
4. Read the aggregated output; note which lookups returned real data versus empty/generic responses.
5. **Verify** anything actionable in a purpose-built tool — the wrapped sources vary in quality.
6. Pivot: an IP's `geolocation` feeds mapping; an email's breach/social hits feed account-existence tools; a username feeds cross-platform search.

## Inputs → Outputs
- **In:** `ip-address`, `email`, `phone`, `username`, or Discord token/server/webhook ID
- **Out:** `geolocation`/ISP, breach + `social-profile` hints, phone carrier/location, Discord account/server metadata (and the input `ip-address` resolution)
- **Empty/negative result looks like:** modules returning generic "not found"/API-error responses — often means a wrapped free API is rate-limited, deprecated, or needs a key, not that the target is clean. Re-check in a dedicated tool.

## Gotchas & OpSec
- **Active:** every module queries external services from your host — use a VM/VPN; assume those services log you.
- Bundled third-party lookups age fast (APIs change/die); expect some modules to be broken and treat all output as unverified.
- Discord token/webhook features are sensitive — only use against assets you're authorised to test; never paste tokens you don't control.
- Read `main.py` before running any downloaded recon tool.

## Overlaps ("do both")
- Overlaps with many single-purpose tools in this library (IP geo, email breach, username search, Discord lookups). Use ReconXplorer for fast triage, then the dedicated tool for authoritative confirmation of any hit.

## Trust & verifiability
`trust: unverified` — a small single-author toolkit aggregating third-party lookups of mixed reliability. It's a legitimate convenience wrapper, but inspect the code, expect broken modules, and verify every finding in a primary source before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reconxplorer |
| category | communities-forums |
| selectorsIn → selectorsOut | ip-address, email, phone, username → geolocation, email, social-profile, ip-address |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
