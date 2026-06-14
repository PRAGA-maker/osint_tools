---
id: disposable-email-domains
name: Disposable Email Domains
description: Use when you have an email domain and want to know if it is a known disposable/temporary provider — returns a yes/no match against a large, actively maintained open blocklist.
url: https://github.com/disposable-email-domains/disposable-email-domains
category: email
path:
- email
- email-verification
bestFor: Offline flagging of whether an email's domain is a disposable/temporary provider.
selectorsIn:
- domain
- email
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source. No account, no paywall, no network call needed to match.
opsec: passive
opsecNote: Pure offline list comparison — clone the blocklist and match locally; nothing leaks and the subject is never contacted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Large, long-running, actively maintained community blocklist used by many libraries and services; coverage is broad but, like any list, lags the newest throwaway domains.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- burner-email-providers
- disposable-email-address-dea-detector
aliases: []
tags:
- email-verification
- disposable
- github
- blocklist
source: arf-seed
lastVerified: ''
enrichment: full
---

# Disposable Email Domains

> A large, actively maintained open-source blocklist of disposable/temporary email domains you match against locally — the standard offline reference for throwaway-address detection.

## When to use
You have an `email` (or its `domain`) for a missing person, tipster, or associate and want to know whether it is a disposable/temporary address. A disposable verdict signals the account was meant to be untraceable and tells you not to over-invest in pivoting on it. Best when you want a zero-leak, scriptable check over many addresses.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo: `git clone https://github.com/disposable-email-domains/disposable-email-domains`.
2. It ships as plain-text blocklist files (and is wrapped by many language libraries, e.g. the Python package of the same name).
3. Extract the domain from each target `email` and test membership against the list locally.
4. Pivot: non-disposable domains are worth deeper enrichment (breach search, provider lookup); disposable ones flag deliberate anonymity.

## Inputs → Outputs
- **In:** `domain` (or the domain part of an `email`)
- **Out:** boolean match — disposable/temporary or not
- **Empty/negative result looks like:** no match → domain isn't on the blocklist (could still be a brand-new throwaway provider not yet added).

## Gotchas & OpSec
- A "not found" is not proof of legitimacy — new disposable domains appear faster than any list updates; pair lists to reduce misses.
- OpSec: fully passive and offline; the match runs on your machine, so nothing leaks and no one is contacted.

## Overlaps ("do both")
- Merge with `[[burner-email-providers]]` for broader coverage (overlapping but non-identical sets), and use `[[disposable-email-address-dea-detector]]` for quick one-off web checks.

## Trust & verifiability
`trust: community` — widely adopted, actively maintained open blocklist; coverage is broad but inherently incomplete for the newest domains.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | disposable-email-domains |
| category | email |
| selectorsIn → selectorsOut | domain, email → domain (disposable y/n) |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
