---
id: one-liner-osint
name: One-Liner-OSINT
description: Use when you have a `domain`, `ip-address`, `email`, or `username` and want ready-made shell one-liners to enumerate it fast — returns copy-paste recon commands producing more selectors.
url: https://github.com/yogsec/One-Liner-OSINT
category: search-engines
path:
- search-engines
bestFor: Copy-paste shell one-liners for quick domain/IP/email/username recon.
selectorsIn:
- domain
- ip-address
- email
- username
selectorsOut:
- domain
- ip-address
- email
status: live
pricing: free
costNote: Free open-source GitHub repo (MIT); the one-liners are free, though some invoke services with their own quotas/keys.
opsec: active
opsecNote: The commands themselves are just text, but RUNNING them can be active — subfinder/amass/curl against a target's infrastructure touches their servers or third-party APIs and can be logged. Read each one-liner before running it; route active recon through a VPN/sock-puppet and never run commands you don't understand.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A community-maintained cheat-sheet repo (yogsec); commands are user-contributed — audit each before running rather than trusting blindly.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- osint-tools-yogsec
- yogsec
aliases:
- One-Liner-OSINT
- yogsec one-liners
tags:
- one-liners
- reference
- cheatsheet
- recon
source: gh-topic-osint-framework
lastVerified: '2026-07-23'
enrichment: full
---

# One-Liner-OSINT

> A curated cheat-sheet of copy-paste shell one-liners for OSINT recon — the fast path from one selector (domain, IP, email, username) to a pile of new ones.

## When to use
You have a `domain`, `ip-address`, `email`, or `username` and want to enumerate it quickly without wiring up a full toolchain — subdomains, DNS/infra, exposed endpoints, breach hits, EXIF, social scraping. The repo groups ready-made one-liners by goal (personal data, org infrastructure, breaches, social media, metadata) so you can grab the exact command for the pivot you need.

## How to use it (`bestInteractionPattern`: cli)
1. Open https://github.com/yogsec/One-Liner-OSINT and browse the categorised sections.
2. Find the one-liner matching your selector and goal (e.g. subdomain enumeration for a `domain`, breach lookup for an `email`).
3. **Read it before running** — understand what tool/API it calls and whether it touches the target directly. Install any required tool (subfinder, amass, exiftool, etc.).
4. Run it (route active recon through a VPN/sock-puppet), then feed the emitted selectors — new `domain`s, `ip-address`es, `email`s — into your next step.
5. Pivot: results chain into WHOIS, passive DNS, Shodan, and breach-lookup tools.

## Inputs → Outputs
- **In:** `domain`, `ip-address`, `email`, or `username`
- **Out:** enumerated `domain`s, `ip-address`es, `email`s and other recon artefacts (depending on the one-liner)
- **Empty/negative result looks like:** a command returns nothing — the selector has no exposed footprint for that technique, or a required API key/tool is missing.

## Gotchas & OpSec
- These are commands, not a hosted tool — you supply the environment, tools, and any API keys, and you own the consequences of running them.
- Some one-liners are actively intrusive (direct enumeration of a target's infrastructure). Audit each; assume active unless you confirm it only hits third-party/passive sources.
- Community-contributed — a stale or wrong one-liner can waste time or hit the wrong host; verify before trusting.

## Overlaps ("do both")
- Pairs with `[[osint-tools-yogsec]]` and `[[yogsec]]` — the same author's fuller tool collections; use the one-liners for quick throwaway recon and the tools for repeatable workflows.

## Trust & verifiability
`trust: community` — an open, community-maintained cheat-sheet; the commands are transparent (you can read every one) but unvetted, so audit each before execution.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | one-liner-osint |
| category | search-engines |
| selectorsIn → selectorsOut | domain, ip-address, email, username → domain, ip-address, email |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
