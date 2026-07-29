---
id: seclists
name: SecLists
description: Use when you need ready-made `username`, `password`, and name/subdomain wordlists to seed enumeration or credential-stuffing checks — returns curated list files, not lookups on a person.
url: https://github.com/danielmiessler/SecLists
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: A one-stop collection of usernames, passwords, and fuzzing wordlists to feed other enumeration tools.
selectorsIn: []
selectorsOut:
- username
- password
status: live
pricing: free
costNote: Free and open-source; clone the GitHub repo (large — hundreds of MB).
opsec: passive
opsecNote: The repo itself is inert reference data — cloning it touches only GitHub and reveals nothing about a target. OpSec risk arises from what you DO with the lists (spraying credentials or enumerating names is active and often intrusive); the lists alone are passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Widely used, well-maintained community project by Daniel Miessler and contributors; the de-facto standard wordlist collection in security work.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- robotsdisallowed
- seclists-dns-subdomains
aliases:
- danielmiessler SecLists
tags:
- related-awesome-lists
- wordlists
source: awesome-osint
lastVerified: '2026-07-29'
enrichment: full
---

# SecLists

> The standard open-source collection of security wordlists — usernames, passwords, common names, and subdomain lists — that feed enumeration and fuzzing tools rather than answering a query itself.

## When to use
You are running another tool that needs input lists: subdomain brute-forcing, username enumeration across sites, or checking whether a subject reuses a common password pattern. SecLists supplies vetted, categorised wordlists so you do not hand-assemble them. It surfaces no intelligence on a person by itself — it is raw material for other steps.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo: `git clone https://github.com/danielmiessler/SecLists.git` (it is large; shallow-clone if you only need one folder).
2. Browse the top-level folders: `Usernames/`, `Passwords/`, `Discovery/DNS/` (subdomains), `Discovery/Web-Content/`, etc.
3. Point the relevant tool at the chosen list, e.g. a subdomain brute-forcer at `Discovery/DNS/subdomains-top1million-5000.txt`.
4. For people-OSINT, `Usernames/` lists help seed username-search sweeps; `Names/` lists help guess handles.
5. Pivot: outputs feed enumeration tools like `[[seclists-dns-subdomains]]`-style workflows and username-search across sites.

## Inputs → Outputs
- **In:** none (it is a static dataset you select from)
- **Out:** wordlist files of `username`, `password`, name, and subdomain candidates
- **Empty/negative result looks like:** N/A — it is reference data; "failure" is only picking the wrong list for the task.

## Gotchas & OpSec
- It is huge; clone selectively or you waste disk and time.
- Using the lists against live targets (password spraying, enumeration) is **active and can be intrusive/illegal without authorisation** — the ethics live in the usage, not the repo.
- Keep it updated; lists evolve as new leaks are curated.

## Overlaps ("do both")
- Pairs with `[[seclists-dns-subdomains]]` and `[[robotsdisallowed]]` and any brute-forcer/username-search tool that consumes a wordlist.

## Trust & verifiability
`trust: community` — mature, heavily-used open-source project; the lists are transparent files you can inspect directly before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | seclists |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut |  → username, password |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
