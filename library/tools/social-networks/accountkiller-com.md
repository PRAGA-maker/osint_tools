---
id: accountkiller-com
name: accountkiller.com
description: Use when you have a `username` and want a reference directory of where accounts can exist plus each platform's account/URL structure — returns social-profile enumeration leads, not a person lookup.
url: http://www.accountkiller.com/en/
category: social-networks
path:
- social-networks
bestFor: Enumerating which platforms an account may exist on and understanding each site's account-page conventions.
selectorsIn:
- username
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free, ad-supported directory of 1,300+ account-deletion guides; no account or payment required.
opsec: passive
opsecNote: Purely a reference directory — you browse platform guides, you do not submit a target's selectors anywhere. Fully passive; nothing reaches the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-maintained catalog of account-deletion instructions; useful as a platform index, but it holds no personal data and performs no lookups itself.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- AccountKiller
- accountkiller.com
tags:
- gsocialmedia
- General Social Media Sites
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# accountkiller.com

> A directory of "how to delete your account" guides for 1,300+ services — repurposed in OSINT as a checklist of platforms where a handle might live and how their account pages are structured.

## When to use
This is a **reference**, not a search tool. Reach for it when you have a `username` and are building the list of platforms to check it against, or when you need to know a given service's account/profile URL convention (and whether it even allows public profiles). It does not take a person as input and returns no personal data — it tells you *where to look*, then you run the actual check elsewhere.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.accountkiller.com/en/ and browse the A–Z of services (or search a platform name).
2. For each relevant platform, read the guide to learn: does it host public profiles, what does an account URL look like, and is it "blacklisted" (i.e., near-impossible to delete — which often means sticky, long-lived accounts worth checking).
3. Build your target platform list from that, then run the actual `username`/handle check on `[[social-profiles-finder]]`, `[[user-sherlock]]`, or the platform directly.
4. Pivot: the platform-URL conventions here help you hand-construct candidate profile URLs to test after generating handle variants.

## Inputs → Outputs
- **In:** `username` (as the thing you plan to look up elsewhere) — the site itself is browse-only
- **Out:** `social-profile` enumeration leads (which platforms exist, their account-URL patterns)
- **Empty/negative result looks like:** the platform isn't in the catalog, or the guide only covers deletion with no profile-structure detail — it never returns a hit/no-hit on a specific person.

## Gotchas & OpSec
- Do not mistake this for a namechecker: it performs no lookups and confirms nothing about a specific individual.
- Its "blacklisted / can't be deleted" flags are an OSINT tell — such platforms tend to retain old accounts, so they're higher-yield to check.

## Overlaps ("do both")
- Feeds `[[social-profiles-finder]]` and `[[user-sherlock]]`: use AccountKiller to decide *which* platforms and URL patterns to test, then use those tools to actually resolve a handle to profiles.

## Trust & verifiability
`trust: community` — a crowd-maintained deletion-guide catalog; accurate enough as a platform index, but it holds no data to verify against and should never be cited as evidence about a person.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | accountkiller-com |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
