---
id: manycontacts-sn-results
name: ManyContacts (SN Results)
description: Use when you have an email address and want to enrich it into a name, photo, company, and linked social-network profiles — returns identity/social results tied to that email.
url: https://www.manycontacts.com
category: email
path:
- email
bestFor: Email-to-identity enrichment surfacing linked social-network profiles.
selectorsIn:
- email
selectorsOut:
- name
- social-profile
- employer-org
- image
status: degraded
pricing: freemium
costNote: Historically offered a free "Email Checker" lookup; core product is a paid contact/CRM widget. Free lookup availability has been inconsistent.
opsec: passive
opsecNote: A web-based lookup that queries third-party/social sources; you are not contacting the target. Run from a sock-puppet browser profile to avoid tying queries to you.
humanInLoop: true
humanInLoopReason:
- manual-review
bestInteractionPattern: web-manual
trust: unverified
trustNote: ManyContacts is a commercial contact/CRM vendor whose free "email checker" returned social-network results; coverage and current availability of the free lookup are not verified.
missingPersonsRelevance: high
coverage: []
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- ManyContacts Email Checker
tags:
- email
source: metaosint
lastVerified: ''
enrichment: full
---

# ManyContacts (SN Results)

> Email-enrichment lookup from a CRM vendor — turns an address into a name, photo, company, and the social-network ("SN") profiles linked to it.

## When to use
You have a confirmed `email` for a missing person or an associate and want to expand it into identity context: the person's `name`, `image`, `employer-org`, and any `social-profile` accounts registered with that address. This is the "enrich the email" step after verifying the address exists.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to manycontacts.com and locate its email-checker/lookup feature.
2. Enter the `email`; review the returned identity card and linked social profiles.
3. Manually confirm each hit — vendor enrichment can over-match on common names/avatars.
4. Pivot: returned `social-profile` links feed username/social tooling; `employer-org` feeds workplace lookups.

## Inputs → Outputs
- **In:** `email`
- **Out:** `name`, `social-profile`, `employer-org`, `image`
- **Empty/negative result looks like:** "no data" or only a gravatar — common for privacy-conscious or non-public addresses. Absence is not proof of a fake address.

## Gotchas & OpSec
- The free lookup has come and gone; the site mainly sells a CRM widget, so the feature may be gated or removed.
- Enrichment results can be stale or wrongly linked; treat each social hit as a lead to verify, not a confirmed identity.
- Cross-check social hits against a dedicated email-to-profile tool before relying on them.

## Trust & verifiability
`trust: unverified` — commercial vendor; the OSINT-relevant free lookup is undocumented and its accuracy/availability unverified. Capability described from the "SN Results" labeling and the vendor's known email-checker feature.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | manycontacts-sn-results |
| category | email |
| selectorsIn → selectorsOut | email → name, social-profile, employer-org, image |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes |
