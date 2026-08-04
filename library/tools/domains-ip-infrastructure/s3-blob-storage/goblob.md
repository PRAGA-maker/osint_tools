---
id: goblob
name: goblob
description: Use when you have a target org/`domain` and want to find its publicly exposed Azure blob storage — returns discovered storage accounts, open containers and listed files.
url: https://github.com/Macmod/goblob
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- s3-blob-storage
bestFor: Fast enumeration of publicly readable Azure blob containers and files for a target organisation.
input: Storage-account name guesses (derived from org/domain) and optional custom wordlists
output: Discovered Azure storage accounts, publicly accessible containers, and listed blob files
selectorsIn:
- domain
- employer-org
selectorsOut:
- document-id
- metadata-exif
status: live
pricing: free
costNote: Free and open-source (MIT); install via `go install github.com/Macmod/goblob@latest`. No account needed.
opsec: active
opsecNote: goblob sends many direct requests to Azure storage endpoints for the target, which the target's cloud logging can record. It also warns it can burn bandwidth and rack up cloud costs — throttle goroutines/timeouts and only run against authorised targets.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: An open-source Go tool by Macmod on GitHub; auditable source, but a community project — verify the binary you install and its wordlists.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools: []
aliases:
- Macmod/goblob
tags:
- azure
- blob-storage
- cloud-enumeration
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# goblob

> A fast Go CLI that brute-forces Azure blob storage names to surface an organisation's publicly exposed containers and files — the Azure counterpart to S3 bucket hunting.

## When to use
Your investigation touches an organisation (`employer-org`) or `domain` and you suspect misconfigured Azure storage is leaking documents. goblob takes candidate storage-account names (often derived from the org/brand/domain) plus a container wordlist and reports which storage accounts exist, which containers are publicly readable, and what files they list — a route to leaked documents, backups or media that can corroborate identity, location or activity.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `go install github.com/Macmod/goblob@latest`.
2. Run against a single guessed account name: `goblob <storageaccountname>`, or a list: `goblob -accounts accounts.txt`.
3. Seed account-name guesses from the target's name/brand/domain; tune the bundled wordlist (standard/small/micro) and limit goroutines/timeouts to control load.
4. Review discovered open containers and listed blobs; download only what you are authorised to, and note file metadata as leads.
5. Pivot: exposed documents feed metadata/EXIF extraction; account-naming patterns can reveal further infrastructure.

## Inputs → Outputs
- **In:** guessed storage-account names (from `domain`/`employer-org`) + wordlists
- **Out:** existing storage accounts, publicly readable containers, and listed blob files (potentially documents with recoverable `metadata-exif`)
- **Empty/negative result looks like:** no accounts resolve or all containers return access-denied/404 — meaning nothing is publicly exposed under the guessed names, not that the org has no Azure storage.

## Gotchas & OpSec
- Human-in-the-loop: none; it's a CLI.
- OpSec: **active** — it hammers Azure endpoints for the target and is visible in their cloud logs; it can also incur real bandwidth/cost. Only run against targets you are authorised to test, and rate-limit.
- Scope discipline: enumerating is one thing; downloading/using exposed private data may cross legal lines — stay within your authorisation.

## Overlaps ("do both")
- Pairs with S3/GCS bucket-enumeration tools because organisations spread storage across clouds — the same brand may leak on Azure here and on S3 elsewhere; run the equivalent for each provider.

## Trust & verifiability
`trust: community` — open-source and auditable, but community-maintained; verify the source/binary you install, and confirm any "exposed" finding by directly requesting the reported URL.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
