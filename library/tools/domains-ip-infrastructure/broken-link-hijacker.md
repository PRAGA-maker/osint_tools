---
id: broken-link-hijacker
name: Broken Link Hijacker (BLH)
description: Use when you have a `domain` and want to crawl it for dead links (in `<a href>`/`<img src>`) — returns broken URLs whose expired domains may be hijackable or reveal defunct infrastructure.
url: https://github.com/MayankPandey01/BrokenLinkHijacker
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Crawling a site to enumerate broken outbound links and flag potentially claimable expired domains.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free, open-source Python CLI.
opsec: active
opsecNote: The crawler actively fetches pages on the target site to test its links, so the target's server sees your requests. It is a light crawl, but not passive — run from a sock-puppet host and respect scope/authorization; only crawl sites you're permitted to test.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: Small community bug-bounty tool (~100 stars, limited maintenance); functional but unaudited — verify its findings manually.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools: []
aliases:
- BLH
- BrokenLinkHijacker
tags:
- Domain/IP/Links
source: cyb-detective
lastVerified: '2026-07-28'
enrichment: full
---

# Broken Link Hijacker (BLH)

> A fast Python crawler that walks a website and reports its broken links (from `<a href>` and `<img src>`) — the first step in spotting expired, potentially claimable domains a site still points to.

## When to use
You have a `domain` and want to map its dead outbound links. In security/OSINT this surfaces (1) **broken-link-hijacking** opportunities — expired domains the site still links to that an attacker (or you, defensively) could register — and (2) defunct infrastructure a subject or organization once used but abandoned, which is itself a lead. It's an infrastructure-recon tool, so missing-persons relevance is indirect.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and install: `git clone https://github.com/MayankPandey01/BrokenLinkHijacker && cd BrokenLinkHijacker && pip install -r requirements.txt`.
2. Run: `python3 BLH.py -u https://example.com` (use `-d 1..3` for crawl depth, `-o` to save output).
3. It crawls the site, extracts links, and lists which return errors (dead).
4. For each broken link, check whether the target domain is unregistered/expired (WHOIS) — those are the hijackable/lead-worthy ones.
5. Pivot: an expired domain a subject relied on can be researched via archives; a defensively-relevant one should be reported to the site owner.

## Inputs → Outputs
- **In:** `domain` (site URL to crawl)
- **Out:** `domain` (list of broken/dead links found on the site)
- **Empty/negative result looks like:** no broken links reported — the site's links currently resolve (at your crawl depth); increase depth or accept the site is well-maintained.

## Gotchas & OpSec
- **Active crawl:** the target server logs your requests — get authorization and use a disposable host; keep depth modest to stay light.
- A broken link isn't automatically hijackable — confirm the linked domain is actually expired/unregistered via WHOIS before drawing conclusions.
- Small, lightly-maintained tool; sanity-check results and watch for false positives (temporary 5xx, rate-limiting).

## Overlaps ("do both")
- Pairs with WHOIS/registration tools (to confirm an expired link is claimable) and with `[[xurlfind3r]]` — do both, since URL discovery and live broken-link crawling reveal different slices of a site's link graph.

## Trust & verifiability
`trust: unverified` — a small community tool; its crawl output is directly verifiable (re-check any flagged link and WHOIS the target), so confirm each finding manually before acting.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | broken-link-hijacker |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
