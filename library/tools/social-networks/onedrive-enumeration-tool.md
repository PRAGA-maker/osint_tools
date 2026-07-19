---
id: onedrive-enumeration-tool
name: OneDrive Enumeration Tool
description: Use when you have candidate `username`s and a target's `domain`/tenant and want to confirm which are valid Microsoft 365 accounts — returns valid usernames via OneDrive URL status codes.
url: https://github.com/nyxgeek/onedrive_user_enum
category: social-networks
path:
- social-networks
bestFor: Validating which usernames exist as real Microsoft 365 / OneDrive accounts within a specific organisation's tenant, without authenticating.
selectorsIn:
- username
- domain
selectorsOut:
- username
- email
status: live
pricing: free
costNote: Free open-source Python tool (MIT-style); no cost, but you supply your own username wordlist.
opsec: active
opsecNote: This sends real HTTP probes to Microsoft's OneDrive endpoints for the target tenant. Microsoft may log the requests. It is unauthenticated enumeration but still active reconnaissance — run only with authorisation, from an attributable-to-you-not-your-org sock-puppet host, and throttle threads to avoid noise.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Well-known offensive-security tool by nyxgeek (TrustedSec); ~750+ GitHub stars, updated through 2023. Community-vetted but unofficial — it relies on a Microsoft behaviour that could change.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- account-live-com
aliases:
- onedrive_user_enum
- nyxgeek onedrive enum
tags:
- Social Media
- OneDrive
- account-existence
source: cyb-detective
lastVerified: '2026-07-19'
enrichment: full
---

# OneDrive Enumeration Tool

> A CLI that turns a username wordlist into a list of *valid* Microsoft 365 accounts for a given organisation, by reading OneDrive URL status codes (403 = exists, 404 = not) — no login required.

## When to use
You know a target organisation's `domain`/tenant and have a set of candidate `username`s (e.g. `firstname.lastname`, `flastname` patterns) and need to know which actually exist as Microsoft 365 / OneDrive accounts. Handy for confirming that a person works at an org, resolving the right username format, or narrowing a list of guesses to real accounts you can then pivot on.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo: `git clone https://github.com/nyxgeek/onedrive_user_enum` and ensure Python 3 + requests are installed.
2. Build a username wordlist (`usernames.txt`) using the org's known naming convention.
3. Run, e.g.: `./onedrive_enum.py -t <tenantname> -d <targetdomain.com> -U usernames.txt -o found.txt`
   - `-t` tenant, `-d` domain, `-U` wordlist, `-T` threads (default 100 — lower it to stay quiet), `-o` output file.
4. Accounts returning HTTP 403 exist; 404 do not. Collect the valid usernames from the output.
5. Pivot: valid usernames → likely `email` (`username@domain`) → feed to `[[account-live-com]]` for Microsoft account confirmation and further email OSINT.

## Inputs → Outputs
- **In:** `username` wordlist + target `domain`/tenant
- **Out:** confirmed-valid `username`s (and thus probable `email` addresses) at that org
- **Empty/negative result looks like:** all candidates return 404 (none valid, or wrong tenant/naming pattern), or the tenant has no OneDrive/SharePoint provisioning so the technique doesn't apply.

## Gotchas & OpSec
- **Active reconnaissance:** you are probing Microsoft infrastructure for a named org — only run with authorisation, and throttle threads to reduce detectability.
- Requires the correct tenant name and domain; a wrong tenant yields all-404 false negatives.
- The technique depends on a Microsoft URL/status-code behaviour that has changed before and could change again — verify the tool still works before relying on negatives.

## Overlaps ("do both")
- Pairs with `[[account-live-com]]` — this validates usernames within a *specific org's* tenant, while account.live.com confirms whether an individual email is any Microsoft account. Together they move from "which usernames exist" to "which emails are live".

## Trust & verifiability
`trust: community` — a widely used, reputable offensive-security tool, but unofficial and dependent on undocumented Microsoft behaviour; confirm current functionality rather than trusting stale negatives.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | onedrive-enumeration-tool |
| category | social-networks |
| selectorsIn → selectorsOut | username, domain → username, email |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
