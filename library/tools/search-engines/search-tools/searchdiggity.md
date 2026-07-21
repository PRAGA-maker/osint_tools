---
id: searchdiggity
name: SearchDiggity
description: Use when you have a `domain` (or org) and want to surface exposed files/credentials via automated search-engine dorking — returns `document-id`/`email` leads from Google, Bing and Shodan.
url: https://bishopfox.com/tools/google-hacking-diggity-project
category: search-engines
path:
- search-engines
- search-tools
bestFor: Automated Google/Bing/Shodan dorking of a domain to find publicly exposed documents, directories and credentials.
selectorsIn:
- domain
selectorsOut:
- document-id
- email
status: degraded
pricing: free
costNote: Free Windows GUI download from Bishop Fox. No licence cost, but several back-ends depend on search-engine APIs (Google/Bing) that have changed since the last major release, so some scanners no longer return results.
opsec: passive
opsecNote: Queries Google, Bing and Shodan about the target domain rather than touching the target's own servers, so it is passive toward the subject. The dork queries run under your IP/API keys and can be throttled or blocked by the search engines; use research infrastructure and API keys you are willing to burn. Do not act on any exposed credentials it surfaces — record, do not use.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: desktop-app
trust: trusted
trustNote: Published by Bishop Fox, an established security consultancy, as part of the long-running Google Hacking Diggity Project; the tool is legitimate, though aging.
missingPersonsRelevance: medium
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
- Google Hacking Diggity
- Diggity
- SearchDiggity 3.1
tags:
- search-tools
- google-dorking
source: arf-seed
lastVerified: '2026-07-21'
enrichment: full
---

# SearchDiggity

> Bishop Fox's Windows GUI front-end to the Diggity dorking suite (GoogleDiggity, BingDiggity, ShodanDiggity, and more) — point it at a domain and it runs curated search-engine dorks to surface exposed data.

## When to use
You have a `domain` or organisation tied to a subject and want to know what is publicly exposed and indexable: leaked documents, directory listings, config files, and occasionally credentials sitting in search-engine caches. Useful in infrastructure/attribution work and when a missing person's associated business or personal site may be leaking contact details or documents.

## How to use it (`bestInteractionPattern`: desktop-app)
1. Download SearchDiggity from the Bishop Fox Google Hacking Diggity Project page and install on a Windows machine (or a Windows VM).
2. Add the API keys the scanners need (e.g. a Bing/Azure key, Shodan key) in the tool's settings — several scanners will not run without them.
3. Choose a scanner tab (GoogleDiggity, BingDiggity, DLPDiggity, ShodanDiggity, etc.), enter the target `domain` as the site/scope, and load a dork dictionary or use the built-in one.
4. Run the scan and review the hits; export the result list.
5. Pivot: open exposed `document-id` files and mine them for `name`/`email`/`address`; cross-check exposed hosts in a live infrastructure tool.

## Inputs → Outputs
- **In:** `domain` / site scope (plus keyword dorks)
- **Out:** a list of indexed URLs and files matching sensitive-data dorks — `document-id` leads, occasionally `email`/`password` exposures
- **Empty/negative result looks like:** no hits, or a scanner erroring out because its search API is unavailable/deprecated — the latter is a back-end limitation, not proof the domain is clean.

## Gotchas & OpSec
- **Human-in-the-loop: api-key.** Bing/Shodan scanners require your own API keys; without them those tabs return nothing.
- The project has not seen a major refresh in years — some Google-based scanners broke when the underlying search APIs changed. Treat SearchDiggity as one dorking option, not an exhaustive one, and be ready to run manual dorks.
- Passive toward the target, but search engines may rate-limit or captcha your queries; never re-use exposed credentials you find.

## Overlaps ("do both")
- Complements manual Google/Bing dorking and Shodan searches — SearchDiggity packages known dork dictionaries so you don't hand-type them, but a live manual search catches what its stale scanners miss.

## Trust & verifiability
`trust: trusted` — authored and distributed by Bishop Fox; every hit is a real search-engine result you can (and should) reopen and confirm directly in Google/Bing/Shodan before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | searchdiggity |
| category | search-engines |
| selectorsIn → selectorsOut | domain → document-id, email |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | desktop-app |
| opsec | passive |
| human-in-loop | yes (api-key) |
