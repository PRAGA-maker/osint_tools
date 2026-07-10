---
id: peep-mail-search-tool
name: Peep Mail Search Tool
description: Use when you have a person's `name` and their employer's `domain` and want a best-guess corporate `email` address — returns a likely email pattern to test.
url: http://samy.pl/peepmail/elift.cgi
category: people-search
path:
- people-search
bestFor: Guessing a likely work email address from a full name plus a company domain.
selectorsIn:
- name
- domain
selectorsOut:
- email
status: degraded
pricing: free
costNote: Free legacy web tool by security researcher Samy Kamkar; no account needed.
opsec: passive
opsecNote: The guess itself is generated client/server-side and does not contact the subject. But the *next* step — verifying a guessed address by sending mail or running it through a validator — can be active and may alert the target's mail admin. Stop at the candidate address unless you validate it passively.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Built by a well-known security researcher (Samy Kamkar), but it is an old project page; the underlying CGI is not reliably maintained, so treat output as a heuristic guess only.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- mailcat
aliases:
- PeepMail
- Samy PeepMail
tags:
- toddington
- curated-directory
- people-search
- email-permutation
source: toddington-resources
lastVerified: '2026-07-10'
enrichment: full
---

# Peep Mail Search Tool

> Samy Kamkar's PeepMail — a name-plus-company-domain to likely-corporate-email guesser; a heuristic, not a verified lookup.

## When to use
You know a subject's `name` and where they work (a company `domain`), and you want a candidate `email` to pivot on — to run through breach checks, account-existence oracles, or email-to-profile tools. PeepMail applies common corporate address patterns (e.g. `first.last@`, `flast@`, `firstname@`) to produce a best-guess address.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://samy.pl/peepmail/ (redirects to `sa.my/peepmail/`).
2. Enter the person's full `name` and the company `domain` (e.g. `Steven Jobs` + `apple.com`).
3. Read the output: a suggested email address following the tool's pattern logic.
4. Validate **passively** — feed the candidate to an email-permutation/verification tool or an account-existence oracle rather than emailing it directly.
5. Pivot: a confirmed address feeds `[[mailcat]]` and breach/account tools; a name+domain also feeds other email-permutation generators for a fuller candidate list.

## Inputs → Outputs
- **In:** `name` + `domain`
- **Out:** a single best-guess `email` address
- **Empty/negative result looks like:** the CGI failing to respond or returning a nonsensical/placeholder address — this is an old page and the backend may be dormant, so treat any single guess as unverified.

## Gotchas & OpSec
- This is a **guess**, not a database hit. The address may not exist; never assume it is correct without independent verification.
- The tool is old and the server-side CGI is not reliably maintained (hence `status: degraded`) — if it fails, use a modern email-permutation generator instead.
- OpSec: generating the guess is passive; **verifying** it can be active — do not send test mail from an attributable address.

## Overlaps ("do both")
- Pairs with `[[mailcat]]` and other email-permutation/verification tools — PeepMail proposes one candidate, those expand and validate the full set of likely patterns.

## Trust & verifiability
`trust: community` — a respected researcher's tool, but a heuristic pattern generator on an unmaintained page; output is a lead to verify, not a fact.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | peep-mail-search-tool |
| category | people-search |
| selectorsIn → selectorsOut | name, domain → email |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
