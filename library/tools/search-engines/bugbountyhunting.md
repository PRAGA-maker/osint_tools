---
id: bugbountyhunting
name: BugBountyHunting
description: Use when you have a vulnerability class or technique and want real-world writeups/resources — returns a keyword-searchable index of bug-bounty reports and reference material.
url: https://www.bugbountyhunting.com
category: search-engines
path:
- search-engines
bestFor: A community-curated, keyword-searchable database of bug-bounty writeups and vulnerability references (XSS, SSRF, SQLi, RCE, IDOR, Web3).
selectorsIn: []
selectorsOut: []
status: live
pricing: free
costNote: Free and public; no login required to search or browse. Community-submitted content.
opsec: passive
opsecNote: Passive reading of a public knowledge base; you search techniques, not a target. Nothing about a subject is disclosed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Community-curated aggregator of third-party writeups; quality varies by submission, so treat entries as leads and read the original reports.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- bugbountyhunting.com
tags:
- Search engines
- Bugbounty/vulnerabilities search tools
source: cyb-detective
lastVerified: '2026-08-04'
enrichment: full
---

# BugBountyHunting

> A searchable index of real-world bug-bounty writeups and vulnerability references — a security-research knowledge base, tangential to person-finding.

## When to use
You are working the security/technical angle of a case and want concrete, real-world examples of how a given vulnerability class is found and exploited, or reference material on a specific technique (XSS, SSRF, SQLi, RCE, IDOR, Web3). It indexes writeups; it does not return data about a domain, IP, or person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.bugbountyhunting.com.
2. Use the search box with a vulnerability keyword or technique.
3. Review the matching community writeups and FAQ explanations; follow each out to the original report.
4. Use it to understand or reproduce a technique, or to find prior art on a class of bug.

## Inputs → Outputs
- **In:** a vulnerability class / technique keyword (not a personal selector)
- **Out:** links to relevant writeups and reference material
- **Empty/negative result looks like:** no matching writeups — the technique may be niche or newly named; broaden the keyword or check primary sources (HackerOne reports, blogs).

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive; you disclose nothing about a subject.
- Community-submitted — entry quality varies; always read the linked primary writeup.

## Overlaps ("do both")
- Complements `[[control-validation-compass]]`: BugBountyHunting is offense-oriented real-world writeups, Control Compass maps techniques to detections and tests — use together for both attack and defense context.

## Trust & verifiability
`trust: community` — a useful curated index; reliability rests on the underlying third-party writeups, so verify at the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bugbountyhunting |
| category | search-engines |
| selectorsIn → selectorsOut |  →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
