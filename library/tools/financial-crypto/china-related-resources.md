---
id: china-related-resources
name: China-related resources
description: Use when you have a `name` or `employer-org` in China and want official corporate/court records — returns `employer-org`, `associate`, and business ownership links.
url: https://bellingcat.gitbook.io/toolkit/more/all-tools/china-related-resources
category: financial-crypto
path:
- financial-crypto
bestFor: A curated Bellingcat index of Chinese company registries, court databases, and credit systems for corporate/person research in China.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
- address
status: live
pricing: free
costNote: The Bellingcat index page is free. Most linked databases are free, though some require a Chinese phone number to register or are geofenced to China IPs; a few (e.g. QCC full reports) charge for premium detail.
opsec: passive
opsecNote: Reading the Bellingcat page is passive. The linked Chinese portals may require registration (Chinese mobile number) and log queries; several are geofenced, so you may need a China-based IP/VPN. Register with a sock-puppet identity, never your own.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Maintained by Bellingcat's volunteer team; the page itself is a vetted index, and the sources it points to are official Chinese government/court databases.
missingPersonsRelevance: low
coverage:
- cn
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- about-maps-and-satellites
- bellingcat-meta-content-library
- bellingcat-s-online-investigation-toolkit-2
- license-plate-maps
aliases:
- Bellingcat China resources
- China company research
tags:
- bellingcat-toolkit
- companies-finance
- china
source: bellingcat-toolkit
lastVerified: '2026-07-28'
enrichment: full
---

# China-related resources

> A Bellingcat toolkit page that curates the key Chinese-language databases — company registries, court judgments, and credit/enforcement systems — for researching companies and the people behind them in China.

## When to use
You have a `name` or `employer-org` connected to China and need authoritative records: who owns or controls a company, its shareholders and beneficial owners, court judgments against a person or firm, or whether someone is on the "dishonest persons" enforcement blacklist. This is the map, not a single tool — reach for it whenever a lead runs into a Chinese entity and you don't know which official portal to query. Missing-person relevance is low in the general case but real when a subject or their associates are tied to Chinese business.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://bellingcat.gitbook.io/toolkit/more/all-tools/china-related-resources and read the table (source, what it holds, access/cost).
2. Pick the right database for your lead, e.g.:
   - **QCC / Gongsi.com.cn / 88cha** — company registration, shareholder structure, beneficial ownership.
   - **National Enterprise Credit Information System** — official company credit, penalties, irregularities.
   - **China Judgements Online** — court verdicts across legal areas.
   - **Court Enforcement Information Publicity** — individuals/companies with "dishonest practice" records.
   - **Cninfo** — financial reports of Shanghai/Shenzhen-listed firms.
3. Follow the GIJN guide (also linked) for how to actually query Chinese databases if you're unfamiliar.
4. Register where required (many need a Chinese mobile number) using a sock-puppet, and use a China IP if geofenced.
5. Pivot: shareholder/officer `name`s become `associate` leads; registered `address`es and linked firms extend the network.

## Inputs → Outputs
- **In:** `name` or `employer-org`
- **Out:** `employer-org` (registration, ownership), `associate` (shareholders, officers, co-parties), `address` (registered addresses), plus court/credit findings
- **Empty/negative result looks like:** the entity isn't found in a given registry, or a portal blocks you at registration/geofence — try a sibling source on the same page rather than concluding no record exists.

## Gotchas & OpSec
- Human-in-the-loop: several sources gate behind a Chinese phone number, CAPTCHA, or a China-only IP; expect to register and possibly VPN.
- Everything is Chinese-language — budget for translation and name-transliteration ambiguity.
- These are official records: authoritative, but access rules and URLs change; if a link is dead, check the page's revision history.

## Overlaps ("do both")
- Sits within `[[bellingcat-s-online-investigation-toolkit-2]]`; pair with `[[bellingcat-meta-content-library]]` and mapping tools like `[[about-maps-and-satellites]]` when a lead spans companies and locations.

## Trust & verifiability
`trust: trusted` — Bellingcat curates and vets the index, and each entry points to an official Chinese government or court database, so findings are verifiable at source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | china-related-resources |
| category | financial-crypto |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate, address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
