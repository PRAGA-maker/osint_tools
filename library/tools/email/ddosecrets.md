---
id: ddosecrets
name: DDoSecrets
description: Use when you have a name, email, org, or topic and want to search a large archive of leaked/hacked document datasets — returns links to source documents and datasets that may mention the subject.
url: https://ddosecrets.com/wiki/Special:AllPages
category: email
path:
- email
bestFor: Finding a subject, org, or associate inside published leak/hack document troves.
selectorsIn:
- name
- email
- employer-org
- domain
selectorsOut:
- document-id
- email
- name
- associate
status: live
pricing: freemium
costNote: Public wiki/index is free to browse and search; some large datasets are distribution-restricted (released to vetted journalists/researchers on request).
opsec: passive
opsecNote: Browsing the public index is passive. Some datasets contain sensitive/stolen data — handle on a clean environment, mind legal exposure, and consider Tor for the .onion mirror.
humanInLoop: true
humanInLoopReason:
- manual-review
- legal-gate
bestInteractionPattern: web-manual
trust: community
trustNote: Established transparency/leak-archive collective (Distributed Denial of Secrets); datasets are real but unstructured, of mixed provenance, and may be legally sensitive to download. Verify any subject hit against primary records.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- Distributed Denial of Secrets
- DDoS
tags:
- leaks
- breach-data
source: osint4all
lastVerified: ''
enrichment: full
---

# DDoSecrets

> A transparency collective hosting a searchable archive of leaked and hacked document datasets — a deep, unstructured source you mine by name/org/topic.

## When to use
You have a `name`, `email`, `employer-org`, or `domain` and want to know whether the subject (or a connected organisation/associate) appears inside a published leak trove — corporate breaches, government leaks, militia/extremist forum dumps, etc. Best for context and associations rather than a one-shot address lookup.

## How to use it (`bestInteractionPattern`: web-manual)
1. Browse `Special:AllPages` (the harvested URL) to see the dataset index, or use the site's search to find a relevant trove.
2. Open a dataset's wiki page to read its description, provenance, and access terms; some are publicly downloadable, some are "limited distribution."
3. Within an accessible dataset, search the documents for your selector (full-text grep on downloaded files, or the dataset's own search if provided).
4. Pivot: a hit yields `document-id`s, embedded `email`s, names, and `associate` links to chase in other sources.

## Inputs → Outputs
- **In:** `name`, `email`, `employer-org`, or `domain`
- **Out:** dataset/document references (`document-id`), embedded `email`/`name`, `associate` relationships
- **Empty/negative result looks like:** no dataset references your subject — common, since coverage is topical (orgs, govs, ideological groups) rather than person-indexed.

## Gotchas & OpSec
- Not person-indexed: you are searching document collections, so expect manual review and many irrelevant datasets.
- Human-in-the-loop: large datasets are gated to vetted researchers/journalists, and some content is legally sensitive to download/hold (`legal-gate`).
- OpSec: passive browsing, but handle downloaded leak data on an isolated environment; consider the Tor/.onion mirror and avoid mixing with your operational identity.

## Trust & verifiability
`trust: community` — reputable, long-running leak archive, but datasets are raw, mixed-provenance, and sometimes manipulated upstream. Treat any subject hit as a lead to verify against primary records.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ddosecrets |
| category | email |
| selectorsIn → selectorsOut | name, email, employer-org, domain → document-id, email, name, associate |
| pricing / cost | freemium |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
