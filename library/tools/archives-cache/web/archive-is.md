---
id: archive-is
name: archive.today (archive.is)
description: Use when you have a `domain`/URL and want a permanent, tamper-proof snapshot of a page — captures and retrieves frozen copies, including pages the Wayback Machine won't archive.
url: https://archive.is/
category: archives-cache
path:
- archives-cache
- web
bestFor: On-demand permanent snapshots of volatile or JS-heavy pages, and retrieving existing captures the Wayback Machine missed.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Completely free; no account or payment. Donations support the anonymous operator.
opsec: passive
opsecNote: Reading an existing snapshot is passive and anonymous. Submitting a NEW capture sends the target URL to archive.today's servers (and its capture bot fetches the page), so avoid archiving a URL that embeds your session token, a private link, or anything that would tip off the site owner. Capture from a research browser/VPN.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: community
trustNote: Long-running, widely-relied-on archive with an anonymous operator; snapshots are byte-frozen and citeable, but there's no institutional accountability behind it.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- wayback-machine
- web-archive-org
aliases:
- archive.is
- archive.today
- archive.ph
- archive.li
tags:
- web-archive
- snapshot
- preservation
source: arf-seed
lastVerified: '2026-07-17'
enrichment: full
---

# archive.today (archive.is)

> The complement to the Wayback Machine: an on-demand archiver that freezes a page (rendered, screenshot + HTML) at a permanent URL — and often has captures Wayback doesn't.

## When to use
You have a URL/`domain` and either (a) want to preserve it *now* before it's edited or deleted (a social post, marketplace listing, blog, forum thread tied to your subject), or (b) want to check whether a page that's gone or paywalled was captured before. archive.today renders JavaScript and stores both a screenshot and the HTML, so it frequently captures dynamic pages and content that the Wayback Machine skips or that sites block via robots.txt. Always run it alongside Wayback, not instead of it — their coverage differs.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the site — it rotates across mirror domains (archive.today, archive.is, archive.ph, archive.li, archive.md); any of them works.
2. **Retrieve:** paste the target URL into the lower ("I want to search the archive") box to list existing snapshots with timestamps; open the one you want.
3. **Capture:** paste the URL into the upper ("My url is alive...") box and submit; solve the CAPTCHA if prompted. You get a short permanent snapshot URL (e.g. `archive.ph/AbCdE`) that won't change.
4. Cite/share the permanent short URL in your notes as tamper-proof evidence.
5. Pivot: compare the frozen copy against the live page (or a Wayback capture) to prove what changed and when.

## Inputs → Outputs
- **In:** a URL / `domain`
- **Out:** a permanent snapshot URL with a frozen screenshot + HTML of the page at capture time
- **Empty/negative result looks like:** "no results" on a retrieve means nobody has archived that exact URL here — try the Wayback Machine, or capture it yourself. A failed capture usually means the page blocked the bot or needed a login.

## Gotchas & OpSec
- CAPTCHA on capture (and sometimes on heavy use) — solve manually; there's no official API.
- It archives the URL you give it *as fetched by its bot*, not your authenticated view — don't expect it to capture login-gated content, and don't paste URLs containing your own session tokens.
- Mirror domains come and go and are occasionally blocked by some networks/DNS; just switch to another mirror.
- Anonymous operator: excellent for preservation, but there's no institution to appeal to if a snapshot is removed.

## Overlaps ("do both")
- Always pair with `[[wayback-machine]]` / `[[web-archive-org]]` — Wayback has deeper historical breadth and an API; archive.today catches JS-rendered and robots-blocked pages Wayback misses. Check both for any URL that matters.

## Trust & verifiability
`trust: community` — a long-standing, heavily-used archive whose snapshots are byte-frozen and independently viewable, but it's run anonymously with no institutional backing, so treat single-source snapshots as strong-but-not-authoritative and corroborate critical evidence with a second archive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | archive-is |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
