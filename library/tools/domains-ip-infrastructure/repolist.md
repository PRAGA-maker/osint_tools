---
id: repolist
name: Repolist
description: Use when you have a `domain` running a known CMS/framework and want a targeted content-discovery wordlist — generates path/file wordlists from the framework's GitHub repo to fuzz for hidden endpoints.
url: https://github.com/Ademking/repolist
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Building a precise directory/file wordlist from a CMS or framework's own GitHub repo, to feed content-discovery tools against a site built on it.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free, open-source Python CLI (Ademking/repolist); install via pip.
opsec: passive
opsecNote: Generating the wordlist is passive — it only reads a public GitHub repo, nothing touches the target. It becomes active only when you USE the wordlist with a fuzzer (ffuf/gobuster) against a live site, which hits that server and is logged; tunnel that stage and stay in scope.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Small but active open-source utility (100+ stars); it just extracts paths from a repo, so output correctness is transparent and easy to verify.
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
- Ademking/repolist
tags:
- Domain/IP/Links
- Wordlists generators
- content-discovery
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# Repolist

> Turn a framework's GitHub repo into a tailored content-discovery wordlist — instead of generic path lists, fuzz a target with the exact file/dir names its CMS actually ships.

## When to use
You've fingerprinted a target `domain` as running a specific CMS/framework (WordPress, a JS framework, a particular app) and want to find its hidden or default endpoints. A generic wordlist wastes requests; Repolist reads the framework's own GitHub repository and emits the real file and directory names, giving a high-signal wordlist for content discovery against that site.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip3 install repolist`.
2. Point it at the framework's repo: `repolist -u https://github.com/user/repo` (options for branch, token for private repos, files-only/dirs-only, prefixes/suffixes, proxy).
3. It prints the extracted paths as a wordlist.
4. Pipe straight into a fuzzer: `repolist -u "REPO_URL" | ffuf -u "http://target.com/FUZZ" -w -` (or save and feed to gobuster).
5. Review discovered endpoints for exposed configs, admin paths, or leftover files worth investigating.

## Inputs → Outputs
- **In:** a GitHub repo URL (the CMS/framework the target `domain` runs)
- **Out:** a path/file wordlist → used to discover endpoints on the `domain`
- **Empty/negative result looks like:** an empty/tiny wordlist — wrong or empty repo, or a token needed for a private repo; and downstream, all-404s from the fuzzer means the target isn't running that framework's default layout.

## Gotchas & OpSec
- **Two stages, two risk levels:** generating the list is passive; fuzzing the target with it is active and logged — keep that stage in authorized scope and tunnel it.
- Only as relevant as your CMS fingerprint — feed it the *right* repo, or the wordlist won't match.
- Heavy GitHub scraping may hit rate limits; a token (`-t`) helps.

## Overlaps ("do both")
- Feeds content-discovery fuzzers (ffuf, gobuster) — Repolist supplies a framework-specific wordlist, those tools do the actual endpoint discovery; pair Repolist output with a generic list for breadth plus precision.

## Trust & verifiability
`trust: community` — a small, transparent open-source tool that merely extracts public repo paths; its output is trivially verifiable against the source repository.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | repolist |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
