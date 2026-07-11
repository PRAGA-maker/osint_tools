---
id: inteltechniques-people-search-tools
name: IntelTechniques — People Search Tools
description: Use when you have a `name` (or other identifier) and want to fire it across dozens of people-search sites from one form — returns address, phone, email, dob, associate, and social-profile leads.
url: https://inteltechniques.com/menu/pages/person.tool.html
category: people-search
path:
- people-search
bestFor: A single dashboard of pre-built query forms that push one identifier out to many people-search and public-record sites at once.
selectorsIn:
- name
selectorsOut:
- address
- phone
- email
- associate
- social-profile
- dob
status: live
pricing: free
costNote: The tool page (query launcher) is free to use; several of the destination sites it opens are themselves freemium or paywalled once you land there.
opsec: passive
opsecNote: The launcher just builds and opens queries on third-party sites — it doesn't touch the target. OpSec risk lives on each destination: some people-search sites log searches, show ads, or upsell. Run from a sock-puppet browser/VPN and never log in with an attributable account.
humanInLoop: true
humanInLoopReason:
- captcha
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by Michael Bazzell (IntelTechniques), a widely respected OSINT authority; the tool is a well-known, curated launcher, though the underlying data comes from the third-party sites it queries.
missingPersonsRelevance: high
coverage:
- us
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- brb-free-public-records
- spydialer
aliases:
- IntelTechniques search tool
- Bazzell person search tool
tags:
- people-search
- osint-dashboard
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# IntelTechniques — People Search Tools

> Michael Bazzell's curated launcher: type an identifier once and fire it across dozens of people-search and public-record sites without visiting each by hand.

## When to use
You have a `name` (and ideally a corroborating detail — city, approximate age) and want an efficient breadth-first sweep across the major US/global people-search engines and public-record aggregators. Instead of retyping into ten sites, this page holds pre-built forms that open each site's results for your query. Strong opening move in a person/missing-persons trace to quickly see which aggregators have coverage.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://inteltechniques.com/menu/pages/person.tool.html (if a browser challenge appears, complete it; the page is legitimate).
2. Enter the identifier (name, and where offered phone/email/username) into the relevant field.
3. Launch the query for each destination site; each opens that site's results for your input.
4. Read/triage across sites: `address` and `phone` from aggregators, `email`, `associate`s/relatives, `dob`/age, and `social-profile` links.
5. Pivot: corroborate any single hit against a second source (data brokers disagree); confirm phones via [[spydialer]]; reach authoritative records via [[brb-free-public-records]].

## Inputs → Outputs
- **In:** `name` (plus optional phone/email/username on the relevant sub-forms)
- **Out:** aggregated `address`, `phone`, `email`, `associate`/relative, `dob`/age, and `social-profile` leads across many sites
- **Empty/negative result looks like:** destination sites return no match or only paywalled teasers — common for people with a thin US footprint or non-US subjects; absence across brokers is weak evidence, not proof.

## Gotchas & OpSec
- Bazzell periodically updates/removes tools as sites change their query formats — some launch buttons may point at a site that has since altered its interface.
- Human-in-the-loop: destination people-search sites frequently throw CAPTCHAs and paywalls; solve/triage manually and don't pay reflexively.
- Data-broker results are probabilistic and often stale/conflated — always corroborate before treating a hit as fact.
- OpSec: passive at the launcher; assess logging/anonymity on each destination site.

## Overlaps ("do both")
- Pairs with [[brb-free-public-records]] (free authoritative government sources) and [[spydialer]] (phone confirmation) — the launcher casts a wide net; those verify and add official depth.

## Trust & verifiability
`trust: trusted` — the launcher itself is a curated, well-regarded IntelTechniques resource. Trust the *tool*, but treat each third-party site's data as lead-quality to verify at the source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | inteltechniques-people-search-tools |
| category | people-search |
| selectorsIn → selectorsOut | name → address, phone, email, associate, social-profile, dob |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (captcha) |
