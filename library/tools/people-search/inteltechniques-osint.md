---
id: inteltechniques-osint
name: IntelTechniques OSINT Search Tools
description: Use when you have a `name`, `username`, `email`, `phone` or `domain` and want automated multi-source pivots — a free toolset that fires one selector at dozens of search sources at once.
url: https://inteltechniques.com/tools/
category: people-search
path:
- people-search
bestFor: Automating multi-engine OSINT searches for a single selector (person, username, email, phone, domain) from one page.
selectorsIn:
- name
- username
- email
- phone
- domain
selectorsOut:
- social-profile
- address
- phone
- email
status: live
pricing: free
costNote: The online search tools are free to use; they accompany Michael Bazzell & Jason Edison's paid "OSINT Techniques" book, but the web tools themselves cost nothing.
opsec: passive
opsecNote: The tools are query-builders — they open searches on third-party engines (Google, social sites, brokers) in your browser. Each opened search reaches that destination with your fingerprint; run in a sock-puppet browser. IntelTechniques itself does not store your target or notify anyone.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by Michael Bazzell (IntelTechniques), a widely respected OSINT practitioner; the tools are actively updated (2024/2025 revisions) and are a de-facto standard reference in the field.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- IntelTechniques
- Bazzell OSINT tools
- inteltechniques search tool
tags:
- osint-toolkit
- query-builder
- pivot
- people-search
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# IntelTechniques OSINT Search Tools

> Michael Bazzell's automated OSINT query-builder: type one selector and launch it against dozens of search sources — the field's go-to pivot console.

## When to use
You have a single selector — a `name`, `username`, `email`, `phone`, `domain`, IP, or image — and want to run it comprehensively across many engines and databases without hand-typing each query. Ideal as the hub of an investigation: it turns one datum into a fan-out of searches (social, breach, broker, government, reverse-image) and standardises the pivots so you don't miss a source.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://inteltechniques.com/tools/ in a sock-puppet browser.
2. Choose the tool matching your selector: Person, Username, Email, Telephone, Domain, IP, Images, etc.
3. Enter the selector once.
4. Fire individual sources or "submit all" to open each search (results open on the destination engines).
5. Work the returned pages — the tool routes you; the data lives on the destinations. Confirm and cross-check each hit.
6. Pivot: any result becomes a new selector to feed back into the relevant IntelTechniques tool, iterating the fan-out.

## Inputs → Outputs
- **In:** `name`, `username`, `email`, `phone`, `domain` (also IP, image)
- **Out:** routed searches surfacing `social-profile`s, `address`/`phone`/`email` records, breach and broker hits — aggregated by your own review
- **Empty/negative result looks like:** the tool always launches; "empty" means the destination engines returned nothing. Some destinations may have changed/blocked queries since the tool's last update — check the source directly if a link misfires.

## Gotchas & OpSec
- It's a **query-builder, not a database** — it holds no data and cites no results itself; every hit belongs to a destination you must evaluate.
- Destinations drift: sites change URLs/APIs, so occasional links break between updates — the toolset is actively maintained but not instantaneously.
- OpSec: **passive** to the subject, but each launched search hits a third party with your fingerprint — always use a sock-puppet browser/IP.

## Overlaps ("do both")
- It is the overlap hub for username/email/phone/people tools in this library — it will route you to many of them (`[[user-searcher]]`, reverse-image, breach checks). Use it to ensure full source coverage, then deep-dive the specific tools it surfaces.

## Trust & verifiability
`trust: trusted` — authored and maintained by a leading OSINT practitioner and used industry-wide. The tools are reliable routers; verifiability rests on the destination sources they open, which you should assess individually.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | inteltechniques-osint |
| category | people-search |
| selectorsIn → selectorsOut | name, username, email, phone, domain → social-profile, address, phone, email |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
