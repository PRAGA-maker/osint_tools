---
id: lookupuk
name: LookUpUK
description: Use when you're trying to trace a lost friend/relative in the UK and want a portal of search resources plus reunion message boards — returns links to UK databases and 70,000+ contact-seeking posts.
url: http://www.lookupuk.com
category: people-search
path:
- people-search
bestFor: Tracing lost UK friends/relatives — a resource portal plus long-running reunion message boards.
selectorsIn:
- name
selectorsOut:
- associate
- name
status: live
pricing: free
costNote: The portal and message boards are free; many linked resources (Electoral Roll, Ancestry, phone books) are third-party paid services.
opsec: passive
opsecNote: Browsing is passive. Posting your own "seeking" message publicly reveals your search and contact route to anyone reading the board — use a sock-puppet identity/contact if the enquiry is sensitive.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: community
trustNote: A long-running community reunion portal, not a data source itself; message-board content is user-posted leads to verify, and it mainly links out to other (often paid) databases.
missingPersonsRelevance: high
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- Lookup UK
- lookupuk.com
tags:
- people-search
- reunion
source: metaosint
lastVerified: '2026-07-11'
enrichment: full
---

# LookUpUK

> A veteran UK "find a lost friend or relative" portal — part resource directory to UK databases, part reunion message board with tens of thousands of contact-seeking posts.

## When to use
You're trying to trace someone in the UK (a lost relative, old friend, estranged family) and want both a curated jump-off to UK search resources (electoral roll, phone books, BMD/genealogy) and a community of others posting to reconnect. Genuinely on-point for missing-person/reunion work: the message boards can surface people already searching for — or connected to — your subject.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.lookupuk.com and browse the resource sections (phone, email, genealogy, advanced search links).
2. Search/browse the message boards for the `name`/family/place — 70,000+ posts of people seeking contact.
3. Post your own "seeking" message (use a sock-puppet contact) to invite responses from relatives/acquaintances.
4. Follow the linked databases (Electoral Roll, Ancestry, British phonebook) — noting many are paid third-party services.
5. Pivot: a board respondent is a live `associate` lead; linked databases feed address/BMD lookups.

## Inputs → Outputs
- **In:** `name` (+ place/family context)
- **Out:** links to UK search databases; reunion board posts naming people/`associate`s and contact routes
- **Empty/negative result looks like:** no matching board posts and only pointers to external (paid) databases — the portal itself holds few facts; absence of a post means nobody has sought that person here.

## Gotchas & OpSec
- Portal, not a database: LookUpUK mostly links out — the real data lives in the (often paid) services it points to.
- User-posted leads: board content is unverified and can be old; corroborate before acting.
- OpSec: passive to browse; posting is a disclosure — use a throwaway contact.

## Overlaps ("do both")
- Pairs with `[[curious-fox-united-kingdom]]` and `[[myfamilyannouncements-co-uk]]` — all three connect you to people/records for UK tracing; run the boards in parallel since different communities surface different leads.

## Trust & verifiability
`trust: community` — a community reunion portal; its value is the connections and pointers it brokers, all of which need verification against authoritative records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | lookupuk |
| category | people-search |
| selectorsIn → selectorsOut | name → associate, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
