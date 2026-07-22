---
id: paperpanda
name: PaperPanda
description: Use when you have a paywalled academic article and want a free full-text PDF — returns a legally-available open-access copy in one click.
url: https://chrome.google.com/webstore/detail/paperpanda-%E2%80%94-get-millions/ggjlkinaanncojaippgbndimlhcdlohf
category: public-records
path:
- public-records
bestFor: One-click retrieval of freely available PDF versions of scientific papers behind paywalls.
selectorsIn:
- document-id
selectorsOut:
- document-id
status: live
pricing: free
costNote: Free browser extension; no account or payment. Sources legal open-access copies (repositories, preprints, author pages).
opsec: passive
opsecNote: The extension sends the article DOI/identifier to its lookup backend to find a copy; that discloses which paper you are reading to the extension provider. For sensitive research use a clean browser profile. It retrieves legal open-access copies, not pirated ones.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: community
trustNote: Community-built academic-access extension (Unpaywall-style); it locates legally-hosted copies, so results depend on whether an open version exists.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- PaperPanda
- Paper Panda extension
tags:
- Science
- academic-access
- browser-extension
source: cyb-detective
lastVerified: '2026-07-22'
enrichment: full
---

# PaperPanda

> A browser extension that finds a free, legally-available PDF of a paywalled paper in one click — the enabler for reading source research an investigation depends on.

## When to use
Your investigation hinges on the content of an academic paper (an author's methods, an expert's stated affiliation, data behind a claim) but the publisher wants registration or payment. PaperPanda takes the article you are viewing (or its DOI) and searches open-access repositories, preprint servers, and author pages for a freely-hosted copy. It is a support/access tool rather than a person-finder — its job is to get you the primary document you then read for names, affiliations, and citations.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install PaperPanda from the Chrome Web Store (link above; a Firefox build also exists).
2. Navigate to the article's page (journal page, DOI link, or Google Scholar result).
3. Click the PaperPanda icon; it searches for and opens a legally-available full-text PDF if one exists.
4. Read the paper for author names, institutional affiliations (`employer-org`), acknowledgements, and cited work.
5. Pivot: authors/affiliations feed people- and academic-search; the paper's references feed further primary sources.

## Inputs → Outputs
- **In:** the article you are viewing / its `document-id` (DOI)
- **Out:** an open-access full-text PDF of that `document-id`
- **Empty/negative result looks like:** "no free version found" — no open-access copy exists, so the paywall stands. That is a real outcome, not a bug; try the author's site, a preprint server, or an interlibrary route.

## Gotchas & OpSec
- It only finds legally-hosted copies; a genuine paywall with no open version will return nothing.
- Sending the DOI to its backend reveals your reading interest to the extension provider — use a clean profile for sensitive work.
- Relevance to missing-persons work is indirect: it unlocks documents, it does not search for people.

## Overlaps ("do both")
- Pairs with Google Scholar, Unpaywall, and preprint servers — those locate the citation; PaperPanda (or its peers) fetches the readable full text.

## Trust & verifiability
`trust: community` — a legitimate community access tool that surfaces legally-available copies; coverage depends entirely on whether an open version has been posted, so a null result is meaningful.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | paperpanda |
| category | public-records |
| selectorsIn → selectorsOut | document-id → document-id |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
