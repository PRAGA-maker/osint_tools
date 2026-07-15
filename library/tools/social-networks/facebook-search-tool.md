---
id: facebook-search-tool
name: Facebook Search Tool (Aware Online)
description: Use when you have two Facebook profiles and want to see who they know in common — returns the mutual-friends list, i.e. `associate` and `social-profile` links between them.
url: https://www.aware-online.com/osint-tools/facebook-search-tool/
category: social-networks
path:
- social-networks
bestFor: Finding the mutual friends shared between two Facebook accounts to map connections between people.
selectorsIn:
- username
- social-profile
selectorsOut:
- associate
- social-profile
status: live
pricing: free
costNote: Free browser tool from Aware Online (a Dutch OSINT training company); no account needed. They also sell OSINT courses but the tool itself is free.
opsec: passive
opsecNote: The tool constructs a Facebook URL/query from the two IDs you supply and opens the result — you view public friend data, the targets aren't notified. You must be logged into Facebook (use a sock-puppet account) to see the results Facebook returns.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: community
trustNote: Aware Online is a reputable, well-known OSINT training provider; the tool is a thin, transparent query builder over Facebook's own pages, not a data broker.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: false
localInstall: false
registration: false
invitationOnly: false
relatedTools:
- facebook-search-3
tags:
- facebook
- aware-online
source: osint4all
lastVerified: '2026-07-15'
enrichment: full
---

# Facebook Search Tool (Aware Online)

> A one-purpose query builder from Aware Online — feed it two Facebook profile IDs and it surfaces the friends they have in common, mapping the human link between two people.

## When to use
You have two Facebook profiles and need to know how they're connected — e.g. does a missing person's account share friends with a person of interest, or does an alias account overlap with a known real account? This tool builds the Facebook "mutual friends" view for the pair, returning shared `associate`/`social-profile` links. That connection map is core network analysis: it corroborates that two accounts belong to the same social circle (or the same person), and each mutual friend is a new lead. It only works if at least one of the two profiles has a public friends list.

## How to use it (`bestInteractionPattern`: web-manual)
1. Be logged into a **sock-puppet** Facebook account (results come from Facebook's own pages).
2. Get the two profiles' usernames or numeric IDs.
3. Open https://www.aware-online.com/osint-tools/facebook-search-tool/ and enter the two Facebook users.
4. The tool builds and opens the Facebook query; read the returned list of mutual friends.
5. Pivot: each mutual friend is an `associate` to investigate; a strong overlap between an alias and a real account is evidence of shared identity; feed named friends into further profile searches.

## Inputs → Outputs
- **In:** two Facebook `username`s/IDs (`social-profile` pair)
- **Out:** list of mutual friends — `associate`/`social-profile` links between the two accounts
- **Empty/negative result looks like:** no mutual friends shown — either they genuinely share none, or (more often) both friends lists are private, which the tool cannot bypass. Treat an empty result as inconclusive when lists are hidden.

## Gotchas & OpSec
- Human-in-the-loop: **account-login** — you need an authenticated (sock-puppet) Facebook session for Facebook to serve the results.
- OpSec: **passive** toward the targets, but never use your real Facebook account; viewing profiles from a real account risks "People You May Know" leakage.
- Post-2019 limits: Facebook killed Graph Search, so this narrow mutual-friends function is one of the few reliable relationship queries left — and it still needs a public friends list on at least one side.

## Overlaps ("do both")
- Pairs with `[[facebook-search-3]]` — Social Searcher searches Facebook *content* by keyword/name, while this maps *connections* between two known accounts; use content search to find the accounts, then this to link them.

## Trust & verifiability
`trust: community` — built by a respected OSINT training firm as a transparent query builder over Facebook's own data, so the mutual-friends list is as authoritative as Facebook itself. It stores no data of its own; verify each surfaced friend on their actual profile.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facebook-search-tool |
| category | social-networks |
| selectorsIn → selectorsOut | username, social-profile → associate, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
