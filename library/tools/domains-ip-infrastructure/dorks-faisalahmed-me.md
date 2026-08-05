---
id: dorks-faisalahmed-me
name: dorks.faisalahmed.me (ReconNexus)
description: Use when you have a `domain` and want a one-page launcher of recon/OSINT lookups (DNS, breach, dork-style queries) for it — returns links out to those tools, not data itself.
url: https://dorks.faisalahmed.me
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: A single-page recon dashboard that fans a target domain out to ~15+ DNS/OSINT/breach lookups.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free web app; no account required.
opsec: passive
opsecNote: The page itself just builds and links out to queries, so loading it is passive. But each link you follow runs a real lookup against the target `domain` on a third-party service — some (breach lookups, active DNS/port tools) are active or logged. Treat the OpSec of each destination tool individually and use a sock-puppet session.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: A personal project (formerly a Google-dork constructor, now branded "ReconNexus"); it aggregates links to external tools, so its value is convenience, not any first-party data.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- ReconNexus
- faisalahmed dorks
tags:
- Domain/IP/Links
- Dorks/Pentest/Vulnerabilities
source: cyb-detective
lastVerified: '2026-08-05'
enrichment: full
---

# dorks.faisalahmed.me (ReconNexus)

> A one-page recon launcher: type a domain and it hands you pre-built links into ~15+ DNS, OSINT, breach, and dork-style lookups — a time-saver, not a data source.

## When to use
You have a `domain` and want to blitz the standard opening moves of a website investigation without hand-typing each tool's URL. The page (now branded ReconNexus) pre-fills queries for DNS/WHOIS, subdomain and breach lookups, encoders, and Google-dork-style searches, so you click through instead of copy-pasting. Reach for it at the start of domain triage.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://dorks.faisalahmed.me (append `?d=example.com` to auto-load a target).
2. Enter the target `domain`.
3. Click the pre-built links you want — each opens the relevant third-party tool with your domain already queried.
4. Read results on the destination tools, not here.
5. Pivot: subdomains, mail records, and breach hits become new selectors (`ip-address`, `email`) for the rest of your workflow.

## Inputs → Outputs
- **In:** a `domain`
- **Out:** links to external lookups that themselves return `domain`/DNS/breach data — this tool only routes you
- **Empty/negative result looks like:** a link opens to a third-party tool that returns nothing — that is the destination's result, not this launcher's; the launcher "works" as long as the links build.

## Gotchas & OpSec
- Human-in-the-loop: none to use the launcher; destination tools may require their own logins/CAPTCHAs.
- OpSec: loading the page is passive, but following links fires real queries at the target across many services — some active/logged. Assume each click is attributable; use a puppet session.
- It is a personal aggregator and can rot as linked tools change; verify a destination still works.

## Overlaps ("do both")
- Pairs with a full recon framework or a curated dork list — this is the quick "open all the tabs" convenience layer; the heavy lifting happens in the tools it links to.

## Trust & verifiability
`trust: unverified` — a single-author convenience page with no first-party data; every actual finding must be read and verified on the underlying tool it sends you to.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | dorks-faisalahmed-me |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
