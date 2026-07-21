---
id: ashley-madison
name: Ashley Madison
description: Use when you have an `email`, `username` or `name` and want to check for an Ashley Madison presence — returns `social-profile` links, primarily via the 2015 breach data.
url: https://www.ashleymadison.com
category: dating-classifieds
path:
- dating-classifieds
bestFor: Checking whether a subject has (or had) an Ashley Madison affairs-dating account, mainly by cross-referencing the 2015 breach.
selectorsIn:
- email
- username
- name
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: The live site is free to join but browsing profiles requires registration and (for messaging) credits. The high-value OSINT signal — the 2015 breach — is checked via breach-lookup services, some free (HIBP) and some paid (Dehashed).
opsec: active
opsecNote: Do NOT register or search the live site with any real identity — it is an affairs platform and account creation is itself sensitive and logged. Prefer indirect checks: query the target's email against breach databases rather than touching the live site. If you must use the site, use a fully isolated sock-puppet identity and payment method.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: unverified
trustNote: The company (Ruby Corp) is real and the 2015 breach data is genuine and widely mirrored, but the live site offers no public people-search — attribution rests on the breach dump, which can contain unverified/fake signups.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
aliases:
- Ashley Madison
- ashleymadison.com
- AM breach
tags:
- dating
- breach-data
source: metaosint
lastVerified: '2026-07-21'
enrichment: full
---

# Ashley Madison

> An affairs-focused dating site whose 2015 data breach is the real OSINT asset — cross-reference a subject's email to check for an account, rather than searching the live site.

## When to use
You want to know whether a subject has an Ashley Madison presence — relevant in relationship, infidelity, and background contexts. The live site has no public people-search (you must register and browse), so the durable, low-footprint signal is the **2015 breach**: ~30M+ accounts (emails, some profile detail, and — critically — the fact of signup, which was never email-verified). Check the target's `email` against breach services; treat the live site as a last resort.

## How to use it (`bestInteractionPattern`: web-manual)
1. Preferred (passive): run the subject's `email` through breach-lookup tools — Have I Been Pwned flags Ashley Madison exposure; `[[dehashed]]`-style services can return the associated record fields.
2. Corroborate: the 2015 breach was not email-verified, so a listed email only means *someone* signed up with it — confirm with additional signals (billing data in the dump, reused username, timing).
3. Only if necessary, and never with a real identity: the live site requires registration to browse; use a fully isolated sock puppet and expect an active footprint.
4. Pivot: a confirmed username feeds cross-platform handle tools; a billing name/ZIP from the breach feeds people-search.

## Inputs → Outputs
- **In:** `email` / `username` / `name`
- **Out:** `social-profile` (account existence, breach record fields)
- **Empty/negative result looks like:** no breach hit and no live match — the person likely has no (pre-2015) account, but absence is not proof, and a *positive* email hit is not proof of use given the lack of email verification.

## Gotchas & OpSec
- The 2015 dump was never email-verified — a listed email can be someone signing up with an address that wasn't theirs. Never treat a bare email hit as confirmation of infidelity.
- The live site is **active** OSInt: registering leaves a real footprint on a sensitive platform — avoid it; work from breach data instead.
- Handle the data with care: it concerns a highly sensitive topic and real people.

## Overlaps ("do both")
- Pairs with `[[dehashed]]` and Have I Been Pwned — those are how you actually query the Ashley Madison breach; this entry frames when and why, and warns against the naive live-site approach.

## Trust & verifiability
`trust: unverified` — the breach is genuine but unverified at signup, and the live site gives no authoritative public lookup; every hit is a lead to corroborate with independent signals, never a standalone conclusion.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ashley-madison |
| category | dating-classifieds |
| selectorsIn → selectorsOut | email, username, name → social-profile |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | medium |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes (account-login) |
