---
id: aware-online-com
name: Aware-online.com
description: Use when you have a `name`, `username`, `email`, `phone`, or `image` and want ready-made query builders that generate targeted search/social URLs — returns `social-profile` and `domain` leads.
url: https://www.aware-online.com/en/osint-tools
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Free browser-based query builders that assemble effective search and social-media URLs from a selector.
selectorsIn:
- name
- username
- email
- phone
- image
selectorsOut:
- social-profile
- domain
status: live
pricing: free
costNote: All the custom OSINT tools on the site are free; the paid product is their separate training academy.
opsec: passive
opsecNote: The tools build search URLs client-side. Aware-Online explicitly notes you can enter fake data, then edit the generated URL, so nothing sensitive is stored on their site. You only touch the target platform when you actually open a generated link — do that from a sock-puppet browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Maintained by Aware Online Academy, an established OSINT training provider in the Netherlands; the tools are curated URL builders rather than data sources.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Aware Online OSINT tools
- aware-online osint
tags:
- other-resources
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# Aware-online.com

> A free hub of purpose-built OSINT query builders — feed it a selector and it assembles the right search/social-media URL for you.

## When to use
You have a `name`, `username`, `email`, `phone`, or `image` and want a fast, guided way to construct effective searches on Google, Facebook, Twitter/X, Instagram, YouTube, Reddit, reverse-image engines, and more — without memorizing every advanced-search syntax. Good early in an investigation when you want breadth across many platforms from a single input.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.aware-online.com/en/osint-tools and pick the category matching your selector (People, Usernames, Email, Phone, Images, Social media, Geolocation, etc.).
2. Type the selector into the tool's field (or deliberately enter placeholder data if you're privacy-cautious).
3. Click through — it opens (or gives you) the constructed query URL on the target platform.
4. If you entered placeholder data, edit the real value directly into the generated URL in your own browser so it never leaves your machine.
5. Pivot: open results in a sock-puppet session; feed discovered `social-profile`/`domain` links into enrichment tools.

## Inputs → Outputs
- **In:** `name`, `username`, `email`, `phone`, or `image`
- **Out:** `social-profile`, `domain` (targeted search/query URLs, not a data dump)
- **Empty/negative result looks like:** the generated search opens on the target platform with zero hits — the tool always builds a valid URL, so "empty" means the platform itself found nothing.

## Gotchas & OpSec
- This is a **query builder**, not a database — it never returns records itself, only better-aimed searches. Judge results on the destination platform.
- OpSec is **passive** for the URL construction; the actual leak happens when you open the link, so use a clean browser/IP.
- Platform search parameters drift, so an occasional builder may produce a stale URL — sanity-check the query it generated.

## Overlaps ("do both")
- Pairs with dedicated username tools like `[[whatsmyname]]` and reverse-image engines; Aware-Online orients you quickly across platforms, then a specialist tool goes deep on the best hit.

## Trust & verifiability
`trust: community` — run by a reputable OSINT training academy, but the tools only build queries, so verify every result on the platform it points you to.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | aware-online-com |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | name, username, email, phone, image → social-profile, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
