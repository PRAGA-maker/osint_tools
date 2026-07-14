---
id: teleteg
name: Teleteg
description: Use when you have a topic, `name` or keyword and want to discover public Telegram channels/groups around it — returns social-profile links to communities plus activity metrics.
url: https://teleteg.com/
category: messaging
path:
- messaging
bestFor: Discovering and profiling public Telegram channels and groups by topic, language, location, and activity metrics.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
status: live
pricing: freemium
costNote: Free tier returns the top ~10 results per search; deeper result sets and analytics are paid (tiered per-record pricing, e.g. ~$19/1,000 records and up).
opsec: passive
opsecNote: You search Teleteg's index, not Telegram directly, so the target channels get no visit from you at discovery time. Opening a discovered channel in Telegram is a separate, more active step — do that from a sock-puppet Telegram account.
humanInLoop: true
humanInLoopReason:
- payment-wall-partial
bestInteractionPattern: web-manual
trust: community
trustNote: A third-party Telegram search/analytics service indexing public channels/groups; results are only as complete and current as its crawl.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- telemetr-io
- telegago
aliases:
- Teleteg Telegram search
tags:
- telegram
- telegram-search
source: awesome-osint
lastVerified: '2026-07-14'
enrichment: full
---

# Teleteg

> A public-Telegram search engine — find channels and groups by topic, language, and location, with activity and quality metrics to rank them.

## When to use
You have a topic, `name`, brand, place, or keyword and want to find the public Telegram communities around it — where a subject might post, coordinate, or be discussed. Its differentiator is filtering and metrics (language, country, member count, activity, community age) that help you separate active, relevant channels from dead ones before you ever open Telegram.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://teleteg.com/ and enter a keyword/topic (or a channel `username`/`name`).
2. Filter by language, country, and metrics; the free tier shows the top ~10 hits.
3. Review each result's metrics and description; decide which channels to open.
4. Pivot: a discovered channel/group is a `social-profile` to open (in a sock-puppet Telegram) and to run through Telegram-specific tooling for members, history, and links.

## Inputs → Outputs
- **In:** topic/keyword, `name`, or channel `username`
- **Out:** `social-profile` (Telegram channels/groups) plus activity/quality metrics to rank them
- **Empty/negative result looks like:** few or no channels — either the topic has no public Telegram presence, or the relevant channels are private/unindexed. Absence is not proof; private Telegram spaces are invisible here.

## Gotchas & OpSec
- Human-in-the-loop: the free tier is a teaser (top 10); full result depth is paid per-record.
- Only *public* channels are indexed; private/invite-only groups and one-to-one chats never appear.
- OpSec: passive at the discovery stage; joining/viewing a channel later is active — use a burner Telegram identity.

## Overlaps ("do both")
- Pairs with `[[telemetr-io]]` and `[[telegago]]` — coverage and metrics differ per Telegram search engine, so run more than one before concluding a community doesn't exist.

## Trust & verifiability
`trust: community` — a third-party index, not Telegram itself; verify each discovered channel directly in Telegram and treat metrics as approximate.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | teleteg |
| category | messaging |
| selectorsIn → selectorsOut | name, username → social-profile |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (payment-wall-partial) |
