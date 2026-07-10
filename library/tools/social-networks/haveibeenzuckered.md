---
id: haveibeenzuckered
name: HaveIBeenZuckered
description: Use when you have a `phone` number and want to know if it was exposed in the 2021 Facebook 533M breach — returns whether that number appears in the leaked dataset.
url: https://haveibeenzuckered.com/
category: social-networks
path:
- social-networks
bestFor: Checking whether a phone number was in the 2021 Facebook (533M-record) data breach, implying a Facebook account was tied to it.
selectorsIn:
- phone
selectorsOut:
- metadata-exif
- social-profile
status: live
pricing: free
costNote: Free lookup; no account.
opsec: passive
opsecNote: You check a number against a static leaked dataset held by the site, not against Facebook, so the account owner is not notified. You do disclose the number to a third-party site — use a sock-puppet context and avoid submitting numbers you aren't authorised to check.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A single-purpose checker over the well-documented 2021 Facebook scrape; a hit is a strong signal the number had a Facebook account in that era, but the dataset is fixed (2021) and doesn't reflect current status.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- numberingplans-com
aliases:
- haveibeenzuckered.com
- have I been zuckered
tags:
- facebook
- data-breach
- phone
source: awesome-osint
lastVerified: '2026-07-10'
enrichment: full
---

# HaveIBeenZuckered

> A single-purpose checker for the 2021 Facebook breach — enter a `phone` number and learn whether it appears in the 533-million-record scrape, implying a Facebook account was linked to it.

## When to use
You have a `phone` number and want a quick corroboration that it belonged to a Facebook user (as of 2021). The leaked dataset paired phone numbers with Facebook profile data, so a hit both confirms the number is real/was in use and tells you the person had a Facebook account tied to it — a useful pivot when Facebook itself won't reveal the number-to-account link.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://haveibeenzuckered.com/ and enter the `phone` number in international format.
2. Read the result: whether the number is present in the 2021 breach dataset.
3. Treat a hit as "this number had a Facebook account in 2021" — then search Facebook and people-search for the person behind it.
4. A miss means the number wasn't in this particular scrape, not that there's no Facebook account.
5. Pivot: classify the number's country/type with `[[numberingplans-com]]`; a confirmed FB linkage justifies deeper Facebook and reverse-phone work.

## Inputs → Outputs
- **In:** `phone` number
- **Out:** `metadata-exif` (present/absent in the 2021 FB breach) → implied `social-profile` (a Facebook account existed for it)
- **Empty/negative result looks like:** "not found" — the number isn't in this dataset; it may still have a Facebook account (created later, or not scraped), so absence is inconclusive.

## Gotchas & OpSec
- The dataset is **fixed at 2021** — it says nothing about accounts created since, and a present number may since have been recycled.
- It confirms *linkage*, not the person's identity — you still have to find and verify the account.
- OpSec: passive toward the target; you disclose the number to a third-party site.

## Overlaps ("do both")
- Pairs with `[[numberingplans-com]]` (number classification) and reverse-phone/people-search — HaveIBeenZuckered establishes the historical Facebook link; those attach a current identity.

## Trust & verifiability
`trust: community` — a reliable checker over a known leak; a hit is strong historical evidence, but confirm the actual Facebook account and current details separately.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | haveibeenzuckered |
| category | social-networks |
| selectorsIn → selectorsOut | phone → metadata-exif, social-profile |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
