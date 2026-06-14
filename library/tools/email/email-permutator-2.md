---
id: email-permutator-2
name: Email Permutator
description: Use when you have a person's name and a domain and want every plausible email format — returns a list of candidate addresses to verify (polished.app variant).
url: https://www.polished.app/email-permutator/
category: email
path:
- email
bestFor: Generating all common email-address permutations for a named person at a given domain.
selectorsIn:
- name
- domain
selectorsOut:
- email
status: live
pricing: free
costNote: Free browser-side tool on polished.app; no account.
opsec: passive
opsecNote: Permutations are generated client-side with no network contact, so building the list reveals nothing to the target; only later verification can touch a mail server.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A straightforward free permutator equivalent to the MetricSparrow tool; it only produces strings, so trust hinges on format coverage, not data handling.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- email-permutator
- email-format
- email-dossier
aliases: []
tags:
- email-permutator
source: awesome-osint
lastVerified: ''
enrichment: full
---

# Email Permutator

> A polished.app email permutator: name + domain in, every common candidate address out — an equivalent alternative to the MetricSparrow tool.

## When to use
You have a person's `name` and a likely `domain` and need their actual `email`. This generates the full candidate set of common formats so you can verify which is live. Use it as a drop-in alternative or cross-check to `[[email-permutator]]`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.polished.app/email-permutator/.
2. Enter first name, (optional middle), last name, and the domain.
3. Copy the generated candidate list.
4. Pivot: verify candidates with `[[email-dossier]]` / `[[email-address-validator]]`; narrow first with `[[email-format]]` / `[[email-hunter]]` if the org pattern is known.

## Inputs → Outputs
- **In:** `name` + `domain`
- **Out:** list of candidate `email` addresses (common formats)
- **Empty/negative result looks like:** it always emits permutations; a true "failure" only appears downstream when no candidate validates — implying a wrong domain or an uncommon format.

## Gotchas & OpSec
- Human-in-the-loop: none for generation.
- OpSec: fully passive — client-side generation; only the verification step risks touching a mailserver.
- Covers only common patterns; unusual schemes (IDs, random aliases) are not produced, so a failed set is not proof.

## Overlaps ("do both")
- Equivalent to `[[email-permutator]]` (MetricSparrow) — pick whichever loads; pairs with `[[email-format]]` to shrink the list and `[[email-dossier]]` to verify.

## Trust & verifiability
`trust: community` — simple, transparent generator; reliability is limited only by how completely its format set matches the target's scheme.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | email-permutator-2 |
| category | email |
| selectorsIn → selectorsOut | name, domain → email |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
