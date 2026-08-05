---
id: chibisafe-moe
name: Chibisafe.moe
description: Use when you need your own private, self-hosted file drop to store/share investigation artifacts under your control — returns hosted files with shareable links (no selectors).
url: https://chibisafe.moe/
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: A self-hosted, open-source file-uploader/vault for keeping evidence and screenshots on infrastructure you own.
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and open source (self-hosted); your only cost is the server/hosting you run it on.
opsec: passive
opsecNote: Self-hosting is the OpSec win — files live on your infrastructure, not a third party's, so nothing is exposed to a vendor. But anything you generate a public share link for becomes world-accessible; keep case material private/authenticated, harden the instance, and never rely on a shared community instance for sensitive data.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: docker
trust: community
trustNote: Actively-maintained open-source project (by Pitu); code is public on GitHub, so it is auditable, but a self-hosted tool's security depends on how you deploy it.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: true
registration: true
aliases:
- Chibisafe
- chibisafe.app
tags:
- file-hosting
- self-hosted
- evidence-preservation
source: osint4all
lastVerified: '2026-08-05'
enrichment: full
---

# Chibisafe.moe

> A modern, self-hosted open-source file-uploader — the "keep your evidence on your own box" option when you do not want screenshots and artifacts sitting on a third-party host.

## When to use
This is OpSec infrastructure, not a lookup tool. Reach for it when you want a private place to collect and (selectively) share investigation artifacts — screenshots, saved pages, downloaded files — without handing them to a commercial cloud. You run it yourself (Docker), so you control retention, access, and who ever sees a link. It finds nothing; it stores what you find.

## How to use it (`bestInteractionPattern`: docker)
1. Deploy Chibisafe on a server you control (Docker image; see the project docs at chibisafe.app / GitHub).
2. Create an admin account and lock down registration/access.
3. Upload artifacts; organize with albums and tags; use chunked uploads for large files.
4. Generate share links only when needed, and prefer authenticated/private access for case material.
5. Pivot: it is the holding pen — the intelligence work happens on the files you put in it (metadata, content analysis).

## Inputs → Outputs
- **In:** files you upload (your artifacts)
- **Out:** hosted files with optional shareable links — storage, no personal selectors
- **Empty/negative result looks like:** not applicable — it is storage; the failure mode is a misconfigured/exposed instance leaking files, which is an OpSec error, not a result.

## Gotchas & OpSec
- Human-in-the-loop: you must stand up and administer the instance; account/login required.
- OpSec: self-hosting keeps data off third parties (good), but a public share link or a hardening lapse exposes everything — treat instance security seriously and avoid random public community instances for sensitive files.
- It is DIY infrastructure; you own patching and backups.

## Overlaps ("do both")
- Pairs with capture tools (screenshot/archiver extensions) and metadata analyzers — capture feeds Chibisafe for safekeeping; analysis tools then work over the stored copies.

## Trust & verifiability
`trust: community` — a transparent, auditable open-source project; the trust question is your own deployment's security, not the vendor's, since there is no vendor when you self-host.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | chibisafe-moe |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | docker |
| opsec | passive |
| human-in-loop | yes (account-login) |
