---
id: megatools
name: Megatools
description: Use when you have a MEGA.nz link or account and want to list/download its contents from the command line — returns the downloaded files (leak dumps, shared archives) for offline analysis.
url: https://megatools.megous.com/
category: evidence-capture
path:
- evidence-capture
bestFor: Scripted listing and downloading of MEGA.nz public links and folders (incl. leaked-data dumps).
selectorsIn:
- document-id
selectorsOut: []
status: live
pricing: free
costNote: Free and open-source; packaged in most distros (`apt install megatools`, `brew install megatools`). No account needed for public links.
opsec: active
opsecNote: megadl fetches files from MEGA's servers over your IP; MEGA logs the download. For sensitive/leaked-data links use a sock-puppet IP/VPN, and be mindful of the legal and ethical exposure of downloading breach dumps.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Long-standing open-source MEGA client (megous.com); distro-packaged and widely used, though extractor behaviour can lag MEGA API changes.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- megatools.megous.com
- megadl
tags:
- Downloaders
- mega
- leaks
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Megatools

> Command-line client for MEGA.nz: list and pull down public links or whole folders without the browser — automatable for large or repeated jobs.

## When to use
You have a MEGA.nz share link or folder (often where breach dumps, document leaks, and large archives are distributed) and want to enumerate and download its contents programmatically rather than click-by-click. megatools handles public links without an account and can script bulk retrieval into an evidence folder — the practical way to grab a leaked-data set referenced in an investigation.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `sudo apt install megatools` (Linux) or `brew install megatools` (macOS).
2. Download a public link: `megadl 'https://mega.nz/file/...'` (or a folder link to fetch the whole tree).
3. List a remote folder without downloading: `megals 'https://mega.nz/folder/...'`.
4. With credentials (sock-puppet account) you can also `megaget`/`megaput`/`megals` your own storage; keep creds in a `.megarc`.
5. Preserve: hash downloaded files and record the source link + timestamp for chain-of-custody. Pivot: index the archive and mine it for selectors.

## Inputs → Outputs
- **In:** a MEGA.nz public link or folder (a shared `document-id`/resource)
- **Out:** the downloaded files/directory tree on disk
- **Empty/negative result looks like:** a decryption/"not found" error — the link expired, was taken down, or the key is missing/wrong; MEGA links die quickly, so absence usually means removal.

## Gotchas & OpSec
- MEGA links are ephemeral and frequently removed — grab promptly and preserve provenance.
- API changes can break megatools versions; update if downloads fail unexpectedly.
- OpSec: **active** — MEGA sees your download; use a sock-puppet IP/VPN. Downloading breach dumps carries real legal/ethical risk — confirm authorisation.

## Overlaps ("do both")
- Complements general downloaders like `[[you-get]]` — megatools speaks MEGA's encrypted-link protocol specifically, which generic downloaders can't handle.

## Trust & verifiability
`trust: community` — a mature, distro-packaged open-source client; it retrieves the genuine files from MEGA, with the only reliability caveat being occasional lag behind MEGA's API changes.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | megatools |
| category | evidence-capture |
| selectorsIn → selectorsOut | document-id →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
