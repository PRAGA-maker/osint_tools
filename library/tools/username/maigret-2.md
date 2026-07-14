---
id: maigret-2
name: maigret
description: Use when you have a `username` and want to enumerate accounts across thousands of sites and pull a linked dossier (bios, avatars, IDs) — returns social-profile, name, image.
url: https://pypi.org/project/maigret/
category: username
path:
- username
bestFor: Enumerating a username across thousands of sites and extracting profile details into a dossier.
selectorsIn:
- username
selectorsOut:
- social-profile
- name
- image
status: live
pricing: free
costNote: Free and open source (MIT). Installed via pip/PyPI or run from source; no account or API key required for the core scan.
opsec: passive
opsecNote: Maigret queries each target site directly from YOUR IP, so those sites (and any behind Cloudflare) see your requests — it is not anonymous to the platforms, though it never contacts the person. Run it from a VPN/sock-puppet host, and note that some sites may rate-limit or flag automated checks.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: Widely used, actively maintained open-source successor to Sherlock (soxoj/maigret); large community, transparent site database — but it reports candidate matches that need manual confirmation for false positives.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- Maigret
- soxoj maigret
tags:
- username-enumeration
- account-discovery
source: osint4all
lastVerified: '2026-07-14'
enrichment: full
---

# maigret

> The go-to open-source username hunter: feed it a handle and it checks thousands of sites, then compiles the hits into a rich dossier — bios, avatars, IDs, and cross-linked accounts.

## When to use
You have a `username` (or a candidate handle) and want to map the subject's footprint across the web in one pass: which platforms the name is registered on, plus the profile details (real `name`, avatar `image`, bio, other linked handles) Maigret can extract. It's the first move in username-pivoting an investigation.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install maigret` (or clone the GitHub repo).
2. Run: `maigret <username>` — add `--html`/`--pdf` for a formatted dossier report, or `-a` to check all sites (slower).
3. Review the hits: each claimed account with its URL, plus extracted `name`/avatar/bio where the site exposes them.
4. Manually confirm matches — a common handle produces false positives; verify the profile actually belongs to your subject (consistent avatar, bio, linked accounts).
5. Pivot: confirmed handles feed platform-specific OSINT; extracted avatars feed reverse-image/face tools; discovered secondary usernames feed another Maigret run.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` (accounts across thousands of sites), `name`, `image` (avatars), bios/IDs
- **Empty/negative result looks like:** few or no hits — could mean an uncommon handle, or that sites rate-limited/blocked the scan; re-run and cross-check with another enumerator before concluding the handle is unused.

## Gotchas & OpSec
- Reports candidate matches — always manually confirm to avoid attributing a stranger's account to your subject.
- Some sites block automated checks (Cloudflare, rate limits), producing false negatives; results vary run to run.
- OpSec: passive to the target, but each site sees your IP — run behind a VPN/sock-puppet host.

## Overlaps ("do both")
- Pairs with [[whatsmyname]] and Sherlock-style enumerators (different site lists catch different accounts) and with reverse-image tools that consume the avatars Maigret extracts.

## Trust & verifiability
`trust: trusted` — a mature, community-vetted open-source tool with a transparent site database; the mechanism is reliable, but every reported account still needs human confirmation.
