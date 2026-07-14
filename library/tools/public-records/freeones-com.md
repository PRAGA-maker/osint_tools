---
id: freeones-com
name: FreeOnes
description: Use when a subject may work in the adult-entertainment industry and you have a `name`/stage name — returns aliases, linked social-profiles and biographical bio data from a performer database.
url: https://www.freeones.com/forums/
category: public-records
path:
- public-records
bestFor: Resolving an adult-industry performer's stage name to aliases, linked accounts and bio details for identity disambiguation.
selectorsIn:
- name
- username
selectorsOut:
- name
- social-profile
- associate
status: live
pricing: freemium
costNote: Core performer profiles/bios and the community forum are free to browse; some galleries/content are premium. Identity-useful data (aliases, links, bio) is on the free tier.
opsec: passive
opsecNote: Passive third-party lookup — you browse a database, the subject is not notified. Adult content; use a dedicated sock account and an isolated browser profile, and treat this as a sensitive source (handle findings discreetly and lawfully).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Long-established adult-performer directory with community-maintained bios; useful for alias resolution but user-contributed data can be inaccurate or outdated — corroborate before relying on it.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- freeones.com
- FreeOnes forum
tags:
- professionlicensing
- Profession & Licensing Sites
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# FreeOnes

> A long-running adult-entertainment performer directory (with community forum) — useful in the narrow case of resolving a stage name to real-name leads, aliases, and linked accounts.

## When to use
Reach for this only when the investigation points to the adult-entertainment industry — e.g. a subject who used a stage name, or an image/handle that traces to adult content. FreeOnes maintains performer profiles listing aliases, active years, linked social accounts, and community-added biographical notes, which can help disambiguate a stage identity or link it to other handles. It is a sensitive niche source, not a general people-search — do not route ordinary subjects here. The stub's `address`/`employer-org` outputs overstate it; treat outputs as alias and account leads.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open freeones.com and search the performer `name`/stage name (the site's main directory; the URL points to the community forum).
2. Open the performer profile: note listed aliases, active years, and outbound links to social/streaming accounts.
3. Check the forum threads for community-contributed identity discussion (other names, collaborators/`associate` links) — but weight these as unverified.
4. Read the output as **leads**: aliases feed username enumeration; linked accounts feed social-profile checks.
5. Pivot: a confirmed alias or linked handle feeds broader cross-platform search and image tools.

## Inputs → Outputs
- **In:** `name`/`username` (stage name)
- **Out:** `name` (aliases/other stage names), `social-profile` (linked accounts), `associate` (collaborators mentioned)
- **Empty/negative result looks like:** no matching performer — meaning the name isn't in the directory (not proof the person is unconnected to the industry).

## Gotchas & OpSec
- Sensitive/adult source: handle findings discreetly, lawfully, and only where relevant to the investigation.
- Community-contributed data can be wrong or stale — corroborate any alias/link before acting on it.
- OpSec: passive, but use an isolated sock browser profile given the content.

## Overlaps ("do both")
- Pairs with username-enumeration and reverse-image tools — FreeOnes surfaces the stage aliases and linked handles, those tools spread them across the rest of the web.

## Trust & verifiability
`trust: community` — an established directory but with user-maintained bios, so its alias/link data is a starting point to verify, not a record of fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | freeones-com |
| category | public-records |
| selectorsIn → selectorsOut | name, username → name, social-profile, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
