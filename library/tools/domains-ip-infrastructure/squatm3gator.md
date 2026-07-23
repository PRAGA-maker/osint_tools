---
id: squatm3gator
name: Squatm3gator
description: Use when you have a `domain` and want to enumerate look-alike / typosquat variants and see which are registered — returns candidate squatted domains.
url: https://github.com/david3107/squatm3gator
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Generating and checking cybersquatting / typosquat variants of a domain (substitution, flip, homoglyph).
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open source; self-hosted via Docker. No account or key.
opsec: passive
opsecNote: Generation is local; the registration checks query WHOIS/DNS for the candidate domains, not the original target's servers — so the subject of the original domain sees nothing. The squat domains' registrars/DNS may log the lookups from your host; use a VPN/VPS if that matters.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: docker
trust: community
trustNote: Black Hat Arsenal-presented open-source tool (built on squatm3). Solid for generating variants; "available/registered" status is only as fresh as the WHOIS/DNS it queries at run time.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- squatm3
- david3107/squatm3gator
tags:
- domain-and-ip-research
- typosquatting
- phishing
source: awesome-osint
lastVerified: '2026-07-23'
enrichment: full
---

# Squatm3gator

> A web/Docker tool that generates cybersquatting variants of a domain — substitution, character-flip, and homoglyph look-alikes — and checks which ones are already registered.

## When to use
You have a target `domain` (a brand, an org, a subject's site) and want to find the look-alike domains that could be — or already are — used to impersonate it for phishing. Investigators use it two ways: defensively, to map the squat surface of a brand; and offensively-adjacent, to discover an *existing* malicious look-alike already registered against a victim.

## How to use it (`bestInteractionPattern`: docker)
1. Clone the repo and bring it up with Docker/`docker-compose`; open the web UI at `http://localhost:5000/`.
2. Enter the original `domain` and choose the cybersquatting techniques: substitution, flipping, homoglyph (fast or complete).
3. Run it — the tool generates the variant permutations and checks each for registration/availability.
4. Focus on the **registered** variants: those are the live look-alikes worth investigating (who owns them, what they host).
5. Pivot: a registered squat domain feeds WHOIS/reverse-WHOIS (`[[whoisology]]`) and content/phishing checks (`[[https-openphish-com-feed-txt]]`).

## Inputs → Outputs
- **In:** a base `domain`
- **Out:** generated look-alike `domain` variants, flagged registered vs available
- **Empty/negative result looks like:** all variants "available" — no active squats found for the techniques you ran; broaden the technique set (complete homoglyph) before concluding none exist.

## Gotchas & OpSec
- Registration status is a point-in-time WHOIS/DNS check; a variant registered after your run won't show. Re-run periodically for monitoring.
- Permutation lists can be large; the "complete" homoglyph mode is thorough but slow.
- OpSec: **passive** toward the original target; the candidate-domain lookups originate from your host.

## Overlaps ("do both")
- Complements dnstwist/urlcrazy-style tools — each uses slightly different permutation logic, so running more than one widens coverage of the squat space.

## Trust & verifiability
`trust: community` — a recognised open-source project. Variant generation is deterministic and reliable; treat "registered/available" as a live lookup you should re-verify before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | squatm3gator |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | docker |
| opsec | passive |
| human-in-loop | no |
