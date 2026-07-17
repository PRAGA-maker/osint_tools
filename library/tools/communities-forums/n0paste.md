---
id: n0paste
name: n0paste
description: Use when you have an `email`/`username` and want to check a pastebin for leaked text mentioning it — returns password/credential and data-leak leads.
url: https://n0paste.eu/
category: communities-forums
path:
- communities-forums
bestFor: A pastebin-style site to check (via search-engine dorking) for pasted dumps, credentials or documents mentioning a selector.
selectorsIn:
- email
- username
selectorsOut:
- password
- email
status: live
pricing: free
costNote: Free public paste service; no account needed to read pastes.
opsec: passive
opsecNote: Reading pastes is passive. Never paste a target's data into it (that would republish/leak it), and only view leaked material for legitimate investigative purposes. Use a research browser.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An anonymous paste host with no vetting; content is user-submitted and may include stolen or fabricated data — treat anything found as an unverified lead.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- n0paste.eu
tags:
- pastebins
- leaks
source: awesome-osint
lastVerified: '2026-07-17'
enrichment: full
---

# n0paste

> A Pastebin-style host worth checking for leaked dumps or documents that mention your subject's email or handle.

## When to use
You're canvassing paste sites for a subject's exposure — an `email`, `username`, or other selector appearing in a credential dump, config leak, or pasted document. n0paste is one of many pastebin alternatives where such material surfaces. Because these sites rarely have good native search, you generally reach relevant pastes through a search engine rather than the site itself.

## How to use it (`bestInteractionPattern`: web-manual)
1. Rather than browsing n0paste blind, dork it: `site:n0paste.eu "target@example.com"` (or the username) on Google/Bing.
2. Open any matching paste and read it for the selector in context — associated credentials, other emails, or document content.
3. Note that pastes are ephemeral; if a hit 404s, check the Wayback Machine for a cached copy.
4. Do not submit or re-paste the subject's data anywhere.
5. Pivot: a leaked `password`/credential or co-listed `email` feeds breach-context and email OSINT; never reuse found credentials to access accounts.

## Inputs → Outputs
- **In:** `email`, `username`, or other selector (searched via a dork)
- **Out:** paste content mentioning the selector → `password`/credential and co-listed `email` leads
- **Empty/negative result looks like:** no matching paste — the selector hasn't been posted here (or the paste expired); absence is not proof of no exposure. Check other paste sites and breach tools.

## Gotchas & OpSec
- Content is **unvetted and possibly stolen or fake** — treat every find as an unverified lead and handle leaked data lawfully.
- Native search is weak; rely on search-engine dorks and Wayback for expired pastes.
- Never paste a target's information into the site — that would publish it.

## Overlaps ("do both")
- Pairs with breach-search tools (HIBP-style) and other pastebin monitors — n0paste is one source; comprehensive coverage means checking many paste sites plus breach databases.

## Trust & verifiability
`trust: community` — an anonymous, unmoderated paste host; anything found is an unverified lead requiring corroboration and lawful handling.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | n0paste |
| category | communities-forums |
| selectorsIn → selectorsOut | email, username → password, email |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
