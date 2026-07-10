---
id: buster
name: Buster
description: Use when you have an `email` and want linked accounts, breaches, pastes and reverse-WHOIS domains — returns social-profile, name and domain leads.
url: https://github.com/sham00n/buster
category: email
path:
- email
bestFor: Email reconnaissance from the CLI — mapping an address to social accounts, breach/paste appearances, registered domains and name/username guesses.
selectorsIn:
- email
selectorsOut:
- social-profile
- name
- domain
status: degraded
pricing: free
costNote: Free and open-source (Python). Some data sources (e.g. hunter.io for work emails) benefit from a free API key added to api-keys.yaml; without keys, coverage is reduced.
opsec: passive
opsecNote: Buster queries third-party services and public breach/paste indexes about the email — it does not contact the address owner, so it is passive toward the target. Your queries do hit those third parties, so run behind a VPN and use throwaway API keys.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source email-OSINT tool (1.4k+ stars) by sham00n; effective, but several upstream sources it relies on change or die over time, so results are uneven and some modules may be broken.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- buster
- sham00n/buster
tags:
- email-osint
- breach-check
- cli
source: osint4all
lastVerified: '2026-07-10'
enrichment: full
---

# Buster

> A command-line email-reconnaissance tool — hand it an address and it pulls together linked social accounts, breach/paste appearances, reverse-WHOIS domains and likely name/username variants.

## When to use
You have an `email` and want to expand it into identity: which platforms (Gravatar, GitHub, LinkedIn, Skype, about.me, MySpace, etc.) the address is tied to, whether it appears in known breaches or paste sites, what domains were registered with it (reverse WHOIS), and plausible real-name/username variations. It's an aggregator of many email checks in one run — a strong early step when an email is your only firm selector.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo and install (`python3 setup.py install`).
2. Add optional API keys (e.g. hunter.io) to `api-keys.yaml` to widen coverage.
3. Run against an address: `buster -e target@example.com` (see `-h` for modes — accounts, breaches, domains, variations).
4. Review each section: linked `social-profile`s, breach/paste hits, reverse-WHOIS `domain`s, and derived `name`/username guesses.
5. Pivot: linked accounts feed platform OSINT; a reverse-WHOIS domain feeds infrastructure research; name guesses feed people-search.

## Inputs → Outputs
- **In:** `email`
- **Out:** `social-profile` (linked accounts), `name` (from Gravatar/derivations), `domain` (reverse WHOIS)
- **Empty/negative result looks like:** empty sections or errors — often because a source is rate-limited, needs a key, or has gone offline, NOT proof the email is clean; corroborate a "nothing found" with a second email tool.

## Gotchas & OpSec
- **Uneven/aging sources:** some modules depend on services that have changed or shut down; expect gaps and cross-check.
- API keys materially improve coverage but add third-party accounts — use throwaways.
- **Passive** toward the person, but your queries hit many third parties — use a VPN.

## Overlaps ("do both")
- Pairs with Holehe, `[[account-live-com]]` and breach-search tools — run several email tools, since each checks a different set of sites and breach corpora; combine for confidence.

## Trust & verifiability
`trust: community` — a popular, inspectable open-source tool, but only as current as its upstream sources; verify each linked account and breach hit directly before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | buster |
| category | email |
| selectorsIn → selectorsOut | email → social-profile, name, domain |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (api-key) |
