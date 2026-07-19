---
id: small-tool-to-retreive-vk-com-vkontakte-users-hidden-metadata-state-access-dates-counts-etc-anonymously-without
name: VK FOAF Metadata Retriever
description: Use when you have a VK (VKontakte) numeric user id and want hidden profile metadata without logging in — returns account creation/last-seen dates, state, and other FOAF fields via VK's public FOAF endpoint.
url: https://gist.github.com/cryptolok/8a023875b47e20bc5e64ba8e27294261
category: social-networks
path:
- social-networks
bestFor: Pulling a VK user's hidden FOAF metadata (created/last-login dates, state) anonymously via a small Bash script.
selectorsIn:
- username
- social-profile
selectorsOut:
- dob
- metadata-exif
- name
status: degraded
pricing: free
costNote: Free single-file Bash gist (public); no cost, no account.
opsec: passive
opsecNote: It reads VK's public FOAF XML endpoint with curl and does not log in, so the request is not tied to your VK identity and the target isn't notified. Still route via a sock-puppet IP; VK can log the requesting address, and the FOAF endpoint's availability changes over time.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: An old community gist (cryptolok) that scrapes VK's FOAF endpoint; the technique is genuine but brittle — VK has tightened access, so many profiles now return "deleted/disallowed," and results depend on the target's privacy state.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- VK FOAF scraper
- vkontakte hidden metadata tool
tags:
- vk
- vkontakte
- metadata
- foaf
source: metaosint
lastVerified: '2026-07-19'
enrichment: full
---

# VK FOAF Metadata Retriever

> A small Bash script that queries VKontakte's public FOAF endpoint for a user id and parses out hidden metadata — account creation and last-login dates, profile state, and counts — without logging in. A classic VK-OSINT trick, now brittle.

## When to use
You have a VK numeric user id (resolve a vanity `username` to its id first) and want metadata VK doesn't show on the normal profile: when the account was created, when it was last active, its state, and other FOAF fields. Useful for dating an account's origin (spotting a freshly-made sockpuppet), inferring activity/timezone from last-seen, or confirming a profile is real vs deleted.

## How to use it (`bestInteractionPattern`: cli)
1. Get the script from the gist (https://gist.github.com/cryptolok/8a023875b47e20bc5e64ba8e27294261) and make it executable.
2. Resolve the target's VK id (a vanity name maps to a numeric id via VK's method or the page source).
3. Run the script with the numeric id; it curls `https://vk.com/foaf.php?id=<id>` and greps the XML for created/modified/last-login dates, state, and counts.
4. Read the fields — `ya:created`, `ya:modified`, `ya:lastLoggedIn`, profile state; interpret dates in VK's timezone context.
5. Pivot: a creation date helps date a persona; last-seen supports timezone/behaviour inference; a confirmed real `name`/state feeds other VK and people-search tools.

## Inputs → Outputs
- **In:** VK numeric id (from a `username`/`social-profile`)
- **Out:** account `dob`-style creation/last-login dates, `metadata-exif`-style FOAF fields (state, counts), sometimes a display `name`
- **Empty/negative result looks like:** `publicAccess: disallowed` / `profileState: deleted`, or empty fields — the profile is deleted, private, or VK has restricted FOAF for it; this is common now and not a script bug per se.

## Gotchas & OpSec
- Human-in-the-loop: none, but you must first resolve a vanity name to a numeric id.
- OpSec: **passive/anonymous** (no VK login), but route through a sock-puppet IP; VK still logs the requesting address.
- Brittleness: the FOAF endpoint has been progressively locked down; many profiles return deleted/disallowed regardless of reality. Treat a null result as "unavailable," not proof of anything, and verify the id is correct.

## Overlaps ("do both")
- Pairs with full VK-OSINT suites and username-resolution tools — this narrow trick gets FOAF timestamps a normal profile view hides, while the broader tools resolve ids, enumerate friends/photos, and pull richer profile data.

## Trust & verifiability
`trust: community` — a small, aging gist implementing a real but fragile technique; when it returns data the fields come straight from VK's own FOAF XML (verifiable by fetching the endpoint yourself), but its reliability is limited by VK's tightening access.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | small-tool-to-retreive-vk-com-vkontakte-users-hidden-metadata-state-access-dates-counts-etc-anonymously-without |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → dob, metadata-exif, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
