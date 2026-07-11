---
id: socid-extractor-2
name: socid-extractor
description: Use when you have a `social-profile` URL or page source and want the hidden account IDs, real names, and metadata baked into it — returns internal user IDs and profile metadata for pivoting.
url: https://pypi.org/project/socid-extractor/
category: username
path:
- username
bestFor: Pulling hidden numeric account IDs, real names, and creation dates out of a profile page's source for cross-platform pivoting.
selectorsIn:
- social-profile
- username
selectorsOut:
- device-id
- metadata-exif
- name
status: live
pricing: free
costNote: Free and open-source (Python package / CLI); no account.
opsec: passive
opsecNote: To extract, it fetches the target's public profile page once (or you paste page source you already have), so at most a single normal page request reaches that site from your IP — comparable to viewing the page. It sends nothing to the subject and doesn't log in. Run behind a VPN if you want the fetch off your attributable IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: community
trustNote: Well-known open-source extractor by soxoj (of Maigret); community-maintained parsers for many platforms, inspectable, but individual site parsers rot as sites change their page markup.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
aliases:
- socid_extractor
tags:
- username
- metadata-extraction
- account-id
source: osint4all
lastVerified: '2026-07-11'
enrichment: full
---

# socid-extractor

> A Python extractor that reads a profile page's source and pulls out the identifiers sites leave in the HTML/JSON — internal numeric IDs, real names, emails, creation dates — the durable keys that let you follow a person across platforms.

## When to use
You have a `social-profile` (a URL, or the page source you've already captured) and want the machine-readable identity data hiding behind the rendered page: the stable internal user ID (which survives username changes), a real name or email leaked in metadata, account creation timestamps, and linked IDs. These are stronger pivots than a display name. Reach for it right after finding a profile, to convert it into hard identifiers you can search elsewhere.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install the package: `pip install socid-extractor`.
2. Run it against a supported profile URL (CLI: `socid_extractor --url <profile_url>`), or feed it saved page HTML.
3. Read the extracted fields: internal user/account IDs, name, email/phone fragments, registration date, and other embedded metadata.
4. Verify the parser matched the current page format (sites change markup).
5. Pivot: a stable numeric ID feeds ID-based lookups (e.g. `[[regvk-com]]`-style ID tools, `[[facebook-photos-by-id]]`); a leaked `name`/email feeds people-search; it pairs directly with Maigret/username enumerators.

## Inputs → Outputs
- **In:** `social-profile` (URL or page source) / `username`
- **Out:** `device-id` (internal account/user IDs), `metadata-exif` (embedded profile metadata), `name`
- **Empty/negative result looks like:** no fields extracted — the site isn't supported, changed its markup, or served a login/consent wall instead of the profile. Not proof no data exists; grab the real page source manually and retry, or update the tool.

## Gotchas & OpSec
- Human-in-the-loop: none, but keep the package **updated** — parsers break when platforms restructure pages.
- Only supported sites yield structured output; for others you get nothing.
- OpSec: passive — a single profile fetch (or offline on captured HTML); use a VPN if the fetch should be off your IP.

## Overlaps ("do both")
- Pairs tightly with Maigret/Sherlock and `[[whatsmyname]]` — enumeration finds the profiles; socid-extractor rips the hidden IDs/metadata out of each so you can pivot on durable identifiers.

## Trust & verifiability
`trust: community` — a respected, inspectable open-source tool; outputs are whatever the site actually embedded, so they're reliable when a parser matches, and simply absent (not wrong) when it doesn't.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | socid-extractor-2 |
| category | username |
| selectorsIn → selectorsOut | social-profile, username → device-id, metadata-exif, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | no |
