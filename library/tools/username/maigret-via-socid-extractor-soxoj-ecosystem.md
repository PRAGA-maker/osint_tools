---
id: maigret-via-socid-extractor-soxoj-ecosystem
name: Maigret (via socid_extractor / soxoj ecosystem)
description: Use when you have a profile URL/`social-profile` and want the hidden identifiers behind it — socid_extractor scrapes real `name`, user ID, `email`, and linked accounts to pivot further.
url: https://github.com/soxoj/socid_extractor
category: username
path:
- username
bestFor: Extracting hidden identifiers (real name, numeric user ID, linked accounts, emails) from a known profile page to pivot across platforms.
selectorsIn:
- social-profile
- username
selectorsOut:
- name
- email
- device-id
- social-profile
status: live
pricing: free
costNote: Free, open-source (soxoj); a Python CLI/library. No account or key; pairs naturally with Maigret.
opsec: passive
opsecNote: socid_extractor fetches the target's public profile page from your host, so that platform sees your IP request the page (a normal page view, no login, no notification). Run behind a proxy/VPN from a sock-puppet environment for hygiene.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: trusted
trustNote: By soxoj (author of Maigret), widely used in the OSINT community; it parses public page metadata, so results are as reliable as the source page, and site-specific parsers can break when platforms change.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- social-analyzer
- whatsmyname-web
aliases:
- socid_extractor
- soxoj socid_extractor
tags:
- identifier-extraction
- username
- python
source: gh-topic-osint-resources
lastVerified: '2026-07-10'
enrichment: full
---

# Maigret (via socid_extractor / soxoj ecosystem)

> soxoj's socid_extractor — point it at a known profile page and it scrapes the hidden identifiers (real name, numeric user ID, linked accounts, emails) that let you pivot to the same person elsewhere.

## When to use
You already have one confirmed `social-profile`/URL and want to squeeze out the non-obvious identifiers embedded in that page: the account's numeric/internal ID, a real `name` in metadata, a linked `email`, or cross-links to the person's other accounts. Those IDs are the seeds for cross-platform pivots (e.g. resolving a handle to a stable user ID that survives renames). It complements handle-search tools by going *deep* on one known page rather than *wide* across sites.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install: `pip install socid-extractor` (or clone `https://github.com/soxoj/socid_extractor`).
2. Run against a profile URL: `socid_extractor --url "https://platform.com/targetprofile"` (or import it as a library).
3. Read the extracted fields — user ID (`device-id`-style internal identifier), real `name`, `email`, linked accounts (`social-profile`).
4. Use extracted IDs/emails as new seeds in other tools.
5. Pivot: numeric IDs feed platform-specific ID lookups; emails feed email OSINT; run the handle wide via `[[whatsmyname-web]]`/`[[social-analyzer]]`. It also underpins Maigret's extraction step.

## Inputs → Outputs
- **In:** a known `social-profile` URL or `username`
- **Out:** hidden identifiers — real `name`, internal user ID (`device-id`), `email`, linked `social-profile`s
- **Empty/negative result looks like:** no fields extracted — either the platform isn't supported/changed its page structure, or the page exposes nothing; a null result is a parser gap, not proof the data doesn't exist.

## Gotchas & OpSec
- Coverage is per-site parsers that break when platforms change their HTML/JSON — check you're on the latest version if a known site returns nothing.
- It reads only what the public page exposes; it doesn't bypass privacy or auth.
- OpSec: passive — a normal public page fetch from your IP; mask it with a proxy/VPN and sock-puppet setup.

## Overlaps ("do both")
- Deepens the results of breadth tools `[[whatsmyname-web]]` and `[[social-analyzer]]` — find candidate profiles with those, then extract their hidden IDs here to confirm and pivot.

## Trust & verifiability
`trust: trusted` — a well-regarded soxoj tool that parses genuine page metadata. Extracted values are as authoritative as the source page; verify cross-links before treating them as the same person, and expect occasional parser breakage.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | maigret-via-socid-extractor-soxoj-ecosystem |
| category | username |
| selectorsIn → selectorsOut | social-profile, username → name, email, device-id, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | no |
