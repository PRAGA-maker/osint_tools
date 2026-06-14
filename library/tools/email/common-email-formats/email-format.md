---
id: email-format
name: Email Format
description: Use when you have a company domain and want to know its email address pattern — returns the most common format (e.g. first.last@domain) plus sample known addresses.
url: https://www.email-format.com/
category: email
path:
- email
- common-email-formats
bestFor: Discovering the email-address pattern a company uses so you can construct an individual's likely address.
selectorsIn:
- domain
- employer-org
selectorsOut:
- email
- metadata
status: live
pricing: freemium
costNote: Free domain format lookups; bulk/API access is gated behind paid plans.
opsec: passive
opsecNote: You query email-format.com's collected dataset, not the company's mail server, so nothing is sent to the target; you disclose the domain of interest to email-format.com.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing format-lookup service built from collected sample addresses; the dominant pattern is usually right, but data can be stale or sparse for small orgs.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- email-permutator
aliases: []
tags:
- email-format
source: arf-seed
lastVerified: ''
enrichment: full
---

# Email Format

> email-format.com: enter a company domain and it tells you the email pattern that company uses, with sample known addresses.

## When to use
You know where a person works (an `employer-org` / `domain`) and want to construct their likely work `email`. The site reveals the dominant pattern (first.last@, flast@, first@, etc.), which you then combine with the person's name. Useful when an address itself is the missing link to a person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.email-format.com/.
2. Search the company domain (e.g. `acme.com`).
3. Read the reported dominant format and the sample addresses it has on file.
4. Pivot: apply that format to the person's name to build the candidate address, or feed the pattern + name to `[[email-permutator]]`; then confirm with `[[email-dossier]]` / `[[email-address-validator]]`.

## Inputs → Outputs
- **In:** `domain` / `employer-org`
- **Out:** dominant email format and sample addresses (`email`, `metadata`)
- **Empty/negative result looks like:** "no data for this domain" — common for small/private orgs, or multiple competing formats with low confidence.

## Gotchas & OpSec
- Human-in-the-loop: none for basic lookups; bulk needs an account.
- OpSec: passive; the company is never contacted.
- The dataset can be stale, and large companies sometimes use multiple formats — confirm any constructed address by validation, don't assume.

## Overlaps ("do both")
- Pairs directly with `[[email-permutator]]` / `[[email-permutator-2]]` (turn the pattern into concrete candidates) and a validator (`[[email-dossier]]`) to confirm which candidate is live.

## Trust & verifiability
`trust: community` — established service built from observed addresses; the leading pattern is usually accurate but should be verified before relying on a constructed address.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | email-format |
| category | email |
| selectorsIn → selectorsOut | domain, employer-org → email, metadata |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
