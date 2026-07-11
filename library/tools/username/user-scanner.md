---
id: user-scanner
name: user-scanner
description: Use when you have a `username` or `email` and want to enumerate where it is registered across 300+ sites and breach sources — returns `social-profile`, `email` registration status, breach hints.
url: https://github.com/kaifcodec/user-scanner.git
category: username
path:
- username
bestFor: Fast CLI enumeration of a username/email across hundreds of platforms plus breach-intel enrichment.
selectorsIn:
- username
- email
selectorsOut:
- social-profile
- email
- metadata-exif
status: live
pricing: free
costNote: Free, open-source Python CLI; installable via PyPI (`pip install user-scanner`) or Nix. No account for core scanning; some enrichment sources may have their own limits.
opsec: active
opsecNote: The tool actively queries hundreds of sites for the username/email from your host. Use proxy rotation (built in) and a non-attributable IP; hitting many login/registration endpoints from one address is detectable and rate-limitable.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Open-source project by kaifcodec; inspectable code, but like all username enumerators it produces false positives/negatives as sites change their signup responses.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- kaifcodec user-scanner
tags:
- username-check
- username-enumeration
- email-enumeration
- breach
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
---

# user-scanner

> A 2-in-1 OSINT CLI: check a username or email across 300+ scan vectors and enrich hits with breach intelligence — a Sherlock-style enumerator plus email-registration lookup.

## When to use
You have a `username` (or an `email`) and want to map the subject's footprint fast: which of hundreds of platforms the handle is registered on, whether an email is registered vs available on given services, and whether it appears in breach data (Hudson Rock integration). Ideal early-stage breadth pass to convert one selector into a list of `social-profile` leads.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install user-scanner` (or via Nix).
2. Scan a username: `user-scanner -u johndoe`; scan an email: `user-scanner -e email@example.com`. Bulk lists via `-uf` / `-ef` file flags.
3. Configure proxy rotation for opsec if scanning at volume.
4. Read the console output (platform → Found/Not Found, or Registered/Available) and export structured results to JSON/CSV for the case file.
5. Pivot: open each "Found" `social-profile`, run pattern-generated username variations, and follow breach hints into further email/password intel.

## Inputs → Outputs
- **In:** `username` or `email` (single or bulk)
- **Out:** `social-profile` hits, email registration status, breach `metadata-exif`-style enrichment; JSON/CSV export
- **Empty/negative result looks like:** all "Not Found/Available" — the handle is unused, the sites changed their detection surface, or you're being rate-limited; corroborate a few hits manually before trusting the whole list.

## Gotchas & OpSec
- Username enumerators are inherently noisy — expect both false positives (parked/placeholder pages) and false negatives (sites that block automated checks); verify important hits by hand.
- Active from your IP across many endpoints — use the built-in proxy rotation and a burner IP.
- Breach-intel enrichment (Hudson Rock) may have its own free-tier limits.

## Overlaps ("do both")
- Pairs with other enumerators (Sherlock, Maigret) and with [[namint]] — different tools cover different site lists, and NAMINT supplies the handle variations to feed in.

## Trust & verifiability
`trust: community` — open-source and inspectable, but results are heuristic; always manually confirm a "Found" before asserting the subject owns that account.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | user-scanner |
| category | username |
| selectorsIn → selectorsOut | username, email → social-profile, email, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
