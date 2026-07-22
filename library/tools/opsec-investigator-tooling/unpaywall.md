---
id: unpaywall
name: Unpaywall
description: Use when you're researching an academic subject and hit paywalled papers — Unpaywall finds the free legal open-access copy so you can read affiliations and coauthors — surfaces `employer-org` and `associate` links.
url: https://addons.mozilla.org/en-US/firefox/addon/unpaywall
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Getting the full text of a subject's paywalled research (via legal open-access copies) to mine affiliations and coauthors.
selectorsIn:
- name
- document-id
selectorsOut:
- employer-org
- associate
status: live
pricing: free
costNote: Free browser extension and free API from the non-profit Our Research (formerly Impactstory); no account.
opsec: passive
opsecNote: Unpaywall queries its own open-access index by DOI as you browse — it does not contact the author. It sees the DOIs you look up; use a research browser profile if that browsing pattern is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: browser-extension
trust: trusted
trustNote: Maintained by Our Research, a respected scholarly-infrastructure non-profit; it only links to legally-hosted open-access copies.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
aliases:
- Unpaywall
- oaDOI
tags:
- toddington
- curated-directory
- add-ons-apps-extensions
- academic
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# Unpaywall

> A browser extension that finds free legal open-access copies of paywalled papers — used in OSINT to actually read a subject's research and mine it for affiliations, coauthors and contact detail.

## When to use
Your subject is an academic, researcher or clinician and their work sits behind publisher paywalls. Unpaywall pops a green tab when a free legal copy exists, letting you read the paper — where the gold is the metadata: institutional `employer-org` on the byline, coauthors (`associate`) mapping their professional network, and often a corresponding-author email.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install Unpaywall for Firefox/Chrome (or use the free API / the Unpaywall data in Google Scholar/Europe PMC).
2. Navigate to a paywalled article page (by DOI, `document-id`, or from a Scholar search of the subject's `name`).
3. If a green "open access" tab appears, click it to read the free copy.
4. Harvest: author affiliations (`employer-org`), coauthors (`associate`), funding/acknowledgements, and any listed contact email; pivot those onward.

## Inputs → Outputs
- **In:** `document-id` (DOI) / paper page / author `name` (via Scholar)
- **Out:** free full text → `employer-org` affiliations, coauthor `associate` network, contact emails
- **Empty/negative result looks like:** no green tab — no known legal open-access copy exists (still paywalled); it does not mean the paper isn't real.

## Gotchas & OpSec
- It only surfaces *legal* open-access copies, so many recent papers won't resolve — pair with the publisher/library or preprint servers.
- The byline affiliation is at time of publication; a person may have moved institutions since.
- OpSec: passive; nothing reaches the author.

## Overlaps ("do both")
- Pairs with Google Scholar and ORCID: Scholar/ORCID enumerate the subject's publications and coauthors, Unpaywall gets you inside each paper to read the detail.

## Trust & verifiability
`trust: trusted` — a reputable non-profit indexing legally-hosted copies; the paper content is authoritative, though affiliations reflect publication date.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | unpaywall |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut | name, document-id → employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | no |
