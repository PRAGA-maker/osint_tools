---
id: whatsmyname-python
name: WhatsMyName-Python
description: Use when you have a `username` and want to enumerate which of 600+ sites have an account with that handle — returns matching social-profile links and confirmed usernames.
url: https://github.com/C3n7ral051nt4g3ncy/WhatsMyName-Python
category: username
path:
- username
bestFor: Fast, wide username enumeration across hundreds of social/web platforms using the community WhatsMyName (wmn-data) dataset.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free and open-source (Python); install locally, no account or API key.
opsec: active
opsecNote: The script sends a request to each target site to test whether the username exists, so your IP touches hundreds of platforms in a burst. It never contacts the target person, but the traffic pattern is distinctive — run it behind a VPN/proxy and avoid an attributable IP.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Python port of the well-known WhatsMyName project by C3n7ral051nt4g3ncy; built on the community-maintained wmn-data.json used across many OSINT tools, so coverage is broad and widely trusted.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- WhatsMyName
- WMN
tags:
- username-enumeration
- sherlock-alternative
- social-discovery
source: gh-topic-intelligence-gathering
lastVerified: '2026-07-10'
enrichment: full
---

# WhatsMyName-Python

> A core username-pivot tool — feed one handle and it reports which of 600+ sites host an account under it, mapping a person's social footprint from a single username.

## When to use
You have a `username` (or a strong candidate handle) and want to know everywhere it exists online. This is one of the first moves in username-based OSINT: a missing person's known handle often repeats across dozens of platforms, and WhatsMyName turns that one handle into a list of `social-profile`s to investigate. Built on the same wmn-data.json dataset many OSINT tools share, it balances breadth with a low false-positive rate.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo and install (`pip install -r requirements.txt` / per the README).
2. Run against a username: `python whatsmyname.py -u <username>` (flags vary; see `-h`).
3. Review the confirmed hits — each is a platform where the handle resolves to an existing account.
4. Manually open and verify each hit; username existence does NOT prove it's the same person.
5. Pivot: confirmed profiles feed platform-native OSINT; profile bios often reveal the real `name`, email, or linked accounts to chase next.

## Inputs → Outputs
- **In:** `username`
- **Out:** `social-profile` (accounts found across sites), `username` (confirmed handle per platform)
- **Empty/negative result looks like:** few or no hits — meaning the handle is uncommon or unused; conversely, a common handle yields many hits belonging to different people, so treat all results as leads to verify.

## Gotchas & OpSec
- **Same handle ≠ same person:** popular usernames collide; always confirm identity on each platform.
- Site checks drift out of date; keep the wmn-data list updated to reduce false positives/negatives.
- **Active:** it hammers hundreds of sites from your IP — use a VPN/proxy.

## Overlaps ("do both")
- Pairs with Sherlock and `[[sylva-identity-discovery]]` — run more than one enumerator, since each covers a slightly different site list; Sylva then branches from the confirmed handles to linked identities.

## Trust & verifiability
`trust: community` — a widely used open-source tool on a shared, community-vetted dataset; results are reliable as *leads*, but each hit must be manually confirmed as the same individual.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | whatsmyname-python |
| category | username |
| selectorsIn → selectorsOut | username → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
