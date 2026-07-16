---
id: experts-com
name: Experts.com
description: Use when you have a `name` or field and want to check if someone is a listed expert witness/consultant — returns employer-org, credentials, address and contact leads.
url: https://www.experts.com
category: people-search
path:
- people-search
bestFor: Finding or verifying an expert witness / professional consultant by name or specialty, with their firm and contact details.
selectorsIn:
- name
selectorsOut:
- employer-org
- address
- social-profile
status: live
pricing: free
costNote: Free to browse and search expert profiles; no account needed. Experts pay to be listed, but searching is free to the public.
opsec: passive
opsecNote: Passive browsing of a public professional directory; the listed expert is not notified and nothing is revealed about you. Listed contact details are self-published for business, so they are public by intent.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: An established (since 1994) directory of self-listed expert witnesses and consultants; profiles are self-submitted, so credentials should be independently verified.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- experts.com
tags:
- expert-search
- professional-directory
- expert-witness
source: awesome-osint
lastVerified: '2026-07-16'
enrichment: full
---

# Experts.com

> A directory of expert witnesses and professional consultants: search a name or specialty to find a person's professional profile, firm, credentials, and contact details.

## When to use
When your subject is (or claims to be) a professional expert, consultant, or expert witness. Search their `name` or field to confirm a listing and pull their `employer-org`/firm, stated credentials and experience, business `address`/location, and links to a website or professional profile (`social-profile`). Useful for verifying a credential claim, finding a professional's contact point, or identifying which firm/specialty a person is associated with.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.experts.com.
2. Search by expert name, or browse/search by area of expertise (e.g. "construction defect," "forensic accounting").
3. Open a matching profile for the person's title/credentials, firm, bio, location, and contact/website links.
4. Pivot: firm → `employer-org` and corporate lookups; stated credentials → licensing boards/associations to verify; website/profile links → further identity confirmation and other platforms.

## Inputs → Outputs
- **In:** `name` or field of expertise
- **Out:** expert profile → `employer-org`/firm, `address`/location, credentials, and website/`social-profile` links.
- **Empty/negative result looks like:** no profile for the name — the person isn't listed here (many experts aren't); absence is not evidence they lack the credential, just that they don't advertise on this directory.

## Gotchas & OpSec
- Profiles are self-submitted marketing — verify credentials with the relevant licensing board or professional body, don't take the bio at face value.
- Only covers people who chose to list; a real expert may simply not be here.
- Contact details are for professional outreach; keep in mind reaching out is active and attributable.

## Overlaps ("do both")
- Pairs with licensing-board and professional-association lookups and `[[patent-attorneys-agent-search]]`-style official registers — Experts.com surfaces the self-described profile, official registers verify the credential.

## Trust & verifiability
`trust: community` — a long-established but self-listed directory; treat profiles as leads and confirm credentials/affiliations against authoritative sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | experts-com |
| category | people-search |
| selectorsIn → selectorsOut | name → employer-org, address, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
