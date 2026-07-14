---
id: forensicosint-com-3
name: Forensic OSINT — Username Search
description: Use when you have a `username` and want to enumerate matching accounts across 500+ sites with screenshot evidence capture — returns social-profile links.
url: https://www.forensicosint.com/free-tools/username-search
category: people-search
path:
- people-search
bestFor: Enumerating a single username across 500+ social/forum/gaming sites with automated screenshot and MHTML evidence preservation.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: The username search is free but requires creating a free Forensic OSINT account. Forensic OSINT also sells a paid browser-based evidence-capture product; this specific tool is the free tier.
opsec: passive
opsecNote: Checks are run against target sites to confirm account existence; you are not messaging the subject, but profile pages may be loaded. Sign up with a sock-puppet email, not a personal identity.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Reputable OSINT vendor (Forensic OSINT); the underlying detection is powered by the open-source WhatsMyName project, so the enumeration logic is transparent and community-maintained.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
relatedTools:
- whatsmyname
- sherlock
- namechk
aliases:
- ForensicOSINT username search
- Forensic OSINT WhatsMyName
tags:
- peoplesearch
- People Search Sites
- username-enumeration
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Forensic OSINT — Username Search

> A hosted, evidence-grade username enumerator: type a handle, get its accounts across 500+ sites with screenshots and MHTML captures preserved for you.

## When to use
You have a `username` and want to find everywhere that same handle exists — social media, forums, gaming, niche communities. The differentiator over a plain terminal enumerator is built-in evidence preservation: automated screenshots and MHTML captures of each hit, which matters when the findings need to hold up later. Reach for it when you want breadth plus a defensible record without running your own tooling.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.forensicosint.com/free-tools/username-search and create/sign in to a free account (use a burner email).
2. Enter the `username` and run the search — it checks 500+ sites via the WhatsMyName dataset.
3. Read the results tabs: **Found** (confirmed accounts with screenshot, site category, and direct link), **Not Found**, and **False Positives**.
4. Preserve: download selected results or the auto-captured screenshots/MHTML for your case file.
5. Pivot: each Found `social-profile` feeds face/image tools, bio-scraping, and cross-account correlation.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` (confirmed account links, by site category), screenshots + MHTML evidence
- **Empty/negative result looks like:** everything in the **Not Found** tab — the handle isn't used on the checked sites, or the site's detection pattern is stale. A hit confirms the account *exists*, not that your subject owns it.

## Gotchas & OpSec
- Human-in-the-loop: a free **account login** is required — register with a sock-puppet email.
- Username enumeration proves existence, not ownership; the same handle can belong to different people. Corroborate before attributing.
- Detection relies on WhatsMyName patterns, so newly-added or JS-heavy sites may be missed or throw false positives (there's a whole tab for them).

## Overlaps ("do both")
- Pairs with `[[whatsmyname]]` and `[[sherlock]]` — those are the raw open-source enumerators you can run locally with no login; this wraps the same data with hosted evidence capture. Run a local tool for stealth, this one when you need preserved proof.

## Trust & verifiability
`trust: community` — a credible OSINT vendor building on the transparent, open-source WhatsMyName dataset. The logic is inspectable; just remember hits are existence, not ownership.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | forensicosint-com-3 |
| category | people-search |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
