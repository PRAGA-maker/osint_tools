---
id: openi-nlm-nih-gov
name: Open-i (NLM/NIH)
description: Use when you have a scientific/medical `image` and want its source paper — returns matching figures from open-access biomedical literature via text or reverse-image search.
url: https://openi.nlm.nih.gov/gridquery
category: image-video-face
path:
- image-video-face
bestFor: Searching biomedical/scientific figures and finding the open-access article an image came from.
selectorsIn:
- image
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free official US National Library of Medicine (NIH) service; no account or payment.
opsec: passive
opsecNote: You query a US-government biomedical image index; a submitted image is processed by NLM's servers. No subject is notified. This is scoped to scientific literature, so it's irrelevant (and safe) for images of real people/places — nothing personal is exposed.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by the US National Library of Medicine (NIH); indexes figures from open-access biomedical literature, so matches point to real, citable articles.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- national-center-for-biotechnology
- pubmed
- pubmed-national-center-for-biotechnology-information
aliases:
- Open-i
- Openi
tags:
- Image Search and Identification
- Reverse Image Search Engines and automation tools
- biomedical
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# Open-i (NLM/NIH)

> The US National Library of Medicine's image search — find biomedical figures and charts and trace them back to the open-access papers they came from, by keyword or by image.

## When to use
You have a scientific/medical `image` — a chart, a scan, a figure lifted into a post or document — and you want its provenance: which paper published it, by whom. Open-i indexes millions of figures from open-access biomedical literature and supports both text queries and reverse-image (grid) search. In an investigation this is niche: it de-anonymizes a *scientific* figure to a citable source (author, institution, date), useful when a subject shares research imagery or when you need to check whether a "medical" image is real and where it originates. It is not for photos of people or places.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://openi.nlm.nih.gov/ and choose text search, or use the grid/visual query to search by an example image.
2. For reverse search, supply the figure; review the visually-similar results.
3. Open a match to see the source article (title, authors, journal, date) and citation.
4. Pivot: the paper's authors/affiliations become `name`/`employer-org` leads; the citation feeds PubMed/NCBI.

## Inputs → Outputs
- **In:** `image` (biomedical/scientific figure) or keywords
- **Out:** matching figures + the source article (`document-id`/citation, authors, institution)
- **Empty/negative result looks like:** no similar figures — meaning the image isn't in the open-access biomedical corpus (true for ordinary photos and most non-medical images).

## Gotchas & OpSec
- Human-in-the-loop: none.
- Scope is biomedical open-access literature only — it will not match faces, scenes, or general web images.
- Visual matches need human confirmation; open the source article to verify the figure truly matches.

## Overlaps ("do both")
- Pairs with `[[pubmed]]` / `[[national-center-for-biotechnology]]` — this finds the figure and its article; those search the literature by author/topic to expand the picture.

## Trust & verifiability
`trust: trusted` — an authoritative NIH/NLM service; matches resolve to real, citable open-access articles within its biomedical scope.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | openi-nlm-nih-gov |
| category | image-video-face |
| selectorsIn → selectorsOut | image → document-id |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
