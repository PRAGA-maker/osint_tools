---
id: xposedornot
name: XposedOrNot
description: Use when you have an `email` (or password) and want to know which known data breaches it appears in — returns breach names, leaked data classes, and a risk score.
url: https://xposedornot.com/
category: email
path:
- email
bestFor: Free breach-exposure check for an email — which breaches, what data leaked, and infostealer/stealer-log hits.
selectorsIn:
- email
- password
selectorsOut:
- email
- password
status: live
pricing: free
costNote: Fully free — email breach lookup, password-leak check, stealer-log checks, domain monitoring and API are all no-cost; no account required for a single lookup.
opsec: passive
opsecNote: You query XposedOrNot's own servers, never the target's infrastructure, so nothing is sent to the person. The site states queries are processed in memory and not logged in identifiable form, but you are still disclosing the address to a third party — use it for subjects, not for your own operational identifiers.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Independent open-source project (GitHub) drawing on 11B+ exposed records across 760+ breaches; well-regarded as a free HIBP alternative but not an institutional source — corroborate before acting.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- i-see-you-iseeyou
- passhunt
aliases:
- Xon
- XposedOrNot.com
tags:
- breach
- password
- exposure
- haveibeenpwned-alternative
source: gh-topic-intelligence-gathering
lastVerified: '2026-07-18'
enrichment: full
---

# XposedOrNot

> Free data-breach exposure oracle: paste an email and see every known breach it landed in, what data leaked, and whether it shows up in infostealer stealer-logs.

## When to use
You have a subject's `email` and want to enumerate the online services they used and the breaches that touched them. Breach hits are pivots: a breach tied to a niche gaming, dating, or forum site tells you the person held an account there, which becomes a new place to search for a username, display name, or reused password. Also use it as a fast free second opinion when Have I Been Pwned is rate-limited or gated.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://xposedornot.com/ and use the email breach search box (or the password/stealer-log tools).
2. Enter the target `email` and submit. No login is required for a single lookup.
3. Read the result:
   - A list of named breaches, each with the categories of data exposed (passwords, names, IPs, phone numbers, etc.) and an overall risk score.
   - The stealer-log section flags whether the address appears in infostealer malware dumps — a strong signal the person's device was compromised.
4. For bulk or repeat work, use the free JSON API (`api.xposedornot.com/v1/breach-analytics?email=...`) instead of the web form.
5. Pivot: each breach name → look up which service it is → search that platform for the subject's username; a stealer-log hit → treat associated credentials/devices as compromised leads.

## Inputs → Outputs
- **In:** `email` (also supports a `password` leak check via k-anonymity hash, and domain monitoring)
- **Out:** list of breaches, `email`/`password`-class exposure per breach, risk score, stealer-log presence
- **Empty/negative result looks like:** "No breaches found" / an empty breach list — means the address is not in XposedOrNot's dataset, NOT that the person is breach-free (coverage differs from HIBP).

## Gotchas & OpSec
- Coverage is not identical to Have I Been Pwned — a clean result here does not mean clean elsewhere; run both.
- Breach data is aggregated from public dumps of varying quality; treat leaked names/phones as leads to verify, not facts.
- Never enter your own operational email/passwords; use it against subjects. The service claims not to log identifiably, but you are still sending the selector to a third party.

## Overlaps ("do both")
- Pairs with `[[passhunt]]` and `[[i-see-you-iseeyou]]` — run this for breach enumeration, then those to extend account/exposure discovery where XposedOrNot's dataset is thin.

## Trust & verifiability
`trust: community` — open-source, transparent about methodology and privacy, and widely cited as a free HIBP alternative, but it is a solo/community project without institutional backing, so corroborate any actionable finding.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | xposedornot |
| category | email |
| selectorsIn → selectorsOut | email, password → email, password |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
