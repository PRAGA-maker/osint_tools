---
id: krebs-on-security
name: Krebs on Security
description: Use when you have a threat-actor alias, breach name, scam pattern, or malware/campaign name and want deep investigative background — returns long-form reporting naming actors, infrastructure, and TTPs.
url: https://krebsonsecurity.com/feed/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Researching threat actors, breaches, and fraud campaigns through in-depth investigative journalism.
selectorsIn:
- username
- domain
selectorsOut:
- associate
- domain
- name
status: live
pricing: free
costNote: Free to read (web and RSS); optional mailing list. No paywall.
opsec: passive
opsecNote: Reading the blog/feed is fully passive — you are consuming published journalism, revealing nothing about your case. Standard browsing hygiene (VPN) is sufficient; do not act on named individuals without independent corroboration.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Written by Brian Krebs, a veteran investigative security journalist with a long track record; reporting is well-sourced, though it is journalism to corroborate, not a primary database.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- KrebsOnSecurity
- Brian Krebs blog
tags:
- osint-rss-feeds
- threat-intelligence
- cybercrime
- reference
source: awesome-osint
lastVerified: '2026-08-04'
enrichment: full
---

# Krebs on Security

> Brian Krebs's investigative security blog — the go-to open source for deep, named reporting on cybercrime actors, breaches, and fraud networks.

## When to use
You have a lead tied to cybercrime or online fraud — a threat-actor `username`/handle, a breach or campaign name, a scam typology, a suspicious `domain` — and you want authoritative background before acting. Krebs regularly names the people and infrastructure behind ransomware crews, botnets, proxy/fraud networks, and SIM-swap rings, often connecting handles to real identities and associates. In a missing-persons or fraud investigation it is a reference layer: it can turn an alias or campaign into named `associate`s, linked `domain`s, and context.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://krebsonsecurity.com/ (subscribe to the RSS feed at `/feed/` to monitor new reporting).
2. Use the site search or a site-scoped web search (`site:krebsonsecurity.com "<alias/breach/domain>"`) for your term.
3. Read the long-form article: note named actors, aliases, associated domains/infrastructure, dates, and cited sources.
4. Treat claims as leads — follow the article's own citations/primary sources to corroborate before relying on any identity attribution.
5. Pivot: named `associate`s and `domain`s feed people-search and infrastructure tools; a confirmed alias feeds username enumeration.

## Inputs → Outputs
- **In:** a threat-actor `username`/alias, breach/campaign name, or `domain`
- **Out:** investigative context → named `associate`s, linked `domain`s, possible real `name`s behind handles
- **Empty/negative result looks like:** no article matches your term — Krebs covers notable/newsworthy cases, so most everyday subjects will not appear; absence here says nothing about the subject.

## Gotchas & OpSec
- Human-in-the-loop: none; it is a blog to read.
- OpSec: **passive** — consuming published journalism leaks nothing about your investigation.
- It is reporting, not a database: attributions can be contested and are point-in-time. Always trace back to the primary sources Krebs cites before treating a name as fact.

## Overlaps ("do both")
- Pairs with primary-source and infrastructure tools like `[[whois-lookup]]` and breach-search resources — Krebs supplies the narrative and names; those tools verify the domains, dates, and accounts he references.

## Trust & verifiability
`trust: trusted` — authored by an established investigative journalist with a strong track record and cited sourcing; still, it is secondary reporting, so corroborate any actionable attribution against the primary evidence it references.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | krebs-on-security |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username, domain → associate, domain, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
