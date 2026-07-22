---
id: snippet-host
name: snippet.host
description: Use when you have a `username` or keyword and want public code/text pastes — returns snippets that may leak credentials, contacts, or handles.
url: https://snippet.host/
category: communities-forums
path:
- communities-forums
bestFor: Searching a minimal paste/snippet host for leaked code, config, or text tied to a handle or keyword.
selectorsIn:
- username
selectorsOut:
- social-profile
- email
status: live
pricing: free
costNote: Free to read public snippets and to post; a free account is only needed to manage/keep your own snippets.
opsec: passive
opsecNote: Reading public snippets is passive. It also runs a Tor hidden service, so it is used to share sensitive material — treat any credentials/PII you find as live and handle responsibly; never re-post or exfiltrate. Do not log in with a real identity.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent minimalist paste host; content is anonymous, user-submitted, and unmoderated for accuracy.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- snippet.host
tags:
- pastebins
- paste-site
source: awesome-osint
lastVerified: '2026-07-22'
enrichment: full
---

# snippet.host

> A minimal, expiring paste host (with a Tor mirror) — one more paste site to sweep for leaked code, configs, credentials, and handles tied to your subject.

## When to use
You are running paste-site reconnaissance: a `username`, `email`, project name, or distinctive string may have been dropped here in a code or text snippet — leaked credentials, a config file, a contact list, or a note. Because pastes are often shared during breaches or by the subject themselves, a hit can surface an `email`, a reused handle, or infrastructure details. Use it alongside other paste hosts, not alone.

## How to use it (`bestInteractionPattern`: web-manual)
1. There is no rich internal search, so query a search engine scoped to the host: `site:snippet.host "<username>"` (or an email/keyword).
2. Open matching public snippets and read for credentials, contact details, reused handles, and internal references.
3. Note the paste's expiry — content may be set to self-delete, so capture anything relevant immediately.
4. Do not authenticate with a real identity; treat found secrets as sensitive.
5. Pivot: a leaked `email` feeds breach/email-OSINT; a reused `username` feeds a cross-site enumerator; infrastructure strings feed domain/IP lookups.

## Inputs → Outputs
- **In:** `username` / `email` / keyword
- **Out:** public snippets that may contain `email`, reused handles (`social-profile`), and technical leads
- **Empty/negative result looks like:** no indexed pastes match — expected, since most content is ephemeral and search engines index only a slice. Absence is weak evidence; recheck other paste hosts.

## Gotchas & OpSec
- Pastes expire (from burn-after-read up to a year), so indexed copies may be gone by the time you click — snapshot fast.
- Search relies on external engines; the site itself offers little discovery, so coverage is partial.
- The Tor hidden service signals sensitive use; handle any credentials ethically and do not redistribute.

## Overlaps ("do both")
- Pairs with other paste-site and breach tools — each host indexes different content, so sweep several; a handle absent here may sit on another paste site.

## Trust & verifiability
`trust: community` — a legitimate but anonymous, unmoderated paste host; anything found is user-submitted and must be corroborated and handled with care.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | snippet-host |
| category | communities-forums |
| selectorsIn → selectorsOut | username → social-profile, email |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
