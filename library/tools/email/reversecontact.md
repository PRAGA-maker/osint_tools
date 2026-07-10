---
id: reversecontact
name: ReverseContact
description: Use when you have an `email` (or domain) and want to resolve it to a real person and their LinkedIn/work identity — returns `name`, `social-profile`, `employer-org` and job details.
url: https://www.reversecontact.com/
category: email
path:
- email
bestFor: Email-to-LinkedIn/identity enrichment — turning a bare email address into a full name, LinkedIn profile, employer, and role.
selectorsIn:
- email
selectorsOut:
- name
- social-profile
- employer-org
status: live
pricing: freemium
costNote: Effectively a paid B2B enrichment API — pay-as-you-go, no real free trial (any free credits are minimal). Requires registration and an API key; pricing is via their portal/sales. Treat as paid.
opsec: passive
opsecNote: You submit the target's email to a third-party enrichment service, which stores/logs the query and matches it against its 800M-profile database. No signal reaches the target, but you are disclosing the selector to a commercial vendor — use an investigative account, not personal.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: api
trust: community
trustNote: Commercial enrichment vendor (claims GDPR/CCPA compliance, ~80% match rate). Data is aggregated from public/third-party sources, so matches can be stale or wrong — verify before relying.
missingPersonsRelevance: high
coverage:
- global
auth: api-key
api: true
localInstall: false
registration: true
aliases:
- Reverse Contact
- reversecontact.com
tags:
- email
- linkedin
- enrichment
source: gh-topic-osint-resources
lastVerified: '2026-07-10'
enrichment: full
---

# ReverseContact

> A commercial email-to-LinkedIn enrichment API: feed it an email address, get back the person's real name, LinkedIn profile, employer, and role.

## When to use
You have an `email` (from a breach, a signup, a header, a scrape) and need to know **who it belongs to** and where they work. ReverseContact matches the address against a large B2B identity database and returns a LinkedIn profile plus enriched fields — a fast email→identity pivot. Reach for it when the email is your only selector and you want a name/employer/social handle to keep the investigation moving. Best for professional/work-adjacent emails; weakest on throwaway personal addresses.

## How to use it (`bestInteractionPattern`: api)
1. Register at reversecontact.com and obtain an API key (there is no meaningful anonymous/free path — expect to pay per lookup).
2. Try the interactive API playground on the homepage to sanity-check a single email before committing to volume.
3. Call the enrichment endpoint with the target `email` (a company domain can also be enriched for firmographics).
4. Read the response: full `name`, LinkedIn URL (`social-profile`), current `employer-org`, job title, location, and other social/work fields (their demo cites ~247 fields).
5. Pivot: LinkedIn profile → deeper social/employment mapping; employer → corporate registries; name+location → people-search and public records.

## Inputs → Outputs
- **In:** `email` (or company domain)
- **Out:** `name`, `social-profile` (LinkedIn URL), `employer-org`, job title, location, other enriched fields
- **Empty/negative result looks like:** a no-match / low-confidence response (they cite ~80% match, so ~1 in 5 fails). A miss means the email isn't in their B2B data — common for purely personal/consumer addresses — not that the person doesn't exist.

## Gotchas & OpSec
- **Paid + key required:** not a free web lookup; budget for per-query cost and manage the API key.
- Aggregated data can be **stale** (old employer, changed name) or mismatched — treat a hit as a lead and confirm on LinkedIn directly.
- OpSec: passive toward the target, but you disclose the email to a commercial vendor that logs it; use an investigative account.

## Overlaps ("do both")
- Pairs with free email-existence/account tools like `[[account-live-com]]` and with Hunter/EmailRep-style checks — those confirm an address is live; ReverseContact tries to name the human behind it.
- Cross-verify the returned LinkedIn against the employer's site/registry.

## Trust & verifiability
`trust: community` — a legitimate commercial vendor, but its output is aggregated third-party data with a real error rate. Verify every decisive hit (name, employer) against the actual LinkedIn profile or a primary source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | reversecontact |
| category | email |
| selectorsIn → selectorsOut | email → name, social-profile, employer-org |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | api |
| opsec | passive |
| human-in-loop | yes (api-key) |
