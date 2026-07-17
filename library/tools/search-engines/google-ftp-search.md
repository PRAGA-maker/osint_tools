---
id: google-ftp-search
name: Google FTP Search
description: Use when you want to find files on open FTP/index servers — a Google Custom Search Engine scoped to open directories, returning downloadable files and listings.
url: https://cse.google.com/cse/home?cx=014863114814409449623:jc-vjhl_c5g
category: search-engines
path:
- search-engines
bestFor: Finding files exposed on open FTP servers and public "index of" directories via a scoped Google Custom Search.
selectorsIn:
- name
selectorsOut:
- document-id
- domain
status: degraded
pricing: free
costNote: Free Google Custom Search Engine; no account needed.
opsec: passive
opsecNote: Searching is passive (you query Google's index, not the servers). Actually downloading a file connects you to that FTP/host, which logs your IP — use a VPN/sock puppet before opening or downloading anything you find.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party-configured Google Custom Search Engine, not an official Google product; results depend on Google still indexing open-directory/FTP content, which has declined over time.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- google
- filepursuit
- opendirectory-search
aliases:
- Google FTP search CSE
- open directory search
tags:
- toddington
- curated-directory
- file-search
source: toddington-resources
lastVerified: '2026-07-17'
enrichment: full
---

# Google FTP Search

> A Google Custom Search Engine scoped to open FTP servers and "index of" directories — for finding loose files (documents, media, backups) exposed on public hosts.

## When to use
You're hunting for files a subject or organization may have left on an open FTP server or a browsable web directory — documents, images, leaked backups, media. This CSE narrows Google to open-directory/FTP-style results, surfacing downloadable files that normal search buries. A niche file-discovery angle (low direct MP relevance) that occasionally turns up documents or images tied to a name.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the CSE at the URL and enter your terms (a `name`, filename, or keyword).
2. Refine with operators: `intitle:"index of"`, filename/extension terms, quoted phrases.
3. Review results — many will be directory listings (`index of ...`) or direct file links.
4. **Before opening/downloading**, switch to a VPN/sock-puppet — the host logs your connection.
5. Pivot: recovered documents/images → metadata (EXIF) and content analysis; a host/`domain` → infrastructure lookups. For a more modern open-directory search, try `[[filepursuit]]`.

## Inputs → Outputs
- **In:** a `name`, filename, or keyword
- **Out:** open-directory listings and direct file links (`document-id` files, host `domain`)
- **Empty/negative result looks like:** few/no results — open FTP/index content has shrunk and Google indexes less of it now; a null is common and not meaningful. Try FilePursuit or dedicated open-directory engines.

## Gotchas & OpSec
- **Degraded over time:** open FTP indexing has declined and this CSE's config may be stale — expect thinner results than it once returned.
- Downloading connects you directly to the host (which logs you) — use a VPN before touching any file.
- Files on open servers can be bait/malware — handle downloads in a sandbox.

## Overlaps ("do both")
- Pairs with `[[filepursuit]]` — a purpose-built open-directory/file search engine with fresher coverage; run both, since indexes differ.
- Pairs with `[[google]]` using your own `intitle:"index of"` dorks for more control.

## Trust & verifiability
`trust: community` — a user-configured Custom Search Engine, not an official Google service. Results are real Google index hits but coverage is narrow and aging; the *files* themselves are unverified — inspect safely and corroborate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | google-ftp-search |
| category | search-engines |
| selectorsIn → selectorsOut | name → document-id, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
