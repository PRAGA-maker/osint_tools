---
id: one-liner-osint-github-com
name: One Liner OSINT (github.com)
description: Use when you have a `name` (or email/phone/handle) and want ready-made Google-dork one-liners to surface profiles, leaks, and documents — returns social-profile and name leads.
url: https://github.com/yogsec/One-Liner-OSINT
category: search-engines
path:
- search-engines
bestFor: Copy-paste Google/search dorks for personal-info discovery — profiles, resumes, leaked emails, exposed documents — organized by selector.
selectorsIn:
- name
- email
- username
selectorsOut:
- name
- social-profile
- email
status: live
pricing: free
costNote: Free open-source GitHub reference (a README of dork strings); no account or payment.
opsec: passive
opsecNote: The repo itself is a static reference — reading it is passive. OpSec depends on where you RUN the dorks: run them logged-out in a sock-puppet browser/VPN so the queries aren't tied to you, and note that some dorks point at breach/leak sites whose pages may be logged or hostile.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-curated dork collection on GitHub; the operators (`site:`, `filetype:`, `intext:`) are standard and inspectable, but coverage/quality of any single dork varies.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- google-dorking
- intelligence-x
aliases:
- One-Liner-OSINT
- yogsec one-liner osint
tags:
- searchengines
- Search Engines
- google-dorks
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# One Liner OSINT (github.com)

> A curated GitHub README of copy-paste search-engine dorks, grouped by what you're hunting — people, emails, leaks, documents — so you don't have to hand-craft `site:`/`filetype:` queries.

## When to use
You have a `name`, `email`, `username`, or `phone` and want fast, structured Google/search-engine dorks to find associated profiles, resumes/CVs, leaked credentials, exposed documents, or geolocation/image traces. It is a recipe book, not a running tool: reach for it when you want proven query patterns to paste into a search engine rather than reinventing dork syntax each time.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the repo: https://github.com/yogsec/One-Liner-OSINT and jump to the section matching your selector (personal info, email/leaks, social profiles, documents, org recon).
2. Copy a one-liner and substitute the target's value (name, email, handle, domain) into the placeholder.
3. Run it in a **logged-out, sock-puppet** browser against Google (or another engine if Google blocks the operator).
4. Read results; iterate with adjacent dorks in the same section (e.g. try `filetype:pdf` and `filetype:xlsx` variants).
5. Pivot: profiles feed username/social tooling; leaked-email hits feed breach lookups like [[intelligence-x]].

## Inputs → Outputs
- **In:** `name`, `email`, `username` (whatever the chosen dork targets)
- **Out:** `social-profile` URLs, real-`name` corroboration, exposed `email`s/documents, image/geolocation leads
- **Empty/negative result looks like:** the search engine returns nothing or unrelated hits — a dork is only as good as the target's footprint; try a broader variant before concluding absence.

## Gotchas & OpSec
- Google increasingly throttles advanced-operator queries and may serve a CAPTCHA; rotate to Bing/DuckDuckGo/Yandex or slow down.
- Some dorks intentionally point at breach/paste/leak sites — those pages can be logged or hostile; visit via a sandbox/VPN and never authenticate.
- OpSec: reading the repo is passive; the risk is entirely in where and how you execute the dorks — keep them un-attributable.

## Overlaps ("do both")
- Pairs with general [[google-dorking]] technique guides (this repo is the ready-made catalog) and with [[intelligence-x]] for the leak/breach dorks, which surface data those search dorks only hint at.

## Trust & verifiability
`trust: community` — a community-maintained list of standard, inspectable search operators. Each dork is transparent (you can read exactly what it queries), but the *quality* of any result depends on the search engine and the target, so verify hits directly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | one-liner-osint-github-com |
| category | search-engines |
| selectorsIn → selectorsOut | name, email, username → name, social-profile, email |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
