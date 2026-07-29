---
id: thispersondoesnotexistapi-unofficial
name: ThisPersonDoesNotExistAPI (unofficial)
description: Use when you need to fetch AI-generated sock-puppet `face`/`image` files programmatically at scale — returns a random non-existent person's portrait via a small Python library.
url: https://github.com/David-Lor/ThisPersonDoesNotExistAPI
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Scripted/bulk retrieval of ThisPersonDoesNotExist GAN faces (with built-in de-duplication) for provisioning many sock-puppet avatars at once.
selectorsIn: []
selectorsOut:
- face
- image
status: degraded
pricing: free
costNote: Free and open-source (Apache-2.0). It's a thin Python wrapper around the public thispersondoesnotexist.com endpoint — no API key, no cost.
opsec: passive
opsecNote: A defensive/tooling utility — it produces synthetic faces, so no real person is queried. It scrapes a third-party site programmatically, so throttle requests, and reverse-image-check any face before use. Never reuse the same generated face across personas.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: python-lib
trust: community
trustNote: Small open-source library (Apache-2.0) — but the repo was archived (read-only, unmaintained) in April 2026, so it may break if the upstream site changes its endpoint. Verify it still fetches before depending on it.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- this-person-does-not-exist
- this-baseball-player-does-not-exist
aliases:
- ThisPersonDoesNotExistAPI
- David-Lor TPDNE API
tags:
- Sock Puppets
- sock-puppet-avatar
- gan-face
- python-lib
source: cyb-detective
lastVerified: '2026-07-29'
enrichment: full
---

# ThisPersonDoesNotExistAPI (unofficial)

> A small Python wrapper that pulls GAN faces from thispersondoesnotexist.com in code, with checksum de-duplication — for provisioning many sock-puppet avatars programmatically rather than clicking one at a time.

## When to use
You need more than one throwaway avatar — you're scripting the setup of a batch of research/sock-puppet accounts and want to fetch, save, and de-duplicate synthetic faces automatically. This library wraps the public ThisPersonDoesNotExist endpoint so you can grab faces in a loop and dedupe by MD5. For a single face, just use the website directly; this is the automation path.

## How to use it (`bestInteractionPattern`: python-lib)
1. Install: `pip install thispersondoesnotexist` (Python 3.6+, requires `requests`).
2. In code, call the fetch function/class to retrieve a JPEG of a non-existent person; use the built-in save + MD5 checksum to auto-name files and skip duplicates.
3. Loop with a polite delay between requests to fetch a batch; store the checksums so you never reuse a face.
4. Before assigning any face to a persona, reverse-search it (`[[pimeyes]]` / Google Images) to confirm zero matches, and lightly recompress to strip predictable raw-GAN characteristics.
5. Pivot: feed the avatars into your persona-provisioning workflow (paired with an isolation tool like `[[sessionbox]]`).

## Inputs → Outputs
- **In:** none — it generates/fetches, it doesn't search.
- **Out:** `face`, `image` — JPEGs of AI-generated people, with MD5 checksums for de-dup.
- **Empty/negative result looks like:** an HTTP error or empty response — the upstream site changed its endpoint or is blocking automated fetches. Since the repo is archived/unmaintained, this is a real risk; fall back to the site directly.

## Gotchas & OpSec
- Human-in-the-loop: none, but you must vet each face for GAN artifacts and reuse.
- OpSec: **passive** for targets (nobody real is queried). Throttle to avoid hammering the upstream site, and treat every face as one-persona-only.
- **Unmaintained:** archived April 2026 — it can silently break when thispersondoesnotexist.com changes. Test before relying on it in a pipeline.
- Never present a synthetic face as a real named individual.

## Overlaps ("do both")
- Wraps `[[this-person-does-not-exist]]` — the same faces via the website when you only need one or when the library breaks.
- Overlaps with `[[this-baseball-player-does-not-exist]]` as an alternative GAN-avatar source with a different look.

## Trust & verifiability
`trust: community` — a small, now-archived open-source utility. Trust is moot for the output (the faces are deliberately non-real); the practical risk is reliability, so confirm it still fetches before building on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | thispersondoesnotexistapi-unofficial |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | — → face, image |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | python-lib |
| opsec | passive |
| human-in-loop | no |
