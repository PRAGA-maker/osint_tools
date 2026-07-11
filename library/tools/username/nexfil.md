---
id: nexfil
name: NExfil
description: Use when you have a `username` and want to find matching accounts across ~350 platforms fast — returns social-profile links.
url: https://github.com/thewhiteh4t/nexfil
category: username
path:
- username
bestFor: Fast username enumeration across hundreds of social/web platforms from the CLI.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free and open-source (MIT). No account or API key required.
opsec: active
opsecNote: NExfil connects directly from your host to each of the ~350 target sites to check for the username, so those sites see your IP and user-agent. Run it from a VPN/sock-puppet network if you don't want the enumeration traced back to you. It does not log in anywhere, so no account is exposed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Maintained by thewhiteh4t, a well-known OSINT tool author; open source and inspectable, but results are unverified matches you must confirm by hand.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
aliases:
- nexfil
tags:
- username-check
- username-enumeration
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# NExfil

> A fast command-line username hunter that checks a handle against ~350 sites in under 20 seconds.

## When to use
You have a `username` (a handle the subject reuses) and want a quick, broad sweep for accounts carrying that same name across social media, forums, dev sites, and web services. Reach for it early in username-pivoting to build a candidate list of `social-profile` URLs, then verify each by hand.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install nexfil` (or clone `https://github.com/thewhiteh4t/nexfil` and `pip install -r requirements.txt`). Python 3 required.
2. Single handle: `nexfil -u johndoe`. Multiple: `nexfil -l johndoe,john.doe`. From a file: `nexfil -f users.txt`.
3. Read the output: it prints each URL where the username was found. Results are also written to a `.txt` file.
4. Verify every hit manually — a "found" line only means the URL exists, not that it belongs to your subject.
5. Pivot: confirmed profiles feed `[[nexfil]]`-adjacent tools and cross-checks; a distinctive bio/photo on one profile feeds reverse-image and name searches.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` (list of URLs where the handle resolves)
- **Empty/negative result looks like:** no found lines / an empty results file — the handle isn't in NExfil's site list under that name. That is not proof the person has no accounts, only that this handle wasn't matched.

## Gotchas & OpSec
- False positives: some sites return a generic page for any handle; always open and eyeball the hit.
- OpSec: **active** — you touch every checked site directly. Use a VPN/sock-puppet IP for sensitive work.
- Site list drifts as platforms change their detection; a "not found" can be a broken checker rather than a real absence. Cross-check with a second enumerator.

## Overlaps ("do both")
- Pairs with broader username tools and manual checks — run more than one enumerator because each covers a different, partially-overlapping site list, so one finds what the other misses.

## Trust & verifiability
`trust: community` — open-source and from a reputable author, but it is an automated matcher: treat every result as a lead to confirm, not a fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nexfil |
| category | username |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
