---
id: the-endorser
name: the-endorser
description: Use when you have LinkedIn `social-profile` URLs and want a relationship graph built from shared skill endorsements — returns `associate` links and a visual `name`-to-`name` network.
url: https://github.com/eth0izzle/the-endorser
category: social-networks
path:
- social-networks
bestFor: Visualising which people are connected through LinkedIn skill endorsements across several target profiles.
selectorsIn:
- social-profile
- name
selectorsOut:
- associate
- name
status: degraded
pricing: free
costNote: Free, open-source (Python). No cost, but it drives a real LinkedIn session via Selenium, so it needs your (or a sock-puppet's) LinkedIn login.
opsec: active
opsecNote: This logs into LinkedIn and scrapes profiles with an automated browser — LinkedIn's ToS forbids scraping, it detects automation, and views may notify targets or get the account banned. Use a dedicated sock-puppet LinkedIn account and a non-primary IP; never your real account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: cli
trust: community
trustNote: Open-source tool by eth0izzle; the code is inspectable but the repo is explicitly no longer maintained, so it likely breaks against current LinkedIn markup.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: true
registration: false
aliases:
- eth0izzle the-endorser
tags:
- linkedin
- graph
- endorsements
- relationship-mapping
source: awesome-osint
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- shhgit
---

# the-endorser

> A Python/Selenium tool that turns LinkedIn skill endorsements into a relationship graph — who endorses whom, drawn as a network of people and shared skills.

## When to use
You have two or more LinkedIn `social-profile` URLs and want to surface hidden `associate` links between them via endorsements: people who endorse the same skills for multiple targets often share a real-world connection. Useful for mapping a subject's professional cluster when explicit connection lists are hidden. Note the tool is **unmaintained** — treat it as a technique/reference and expect to patch it against LinkedIn's current DOM.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo and install requirements (`pip install -r requirements.txt`); it uses Selenium WebDriver, so a browser driver is required.
2. Provide LinkedIn credentials (use a sock-puppet account) as the tool prompts.
3. Run `python3 the-endorser.py <profile_URL_1> <profile_URL_2> ...` with the target profile URLs.
4. Read the generated Digraph: square box = a skill, ellipse = a person; people with multiple in-arrows from different targets are shared connections worth investigating.
5. Pivot: take the surfaced `associate` names into people-search and re-run the graph outward from newly found profiles.

## Inputs → Outputs
- **In:** LinkedIn `social-profile` URLs (+ your sock-puppet login)
- **Out:** a relationship `associate` graph and the `name`s of connecting individuals
- **Empty/negative result looks like:** an empty/sparse graph — targets are outside your network degree, endorsements are hidden, or (most likely now) LinkedIn changed its markup and the scraper fails; the README notes it works best when targets are within your 3rd-degree network (or you use a Premium/Recruiter account).

## Gotchas & OpSec
- **No longer maintained** — expect it to break against today's LinkedIn and require code fixes.
- Automated LinkedIn scraping violates ToS and is detectable; a sock-puppet account risks a ban, so never use a real/primary account.
- Depth is limited by your network degree unless the account has Premium/Recruiter reach.

## Overlaps ("do both")
- Pairs with manual LinkedIn review and any connection/relationship-mapping tool — the endorser automates the endorsement angle specifically, which manual review is tedious at.

## Trust & verifiability
`trust: community` — open-source and inspectable, but archived/unmaintained; endorsement links are suggestive of a relationship, not proof, so corroborate before asserting an association.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | the-endorser |
| category | social-networks |
| selectorsIn → selectorsOut | social-profile, name → associate, name |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (account-login) |
