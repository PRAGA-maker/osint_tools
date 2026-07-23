---
id: website-diff
name: Website-Diff (Wayback-Diff)
description: Use when you have a `domain`/URL and want to compare two versions of a page (live or Wayback snapshots) and see the meaningful changes — returns a scored, noise-stripped diff of what changed.
url: https://github.com/GeiserX/Website-Diff
category: archives-cache
path:
- archives-cache
bestFor: Diffing two versions of a web page (live vs archive, or two archive snapshots) with banners/analytics stripped and changes scored by significance.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open source (GPL-3.0); install via pip, from source, or Docker. Not intended for commercial use.
opsec: active
opsecNote: Diffing live URLs fetches those pages from YOUR machine, so the target server sees the request; diffing two Wayback snapshots only touches the Internet Archive, which is fully passive. Prefer archive-vs-archive when you don't want to touch the target.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source tool (GeiserX) built around Wayback Machine snapshots; deterministic diffing whose output you can re-verify by inspecting the snapshots yourself.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- buscapaginasblancas
- wayback-archive
aliases:
- Website-Diff
- wayback-diff
tags:
- diff
- change-detection
- wayback
- archive
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Website-Diff (Wayback-Diff)

> An open-source CLI/Docker tool that compares two versions of a web page — live or Wayback snapshots — strips boilerplate, and scores the changes by significance.

## When to use
You want to know what changed on a page over time — a bio that was edited, a listing that was altered, a claim that was quietly removed. Website-Diff compares two versions (live-vs-archive or two archive snapshots), automatically removing banners, analytics scripts, and Wayback playback/rewrite noise, then classifies each change as High/Medium/Low significance and can render a visual diff. Ideal for catching meaningful edits without drowning in cosmetic churn.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install wayback-diff`, from source, or run the Docker image.
2. Provide two targets — two Wayback snapshot URLs, or a live URL vs a snapshot.
3. Run the comparison; it strips boilerplate and outputs the scored diff (High/Medium/Low changes).
4. Optionally generate the screenshot/visual diff for a side-by-side view.
5. Pivot: a High-significance removal points you at content worth recovering in full from the archive.

## Inputs → Outputs
- **In:** two versions of a `domain`/URL (live and/or Wayback snapshots)
- **Out:** a significance-scored diff of what changed, optionally a visual diff
- **Empty/negative result looks like:** no significant changes reported — the versions are effectively identical after stripping noise (or you compared the same snapshot); not an error.

## Gotchas & OpSec
- Diffing a **live** URL contacts the target; use archive-vs-archive to stay passive.
- Depends on Wayback having the snapshots you want — if the page wasn't archived at the relevant time, there's nothing to diff (consider forcing a capture going forward).
- Significance scoring is heuristic; review Medium/Low changes too when the edit is subtle.

## Overlaps ("do both")
- Pairs with the Wayback Machine and change-monitoring services — this scores *what* changed between two known versions, while a monitor watches for *future* changes and the archive supplies the snapshots.

## Trust & verifiability
`trust: community` — an open-source tool over Internet Archive snapshots; every diff is re-verifiable by opening the two snapshots yourself.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | website-diff |
