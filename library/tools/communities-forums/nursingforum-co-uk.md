---
id: nursingforum-co-uk
name: nursingforum.co.uk
description: Use when you have a `username` or `name` and want to find a UK nurse's forum posts, member profile, or jobseeker/CV entries — returns a `social-profile` and possible `employer-org` context.
url: http://www.nursingforum.co.uk/default.aspx
category: communities-forums
path:
- communities-forums
bestFor: Locating a UK nursing professional's forum activity, member profile, or CV/jobseeker posts by username or name.
selectorsIn:
- username
- name
selectorsOut:
- social-profile
- employer-org
status: live
pricing: free
costNote: Free to browse and register; account needs only email, username and password. No payment for public sections.
opsec: passive
opsecNote: Browsing public forum threads and member profiles is passive and leaves no trace to the target. If you register to reach gated areas you create an account record on a third-party site — use a sock-puppet email. The "Nurses Only Forum" asks for NMC registration credentials you will not have; do not attempt to fake professional credentials.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Small independent UK community board (© Hillcroft Surgery Supplies Ltd); user-generated content, so treat any claim as a lead, not verified fact.
missingPersonsRelevance: medium
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
aliases:
- Nursing Forum UK
tags:
- forums
- Forums
source: uk-osint
lastVerified: '2026-07-21'
enrichment: full
---

# nursingforum.co.uk

> A niche UK forum "for Nurses by Nurses" — useful as a haystack when your subject is (or claims to be) a UK nursing professional.

## When to use
You have a `username` or `name` and reason to believe the subject works in UK healthcare/nursing. This board carries member profiles, discussion posts, a jobs/CV section and jobseeker messages, so a hit can tie a handle to a nursing role, a location, or an employer mentioned in a post.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://www.nursingforum.co.uk/ in a normal browser.
2. Reuse a known `username` in the site's member search (or search-engine dork it: `site:nursingforum.co.uk "handle"`).
3. Alternatively browse the Jobs / CV and jobseeker sections where members post work history, region and contact intent.
4. Read a matching member profile and their post history for corroborating detail (locality, specialty, employer, other handles).
5. Pivot: a confirmed handle feeds cross-platform username tools; a stated employer feeds `[[analystforum-com]]`-style profession-board searches or employer OSINT.

## Inputs → Outputs
- **In:** `username` or `name`
- **Out:** `social-profile` (member page + post history), sometimes `employer-org` / locality gleaned from posts
- **Empty/negative result looks like:** no member match and no `site:` dork hits — treat as "not present here," not proof the subject isn't a nurse.

## Gotchas & OpSec
- Human-in-the-loop: none for public browsing. Registration is trivial (email + username), but the "Nurses Only Forum" gate asks for genuine NMC credentials — do not fabricate them.
- Small board: content volume is low, so absence is weak evidence.
- OpSec: passive while reading public pages; sock-puppet any registration.

## Overlaps ("do both")
- Pairs with `[[analystforum-com]]` and other profession-specific forums — each covers a different occupation, so pick the board matching the subject's claimed field.

## Trust & verifiability
`trust: community` — user-generated posts on a small independent forum; corroborate any factual claim elsewhere before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nursingforum-co-uk |
| category | communities-forums |
| selectorsIn → selectorsOut | username, name → social-profile, employer-org |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
