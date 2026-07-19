---
id: web-archive-org
name: web.archive.org (Wayback Machine)
description: Use when you have a domain/URL and want its historical snapshots — returns past versions of a page (deleted content, old contact details, prior identities) and can save a live page now.
url: https://web.archive.org/save
category: archives-cache
path:
- archives-cache
bestFor: Recovering deleted/changed web pages and preserving a live page before it disappears.
selectorsIn:
- domain
selectorsOut:
- document-id
- name
- email
- phone
status: live
pricing: free
costNote: Free public service of the Internet Archive; no account needed to browse snapshots or to Save Page Now.
opsec: passive
opsecNote: Browsing existing snapshots is fully passive — the target's server is not touched, only Archive's. "Save Page Now" is DIFFERENT — it makes the Archive fetch the live URL, which can appear in the target site's logs (from Archive's IP, not yours). Prefer browsing existing captures; only save when you accept that fetch.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the Internet Archive, a long-established nonprofit; snapshots are timestamped and widely accepted as evidence, though captures can be partial.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- archive-org
- internet-archive
- internet-archive-open-source-videos
- internet-archive-videos
- parler-archives
- snitch-list
- the-twitter-stream-grab
- tv-closed-caption-search
- wayback-machine
- wayback-machine-2
- web-archive-org-2
aliases:
- Wayback Machine
- web.archive.org
- Save Page Now
tags:
- archive
- Archive & Cached Related Sites
source: uk-osint
lastVerified: '2026-07-19'
enrichment: full
---

# web.archive.org (Wayback Machine)

> The Internet Archive's time machine for the web — retrieve what a page said before it was edited or deleted, and freeze a live page as timestamped evidence.

## When to use
You have a URL, profile, or `domain` that has changed or vanished and you need what it used to show: a deleted social bio, an old "contact us" page with a phone/email, a since-scrubbed name or address, a company page before it was sanitised, or a listing that's been taken down. It's essential for reconstructing a person's or entity's online history and for preserving volatile evidence (a live profile) before the subject deletes it.

## How to use it (`bestInteractionPattern`: web-manual)
1. To **retrieve history:** go to `https://web.archive.org/web/*/<url>` (or the Wayback Machine homepage) and enter the target URL; pick a date from the calendar of captures.
2. Compare snapshots across dates to see what was added/removed and when — note the exact capture timestamp for citation.
3. Extract selectors from old versions: a `name`, `email`, `phone`, or `document-id` that the live page no longer shows.
4. To **preserve a live page:** submit the URL at `https://web.archive.org/save` (this fetches the live page — see OpSec). Record the resulting archive URL as evidence.
5. Pivot: recovered contact details feed people/phone/email OSINT; an old URL structure feeds domain history.

## Inputs → Outputs
- **In:** `domain` / URL (optionally a date)
- **Out:** historical page versions → `document-id`, plus any `name`/`email`/`phone` those old pages contained
- **Empty/negative result looks like:** "Hrm. Wayback Machine has not archived that URL" — the page was never captured (low-traffic or robots-blocked at the time); try a parent URL, a different capture date, or another archive like `[[archive-today]]`.

## Gotchas & OpSec
- Human-in-the-loop: none, but captures are incomplete — missing dates, broken images/CSS, and pages that blocked archiving simply won't be there.
- OpSec: browsing snapshots is passive; **Save Page Now actively fetches the live target** (from Archive's IP) and can show in the site's logs — don't save if the subject shouldn't see a fetch.
- Sites can retroactively remove their content from the Wayback Machine, so capture what you need promptly.

## Overlaps ("do both")
- Pairs with `[[archive-org]]` (the broader Internet Archive media/books) and `[[archive-today]]`-style mirrors — different archives capture different moments; when one has no snapshot, another often does.

## Trust & verifiability
`trust: trusted` — a first-party Internet Archive service; timestamped captures are broadly accepted as evidence, with the caveat that a capture may be partial and can later be excluded on rights-holder request.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | web-archive-org |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → document-id, name, email, phone |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
