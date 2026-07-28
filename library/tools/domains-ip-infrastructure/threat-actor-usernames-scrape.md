---
id: threat-actor-usernames-scrape
name: Threat Actor Usernames Scrape
description: Use when you have a `username` and want to know whether it appears among ~812k handles scraped from cybercrime/dark-web forums — returns social-profile/associate leads.
url: https://github.com/spmedia/Threat-Actor-Usernames-Scrape
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Checking a username against a free bulk dataset of cybercrime-forum handles for CTI enrichment.
selectorsIn:
- username
selectorsOut:
- social-profile
- associate
status: live
pricing: free
costNote: Free, open dataset on GitHub (text/JSON files); clone or download, no account.
opsec: passive
opsecNote: Searching is done locally against downloaded files, so nothing touches any forum or the subject — fully passive. Cloning the repo is a normal GitHub action. Do not log into the source cybercrime forums yourself to "confirm" a hit; that is active and risky.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A single researcher's (spmedia) crowd-scraped compilation from active and defunct forums; unofficial and unvetted. Presence is a lead, not identity proof, and the data can be stale or contain scraping artefacts.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
relatedTools:
- phishingseclists
- crypto-scam-and-crypto-phishing-url-threat-intel-feed
- telegram-channel-joiner
aliases:
- spmedia Threat Actor Usernames
tags:
- threat-actor-search
- username
- dark-web
source: awesome-osint
lastVerified: '2026-07-28'
enrichment: full
---

# Threat Actor Usernames Scrape

> A free, downloadable dataset of ~812k usernames scraped from cybercrime and dark-web forums (Cracked, HackForums, Dread, the old BreachForums, Nulled, and more) — a poor-man's threat-intel corpus.

## When to use
You have a `username` (or a handle a subject reuses) and want to know whether it surfaces on cybercrime forums — a quick way to tie an alias to threat-actor activity without paying for a commercial CTI platform. Infrastructure/CTI-oriented; low relevance to typical missing-person work but useful when an investigation touches fraud or online-crime personas.

## How to use it (`bestInteractionPattern`: cli)
1. Clone or download the repository from GitHub.
2. Search the text/JSON files locally for the target username (e.g. `grep -ri "<handle>"`).
3. Note which forum source(s) the handle appears in and whether the forum is active or defunct.
4. Treat a match as a lead: the same string can belong to different people across sites.
5. Pivot: a forum handle → username-search tools to find the same alias elsewhere; correlate registration timing/context to build an `associate`/persona map.

## Inputs → Outputs
- **In:** `username` / handle
- **Out:** forum-source matches (a `social-profile`/`associate` lead pointing at cybercrime-forum presence)
- **Empty/negative result looks like:** no match in the files — meaning the handle isn't in this particular scrape, not that it never existed on any forum. Coverage is limited to the sources the author scraped.

## Gotchas & OpSec
- **Leads, not proof:** a username collision does not identify a person; corroborate before attributing.
- Static snapshot — it ages; re-pull for the latest, and don't assume completeness.
- Do NOT visit/log into the source forums to verify; searching the local dataset is the passive, safe step.

## Overlaps ("do both")
- Pairs with username-enumeration tools (to find the alias across the clear web) and with `[[phishingseclists]]` for related threat-intel corpora.

## Trust & verifiability
`trust: community` — an unofficial, single-maintainer scrape. Good for cheap enrichment and lead generation; verify any attribution through independent evidence before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | threat-actor-usernames-scrape |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | username → social-profile, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
