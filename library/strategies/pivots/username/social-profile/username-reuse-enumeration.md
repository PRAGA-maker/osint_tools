---
id: username-reuse-enumeration
name: username-reuse-enumeration
description: Use when you have a username and want the subject's accounts across platforms — people reuse handles, so one handle often unlocks a whole footprint.
type: technique
phase: pivot
pivotFrom:
- username
pivotTo:
- social-profile
- image
- email
- name
- associate
platforms:
- reddit
- instagram
- tiktok
- github
- twitter
- telegram
- steam
summary: Most people reuse the same (or a slightly varied) handle across platforms. Running a known username through cross-platform enumerators returns a list of candidate profiles; each confirmed profile is a fresh node that leaks more selectors (a profile photo → face, a linked email, a real name, a follower graph). This is usually the single highest-yield early pivot in a username-seeded case.
missingPersonsRelevance: high
whenToUse: You hold a username (from a social post, gamertag, email local-part, or another profile) and want to expand the footprint.
steps:
- Run the handle through a cross-platform enumerator (`tools/username/...`: WhatsMyName, Sherlock, Maigret) — passive, do this first.
- Also try handle VARIANTS — same name with `_`, numbers, `.`, common suffixes; and the email local-part as a handle.
- For each hit, OPEN and CONFIRM it's the same person before trusting it (profile photo, bio, location, writing style, linked accounts).
- Harvest selectors from each confirmed profile — profile image (→ face search), display name (→ real name), linked sites/email, follower/following (→ associates).
- Feed new usernames/emails found on those profiles back into step 1 (the pivot recurses).
signals:
- Multiple platforms return the same handle with a consistent photo/bio — strong same-person convergence.
- A profile links out to another account, closing a loop you'd independently found (mutual confirmation).
pitfalls:
- Handle collision — common handles (e.g. "mike") belong to many people; a hit is a CANDIDATE, not a confirmation. Verify before pivoting.
- Enumerators produce false positives (site returns 200 for non-existent users); always eyeball the actual profile.
- Tunneling into one platform's profile before enumerating the rest (breadth first — see `phase-pivot`).
toolsUsed:
- whatsmyname-web
- sherlock
- maigret
evidence: []
trust: trusted
relatedStrategies:
- phase-pivot
- pivot-username-to-face
- antipattern-forcing-the-match
tags:
- username
- social
- high-yield
source: ''
---

# Username → Social profiles (handle-reuse enumeration)

## The move
A username is rarely just one account. People reuse handles out of convenience, so one known handle is a key that often opens a dozen doors. Enumerate it across platforms, confirm each hit, and harvest the new selectors each confirmed profile leaks.

## Why it's high-yield
A confirmed profile is a *selector factory*: it gives you a `face` (profile photo → face search), a `name` (display name), often an `email` or linked site, and an `associate` graph (followers). In a CTF this single pivot frequently produces the chain that wins the case.

## How to run it
1. **Enumerate** (passive): WhatsMyName / Sherlock / Maigret across 600–3000 sites. Start here because it's free, fast, and contactless.
2. **Vary the handle**: `_`, `.`, digits, country/year suffixes, and the **email local-part** as a handle. Reuse is fuzzy, not exact.
3. **Confirm each hit** — this is the step people skip. A 200 response ≠ a real account, and a real account ≠ *your* subject. Check photo, bio, location, post cadence, writing style, and cross-links.
4. **Harvest** selectors from each confirmed profile and **recurse** any new handle/email.

## Verification discipline
Handle collisions are the main failure. Treat every hit as a candidate until at least two independent signals agree (e.g., same face *and* same city). Then promote it to a confirmed selector in your log. See `[[antipattern-forcing-the-match]]`.

---
## Metadata
| field | value |
|---|---|
| type | technique |
| pivot | username → social-profile, image, email, name, associate |
| platforms | reddit, instagram, tiktok, github, twitter, telegram, steam |
| MP relevance | high |
| tools | whatsmyname-web, sherlock, maigret |
