---
id: osintcombine-com-2
name: OSINT Combine — Mastodon Investigation Guide
description: Use when you have a `username`/`name` and need a method for finding and investigating a subject on Mastodon/the Fediverse — a reputable how-to guide returning tools and techniques, not a lookup itself.
url: https://www.osintcombine.com/post/let-s-get-on-with-mastodon
category: social-networks
path:
- social-networks
bestFor: Learning the workflow and third-party tools for locating and investigating Mastodon/Fediverse accounts.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
status: live
pricing: free
costNote: Free public article on the OSINT Combine blog. Some tools it recommends need their own account (e.g. a Twitter/X account for migration-finder tools).
opsec: passive
opsecNote: Reading the guide is passive. The techniques it describes range from passive (third-party keyword search) to active (native searching requires a Mastodon account) — apply the relevant per-tool OpSec when you execute them.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: OSINT Combine is a well-regarded professional OSINT training/tooling company; their guidance is reliable, though individual third-party tools it links can change or disappear.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- facebook-geo
- instagram-explorer
- osint-combine-blog
- osint-combine-reddit-post-analyzer
- osint-combine-tiktok-quick-search
- osint-combine-tools
- osintcombine-com
- snapchat-multi-viewer-osint-combine
aliases:
- Let's get on with Mastodon
- OSINT Combine Mastodon guide
tags:
- mastodon
- Mastodon Related Sites
source: uk-osint
lastVerified: '2026-07-14'
enrichment: full
---

# OSINT Combine — Mastodon Investigation Guide

> A reputable how-to article (not a lookup tool) that lays out the workflow and third-party tools for finding and investigating Mastodon/Fediverse accounts.

## When to use
You have a `username` or `name` and suspect the subject is on Mastodon or the wider Fediverse, and you need a method — because Mastodon is decentralised across many servers and its native search is deliberately limited. Treat this file as a strategy reference: read it to know which tools to reach for and how to combine native and third-party search.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read the guide at the URL for the current workflow. Its key steps:
2. **Native search:** if you know the handle *and* home server, search within Mastodon (results are limited to profiles, not post content).
3. **Third-party people/keyword search:** try `search.noc.social` and `fediverse.info/explore/people` to find profiles across servers (these search profile info, not "toots").
4. **Twitter→Mastodon migration:** for users who moved keeping their handle, use `fedifinder.glitch.me` or `debirdify.pruvisto.org` (both need a Twitter/X account).
5. **Hashtag/server intel:** use `mastovue.glitch.me` for federated hashtag results and `fediverse.observer/map` + `/stats` for server-level context; for a specific instance, pivot to WHOIS/DNS (`dnsdumpster.com`), `builtwith.com`, and `urlscan.io`.
6. Read the output: the matching Fediverse `social-profile`(s), plus server/domain intel. Pivot on the home instance's domain for operator/hosting leads.

## Inputs → Outputs
- **In:** `username`/`name` (and known server, if any)
- **Out:** `social-profile` (Mastodon/Fediverse accounts), plus server/domain leads
- **Empty/negative result looks like:** no cross-server profile match — the subject may use a handle unlike their other identities, or be on a small unindexed instance. Try instance-specific search directly.

## Gotchas & OpSec
- This is a guide, not a search box — the value is the method and the linked tools, several of which are volunteer-run (glitch.me) and may break.
- Native Mastodon search needs an account (active); third-party keyword tools are passive. Apply the right OpSec per step.
- Migration-finder tools require a Twitter/X account — use a sock, not your own.

## Overlaps ("do both")
- Complements domain/infrastructure tools (WHOIS, dnsdumpster, urlscan) — once you find the subject's home instance, investigate the server itself, not just the profile.

## Trust & verifiability
`trust: trusted` — authored by OSINT Combine, a respected professional OSINT provider. The methodology is sound; just re-verify that any linked third-party tool is still live before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osintcombine-com-2 |
| category | social-networks |
| selectorsIn → selectorsOut | username, name → social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
