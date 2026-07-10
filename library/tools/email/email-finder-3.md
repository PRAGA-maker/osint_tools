---
id: email-finder-3
name: Email Finder (Experte)
description: Use when you have a person's `name` and their company `domain` and want their real work `email` — returns a list of likely address permutations each SMTP-validated as valid/invalid/unknown.
url: https://www.experte.com/email-finder
category: email
path:
- email
bestFor: Turning a name + company domain into a validated best-guess work email address.
selectorsIn:
- name
- domain
selectorsOut:
- email
status: live
pricing: free
costNote: Completely free, no signup; Experte states it does not store requested data.
opsec: active
opsecNote: Experte generates permutations and validates each by connecting to the target's mail server — an SMTP probe reaches the subject's mail provider (from Experte's infrastructure, not yours, so it is not directly attributable to you). It never emails the person. Stop at the validated address; don't send test mail yourself.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Experte.com is an established German tools site; the finder does real SMTP validation, but "catch-all" mail servers return "unknown", so results are high-quality guesses, not guarantees.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- peep-mail-search-tool
- mailcat
aliases:
- Experte Email Finder
tags:
- Emails
- email-permutation
- email-validation
source: cyb-detective
lastVerified: '2026-07-10'
enrichment: full
---

# Email Finder (Experte)

> Experte's email finder — name + company domain in, a list of likely work addresses out, each checked against the mail server so you know which one is real.

## When to use
You have a subject's `name` and know where they work (a company `domain`) and you want their actual work `email` to pivot on — for breach checks, account-existence oracles, or email-to-profile enrichment. Unlike a raw permutation guesser, this one validates each candidate against the mail server, so you get a shortlist ranked by deliverability rather than a single blind guess.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.experte.com/email-finder.
2. Enter the person's first name, last name, and company `domain` (e.g. `Tim` `Cook` `apple.com`).
3. Read the output: candidate addresses each marked **valid**, **invalid**, or **unknown**. A single "valid" is your best pivot; several "unknown" means a catch-all server that accepts everything.
4. Confirm passively — feed a "valid" address to an account-existence oracle or breach check rather than emailing it.
5. Pivot: a confirmed `email` feeds `[[mailcat]]`, breach lookups, and account-existence checks.

## Inputs → Outputs
- **In:** `name` (first + last) + `domain`
- **Out:** ranked list of candidate `email` addresses with valid/invalid/unknown status
- **Empty/negative result looks like:** all candidates "invalid" (the person likely isn't on that domain, or uses an unusual pattern) or all "unknown" (a catch-all server — validation is inconclusive, treat the best-pattern guess as unverified).

## Gotchas & OpSec
- Catch-all mail servers return "unknown" for every address — don't over-trust a permutation just because it wasn't marked invalid.
- Validation is an SMTP probe to the target's mail provider; it originates from Experte, not you, but it is still an active touch of the subject's infrastructure. Don't escalate by sending real mail.
- OpSec: effectively **active** at the mail-server level, though not attributable to your IP.

## Overlaps ("do both")
- Pairs with `[[peep-mail-search-tool]]` and `[[mailcat]]` — those generate/permute candidates; Experte's advantage is the built-in SMTP validation that tells you which candidate is live.

## Trust & verifiability
`trust: community` — an established tools vendor doing genuine SMTP validation; results are strong leads, but catch-all servers and pattern quirks mean a "valid" flag should still be corroborated before you rely on the address.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | email-finder-3 |
| category | email |
| selectorsIn → selectorsOut | name, domain → email |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | active |
| human-in-loop | no |
