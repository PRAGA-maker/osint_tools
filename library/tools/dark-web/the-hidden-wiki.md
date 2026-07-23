---
id: the-hidden-wiki
name: The Hidden Wiki
description: Use when you have a dark-web investigation and want a starting directory of Tor .onion services — returns categorised links to onion sites (a jump-off point, not a search of a person).
url: http://zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion/wiki/index.php/Main_Page
category: dark-web
path:
- dark-web
bestFor: A categorised index of Tor onion services to orient a dark-web investigation.
selectorsIn: []
selectorsOut:
- social-profile
status: degraded
pricing: free
costNote: Free to browse, but requires the Tor Browser; the canonical .onion address changes over time and countless clones exist.
opsec: active
opsecNote: Reaching it requires Tor — use the Tor Browser on a hardened/throwaway system, never your normal browser or IP. Many "Hidden Wiki" mirrors are scams, phishing, or link to illegal and malware-laden content; treat every link as hostile, click nothing transactional, and be aware of the legal exposure of even visiting some listed services. Verify you have the current legitimate address, as the URL rotates and impostors abound.
humanInLoop: true
humanInLoopReason:
- legal-gate
bestInteractionPattern: web-manual
trust: unverified
trustNote: A community-edited onion directory with no authority behind it; links are unvetted, frequently dead, and often malicious or scam. Useful only as an orientation index, never as a trusted source.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Hidden Wiki
tags:
- darkweb
- Dark Web Links
- onion-directory
source: uk-osint
lastVerified: '2026-07-23'
enrichment: full
---

# The Hidden Wiki

> A long-standing, community-edited directory of Tor onion services — a rough table of contents for the dark web to orient an investigation, with the heavy caveat that its links are unvetted, often dead, and frequently malicious.

## When to use
You are conducting an authorised dark-web investigation and need a starting index of onion services — marketplaces, forums, services, wikis — rather than a search of a specific person. Reach for The Hidden Wiki to get your bearings on what onion resources exist in a category. It is a jump-off directory, not a lookup: it won't resolve a username or email, and everything it lists must be independently verified. Because the address rotates and clones are rampant, confirm you have the legitimate current URL before trusting anything.

## How to use it (`bestInteractionPattern`: web-manual)
1. Using the Tor Browser on a hardened/isolated system, obtain the *current* legitimate Hidden Wiki address from a reputable source (addresses change; the one recorded here may be stale).
2. Browse the categorised link lists to see what onion services exist in your area of interest.
3. Treat every link as untrusted — expect dead links, phishing clones, scams, and illegal content. Do not log in, transact, or download.
4. Cross-check any onion service against other dark-web indexes and reputable reporting before relying on it.
5. Pivot: a verified onion service can feed targeted dark-web collection; note the strong legal and OpSec constraints throughout.

## Inputs → Outputs
- **In:** none (a category/topic to browse; not a person selector)
- **Out:** categorised onion links (`social-profile`-adjacent service pages) as leads to verify
- **Empty/negative result looks like:** dead links, a mirror that's actually a phishing clone, or listings for services long gone — absence and rot are the norm here, not the exception.

## Gotchas & OpSec
- Human-in-the-loop / legal-gate: some listed services are illegal to access; understand your legal footing before visiting anything.
- Requires Tor; never reach it from your real browser/IP. Use a throwaway, hardened environment.
- Impersonation: many "Hidden Wiki" sites are scams. Verify the address independently and trust nothing it links to.

## Overlaps ("do both")
- Complements dark-web search engines and curated onion indexes — use several, since each rots and each mirror differs. This is orientation only; pair with reputable dark-web monitoring/reporting for anything you'll act on.

## Trust & verifiability
`trust: unverified` — a community-edited, unauthoritative directory riddled with dead and malicious links; it has zero inherent trust, so every listing must be independently confirmed and every visit treated as hostile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-hidden-wiki |
| category | dark-web |
| selectorsIn → selectorsOut |  → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (legal-gate) |
