---
id: awesome-telegram-osint
name: Awesome Telegram OSINT
description: Use when you have a Telegram `username`/`phone` and need the right tool for it — a curated catalog of Telegram OSINT search engines, bots, directories and guides to pick from.
url: https://github.com/ItIsMeCall911/Awesome-Telegram-OSINT
category: messaging
path:
- messaging
bestFor: Finding the current tools, bots and channel directories to investigate Telegram users, groups and channels.
selectorsIn:
- username
- phone
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free open GitHub list; the individual tools/bots it links to have their own (varying) pricing and access terms.
opsec: passive
opsecNote: Reading the list is passive. The tools and especially the bots it points to are NOT — many require you to message a bot or query a service, which exposes your account/query. Vet each linked tool's OpSec before using it, and use sock-puppet accounts for any Telegram bot.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Well-maintained community catalog (2.8k+ stars). It's a reliable index, but it does not vouch for the linked tools — some third-party bots are sketchy, so judge each on its own merits.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Awesome Telegram OSINT list
tags:
- telegram
- awesome-list
- catalog
source: gh-topic-osint-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Awesome Telegram OSINT

> A curated index of Telegram-investigation tools — not a lookup itself, but the map you consult to find the current search engine, bot, or directory for the Telegram job in front of you.

## When to use
You're investigating a Telegram `username`, `phone`, group, or channel and need to know *which* tool to reach for — Telegram's tooling churns fast, and this list tracks the working search engines (Intelligence X, buzz.im), channel/group directories, resolver bots (username/phone → account), and technique guides in one place. Use it as a starting index whenever a Telegram lead needs a specialised tool you don't already have.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://github.com/ItIsMeCall911/Awesome-Telegram-OSINT.
2. Jump to the relevant section: Search Engines, Directories & Catalogues, Tools, Bots, or Educational Resources.
3. Pick a tool matching your selector — e.g. a resolver bot for `username`→account or `phone`→account, a directory to find channels by topic, or a search engine to find messages mentioning a term.
4. **Vet before you use:** open the linked tool, check whether it's still live, what it costs, and what it exposes about you.
5. Run the chosen tool under a sock-puppet Telegram account; feed results (`social-profile`, group membership) into your wider investigation.

## Inputs → Outputs
- **In:** a Telegram lead (`username`, `phone`, group/channel, or keyword) and the need for a matching tool
- **Out:** links to Telegram OSINT tools/bots/directories to run → ultimately `social-profile`/membership data from those tools
- **Empty/negative result looks like:** the list is comprehensive, so the "miss" is downstream — a linked tool may be dead, paywalled, or scammy. Treat every entry as a candidate to verify, not an endorsement.

## Gotchas & OpSec
- It's an **index, not a tool** — the actual OpSec risk lives in the bots/services it links to. Many Telegram resolver bots log your queries or require you to expose your account; always use a sock puppet.
- Links rot and tools change hands; check each entry is current before relying on it.
- Inclusion is not vetting — some third-party Telegram bots are dubious or outright malicious. Judge each independently.

## Overlaps ("do both")
- Use it alongside dedicated Telegram tools already in this library and general people/username search: the list points you to the specialised Telegram resolver, while your standard username/phone tools corroborate whatever it returns.

## Trust & verifiability
`trust: community` — a reputable, actively maintained catalog; trustworthy as an index, but it makes no guarantees about the linked tools, so verify the liveness, cost, and safety of any tool before acting on its output.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | awesome-telegram-osint |
| category | messaging |
| selectorsIn → selectorsOut | username, phone → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
