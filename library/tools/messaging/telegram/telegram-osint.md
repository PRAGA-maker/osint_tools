---
id: telegram-osint
name: Telegram-OSINT (resource hub)
description: Use when you're starting a Telegram investigation and want a curated map of Telegram-specific tools and playbooks — returns pointers to the right tool for a given selector.
url: https://github.com/The-Osint-Toolbox/Telegram-OSINT
category: messaging
path:
- messaging
- telegram
bestFor: Orienting a Telegram investigation — a curated reference of Telegram OSINT tools, bots, and investigative workflows to pick from.
selectorsIn:
- username
- phone
selectorsOut:
- social-profile
- metadata-exif
status: live
pricing: free
costNote: Free, open GitHub reference repository; the tools it links have their own pricing/OpSec.
opsec: passive
opsecNote: Reading the repo is passive. OpSec depends entirely on which linked tools you then run — some (bots, member scrapers) are active and require a Telegram account; evaluate each on its own before use.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-curated resource list (The OSINT Toolbox), not a tool itself; useful as a directory, but each linked tool must be independently verified for currency and trust before you rely on it.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- telegram-finder
- creationdatebot
aliases:
- The-Osint-Toolbox/Telegram-OSINT
tags:
- telegram
- resource-hub
- playbook
source: arf-seed
lastVerified: '2026-07-10'
enrichment: full
---

# Telegram-OSINT (resource hub)

> A curated GitHub reference of Telegram-specific OSINT tools and workflows — not a single tool, but the map you consult to pick the right Telegram tool for the selector you hold.

## When to use
You're beginning (or stuck in) a Telegram investigation and want to know what tools and techniques exist — phone→account lookups, account-age estimators, group/channel member analysis, message search, and investigative methodology. Rather than a discrete function, this is an orientation resource: use it to choose the specific tool that matches your input (a username, a phone, a group link) and then go run that tool.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/The-Osint-Toolbox/Telegram-OSINT and skim its categories/README.
2. Match your current selector to a listed tool: e.g. a `phone` → a number-to-account resolver; an account → an age/creation estimator; a group → a member/analysis tool.
3. Before using any linked tool, verify it's still live and assess its OpSec (many Telegram bots are third-party and active).
4. Follow the repo's methodology notes for a structured Telegram workflow.
5. Pivot: for concrete steps, jump to `[[telegram-finder]]` (phone→account) and `[[creationdatebot]]` (account age), then group/channel analysis.

## Inputs → Outputs
- **In:** whatever you hold (`username`, `phone`, group link) — used to *select* a tool
- **Out:** pointers to Telegram tools that yield `social-profile`/`metadata-exif` (the linked tools produce the actual data)
- **Empty/negative result looks like:** the repo lists nothing for your exact need, or links have gone stale — treat it as a starting map, not an exhaustive/guaranteed-current index.

## Gotchas & OpSec
- It's a **directory, not a tool** — it produces no data itself; the value is in what it points you to.
- Curated lists **rot** — verify each linked tool is alive and safe before running it; some are risky third-party bots.
- OpSec: reading is passive; downstream tools vary from passive to active — assess individually.

## Overlaps ("do both")
- Use it to reach concrete tools like `[[telegram-finder]]` and `[[creationdatebot]]`; the hub orients, those execute. Consult the hub first, then run the specific tool.

## Trust & verifiability
`trust: community` — a helpful community-maintained index, but not authoritative and possibly out-of-date; independently verify any tool it links before relying on its output.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | telegram-osint |
| category | messaging |
| selectorsIn → selectorsOut | username, phone → social-profile, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
