---
id: burner-email-providers
name: Burner Email Providers
description: Use when you have an email domain and want to know if it is a known burner/disposable provider — returns a yes/no match against an open, maintained domain list.
url: https://github.com/wesbos/burner-email-providers
category: email
path:
- email
- email-verification
bestFor: Flagging whether an email's domain is a disposable/throwaway provider.
selectorsIn:
- domain
- email
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open-source (MIT). No account, no paywall.
opsec: passive
opsecNote: Pure local list comparison — clone the list and match offline; no network call reveals your query, and the subject is never contacted.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular, actively maintained open-source list (wesbos) used by many apps; community-curated, so coverage is broad but not exhaustive and lags brand-new throwaway domains.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- disposable-email-domains
aliases: []
tags:
- email-verification
- burner
- github
source: arf-seed
lastVerified: ''
enrichment: full
---

# Burner Email Providers

> An open-source, regularly updated list of disposable/burner email domains you can match against locally — fast triage of whether an address is throwaway.

## When to use
You have an `email` (or just its `domain`) for a missing person, a tipster, or an associate and want to know whether it is a disposable/burner address. A burner domain signals the account was meant to be untraceable — which itself is an investigative signal, and tells you not to over-invest in pivoting on that mailbox.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo: `git clone https://github.com/wesbos/burner-email-providers`.
2. The list ships as a plain text file of domains (and a JSON build); load it into your script or grep it.
3. Extract the domain from the target `email` and check membership against the list.
4. Pivot: a non-burner domain is worth deeper enrichment (breach search, provider lookup); a burner domain tells you the account was likely intended to be disposable.

## Inputs → Outputs
- **In:** `domain` (or the domain part of an `email`)
- **Out:** boolean match — burner/disposable or not
- **Empty/negative result looks like:** no match → domain is not in the known-burner list (could still be a niche/new disposable provider the list hasn't captured).

## Gotchas & OpSec
- A "not found" is not proof the domain is legitimate — new throwaway domains appear faster than any list updates.
- OpSec: fully passive and offline; the match happens on your machine, so nothing leaks and no one is contacted.

## Overlaps ("do both")
- Pair with `[[disposable-email-domains]]` — both are open lists of throwaway domains with overlapping but non-identical coverage; merge them for fewer misses.

## Trust & verifiability
`trust: community` — widely used open-source list under active maintenance; coverage is broad but inherently incomplete for brand-new domains.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | burner-email-providers |
| category | email |
| selectorsIn → selectorsOut | domain, email → domain (burner y/n) |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
