---
id: pyba
name: PyBA (PyBrowserAutomation)
description: Use when a lookup needs repeatable browser steps and you have an `email`/`username`/`domain` to run — returns extracted data plus a reusable Playwright script.
url: https://github.com/fauvidoTechnologies/PyBrowserAutomation/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Turning a one-off "navigate this site and pull X" task into a repeatable, LLM-driven Playwright automation.
selectorsIn:
- username
- email
- domain
selectorsOut:
- social-profile
- associate
status: degraded
pricing: free
costNote: Free and open-source (MIT). No purchase; but it drives an LLM, so you supply your own API key/costs for the model provider you choose.
opsec: active
opsecNote: It actually visits target sites and can log in, so every action originates from your infrastructure and is attributable — route it through controlled proxies and sock-puppet accounts. Also note you're sending page content to an LLM provider; don't feed sensitive material to a third-party model you don't control.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: python-lib
trust: community
trustNote: A small, single-maintainer open-source project (~30 stars, pre-1.0, active development as of late 2025); promising but early — review the code and pin a version before operational use.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools: []
aliases:
- PyBA
- py-browser-automation
- PyBrowserAutomation
tags:
- automation
- browser-automation
- playwright
- llm
source: awesome-osint
lastVerified: '2026-08-05'
enrichment: full
---

# PyBA (PyBrowserAutomation)

> "Tell the AI what to do once, get a Python script you can run forever" — an LLM-guided browser agent that navigates a site for you and exports the session as a standalone Playwright script.

## When to use
You have a repeatable collection task — check a `username` across a set of sites, pull fields from profiles, walk a paginated listing — and you'd rather encode it once than click through by hand each time. PyBA drives a real browser with an LLM, extracts structured data (Pydantic models), and, crucially, exports a deterministic Playwright script you can rerun without the model. Good for scaling a proven manual workflow; overkill for a single lookup.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install from PyPI (`pip install`) or Homebrew per the repo README; pin the version (it's pre-1.0).
2. Configure an LLM provider (OpenAI / Google VertexAI / Gemini) with your own API key, and set up a browser profile behind your proxy.
3. Describe the task in natural language (e.g. "for each username, open the profile and extract display name, bio, and linked accounts"); pick an exploration mode (Normal/Step/DFS/BFS).
4. Run it against sock-puppet accounts; review the extracted data and the generated Playwright script.
5. Reuse the exported script for future runs without the LLM, and log results to SQLite/Postgres if you need an audit trail.

## Inputs → Outputs
- **In:** `username` / `email` / `domain` (whatever your scripted task consumes)
- **Out:** structured extracted data → `social-profile`, `associate` links, plus a reusable script
- **Empty/negative result looks like:** the agent fails to complete a step (site layout changed, bot-blocked, login challenge) or returns empty structured fields. Because it's early-stage, expect to iterate on the prompt and handle CAPTCHAs/logins manually.

## Gotchas & OpSec
- **Active + attributable:** it really visits and can log into sites — isolate network and identity as with any automation.
- **Third-party LLM exposure:** page content goes to your chosen model provider; don't send sensitive evidence to a model you don't control.
- Pre-1.0 and single-maintainer — read the code, pin a version, and don't assume stability.

## Overlaps ("do both")
- It's the automation layer beneath manual browser OSINT: prototype a lookup by hand, then have PyBA turn the proven steps into a repeatable Playwright script for scale. Pair it with your own sock-puppet infrastructure and capture tooling.

## Trust & verifiability
`trust: community` — an early, low-star open-source project; verify by reading the source, pinning a release, and confirming its extractions against the live pages before trusting the output.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | pyba |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username, email, domain → social-profile, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | python-lib |
| opsec | active |
| human-in-loop | yes (api-key) |
