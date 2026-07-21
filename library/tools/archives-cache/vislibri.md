---
id: vislibri
name: viaLibri
description: Use when a lead is a rare/old/second-hand book or document and you want to locate a copy and its sellers — returns marketplace listings (`address`/seller leads) across 200+ book sites.
url: https://www.vialibri.net/
category: archives-cache
path:
- archives-cache
bestFor: Meta-searching 200+ antiquarian/used-book marketplaces at once to find a specific rare book, pamphlet or document and who is selling it.
selectorsIn:
- name
selectorsOut:
- address
status: live
pricing: free
costNote: Free to search across the network. Optional free account unlocks saved searches / want-list alerts (Libribot). Purchases happen on the seller's own site.
opsec: passive
opsecNote: Passive — you search a book aggregator, not any person tied to the book. No target interaction. If you later contact a seller, that is an active step under your own identity; use a research contact.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: viaLibri is a long-established, well-known antiquarian-book meta-search; listing data comes from real marketplaces (AbeBooks, Biblio, eBay, and 200+ dealer sites) though individual listings are seller-provided.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- vialibri
- vialibri.net
tags:
- Archives of documents/newspapers
- rare-books
source: cyb-detective
lastVerified: '2026-07-21'
enrichment: full
---

# viaLibri

> A meta-search across 200+ antiquarian, rare and used-book marketplaces — the way to find a specific old book, self-published title, or document and the dealers who hold it.

## When to use
Your lead is a physical publication: a rare/out-of-print book, a self-published or vanity title tied to a subject, a local-history volume, a pamphlet or a signed/inscribed copy. viaLibri finds copies for sale across the antiquarian trade in one query, which can surface an author's obscure work, an inscription/provenance, or a dealer who can describe a copy. It searches for-sale inventory, not library holdings.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.vialibri.net/.
2. Search by title, author `name`, keyword, or ISBN across the aggregated marketplaces.
3. Review listings — each shows the seller, price, condition, and a "Direct from Seller" link to the dealer's own site.
4. For an ongoing hunt, create a free account and save the search so Libribot emails you when a matching copy appears.
5. Pivot: a seller's description may reveal inscriptions/provenance (a `name`, dedication, prior owner); a dealer location is an `address` lead; the author record feeds authorship research.

## Inputs → Outputs
- **In:** a book/document identifier — title, author `name`, keyword, or ISBN
- **Out:** for-sale listings across the trade — seller identity/location (`address`), price, condition, and provenance/inscription notes
- **Empty/negative result looks like:** no listings — the item isn't currently for sale anywhere in the network (very common for truly rare/personal items). Save the want-list alert rather than concluding it doesn't exist; also check library catalogues (WorldCat).

## Gotchas & OpSec
- It indexes items **for sale**, not library holdings — pair with a library union catalogue for non-commercial copies.
- Listing details are seller-written and can be inaccurate; confirm inscriptions/provenance with the dealer.
- Fully passive; only contacting a seller is active.

## Overlaps ("do both")
- Complements library union catalogues (e.g. WorldCat) — viaLibri finds purchasable copies and dealer provenance, the catalogue finds institutional holdings of the same title.

## Trust & verifiability
`trust: trusted` — an established meta-search over real marketplaces; the aggregation is reliable, while each individual listing's claims (edition, inscription, condition) rest on the selling dealer and should be verified with them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | vislibri |
| category | archives-cache |
| selectorsIn → selectorsOut | name → address |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
