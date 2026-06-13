---
id: mvo-name-to-verified-hub-enumeration
name: 'MVO case: name dork to face-verified Facebook hub, then enumerate the selector graph'
description: Use when you have only a name and a BOLO photo and need a disciplined identity-first chain that turns one confirmed profile into a wide, verified selector graph.
type: case-study
summary: 'In the Trace Labs Nov 2025 Most-Valuable-OSINT-winning case, the team opened on the missing person''s name with a Google dork, which surfaced news and family posts yielding multiple reference photos plus loose selectors. They located a candidate Facebook profile by name and — critically — face-verified it against the BOLO with a face-comparison tool BEFORE enumerating it, avoiding the same-name-stranger trap. The confirmed profile was then treated as a hub, not an endpoint: it expanded into roughly 24 linked accounts/directories, 14 usernames, 4 emails (which pivoted into ~10 further email-linked accounts), 2 addresses, and 2 relatives. The transferable chain is name -> reference photos -> candidate profile -> FACE VERIFY -> enumerate hub -> email/friend second wave, with verification gating enumeration at the start so no downstream pivot inherits a misidentification.'
missingPersonsRelevance: high
phase: verification
pivotFrom:
- name
pivotTo:
- social-profile
- username
- email
- address
- associate
platforms:
- google
- facebook
steps:
- Google-dork the missing person by name to surface news/family posts; harvest every reference photo and loose selector (usernames, handles, associates).
- Locate a candidate profile (here, Facebook) by searching the name directly.
- Face-verify the candidate's profile photo against the BOLO with a face-comparison tool BEFORE investing time enumerating it.
- Only after a match, treat the profile as a hub and enumerate every linked account, username, email, address, and relative it exposes.
- Run a second wave from the extracted emails (email-to-account / registration lookups) to surface accounts the username sweep alone would miss.
- Tie each new selector back to the verified subject before trusting it; keep a sourced inventory for the report.
signals:
- The face-comparison returns a high-confidence match to the BOLO, locking identity before enumeration.
- A single confirmed hub yields dozens of new selectors, and extracted emails resolve to additional accounts.
pitfalls:
- Enumerating a same-name profile without face-verifying first, building the whole case on a stranger.
- Selector sprawl - collecting dozens of accounts without tying each back to the verified subject.
- Trusting an automated face score alone on a low-quality or filtered photo without a context sanity check.
toolsUsed:
- Google
- Facebook
- FaceComparison
- people-search sites
tags:
- tracelabs
- mvo
- identity-verification
- enumeration
- selector-graph
evidence:
- type: ctf-writeup
  url: https://github.com/OSINTI4L/TraceLabs-CTF-MVO-Write-up-11.25
  note: 'Nov 2025 MVO-winning writeup: name dork -> candidate Facebook profile -> FaceComparison vs BOLO match -> enumeration yielded ~24 accounts/directories, 14 usernames, 4 emails, ~10 email-linked accounts, 2 addresses, 2 relatives.'
trust: community
source: osinti4l-mvo-writeup
relatedStrategies:
- Find the Facebook profile by name, then face-verify against the BOLO before trusting it
- Enumerate one confirmed profile into a wide selector graph via people-search and linked profiles
- Pivot through verified-profile emails into a second wave of linked accounts
- antipattern-forcing-the-match
- antipattern-automation-without-verification
---

# MVO case: name dork to face-verified Facebook hub, then enumerate the selector graph

> In the Trace Labs Nov 2025 Most-Valuable-OSINT-winning case, the team opened on the missing person's name with a Google dork, which surfaced news and family posts yielding multiple reference photos plus loose selectors. They located a candidate Facebook profile by name and — critically — face-verified it against the BOLO with a face-comparison tool BEFORE enumerating it, avoiding the same-name-stranger trap. The confirmed profile was then treated as a hub, not an endpoint, expanding into a wide selector graph. The transferable chain is name → reference photos → candidate profile → FACE VERIFY → enumerate hub → email/friend second wave.

**When to use:** When you have only a name and a BOLO photo and need a disciplined identity-first chain that turns one confirmed profile into a wide, verified selector graph.

## The pivot chain that worked
1. **Seed from the name.** A Google dork of the MP by name surfaced news coverage and family posts — yielding multiple reference photos (reusable for face verification) and loose selectors (usernames, handles, associates). The name is the cheapest, highest-yield first pivot in a thin-selector case.
2. **Locate a candidate.** Searching the name directly on Facebook returned a plausible profile.
3. **Verify before you build.** The candidate's profile photo was compared against the BOLO image with a face-comparison tool, returning a match. This is the load-bearing step: it gates enumeration on a confirmed identity so nothing downstream inherits a same-name misidentification.
4. **Treat the profile as a hub.** Only after the match did the team enumerate — and the one confirmed Facebook profile expanded into roughly 24 linked accounts/directories, 14 usernames, 4 emails, 2 addresses, and 2 relatives.
5. **Run the email second wave.** The 4 extracted emails pivoted (email-to-account / registration lookups) into ~10 additional linked accounts the username sweep alone would not have surfaced.

## The verification step
Face comparison against the BOLO **before** enumeration is what makes the chain defensible — it converts "a profile with the right name" into "the subject," documented with the tool and result. See `[[Find the Facebook profile by name, then face-verify against the BOLO before trusting it]]`.

## The lesson
Verify identity *first*, then enumerate — a confirmed profile is a hub, not an endpoint, and each new selector is a fresh pivot surface and a possible point of current contact. Skipping the face-verify is `[[antipattern-forcing-the-match]]`; trusting the enumeration output without tying each account back to the subject is `[[antipattern-automation-without-verification]]`. The discipline is what won Most Valuable OSINT.

## Signals it's working
- The face-comparison returns a high-confidence match to the BOLO, locking identity before enumeration.
- A single confirmed hub yields dozens of new selectors, and extracted emails resolve to additional accounts.

## Pitfalls
- Enumerating a same-name profile without face-verifying first, building the whole case on a stranger.
- Selector sprawl — collecting dozens of accounts without tying each back to the verified subject.
- Trusting an automated face score alone on a low-quality or filtered photo without a context sanity check.

**Tools:** Google, Facebook, FaceComparison, people-search sites

_Harvested from `osinti4l-mvo-writeup` — methodology only, no case PII. Promote/curate as needed._

---
## Metadata
| field | value |
|---|---|
| type | case-study |
| phase | verification |
| MP relevance | high |
| related | Find the Facebook profile by name, then face-verify against the BOLO before trusting it; antipattern-forcing-the-match |
