---
id: email-hunter
name: Email Hunter
description: Use when you have a company domain (and optionally a name) and want its email addresses and format — returns known addresses, the org email pattern, and confidence scores.
url: https://emailhunter.co
category: email
path:
- email
bestFor: Finding the email addresses and address pattern associated with a company domain (now Hunter.io).
selectorsIn:
- domain
- employer-org
- name
selectorsOut:
- email
- metadata
status: live
pricing: freemium
costNote: emailhunter.co now redirects to Hunter.io; free tier gives limited searches/verifications per month, more requires an account/paid plan.
opsec: passive
opsecNote: Domain searches hit Hunter's crawled index, not the company's mail server; constructing/verifying an address may trigger Hunter's own SMTP checks. Use behind an account you are comfortable attributing.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: web-manual
trust: trusted
trustNote: Hunter.io is a widely used, reputable commercial email-finding service with transparent confidence scoring and source citations per address.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Hunter.io
- Hunter
tags:
- email
- email-finder
source: metaosint
lastVerified: ''
enrichment: full
---

# Email Hunter

> The original domain for Hunter.io: enter a company domain and get its known email addresses, the address pattern, and per-result confidence with sources.

## When to use
You know a person's `employer-org` / `domain` and want to find or construct their work `email`. Hunter returns addresses already seen on the web plus the org's dominant pattern, and (with a name) proposes the most likely address with a confidence score and the pages it was found on. Strong when an address is the link between a name and an online footprint.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://emailhunter.co (redirects to hunter.io) and sign in / create a free account.
2. Use Domain Search: enter the company domain to list known addresses and the pattern; or Email Finder: enter full name + domain to get the single most likely address.
3. Read the confidence score and the cited source pages for each result.
4. Pivot: confirm the chosen address with `[[email-dossier]]` / `[[email-address-validator]]`, then run it through `[[email-breach-analysis]]` and username tooling.

## Inputs → Outputs
- **In:** `domain` / `employer-org` (+ optional `name`)
- **Out:** known `email` addresses, the org pattern, confidence scores and source citations (`metadata`)
- **Empty/negative result looks like:** no addresses indexed for the domain (small/private orgs), or a low-confidence guess with no corroborating sources — treat low confidence as unverified.

## Gotchas & OpSec
- Human-in-the-loop: account login required; free tier is rate-limited per month.
- OpSec: domain search is passive (crawled index); verification may trigger SMTP probing on Hunter's side. Your searches are tied to your Hunter account.
- Confidence is probabilistic — always validate the constructed address before relying on it.

## Overlaps ("do both")
- Pairs with `[[email-format]]` (cross-check the pattern) and `[[email-permutator]]` (generate candidates when Hunter has no direct hit); validate all with `[[email-dossier]]`.

## Trust & verifiability
`trust: trusted` — established commercial service with source citations and confidence scoring, which makes its results auditable.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | email-hunter |
| category | email |
| selectorsIn → selectorsOut | domain, employer-org, name → email, metadata |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
