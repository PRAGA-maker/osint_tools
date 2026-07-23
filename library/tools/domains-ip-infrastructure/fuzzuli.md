---
id: fuzzuli
name: fuzzuli
description: Use when you have a `domain` and want to hunt exposed backup/sensitive files on its web server — generates a domain-tailored wordlist and probes URLs, returning reachable file paths.
url: https://github.com/musana/fuzzuli
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Finding leaked backup/archive files (e.g. example.com.zip, backup.sql) by fuzzing domain-derived URL guesses.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open source (MIT); a Go CLI. A hosted web interface exists at fuzzuli.musana.net for light use.
opsec: active
opsecNote: This ACTIVELY probes the target's web server with many requests from your IP — it is intrusive, generates server logs, and can trip WAF/rate limits or look like an attack. Only run it against assets you are authorized to test; use it on your own/authorized infrastructure or with explicit scope. Route through controlled infrastructure and throttle.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: Popular community pentest tool (musana on GitHub); code is open and auditable, but it's an offensive utility, not an institutional service.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- fuzzuli
- musana/fuzzuli
tags:
- url-fuzzing
- backup-file-discovery
- pentest
- domain-and-ip-research
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# fuzzuli

> A Go URL-fuzzer that builds a wordlist from the target's own domain name and probes for exposed backup/archive files — the kind of `example.com.zip` or `db_backup.sql` that leaks source and data.

## When to use
You have a `domain` you're authorized to assess and want to check whether backup or sensitive files are sitting exposed on its web root. fuzzuli's trick is a *dynamic* wordlist derived from the domain (shuffle/reverse/mixed permutations), so it finds host-specific filenames generic wordlists miss. Squarely a security-recon tool — use it for authorized attack-surface assessment of infrastructure tied to an investigation, not against arbitrary third-party sites.

## How to use it (`bestInteractionPattern`: cli)
1. Install the Go binary from https://github.com/musana/fuzzuli (`go install`), or use the hosted UI for light checks.
2. Point it at the target `domain`/URL; choose method(s) — regular, shuffle, reverse, mixed, etc.
3. It generates the tailored wordlist and requests each candidate path, reporting responses that indicate a reachable file (`selectorsOut`).
4. Review any hits manually; a downloadable backup/archive may expose source, configs, or data to feed the rest of your investigation.

## Inputs → Outputs
- **In:** `domain` (target host/URL)
- **Out:** reachable backup/sensitive file URLs on that `domain` (status/size signals)
- **Empty/negative result looks like:** all probes return 404/403 — no exposed backups found by these permutations (or a WAF is blocking you); it's not proof none exist.

## Gotchas & OpSec
- Human-in-the-loop: none, but authorization is mandatory.
- OpSec: **active/intrusive** — heavy request volume straight at the target's server, logged and WAF-detectable. Only run with permission; throttle and use controlled infrastructure.
- Noisy by design; expect blocks and false negatives when a WAF or rate limiter intervenes.

## Overlaps ("do both")
- Pairs with content-discovery fuzzers (ffuf, dirsearch, feroxbuster) — those brute-force common paths, while fuzzuli specializes in domain-derived backup filenames; run both for fuller coverage of an authorized target.

## Trust & verifiability
`trust: unverified` — an open-source community pentest tool; auditable and popular, but offensive tooling whose use is your legal responsibility. Confirm every hit manually before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | fuzzuli |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
