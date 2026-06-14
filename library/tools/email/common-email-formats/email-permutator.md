---
id: email-permutator
name: Email Permutator
description: Use when you have a person's name and a domain and want every plausible email format — returns a list of candidate addresses to verify.
url: https://metricsparrow.com/toolkit/email-permutator/
category: email
path:
- email
- common-email-formats
bestFor: Generating all common email-address permutations for a named person at a given domain.
selectorsIn:
- name
- domain
selectorsOut:
- email
status: live
pricing: free
costNote: Free browser-side tool (MetricSparrow toolkit); no account.
opsec: passive
opsecNote: Permutations are generated locally in the browser with no network contact — generating the list reveals nothing. Verifying the candidates later is the step that may touch a mail server.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A long-standing, widely cited free utility; it only generates strings, so there is little to mis-trust beyond completeness of the format set.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- email-format
- email-dossier
aliases:
- MetricSparrow Email Permutator
tags:
- email-permutator
source: arf-seed
lastVerified: ''
enrichment: full
---

# Email Permutator

> The classic MetricSparrow permutator: enter first/last name and a domain, get every common address format as a ready-to-verify list.

## When to use
You have a person's `name` and a likely `domain` (their employer or a known mail domain) and need their actual `email`. The permutator builds the candidate set (first.last@, flast@, first@, f.last@, etc.); you then verify which one is live. Core step when an address is the bridge from a name to accounts and breaches.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://metricsparrow.com/toolkit/email-permutator/.
2. Enter first name, (optional middle), last name, and the domain.
3. Copy the generated list of candidate addresses.
4. Pivot: verify the candidates with `[[email-dossier]]` / `[[email-address-validator]]` to find the live one; narrow the set first using `[[email-format]]` if you know the org pattern.

## Inputs → Outputs
- **In:** `name` + `domain`
- **Out:** list of candidate `email` addresses (every common format)
- **Empty/negative result looks like:** always produces output (it just permutes); "failure" only shows up downstream when none of the candidates validate — meaning wrong domain, an uncommon format, or a private mailbox.

## Gotchas & OpSec
- Human-in-the-loop: none for generation.
- OpSec: fully passive — generation is local in the browser; only the later verification step can touch a mailserver, so choose a passive verifier or accept that risk.
- It only covers common patterns; unusual formats (employee IDs, random aliases) won't appear, so a fully-failed candidate set is not conclusive.

## Overlaps ("do both")
- Pairs with `[[email-format]]` / `[[email-hunter]]` (identify the right pattern first to shrink the list) and `[[email-dossier]]` (verify). `[[email-permutator-2]]` is an equivalent alternative.

## Trust & verifiability
`trust: community` — well-known, transparent string generator; the only limit is whether its format set covers the target's actual scheme.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | email-permutator |
| category | email |
| selectorsIn → selectorsOut | name, domain → email |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
