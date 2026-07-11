---
id: familyecho-com
name: Family Echo
description: Use when you have gathered several relatives (`name`/`associate`) and want a free workspace to build and visualise the family tree — returns an interactive relationship diagram you construct.
url: https://www.familyecho.com/
category: public-records
path:
- public-records
bestFor: Assembling scattered relative leads into one shareable, visual family tree to see relationships and gaps at a glance.
selectorsIn:
- name
- associate
selectorsOut:
- associate
status: live
pricing: free
costNote: Free web service; basic tree-building works without an account, while saving, sharing and adding photos require a (free) sign-in.
opsec: passive
opsecNote: This is a private workspace you populate — it does NOT search anyone's data, so it leaks nothing about a subject. Trees are private to invited members; keep your working tree unshared, and remember you are entering third parties' personal data, so store it responsibly.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A legitimate long-running free genealogy webapp; it is a construction/visualisation tool, not a data source, so "trust" concerns your own input accuracy, not third-party data quality.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- familyecho.com
- Family Echo tree builder
tags:
- genealogybdmANDwills
- Genealogy Linked Sites
- family-tree
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# Family Echo

> A free online family-tree builder — the whiteboard where you assemble the relatives you've found into a clear, shareable relationship map.

## When to use
You've collected relative leads from obituaries, grave records, people-search aggregators and social comments, and now you need to *organise* them: who is whose parent/sibling/spouse, where the gaps are, which surname to chase next. Family Echo is a workspace, not a lookup — it won't surface a stranger's tree (trees are private) — but it turns a pile of `name`/`associate` fragments into a visual `associate` network that exposes the missing links to go find.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.familyecho.com/ and start a new tree (no account needed to begin).
2. Add each known person with names, dates/places, marriage and relationship links; attach notes and photos.
3. Switch views (partial/complete/classic, adjustable generations) to see the structure and spot missing parents/spouses/children.
4. Sign in to save/share privately with collaborators (e.g. a case team).
5. Pivot: each empty slot (an unnamed parent, a missing sibling) becomes a targeted query for grave/obituary/records tools; a completed branch corroborates a subject's family context.

## Inputs → Outputs
- **In:** `name`s and `associate` (relatives) you have already gathered
- **Out:** an interactive `associate` relationship diagram, with gaps made visible
- **Empty/negative result looks like:** there is no "search" here — an empty tree just means you haven't entered data yet; do not expect to look up someone else's existing tree.

## Gotchas & OpSec
- Not a data source: this builds trees from YOUR input; it does not discover relatives for you.
- Privacy: trees are private/invite-only — you won't find a target's tree here, and you shouldn't publish one containing living people's data.
- OpSec: passive (no external queries), but you are handling third parties' PII — store and share carefully.

## Overlaps ("do both")
- Pairs with `[[github-io]]` grave/genealogy search and obituary tools — those find the relatives, Family Echo organises them.
- Pairs with `[[ufind-name]]`/`[[usphonebook]]` — aggregators surface named relatives that you slot into the tree.

## Trust & verifiability
`trust: community` — a reputable free tool whose reliability depends entirely on the accuracy of what you enter; it neither vouches for nor supplies external data.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | familyecho-com |
