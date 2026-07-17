---
id: archive-vn
name: Archive.vn
description: Use when you have a `domain` or URL and want an on-demand, permanent snapshot of a page (including JS-heavy or short-lived content) — returns a frozen archived capture (document-id) with its own citable URL.
url: https://archive.vn/
category: archives-cache
path:
- archives-cache
bestFor: Capturing and later retrieving a permanent snapshot of a page that the Wayback Machine missed or rendered incompletely.
selectorsIn:
- domain
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free to search and to create captures; no account required. archive.vn is one of several interchangeable domains (archive.today, archive.ph, archive.is, archive.li) for the same service.
opsec: active
opsecNote: Creating a new capture makes archive.today fetch the target URL from its own servers, so your IP is hidden from the target — but the "Save Page Now" request is triggered by you and the resulting snapshot is public and permanent. Searching existing captures is passive. Do not archive a URL you would not want publicly linked to your investigation.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independently operated archive of unclear ownership, but widely used and cited in journalism/OSINT; snapshots are byte-frozen and carry a permanent shortlink, so a capture is verifiable even if the operator is anonymous.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- archive-org
- wayback-archive-it-org
aliases:
- archive.today
- archive.ph
- archive.is
tags:
- Archives
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Archive.vn

> archive.today (mirrored at archive.vn / .ph / .is / .li) — an on-demand page freezer that captures a full visual + HTML snapshot, including dynamic pages the Wayback Machine can't handle.

## When to use
You have a `domain` or specific URL and either (a) need to preserve a page right now before it changes or is deleted — a social post, a marketplace listing, a profile the subject may scrub — or (b) the Wayback Machine has no capture or only a broken one. archive.today renders JavaScript and stores a flat snapshot, so it often succeeds where web.archive.org shows a blank shell.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://archive.vn/ (or any mirror: archive.today, archive.ph, archive.is).
2. To find existing captures: paste the URL into the lower "I want to search the archive for saved snapshots" box and submit.
3. To create a new capture: paste the URL into the upper "My url is alive and I want to archive its content" box and submit; wait for the render, then copy the resulting permanent shortlink (e.g. `archive.ph/abcde`).
4. Read the frozen snapshot — a fixed rendering of the page as of the capture moment, with both screenshot and text.
5. Pivot: recovered contact details/handles feed email/username tools; the permanent link is safe to cite in a report.

## Inputs → Outputs
- **In:** `domain` or full page URL
- **Out:** a permanent archived snapshot (`document-id`) with a citable shortlink
- **Empty/negative result looks like:** the search returns "no results" (no one has archived it — you can create one), or a capture attempt fails/loops (the page blocks archiving, or requires a login the archiver can't pass).

## Gotchas & OpSec
- Frequently sits behind a Cloudflare CAPTCHA or is temporarily unreachable; retry, switch mirror domains, or come back later.
- Cannot capture pages behind authentication; login-gated content archives as the logged-out view.
- OpSec: searching is **passive**; creating a capture is **active** and produces a public, permanent record — deliberate before archiving anything sensitive.

## Overlaps ("do both")
- Pairs with [[archive-org]] — the Wayback Machine has deeper historical depth; archive.today wins on dynamic pages and on-demand freshness. Check both.
- Pairs with [[wayback-archive-it-org]] for curated institutional crawls.

## Trust & verifiability
`trust: community` — the operator is anonymous, but each snapshot is byte-frozen behind a permanent shortlink and is widely cited in journalism and OSINT, so a capture is independently verifiable regardless of who runs the service.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | archive-vn |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
