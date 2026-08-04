---
id: profounder
name: Profounder
description: Use when you have a `username`/nickname and want to hunt for accounts and harvest URLs from a page — returns candidate profiles and scraped links.
url: https://github.com/d8rkmind/Profounder
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Scripted username hunting across sites plus URL scraping from a given page, as a lightweight enumeration helper.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free open-source script on GitHub; run it yourself. No account.
opsec: active
opsecNote: It queries sites for the username and fetches pages — that traffic hits the target platforms. Route through a sock-puppet IP, do not authenticate, and read the script before running.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: A personal open-source project (d8rkmind); auditable but unsupported — verify results manually, as username-hunting scripts produce false positives.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- pyosint
aliases:
- d8rkmind Profounder
tags:
- Tools collections/toolkits
- username-enumeration
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# Profounder

> A small script that hunts a nickname across sites and scrapes URLs from a page — a lightweight username-enumeration and link-harvesting helper.

## When to use
You have a `username`/nickname and want a quick scripted sweep for accounts that use it, or you want to pull all links out of a page you are examining. It is a helper to widen the net; results always need manual confirmation.

## How to use it (`bestInteractionPattern`: cli)
1. Clone https://github.com/d8rkmind/Profounder and install its (Python) dependencies.
2. **Read the script** to confirm which sites/endpoints it queries.
3. Run it with the target `username` (or point its scraper at a URL) from a sock-puppet environment.
4. Manually verify each hit — matching a username string is not proof it is the same person — then pivot confirmed profiles into deeper account analysis.

## Inputs → Outputs
- **In:** a `username`/nickname (or a URL to scrape)
- **Out:** candidate `social-profile`s and scraped links
- **Empty/negative result looks like:** no hits (rare/unique nickname or changed site markers) — corroborate with a maintained username-search tool before concluding absence.

## Gotchas & OpSec
- Human-in-the-loop: none, but the project may be dated — site checks can break as platforms change.
- OpSec: **active** — the sweep touches target platforms; use a sock-puppet IP and never authenticate.
- Username matches are noisy — always verify identity manually.

## Overlaps ("do both")
- Overlaps with maintained username-search tools (Sherlock, WhatsMyName): those have larger, curated site lists; run one of them alongside Profounder and reconcile the hits.

## Trust & verifiability
`trust: unverified` — an unsupported personal script; treat its output as leads to verify, and audit the code before running.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | profounder |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
