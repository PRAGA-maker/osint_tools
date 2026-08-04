---
id: seclists-dns-subdomains
name: SecLists DNS Subdomains
description: Use when you have a `domain` and want high-quality wordlists to feed a subdomain brute-forcer — supplies the input lists, not results, so it yields candidate `domain`s via other tools.
url: https://github.com/danielmiessler/SecLists/tree/master/Discovery/DNS
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- subdomains
bestFor: Supplying curated DNS/subdomain wordlists to drive subdomain enumeration and permutation tooling.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source (MIT); clone or download from GitHub, no account needed.
opsec: passive
opsecNote: The repository itself is inert data — downloading wordlists touches only GitHub and leaks nothing about your target. OpSec risk lives entirely in how you *use* the lists: brute-forcing subdomains against a target's DNS is active and can be logged. Keep that step to passive resolvers or authorized engagements.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: The de-facto standard security wordlist collection, maintained by Daniel Miessler with a large contributor base; widely vetted and used across the industry.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- seclists
tags:
- domains-ip-infrastructure
- subdomains
- wordlists
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# SecLists DNS Subdomains

> The `Discovery/DNS` corner of SecLists — the industry-standard subdomain wordlists that feed brute-force enumeration tools. It's ammunition, not a scanner.

## When to use
You have a target `domain` and you're about to enumerate its subdomains with a resolver/brute-forcer (amass, gobuster, ffuf, dnsx, shuffledns, etc.) and need a good wordlist. SecLists' DNS directory provides everything from tiny top-N lists to multi-million-entry combinations, plus permutation lists. Reaching for a proven wordlist here is what makes the difference between finding `vpn.` / `staging.` / `mail.` subdomains and missing them.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo: `git clone --depth 1 https://github.com/danielmiessler/SecLists.git` (or download just the `Discovery/DNS` folder).
2. Pick a list matched to your time budget — e.g. `subdomains-top1million-5000.txt` for a fast pass, `bitquark-subdomains-top100000.txt` or the large `dns-Jhaddix.txt` for depth.
3. Feed it to your enumeration tool, e.g. `gobuster dns -d target.com -w SecLists/Discovery/DNS/subdomains-top1million-5000.txt` or `ffuf`/`dnsx` equivalents.
4. Read the tool's output — the wordlist only supplies candidates; your resolver confirms which subdomains actually exist.
5. Pivot: resolved subdomains become new `domain`s to fingerprint (hosting, certs, tech stack) and to run through content-discovery.

## Inputs → Outputs
- **In:** `domain` (the target you enumerate against) + a chosen wordlist file
- **Out:** candidate subdomain `domain`s (once run through an external brute-forcer/resolver)
- **Empty/negative result looks like:** not applicable to the repo itself — it always "returns" wordlists. A downstream run that resolves nothing means the wordlist didn't match this target's naming; try a larger or permutation list, or a passive-source approach instead.

## Gotchas & OpSec
- Human-in-the-loop: none for obtaining lists; you drive the actual enumeration tool.
- OpSec: the download is **passive**, but *brute-forcing* subdomains sends live DNS queries that a target can log. Prefer passive sources (CT logs, `[[seclists]]`-driven passive enum) first, and only brute-force where you're authorized.
- Bigger is not always better: huge lists cost time and generate noise. Match list size to the engagement.

## Overlaps ("do both")
- Part of the broader `[[seclists]]` collection — this is specifically its DNS/subdomain slice. Pair with passive subdomain sources (certificate transparency, DNS aggregators): passive finds what exists quietly, brute-forcing with these lists finds what passive missed.

## Trust & verifiability
`trust: trusted` — SecLists is a long-standing, heavily-used, openly-maintained project (Daniel Miessler + many contributors). The wordlists are plain text you can inspect, and their provenance is transparent on GitHub.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | seclists-dns-subdomains |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
