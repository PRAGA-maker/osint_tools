---
id: linkedin
name: LinkedIn
description: Use when you have a `name` or `employer-org` and want professional history, current employer, colleagues, and location — returns `social-profile`, `employer-org`, `associate`, `geolocation`.
url: https://www.linkedin.com/
category: public-records
path:
- public-records
- employee-profiles-and-resumes
bestFor: Professional background research, employee enumeration, and corporate structure mapping from a name or company.
selectorsIn:
- name
- employer-org
- username
selectorsOut:
- social-profile
- employer-org
- associate
- geolocation
- physical-description
status: live
pricing: freemium
costNote: Free to search and view basic profiles with an account; deeper reach (full names of 3rd-degree connections, unlimited search, InMail) needs paid Premium/Sales Navigator.
opsec: active
opsecNote: Viewing a profile can notify the target that you viewed them. Switch your account to Private/Anonymous browsing mode (Settings → Visibility → Profile viewing options) BEFORE looking at anyone, and use a sock-puppet account with no connection overlap to the subject.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: First-party professional network operated by Microsoft/LinkedIn; profile data is self-reported by users, so titles/dates can be inflated but identity signals are generally reliable.
missingPersonsRelevance: medium
coverage:
- global
auth: account
api: false
localInstall: false
registration: true
invitationOnly: false
relatedTools:
- linkedin-advanced-search
- linkedin-com
- linkedin-groups
- griffin-glynn-hatless1der
- www-linkedin-com-pub-dir-people-search
- hatless-investigations-group
aliases:
- LinkedIn.com
tags:
- social-networks
- employee-profiles
- professional-network
source: arf-seed
lastVerified: '2026-07-22'
enrichment: full
---

# LinkedIn

> The default first stop for professional identity: current employer, work history, location, and a visible web of colleagues around any working-age subject.

## When to use
You have a `name` (ideally plus a city or employer to disambiguate), a company (`employer-org`), or a `username` and want to establish where a person works now, their career history, their professional network, and often a photo and current city. In a missing-persons context it anchors a working-age subject to an employer and geography, surfaces colleagues who may have recent contact, and confirms the identity behind a name found elsewhere.

## How to use it (`bestInteractionPattern`: web-manual)
1. Log in with a **sock-puppet account** and first set Profile-viewing to **Private/Anonymous mode** (Settings → Visibility → "Profile viewing options").
2. Search the `name` in the top search bar; filter by Location and Current company to disambiguate common names.
3. Open candidate profiles: read the headline, experience timeline, education, location, "About," and the profile photo.
4. Enumerate the network: the People / "Experience at [company]" views on a company page list current employees (`associate` leads); mutual connections hint at real-world circles.
5. For deeper filtering (title + region + keyword), use `[[linkedin-advanced-search]]`. Pivot names and employers found here into people-search, email-permutation, and company-registry tools.

## Inputs → Outputs
- **In:** `name`, `employer-org`, or `username`
- **Out:** `social-profile`, `employer-org` (current + past), `associate` (colleagues/connections), `geolocation` (city/region), `physical-description` (profile photo), education
- **Empty/negative result looks like:** no matching profile, or generic matches with no distinguishing employer/location. Many people have no LinkedIn presence, so absence is not evidence they aren't working — just that they don't use the platform.

## Gotchas & OpSec
- Human-in-the-loop: search requires a logged-in account; heavy searching triggers rate limits and "commercial use limit reached" walls.
- OpSec: this is **active** — without private-mode set, the subject sees you in "who viewed your profile." Never view from an account linked to the real investigator.
- Self-reported data: titles, dates, and locations are user-entered and can be aspirational or out of date. Corroborate before relying on them.

## Overlaps ("do both")
- Pairs with `[[linkedin-advanced-search]]` and `[[www-linkedin-com-pub-dir-people-search]]` for precision filtering and logged-out public directory access, and with company-registry / people-search tools to convert an employer and name into contact details.

## Trust & verifiability
`trust: trusted` — genuine first-party platform, so account existence and network structure are authoritative; the *content* of each profile is self-reported and should be treated as claims to verify, not facts.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | linkedin |
| category | public-records |
