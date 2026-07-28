---
id: archive-today
name: Archive.today
description: Use when you have a `domain` or `social-profile` URL and want a permanent, tamper-proof snapshot of the page as it looks now — returns an archived copy that survives deletion or edits.
url: https://archive.today
category: archives-cache
path:
- archives-cache
bestFor: On-demand archiving of a single live page (including JS-heavy social feeds) and searching for existing snapshots of a URL.
selectorsIn:
- domain
- social-profile
selectorsOut:
- social-profile
- name
- image
status: live
pricing: free
costNote: Free public service funded by donations; no account or payment required to save or view snapshots.
opsec: active
opsecNote: Submitting a URL causes archive.today's own servers (not you) to fetch the target page, so the target site sees archive.today's IP, not yours — good separation. But the resulting snapshot is public and permanent; anyone (including the subject) can later discover that the page was archived. Do not archive a URL you don't want on the public record.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running independent archiving project (aka archive.ph / archive.is / archive.li); widely used by journalists and researchers. Snapshots are frozen server-side renders, so content integrity is high, but the operator is anonymous.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- wayback-machine
aliases:
- archive.is
- archive.ph
- archive.li
- archive.today
tags:
- bellingcat-toolkit
- archiving
source: bellingcat-toolkit
lastVerified: '2026-07-28'
enrichment: full
---

# Archive.today

> On-demand web archiver that freezes a single page — including Facebook, X/Twitter and other JS-heavy pages the Wayback Machine often mangles — into a permanent, citable snapshot.

## When to use
You have found a live page (a `social-profile`, a post, a listing, a news article on a `domain`) that is relevant to a case and you need proof of its current state before it can be edited or deleted. Archive.today captures a pixel-accurate, server-rendered copy you can cite later. Also use it in reverse: paste a URL to check whether someone has *already* archived a page you can no longer reach live.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://archive.today (or a mirror: archive.ph / archive.is / archive.li).
2. To **save**: paste the target URL into the red "My url is alive..." box and press "save". Solve the CAPTCHA if prompted. Wait while its servers render the page; you get a permanent `archive.today/XXXXX` short-link plus a full-page screenshot.
3. To **search**: paste the URL into the blue "I want to search the archive..." box to list all existing snapshots of that exact URL over time.
4. Read the output: the snapshot is a static copy — links, text and images as they were at capture time. Compare multiple snapshots to see how a page changed.
5. Pivot: record the short-link in your case notes as evidence; harvest names/images/handles visible in the frozen copy even after the live page is taken down.

## Inputs → Outputs
- **In:** a URL (`domain` / `social-profile` / specific post)
- **Out:** a permanent snapshot revealing `social-profile`, `name`, `image` and page text frozen at capture time
- **Empty/negative result looks like:** "No results" in the search box means nobody has archived that exact URL yet (try trailing-slash / www variants); a save that stalls or errors usually means the page blocked the archiver or requires login.

## Gotchas & OpSec
- Human-in-the-loop: a CAPTCHA often gates saves; solve it manually.
- URL-exact: the search matches the precise URL string, so tiny differences (`?utm=`, `/`, `www.`) hide existing snapshots — try variants.
- It archives only what a logged-out visitor sees; login-walled content (private profiles, DMs) can't be captured.
- The snapshot is **public and permanent** — do not create a lasting public record of a sensitive page you'd rather keep quiet.

## Overlaps ("do both")
- Pairs with `[[wayback-machine]]` — the Wayback Machine has far deeper historical coverage and an API, while archive.today captures JS-heavy social pages more faithfully and lets you force a snapshot on demand. Archive in both to hedge.

## Trust & verifiability
`trust: community` — an established, widely-cited independent archive; snapshots are frozen server-side renders so content integrity is strong, but the operator is anonymous and the service occasionally changes domains/blocks scrapers.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | archive-today |
| category | archives-cache |
| selectorsIn → selectorsOut | domain, social-profile → social-profile, name, image |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (captcha) |
