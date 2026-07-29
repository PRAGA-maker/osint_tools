---
id: cupp
name: Cupp
description: Use when you have personal facts about a subject (`name`, `dob`, pets, partner) and — in an authorised test — want a tailored password guess-list — returns a custom `password` wordlist.
url: https://github.com/Mebus/cupp
category: ai-analysis-automation
path:
- ai-analysis-automation
- wordlist
bestFor: Building a targeted password dictionary from a person's known personal details for authorised penetration testing / forensic access.
selectorsIn:
- name
- dob
- associate
selectorsOut:
- password
status: live
pricing: free
costNote: Free and open-source (Python, GPL-3.0); no account.
opsec: active
opsecNote: CUPP only *generates* a wordlist locally — that step is passive and self-contained. But using the list to attempt logins against an account is active, intrusive, and unlawful without authorisation. Legal-gate this to consented pentests or lawful forensic access; generating and testing against a subject's real accounts without authority is account compromise.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: unverified
trustNote: Long-standing, widely-used open-source profiler (originally Muris Kurgas, maintained by Mebus); inspectable but community-maintained.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- CUPP
- Common User Passwords Profiler
tags:
- wordlist
- password-profiling
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# Cupp

> The Common User Passwords Profiler: feed it what you know about a person and it produces a guess-list of passwords they might have chosen — for authorised testing only.

## When to use
Within a **consented penetration test or lawful forensic investigation**, when you need to recover access to an account/device and have rich personal detail about its owner — `name`, `dob`, partner/child/pet names (`associate`), important dates, hobbies. CUPP mutates those facts (leet-speak, appended years, concatenations) into a targeted `password` dictionary far smaller and more likely-to-hit than a generic wordlist. It is not a people-finder; it consumes person-data you already have.

## How to use it (`bestInteractionPattern`: cli)
1. Clone and run (Python 3): `python3 cupp.py -i` for interactive profiling.
2. Answer the prompts with the subject's known details (names, dates, nicknames, pets, keywords).
3. CUPP writes a `<name>.txt` wordlist with mutations/variations.
4. Enhance an existing list with `-w`, or pull default-credential lists with `-a`.
5. Use the list **only** against systems you are authorised to test (e.g. with a cracking tool on a hash you lawfully hold).

## Inputs → Outputs
- **In:** personal facts — `name`, `dob`, `associate` (partner/pet/child), keywords, dates
- **Out:** a custom `password` wordlist (text file)
- **Empty/negative result looks like:** a wordlist that yields no hit when tested — the subject's real password wasn't derived from the details you supplied; not proof of anything.

## Gotchas & OpSec
- **Generating** is local/passive; **using** the list against real accounts is active and requires authorisation — treat that as a hard legal gate.
- Quality depends entirely on the personal detail you feed it; garbage in, garbage out.
- Modern accounts with rate-limiting/MFA blunt dictionary attacks regardless of list quality.

## Overlaps ("do both")
- Complements breach-data lookups: breaches may hand you the *actual* reused password, while CUPP guesses a *fresh* one — check breaches first, profile with CUPP if none.

## Trust & verifiability
`trust: unverified` — mature, open-source, and inspectable, but community-maintained; the tool is deterministic, so its output is fully auditable before use.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | cupp |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | name, dob, associate → password |
| pricing / cost | free |
| trust | unverified |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
