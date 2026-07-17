---
id: google-hacking-database
name: Google Hacking Database
description: Use when you want proven, categorized Google dork queries to find exposed files, cameras, logins, and data — returns a searchable library of curated dorks you adapt to your target.
url: https://www.exploit-db.com/google-hacking-database
category: search-engines
path:
- search-engines
- search-engine-guides
bestFor: Looking up battle-tested Google dork templates by category to surface exposed content.
selectorsIn:
- domain
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free public database maintained by OffSec (Exploit-DB). No account required to browse or copy dorks.
opsec: passive
opsecNote: Browsing the GHDB is passive. Running a dork executes a normal Google search — Google logs your IP/query, and hitting sensitive resources you find could itself be logged by that resource. Only view exposed data you're authorized to; use a VPN/sock-puppet for the searching.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by OffSec as part of Exploit-DB, a long-standing, reputable security resource; the dorks are community-submitted but curated.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- exploit-db
- dorksearch-com
aliases:
- GHDB
- Google Hacking Database
tags:
- google-dorks
- search-operators
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# Google Hacking Database

> The GHDB — OffSec's curated, categorized library of proven Google dorks for surfacing exposed files, directories, login portals, cameras, and leaked data.

## When to use
You want ready-made, field-tested dork templates rather than composing operators from scratch. Given a `domain`, `name`, or keyword, browse the GHDB's categories (Files Containing Juicy Info, Sensitive Directories, Login Pages, Files Containing Passwords, etc.), copy a relevant dork, and adapt it with `site:` or your target term. It's the reference companion to any dork-building workflow — the place proven patterns are collected and described.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.exploit-db.com/google-hacking-database.
2. Browse or search by category/keyword to find a dork matching your goal (exposed documents, directory listings, config files, exposed devices).
3. Copy the dork and tailor it — add `site:targetdomain.com`, swap in the subject's `name`/keyword, or narrow `filetype:`.
4. Run it on Google and review results; only access data you're authorized to view.
5. Pivot: exposed documents (`document-id`) → download/metadata analysis; exposed profiles/pages → the relevant selector tools.

## Inputs → Outputs
- **In:** a category/keyword to find a dork; then a `domain`/`name` to target when you run it
- **Out:** a curated dork template, and (once run on Google) links to exposed documents/pages (`document-id`)
- **Empty/negative result looks like:** the GHDB category has no matching dork, or the adapted dork returns nothing on Google — the exposure isn't indexed. Loosen the dork or try a different category.

## Gotchas & OpSec
- The GHDB is a **reference**, not a scanner — it lists dorks; you still run them on Google, subject to Google's CAPTCHA/rate limits.
- Some listed dorks are old and no longer productive as sites patch exposures; treat them as starting points.
- Legal/ethical line: dorking only finds already-public content, but *accessing* exposed sensitive data can cross into unauthorized access. Stay within scope.
- OpSec: **passive** to browse; running dorks is a logged Google search.

## Overlaps ("do both")
- Pairs with [[dorksearch-com]] (interactive dork builder) and [[exploit-db]] (the broader Exploit-DB it lives in) — GHDB supplies the proven patterns, a builder helps you assemble variants.

## Trust & verifiability
`trust: trusted` — a curated, long-running OffSec resource; individual dorks are community-submitted, so verify each still works by running it, but the database itself is authoritative and well-maintained.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-hacking-database |
| category | search-engines |
| selectorsIn → selectorsOut | domain → document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
