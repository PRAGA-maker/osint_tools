---
id: hudson-rock-cavalier
name: Hudson Rock Cavalier
description: Use when you have an `email` or `domain` and want to know if it was compromised by infostealer malware — returns infection status plus leaked credentials/`device-id` context.
url: https://cavalier.hudsonrock.com/
category: email
path:
- email
bestFor: Free check of whether an email, domain or username appears in infostealer (info-stealer malware) infection data.
selectorsIn:
- email
- domain
- username
selectorsOut:
- email
- device-id
- password
status: live
pricing: freemium
costNote: Free tier lets anyone check emails/domains/usernames (and monitor up to 3 of each) plus a free public API; the full breach details, exposed credentials and enterprise data need a paid Cavalier plan.
opsec: passive
opsecNote: You query Hudson Rock's database, not the target's machine or accounts — nothing is sent to the subject, so this is passive and safe. Do not enter your own operational credentials; only submit the selectors you are investigating. Results reveal a compromise, not a way to act on it.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Hudson Rock is an established cybercrime-intelligence vendor; its infostealer dataset is widely cited and its free lookups are drawn from the same commercial data.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- hudson-rock
- haveibeenpwned
aliases:
- HudsonRock
- Cavalier
tags:
- email
- infostealer
- breach
- credentials
source: inteltechniques-tools
lastVerified: '2026-07-17'
enrichment: full
---

# Hudson Rock Cavalier

> A free window into infostealer-malware infections: check whether an email, domain, or username turns up on a machine compromised by info-stealing malware.

## When to use
You have an `email`, `domain`, or `username` and want to know if it has been caught in infostealer malware logs — data harvested from victims' infected computers (saved logins, autofill, cookies). A hit tells you the subject (or their organisation) had a machine compromised, which both flags a security exposure and hands you a cluster of the credentials/services that were on that machine. This is distinct from ordinary breach-corpus lookups: it's about *this person's device* being infected, which is a strong signal of active use and leaks the accounts they were logged into.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://cavalier.hudsonrock.com/.
2. Enter the `email`, `domain`, or `username` you're investigating in the relevant free lookup.
3. Read the result: whether it appears in infostealer data, roughly when/how many infections, and (in free vs paid tiers) what services/credentials were exposed on the infected machine.
4. For automation, hit the free public API endpoints (e.g. `/api/json/v2/osint-tools/search-by-domain?domain=...`).
5. Pivot: exposed services reveal other accounts/`email`s to chase; a compromised corporate `domain` widens to employee exposure; the presence of an infection corroborates that an address is real and active.

## Inputs → Outputs
- **In:** `email`, `domain`, or `username`
- **Out:** infection status, associated exposed services/`email`s, and (paid) leaked `password`/`device-id` context
- **Empty/negative result looks like:** "not found in infostealer data" — the selector isn't in Hudson Rock's infection dataset. That is good news for the person, not proof they've never been breached elsewhere (use a general breach checker too).

## Gotchas & OpSec
- "Not infected" ≠ "never breached" — this covers infostealer logs specifically, a subset of all exposure. Pair with a broad breach checker.
- Full credential detail is gated behind paid plans; the free tier confirms exposure and gives partial context.
- OpSec: passive; you never touch the subject. Never paste your own live credentials into the box.

## Overlaps ("do both")
- Pairs with `[[hudson-rock]]` (the broader Hudson Rock tooling) and `[[haveibeenpwned]]` — HIBP covers traditional data-breach corpora while Cavalier covers infostealer-infected machines, so together they cover complementary exposure types.

## Trust & verifiability
`trust: trusted` — Hudson Rock is a recognised cybercrime-intelligence firm and the free lookups draw on its commercial infostealer dataset. Treat a hit as a reliable signal of infostealer exposure; corroborate any specific leaked credential before acting on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | hudson-rock-cavalier |
| category | email |
| selectorsIn → selectorsOut | email, domain, username → email, device-id, password |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
