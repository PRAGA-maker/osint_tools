---
id: inspy
name: InSpy
description: Use when you have an `employer-org` + `domain` and want a company's likely employees and their email pattern — returns candidate `name`s, roles and guessed `email`s. (Deprecated/unmaintained.)
url: https://github.com/jobroche/InSpy
category: social-networks
path:
- social-networks
- linkedin
bestFor: Enumerating a target company's employees and inferring the corporate email format from a company name + domain (historically, via LinkedIn + Hunter.io).
selectorsIn:
- employer-org
- domain
selectorsOut:
- name
- email
- employer-org
status: down
pricing: free
costNote: Open-source and free, but it requires your own Hunter.io API key (paste into InSpy.py). Note the repo is deprecated and no longer maintained (last release Aug 2018).
opsec: active
opsecNote: Employee enumeration and email-pattern probing generate outbound requests tied to your infrastructure/keys and touch third-party services (Hunter.io); run from isolated infrastructure and a dedicated API key, never a personal one.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: unverified
trustNote: A well-known but DEPRECATED pentest recon tool (jobroche/InSpy); LinkedIn's anti-scraping changes since 2018 mean it likely no longer works as originally designed — treat as historical unless you verify it runs.
missingPersonsRelevance: medium
coverage:
- global
auth: api-key
api: true
localInstall: true
registration: true
invitationOnly: false
relatedTools:
- footprintiq
aliases:
- jobroche/InSpy
tags:
- linkedin
- employee-enumeration
- email-pattern
- cli
- python
- deprecated
source: arf-seed
lastVerified: '2026-07-13'
enrichment: full
---

# InSpy

> A classic Python LinkedIn-enumeration tool — company name in, likely employees and their email format out. Now deprecated; document it so you know why a run fails.

## When to use
You have a target `employer-org` and its `domain` and want a list of probable employees plus the corporate email pattern (e.g. `first.last@corp.com`) for pivoting or verification. This is org-to-people enrichment. **Caveat:** the tool is unmaintained (since 2018) and depends on scraping/Hunter.io in ways LinkedIn has since broken — reach for a current alternative first, and use InSpy only if you confirm it still runs.

## How to use it (`bestInteractionPattern`: cli)
1. Clone `https://github.com/jobroche/InSpy` and install its Python dependencies.
2. Obtain a Hunter.io API key and paste it into the `hunterio` variable in `InSpy.py`.
3. Run against a company name, optionally passing a domain, email-format pattern, and a titles/departments file.
4. Export results to HTML/CSV/JSON/XML and read candidate employees, roles, and guessed emails.
5. Pivot: guessed emails feed email verification and breach checks; named employees feed people-search — but re-verify everything given the tool's age.

## Inputs → Outputs
- **In:** `employer-org` (company name) + `domain`
- **Out:** candidate `name`s with roles, inferred corporate `email` pattern/addresses
- **Empty/negative result looks like:** empty output or errors — the most likely cause today is that LinkedIn/Hunter changes have broken the tool, not that the company has no employees; a null here is uninformative.

## Gotchas & OpSec
- **Deprecated**: last release 2018, no maintenance — assume breakage and prefer a maintained employee-enumeration tool.
- Human-in-the-loop: needs your own Hunter.io API key; that key attributes queries to you.
- OpSec: active — enumeration touches third-party services from your infrastructure; isolate it.

## Overlaps ("do both")
- Pairs with `[[footprintiq]]` and current LinkedIn/email-pattern tools — use a maintained enumerator for the actual work and treat InSpy as a reference to the technique.

## Trust & verifiability
`trust: unverified` / `status: down` — a historically important but abandoned tool; do not rely on its output without first confirming it still functions and cross-checking every field.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | inspy |
