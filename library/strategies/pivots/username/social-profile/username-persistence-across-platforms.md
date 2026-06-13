---
id: username-persistence-across-platforms
name: Username persistence across platforms
description: Use when Immediately after recovering any username or handle for the subject or a close associate.
type: technique
summary: People reuse the same handle, nickname, avatar, or profile photo across many platforms. Once you recover any one username, enumerate it everywhere with a username checker to discover accounts on platforms you would not have thought to check. The first analytic question is whether the subject uses a consistent identifier across platforms; if so, a single handle unlocks a cluster of profiles. Treat the checker output as leads to verify, not confirmed hits.
missingPersonsRelevance: high
phase: pivot
pivotFrom:
- username
pivotTo:
- social-profile
- username
- email
platforms:
- instagram
- twitter
- reddit
- tiktok
- telegram
steps:
- Extract the candidate username/handle.
- Run it through a username enumeration tool (Sherlock, WhatsMyName, Namecheckr) across many platforms.
- Also test obvious variants (added numbers, underscores, name initials).
- Manually verify each hit by matching avatar/photo/bio to the subject before treating it as the same person.
- Pivot newly found profiles back into friend and tag enumeration.
signals:
- Same avatar/photo appears under the handle on multiple sites
- Bio details (city, school) match across accounts
pitfalls:
- Trusting checker hits without verifying they are the same person
- Spending 20 minutes feeding data into a tool when a manual check would be faster
- Forgetting handle variants
toolsUsed:
- Sherlock
- WhatsMyName
- Namecheckr
- Namechk
tags:
- username
- enumeration
- pivot
- cross-platform
evidence:
- type: writeup
  url: https://medium.com/@cyberbychase/osint-methodology-and-tradecraft-tips-for-winning-the-trace-labs-black-badge-from-team-federal-ebe737d70c6a
  note: Sherlock and WhatsMyName; people reuse handles across sites
- type: writeup
  url: https://www.osintme.com/index.php/2021/11/14/a-noobs-guide-to-trace-labs-search-party-ctf/
  note: Establish whether subject uses same nickname/handle/avatar/photo across platforms as the best research angle
- type: writeup
  url: https://shandyman.online/blog/on-a-mission-a-tracelabs-ctf-missing-persons-writeup/
  note: Namecheckr and WhatsMyName for initial cross-platform profile discovery
trust: community
source: searchparty-writeups
---

# Username persistence across platforms

> People reuse the same handle, nickname, avatar, or profile photo across many platforms. Once you recover any one username, enumerate it everywhere with a username checker to discover accounts on platforms you would not have thought to check. The first analytic question is whether the subject uses a consistent identifier across platforms; if so, a single handle unlocks a cluster of profiles. Treat the checker output as leads to verify, not confirmed hits.

**When to use:** Immediately after recovering any username or handle for the subject or a close associate.

## Steps
- Extract the candidate username/handle.
- Run it through a username enumeration tool (Sherlock, WhatsMyName, Namecheckr) across many platforms.
- Also test obvious variants (added numbers, underscores, name initials).
- Manually verify each hit by matching avatar/photo/bio to the subject before treating it as the same person.
- Pivot newly found profiles back into friend and tag enumeration.

## Signals it's working
- Same avatar/photo appears under the handle on multiple sites
- Bio details (city, school) match across accounts

## Pitfalls
- Trusting checker hits without verifying they are the same person
- Spending 20 minutes feeding data into a tool when a manual check would be faster
- Forgetting handle variants

**Tools:** Sherlock, WhatsMyName, Namecheckr, Namechk

_Harvested from `searchparty-writeups` — methodology only, no case PII. Promote/curate as needed._
