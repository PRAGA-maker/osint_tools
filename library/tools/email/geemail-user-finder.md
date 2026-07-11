---
id: geemail-user-finder
name: geeMail User Finder
description: Use when you have one or many candidate `email` addresses and want to confirm which are registered Gmail accounts — returns a validated `email` existence verdict per address.
url: https://github.com/dievus/geeMailUserFinder
category: email
path:
- email
bestFor: Bulk-validating whether a list of addresses are live Gmail/Google accounts.
selectorsIn:
- email
selectorsOut:
- email
status: live
pricing: free
costNote: Free, open-source Python CLI. No API key or account needed.
opsec: active
opsecNote: The tool sends requests to Google's own endpoints for each address, so you are probing Google's infrastructure — not the subject, who is not notified. The author warns Google "may or may not appreciate account testing like this," so route through a VPN/clean IP and keep volumes modest to avoid rate-limiting or blocks.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source tool by a known OSINT author (dievus/The OSINT Curious); inspect the code before running. Existence is inferred from cookie behaviour and can occasionally false-positive.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- geeMailUserFinder
tags:
- Emails
- account-existence
source: cyb-detective
lastVerified: '2026-07-11'
enrichment: full
---

# geeMail User Finder

> A Python CLI that tells you whether an address is a real Google/Gmail account — validate one email or a whole list at once.

## When to use
You have candidate `email` address(es) — guessed permutations of a subject's name, addresses harvested from a breach or a form, or a list to triage — and you need to know which actually exist as Google accounts before investing in deeper enrichment. Confirming a live Gmail also implies a broader Google footprint (YouTube, Drive, Maps reviews, Android) worth pivoting into.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and set up: `git clone https://github.com/dievus/geeMailUserFinder`, then install its Python requirements.
2. Route traffic through a VPN/proxy.
3. Check a single address: `python geeMailUserFinder.py -e target@gmail.com`.
4. Or a list: `-r emails.txt`, write results with `-w out.txt`, tune `-t` for timeout, `-v` for verbose.
5. Read output: valid vs. not, per address. Pivot confirmed accounts into `[[ghunt]]`-style Google account enrichment and Google Maps/YouTube review hunting.

## Inputs → Outputs
- **In:** `email` (single, or a file of many)
- **Out:** existence verdict per `email` (valid Google account / not)
- **Empty/negative result looks like:** "not valid" for an address — usually means no Google account, but the author notes occasional false positives for names Gmail won't permit, so treat edge cases as "likely not" rather than certain.

## Gotchas & OpSec
- Detection method (cookie issuance) can drift as Google changes its endpoints; if results look uniformly wrong, the technique may have broken — check for an updated release.
- Rate-limit yourself; bursts of checks can get your IP throttled or blocked by Google.
- Confirms existence only — it returns no name, profile, or other data on its own.

## Overlaps ("do both")
- Pairs with `[[ghunt]]` and `[[epieos]]`-style Google enrichment — geeMail confirms the account exists, those turn a confirmed Gmail into profile, reviews, and metadata.

## Trust & verifiability
`trust: community` — open-source and auditable, but the existence signal is inferential; corroborate a critical hit with a second Google-account check.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | geemail-user-finder |
| category | email |
| selectorsIn → selectorsOut | email → email |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
