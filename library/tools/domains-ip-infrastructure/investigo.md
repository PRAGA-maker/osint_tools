---
id: investigo
name: Investigo
description: Use when you have a `username` and want every social platform it exists on — a fast Go CLI (Sherlock-based) that checks the handle across hundreds of sites, returning matching `social-profile` links.
url: https://github.com/tdh8316/Investigo
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Enumerating which of hundreds of social/web platforms a given username exists on, and optionally downloading the found accounts' data.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, open-source Go tool (tdh8316/Investigo); build from source with the Go toolchain.
opsec: active
opsecNote: It directly requests a profile URL on every site it checks, so a run fans out hundreds of connections from your IP — a distinctive pattern to those platforms. Use the built-in `--tor` flag (or a VPN/sock-puppet egress) so the enumeration isn't tied to you.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Active open-source project reusing the Sherlock site database; accuracy tracks Sherlock's — expect occasional false positives/negatives from sites that changed their "user not found" behaviour.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- tdh8316/Investigo
tags:
- Domain/IP/Links
- username-enumeration
- Searchers, scrapers, extractors, parsers
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Investigo

> A Go-based username hunter: give it a handle and it checks hundreds of platforms in parallel, reporting every site where that username has an account — with an option to download the accounts' content.

## When to use
You have a `username` (from an email local-part, a gamertag, a reused handle) and want to find the subject's presence across the web fast. Investigo runs the Sherlock-style check — hundreds of sites at once — and hands back a list of live `social-profile` URLs to pivot into. Reusing a handle across platforms is one of the strongest OSINT pivots, which is why this is genuinely useful in missing-person work.

## How to use it (`bestInteractionPattern`: cli)
1. Install: clone `https://github.com/tdh8316/Investigo` and `go build` (needs a recent Go toolchain), or grab a release binary.
2. Run: `investigo USERNAME` (pass several usernames to check them all).
3. Add flags as needed: `--tor` to route through Tor, `--sites` to limit to specific platforms, `--download` to pull found accounts' data.
4. Read the output — confirmed accounts with their profile URLs; open the real profiles to verify it's the same person (avatar, bio, location).
5. Pivot each `social-profile` into profile-analysis, avatar reverse-image, and cross-account correlation.

## Inputs → Outputs
- **In:** `username` (one or many)
- **Out:** `social-profile` URLs on every platform where the handle resolves
- **Empty/negative result looks like:** few or no hits — the handle is unused, unique to one site, or the subject varies handles per platform; a "found" that 404s on manual check is a false positive.

## Gotchas & OpSec
- **False positives/negatives** are inherent to handle-enumeration — always open and eyeball each hit; a matching username is not proof of the same person.
- The fan-out of requests is **active** and identifiable; use `--tor`/VPN and a sock-puppet posture.
- `--download` fetches account content directly from the platforms — heavier footprint and possible ToS issues; use deliberately.
- Coverage/accuracy follow the Sherlock database's freshness.

## Overlaps ("do both")
- Overlaps with other username-enumeration tools (Sherlock, Maigret, WhatsMyName) — they share site lists but drift apart on coverage and false-positive handling, so running a second checker catches accounts one misses. Confirm survivors by hand.

## Trust & verifiability
`trust: community` — a maintained open-source tool built on the Sherlock dataset; treat every hit as a lead to verify on the live profile, never as confirmation on its own.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | investigo |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
