---
id: cvecrowd
name: CVECrowd
description: Use when you have a `domain`/product and want to know which CVEs the security community is actively discussing right now — returns trending CVEs with Fediverse/Bluesky chatter.
url: https://cvecrowd.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Spotting which vulnerabilities are being talked about in real time across Mastodon/Bluesky, as a successor to the defunct CVETrends.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free to browse; optional account. No paywall on the trending feed.
opsec: passive
opsecNote: You read a public trends site; nothing is sent to any target. Searching by CVE or product leaks only to CVECrowd's own logs.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent project by a security researcher; aggregates public posts from the Fediverse and Bluesky. Signal reflects social chatter, not authoritative severity.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- CVE Crowd
- Crowd Intelligence on CVEs
tags:
- vulnerabilities
- threat-intel
- trending
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# CVECrowd

> A live "what's the security community talking about" board: trending CVEs ranked by how much they're being discussed on the Fediverse and Bluesky.

## When to use
You are assessing the infrastructure or software behind a subject (a `domain`, a self-hosted service, a product) and want an early-warning read on which vulnerabilities are actively being weaponized or discussed — before they surface in slower vulnerability databases. CVECrowd is a triage/awareness tool, not a per-target scanner; its missing-persons relevance is low and indirect (understanding exposure of a site tied to a case).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cvecrowd.com — the front page lists CVEs trending in the last 24 hours / 7 days.
2. For each CVE, read the CVSS/EPSS scores, official description, post/interaction counts, and the threaded discussion pulled from Mastodon and Bluesky.
3. Search a specific CVE ID or product name to see whether it is currently being discussed.
4. Pivot: take a CVE affecting the subject's stack into a vuln database (NVD) or a passive scanner to check whether the subject's `domain` is exposed.

## Inputs → Outputs
- **In:** a CVE ID or product/`domain` context you're investigating
- **Out:** trending CVEs, community discussion volume, links back to source posts (which can surface researcher `social-profile`s discussing an exploit)
- **Empty/negative result looks like:** a CVE with no posts / not on the trending list — means low social chatter, NOT that it is unexploited or low-risk.

## Gotchas & OpSec
- Trend rank measures social buzz, not real-world exploitation or severity — a quiet CVE can still be actively exploited.
- Coverage is limited to the decentralized networks it monitors (Fediverse + Bluesky); Twitter/X-only chatter is invisible since the API restrictions that killed the original CVETrends.
- OpSec: fully passive reading of a public site.

## Overlaps ("do both")
- Complements authoritative databases (NVD/MITRE) and passive scanners — CVECrowd tells you what is *hot*, those tell you what actually *affects the target*. Use the social signal to prioritize, the databases to confirm.

## Trust & verifiability
`trust: community` — a well-regarded independent project, but its ranking is a social-chatter proxy; always confirm a CVE's applicability and severity against a primary source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cvecrowd |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
