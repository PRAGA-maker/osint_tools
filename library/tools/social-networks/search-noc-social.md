---
id: search-noc-social
name: Noc.social Search
description: Use when you have a `username`, handle, or keyword and want to find matching accounts and posts across Mastodon/Fediverse instances — returns `social-profile` links.
url: https://search.noc.social/
category: social-networks
path:
- social-networks
bestFor: Discovering accounts and posts across multiple Mastodon/Fediverse instances that a single instance's search would miss.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- username
status: live
pricing: free
costNote: Free public search front end; no account required.
opsec: passive
opsecNote: You query a third-party search index, not the subject's instance directly, so the target is not notified. Your search terms are logged by the operator; use a sock-puppet browser if the handle you are chasing is sensitive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community-run Fediverse search service; coverage depends on which instances it has federated with, so absence is not proof of absence.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- search.noc.social
- noc.social search
tags:
- mastodon
- fediverse
- username-search
- social-search
source: osint4all
lastVerified: '2026-08-05'
enrichment: full
---

# Noc.social Search

> A cross-instance Fediverse search: it hunts a handle or keyword across many Mastodon servers at once, working around the fact that each instance normally only sees content it has already federated.

## When to use
You have a `username`/handle (or a name/keyword) and suspect the subject is active on Mastodon or the wider Fediverse, but you do not know which instance they are on. A single Mastodon server's search only sees posts it has encountered through federation, so it misses most accounts. This tool searches across instances to surface matching profiles and posts you can then open natively.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://search.noc.social/ (no login).
2. Enter the handle, display name, or keyword you are chasing.
3. Read the results: matching Fediverse accounts and posts across the instances it indexes. Open a hit to view the full profile on its home instance.
4. Pivot: a confirmed `@user@instance` handle feeds username-hunting tools and lets you check whether the same handle exists on other platforms.

## Inputs → Outputs
- **In:** `username`/handle, display `name`, or keyword
- **Out:** `social-profile` links and matching handles across Mastodon/Fediverse instances
- **Empty/negative result looks like:** no matches — often because the account lives on an instance this service has not federated with, so cross-check on other Fediverse search tools before concluding the subject is absent.

## Gotchas & OpSec
- Human-in-the-loop: none.
- OpSec: passive — you query the search service, not the subject's server; the target is not alerted.
- Coverage is partial and federation-dependent: absence here is weak evidence. Confirm a positive hit by opening it on the home instance, and treat a negative as "not found via this index," not "does not exist."

## Overlaps ("do both")
- Pairs with broad username tools like [[sherlock]] — those sweep hundreds of platforms by handle, while this reaches into the Fediverse's federated content those tools do not index; run both.

## Trust & verifiability
`trust: community` — a volunteer-run Fediverse index with no guarantees on completeness. Verify each hit natively on its home instance; the profile there, not this search page, is the record.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | search-noc-social |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile, username |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
