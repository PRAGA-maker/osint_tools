---
id: wagscraper
name: WaGpScraper
description: Use when you have a `name`, topic, or `phone` and want to find public WhatsApp group invite links referencing it — returns working chat.whatsapp.com group links (with names/images) harvested via Google dorks.
url: https://github.com/riz4d/WaGpScraper
category: messaging
path:
- messaging
bestFor: Discovering public WhatsApp group invite links on a keyword via Google dorking, and validating which still work.
selectorsIn:
- name
- phone
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free and open-source (Python); no cost. Relies on Google search, which may rate-limit or CAPTCHA heavy automated querying.
opsec: passive
opsecNote: The scraping step queries Google, not WhatsApp, so it does not alert group members. But ACTUALLY JOINING a discovered group is active and exposes your number/identity — validate links passively and use a burner number if you must enter a group.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: cli
trust: community
trustNote: Small open-source GitHub project (~45 stars); code is short and inspectable, but it depends on Google's unofficial results and an aging `google` Python package, so reliability varies.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- WAGSCRAPER
- WaGpScraper
tags:
- whatsapp
- messaging
- dorking
source: gh-topic-osint-resources
lastVerified: '2026-07-19'
enrichment: full
---

# WaGpScraper

> A small Python tool that Google-dorks for public `chat.whatsapp.com` invite links on a keyword and returns the working ones with their group names/images — a way to find WhatsApp communities tied to a name, place, or interest.

## When to use
You want to find public WhatsApp groups connected to a subject or context — a `name`, an organisation, a locality, an interest, or even a `phone` number that has been posted publicly — because those groups can reveal associates, activity, or a place to observe. The tool automates the "site:chat.whatsapp.com <keyword>" dork and filters to invite links that still resolve.

## How to use it (`bestInteractionPattern`: cli)
1. Clone: `git clone https://github.com/riz4d/WaGpScraper` and `pip install -r requirements.txt`.
2. Run `python3 wagps.py` and supply your search keyword (a name, topic, phone, or place).
3. The script Google-dorks for `chat.whatsapp.com` links matching the keyword, checks which invites are still live, and prints working links with group names/images.
4. Review results in your browser (don't auto-join); assess each group's relevance from its name/image and the keyword context.
5. Pivot: a relevant group can be observed (with OpSec care) for member handles/numbers that feed phone- and username-OSINT tools.

## Inputs → Outputs
- **In:** `name` / topic / `phone` keyword
- **Out:** `social-profile`-style WhatsApp group invite links (name + image + working URL)
- **Empty/negative result looks like:** no links returned — often because Google rate-limited/blocked the query or the dork matched nothing; retry later or refine the keyword rather than assuming no groups exist.

## Gotchas & OpSec
- Human-in-the-loop: expect Google **rate-limiting/CAPTCHA** on repeated runs; pace queries or route through your own search session.
- OpSec: harvesting is **passive** (against Google). **Joining** a discovered group is active and leaks your WhatsApp number/profile to members — never join with a personal account; use a burner if entry is necessary.
- Dependency rot: it uses an unofficial `google` scraping package that breaks when Google changes result markup; if it returns nothing, run the dork manually in a browser as a fallback.

## Overlaps ("do both")
- Pairs with manual Google dorking and other WhatsApp/messaging-OSINT tools — the tool just automates a dork you can also run by hand; combine with phone-lookup tools to enrich numbers surfaced inside discovered groups.

## Trust & verifiability
`trust: community` — a compact, inspectable open-source script; its results are simply filtered Google hits you can reproduce with the same dork in a browser, so verification is trivial, but its reliance on scraping makes uptime inconsistent.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wagscraper |
| category | messaging |
| selectorsIn → selectorsOut | name, phone → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
