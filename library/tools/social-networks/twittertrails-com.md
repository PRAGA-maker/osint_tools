---
id: twittertrails-com
name: TwitterTrails.com
description: Use when you have a claim/rumor or hashtag and want to analyze how it spread on Twitter and how skeptical the audience was — but this .com domain is now dead/repurposed, so treat as defunct.
url: http://twittertrails.com/
category: social-networks
path:
- social-networks
bestFor: (Defunct) investigating rumor propagation, originators, and audience skepticism on Twitter; the .com no longer hosts the tool.
selectorsIn:
- username
selectorsOut:
- social-profile
status: down
pricing: free
costNote: Was a free academic research tool; the twittertrails.com domain has been abandoned and is now parked with unrelated spam/blog content.
opsec: passive
opsecNote: Moot — the tool is offline. When it operated it analyzed public tweets in aggregate (passive; no interaction with any individual subject).
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: unverified
trustNote: The original TwitterTrails was a credible Wellesley College research project (blogs.wellesley.edu/twittertrails), but the twittertrails.com domain is now repurposed and no longer runs it — do not trust content currently served there.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases:
- TwitterTrails
- TRAILS
tags:
- xtwitter
- misinformation
- defunct
source: osint4all
lastVerified: '2026-07-15'
enrichment: full
---

# TwitterTrails.com

> Formerly a Wellesley College research tool for investigating how rumors spread on Twitter — the `.com` domain is now abandoned and repurposed, so the tool is defunct.

## When to use
Do not reach for `twittertrails.com`: the domain no longer hosts the tool and now serves unrelated spam/blog content. It is retained here so an agent recognises the name and does not trust whatever currently sits at that URL. The original TwitterTrails (the "TRAILS" project at Wellesley College) was an interactive tool that, given a rumor or event, collected relevant tweets and reported the originator, burst/propagation characteristics, key propagators, and an audience-skepticism vs. spread chart to gauge a claim's credibility.

## How to use it (`bestInteractionPattern`: web-manual)
1. (Not usable at this URL.) `twittertrails.com` is parked/repurposed; do not enter queries there.
2. For the original research and methodology, see the project's academic home at `blogs.wellesley.edu/twittertrails` (archival/read-only).
3. For live rumor/propagation analysis today, use current misinformation-tracking tooling and X's own Community Notes corpus via `[[notetracker-socialmedialab-ca]]`.

## Inputs → Outputs
- **In:** (formerly) a claim/rumor, hashtag, or event; `username` of a propagator
- **Out:** (formerly) propagation graph, originator, main actors, skepticism-vs-spread credibility signal
- **Empty/negative result looks like:** the current domain returns an unrelated blog, not the tool — there is no working analysis surface.

## Gotchas & OpSec
- Status: **down / domain repurposed** — the live site is now spam-laden and unrelated; flag and move on.
- Do not cite anything currently published on twittertrails.com as if it were the research project's output.

## Overlaps ("do both")
- For living equivalents, pair X Community Notes analysis via `[[notetracker-socialmedialab-ca]]` with general tweet-archive and network-analysis tools.

## Trust & verifiability
`trust: unverified` — the credible original project no longer controls this domain; content served there today is untrusted.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | twittertrails-com |
| category | social-networks |
| selectorsIn → selectorsOut | username → social-profile |
| pricing / cost | free |
| trust | unverified |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
