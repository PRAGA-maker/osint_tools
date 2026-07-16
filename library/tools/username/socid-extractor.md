---
id: socid-extractor
name: socid-extractor
description: Use when you have a profile URL (`social-profile`) and want the hidden account data behind it — returns internal user IDs (`device-id`), `username`, `name`, linked `email` and registration `metadata-exif`.
url: https://github.com/soxoj/socid-extractor
category: username
path:
- username
bestFor: Pulling hidden structured fields (internal user IDs, real names, registration dates, linked emails) from a known profile page across 150+ sites — the pivot engine behind Maigret.
selectorsIn:
- social-profile
selectorsOut:
- username
- name
- email
- device-id
- metadata-exif
status: live
pricing: free
costNote: Free and open-source (Python). `pip install socid-extractor`; no account or key.
opsec: passive
opsecNote: It fetches the profile page you point it at, from YOUR IP — a normal page view, but done by a script. Nothing is sent to the profile owner. For sensitive targets, fetch via a puppet/VPN and avoid authenticated endpoints.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: trusted
trustNote: By soxoj, author of Maigret; socid-extractor is Maigret's extraction engine. Widely used and reliable, though individual site parsers break when sites change their markup.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- socid_extractor
tags:
- profile-parsing
- account-id
- metadata
- python
source: gh-topic-osint-framework
lastVerified: '2026-07-10'
enrichment: full
relatedTools:
- 1c-database-converter
- awesome-osint-mcp-servers
- counter-osint-guide-for-russians
- fravia-soxoj
- gitcolombo
- maigret
- maigret-via-socid-extractor-soxoj-ecosystem
- mailto-analyzer
- marple
- osint-namecheckers-list
- username-generation-guide
---

# socid-extractor

> Point it at a profile URL and it scrapes out the hidden fields the page embeds — internal user IDs, real names, registration dates, linked emails — the data that lets you pivot from one account to the next.

## When to use
You already have one confirmed profile (`social-profile`) and want to extract its **machine-level identity** — especially the internal numeric user ID, which is stable across username changes and often reused or linkable across a platform's products. Reach for it to turn a single profile into pivot material: a linked email, a registration date to correlate accounts, or an ID that ties two profiles to the same person. It's the natural second step after username enumeration finds a profile.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install: `pip install socid-extractor`.
2. CLI: `socid_extractor --url <profile_url>`; or in Python, `from socid_extractor import extract; extract(html)`.
3. Read the structured fields it returns: internal user ID (`device-id`), `username`, display `name`, any exposed `email`, registration/creation date and other `metadata-exif`.
4. Note which fields are present — coverage varies by site and by how much the page leaks.
5. Pivot: internal ID → find the same person's other content on that platform; linked email → email-OSINT (`[[reversecontact]]`, breach checks); registration date → correlate with other accounts created the same time.

## Inputs → Outputs
- **In:** `social-profile` (a profile URL or its HTML)
- **Out:** `username`, `name`, `email` (if exposed), `device-id` (internal user ID), `metadata-exif` (registration date, counts, etc.)
- **Empty/negative result looks like:** no fields extracted / "not supported" — the site isn't in the parser set, or it changed its markup and broke the parser, or the page hides the data. Empty means the extractor can't read that page, not that the account lacks an ID.

## Gotchas & OpSec
- **Site parsers rot:** when a platform changes its HTML/JSON, that site's extraction silently breaks — keep the tool updated and sanity-check output.
- Some fields require the raw page from a logged-out or specific endpoint; results differ by how you fetch.
- OpSec: **passive** — a scripted page view from your IP; use a puppet/VPN for sensitive targets.

## Overlaps ("do both")
- The engine inside Maigret — run Maigret for enumeration + extraction together, or use socid-extractor standalone on a single URL.
- Feed profiles found by `[[gosearch]]`/Sherlock into it; feed extracted emails into email-OSINT.

## Trust & verifiability
`trust: trusted` — from a respected OSINT author and battle-tested via Maigret. Output is parsed directly from the target page, so it's authoritative when it works; verify surprising fields against the live page, since a stale parser can mislabel data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | socid-extractor |
| category | username |
| selectorsIn → selectorsOut | social-profile → username, name, email, device-id, metadata-exif |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | no |
