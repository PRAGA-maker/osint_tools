---
id: facebook-latest-comments-scraper
name: Facebook Latest Comments Scraper (Apify)
description: Use when you have a public Facebook post URL and want the full comment thread as structured data — returns commenter names/usernames, text and timestamps for associate-network mapping.
url: https://console.apify.com/actors/w8bYllu7Jq18uWz99
category: social-networks
path:
- social-networks
bestFor: Bulk-extracting the comments under a public Facebook post into JSON/CSV — the commenters, their handles, and timing.
selectorsIn:
- social-profile
selectorsOut:
- associate
- name
- username
status: live
pricing: freemium
costNote: An Apify actor billed per result / compute (typical Apify pay-as-you-go); the platform's free monthly credit covers small runs, but large scrapes cost money and require an Apify account.
opsec: passive
opsecNote: The actor runs on Apify's cloud infrastructure, not your machine, so the scrape originates from Apify's IPs and leaves no viewer trace tied to you on the target post. Apify logs your jobs/inputs; use a dedicated account and don't submit anything you must keep private.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: api
trust: community
trustNote: A third-party Apify Store actor, not a first-party Facebook feature; reliability depends on the actor author's maintenance and Facebook's anti-scraping defences, which change often.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Apify Facebook comments scraper
tags:
- Social Media
- Facebook
- scraper
source: cyb-detective
lastVerified: '2026-07-11'
enrichment: full
relatedTools:
- apify-s-google-maps-scraper
- dark-web-scraper
- facebook-latest-posts-scraper
- google-maps-scraper
- google-search-scraper
- instagram-hashtag-scraper
- instagram-scraper
- reddit-scraper
- twitter-scraper
- twitter-url-scraper
- youtube-scraper
---

# Facebook Latest Comments Scraper (Apify)

> An Apify cloud actor that turns a public Facebook post into a clean dataset of everyone who commented — names, handles, text and timestamps — ready for link analysis.

## When to use
You have a public Facebook post (an appeal, event, page post, or a subject's own post) and need the *whole* comment thread as data, not screenshots: who commented, their profile handles, what they said, and when. This surfaces the associate cloud around a subject and, via timestamps, who engaged first/most. Reach for it when a thread is too large to expand by hand and you want the results structured for `[[maltego]]`-style analysis.

## How to use it (`bestInteractionPattern`: api)
1. Sign into Apify and open the actor at the console URL (or find "Facebook Latest Comments Scraper" in the Apify Store).
2. Input one or more public Facebook post `social-profile` URLs, plus any result-limit options.
3. Run it; the actor scrapes from Apify's cloud and produces a dataset.
4. Export as JSON/CSV/Excel: each row is a comment with commenter `name`/`username`, text, timestamp, and reply/like counts.
5. Pivot: each commenter handle becomes a fresh subject; frequent/early commenters are candidate close `associate`s — load the dataset into link-analysis tooling.

## Inputs → Outputs
- **In:** public Facebook post URL(s) (`social-profile`)
- **Out:** structured comments → `associate`/`name`/`username` of commenters, text, timestamps, engagement counts
- **Empty/negative result looks like:** an empty or errored run — the post is private/removed, the URL is malformed, comments are disabled, or Facebook blocked the scrape; a private post yields nothing.

## Gotchas & OpSec
- Cost & account: needs an Apify account; large scrapes consume paid credits — scope your run.
- Fragility: Facebook changes markup and rate-limits aggressively, so third-party actors break and get fixed continually; check the actor's recent runs/reviews.
- Public only: this does not bypass privacy — only publicly visible comments are returned.
- OpSec: passive to the subject (Apify's cloud does the fetching), but Apify logs your inputs.

## Overlaps ("do both")
- Pairs with `[[expand-all-facebook-comments-bookmarklet]]` — the bookmarklet is a manual, no-cost fallback; the Apify actor is the scalable, structured option.
- Pairs with `[[maltego]]` — the actor produces the commenter list, Maltego maps the relationships.

## Trust & verifiability
`trust: community` — a third-party Apify Store actor, not an official Facebook export; the data is real public comments, but coverage and stability depend on the actor's upkeep against Facebook's defences, so verify a sample against the live post.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | facebook-latest-comments-scraper |
