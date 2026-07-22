---
id: frg-org-uk
name: Family Rights Group Parents' Forum (UK)
description: Use when you have a `username` and want posts on a UK forum for parents in child-welfare proceedings — returns forum handle, post history, and self-disclosed detail.
url: https://www.frg.org.uk/ParentsForum/viewforum.php?f=13
category: communities-forums
path:
- communities-forums
bestFor: Reading publicly visible posts by parents discussing UK social-services and child-protection proceedings.
selectorsIn:
- username
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free to read; posts are publicly visible without login. Posting requires registration.
opsec: passive
opsecNote: This is a highly sensitive safeguarding forum — parents post anonymously about child-protection, care proceedings, and abuse allegations. Reading is passive, but treat everything here as vulnerable-person data: never register, message, or de-anonymise a poster, and handle any finding under strict minimisation. Content may identify children indirectly; do not exfiltrate or republish.
humanInLoop: true
humanInLoopReason:
- legal-gate
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Family Rights Group, an established UK charity with adviser moderation; the platform is legitimate, though posts are anonymous, emotive, and unverified.
missingPersonsRelevance: medium
coverage:
- gb
auth: none
api: false
localInstall: false
registration: false
aliases:
- FRG Parents Forum
- Family Rights Group forum
tags:
- forums
- Forums
- safeguarding
source: uk-osint
lastVerified: '2026-07-22'
enrichment: full
---

# Family Rights Group Parents' Forum (UK)

> A UK charity-run forum where parents discuss social-services involvement and care proceedings — publicly readable, but sensitive safeguarding territory that demands ethical restraint.

## When to use
You have a `username` that may be reused across sites and you are checking whether it appears on this forum, where parents post (usually anonymously) about child-protection plans, assessments, and care proceedings. A match can corroborate that a handle belongs to someone going through UK family-court/social-services processes and may surface self-disclosed details (region, timeline, family situation). Because of the subject matter, this is a source you read with care, not one you exploit.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open the public forum index (e.g. https://www.frg.org.uk/ParentsForum/viewforum.php?f=13) — topic listings, usernames, post counts, and timestamps are visible without logging in.
2. To check a specific handle, scan the listings or run `site:frg.org.uk "<username>"` in a web search.
3. Read only what is publicly posted; note self-disclosed context (region, dates, circumstances) strictly as leads.
4. Do NOT register, reply, private-message, or attempt to link a handle to a real identity.
5. Pivot: a reused handle can feed a cross-site username checker, but weigh whether pursuing it is proportionate and lawful given the vulnerability of the people involved.

## Inputs → Outputs
- **In:** `username`
- **Out:** the forum `social-profile`/handle and its public post history, with self-disclosed context
- **Empty/negative result looks like:** the handle is not present — expected, since most people never post here and many use throwaway names. Absence tells you nothing about their circumstances.

## Gotchas & OpSec
- **Ethics/legal gate:** this concerns child welfare and vulnerable adults. Handle under data-minimisation, avoid anything that could identify a child, and do not republish or exfiltrate content. If your task is a missing-persons/safeguarding case, coordinate with the appropriate authority rather than acting unilaterally.
- Posts are anonymous, emotionally charged, and unverified — treat all claims as leads, never as fact.
- Registering to see more converts this to an active footprint on a sensitive site; do not.

## Overlaps ("do both")
- Pairs with a cross-site username enumerator — that shows where else a handle lives; combine cautiously, mindful that correlating this handle to other profiles can de-anonymise a vulnerable person.

## Trust & verifiability
`trust: trusted` — the platform is a legitimate, adviser-moderated UK charity resource; the trust rating is for the site's authenticity, not for the anonymous, unverified posts, which must be corroborated and handled ethically.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | frg-org-uk |
| category | communities-forums |
| selectorsIn → selectorsOut | username → social-profile, username |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (legal-gate) |
