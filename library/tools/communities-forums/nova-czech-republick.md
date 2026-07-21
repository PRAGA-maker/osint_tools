---
id: nova-czech-republick
name: Nova (Czech Republic)
description: Use when you have a `name` tied to the Czech Republic and want to check a mainstream Czech news/TV outlet for coverage — returns Czech-language news mentions and `associate` context.
url: http://tn.nova.cz
category: communities-forums
path:
- communities-forums
bestFor: Searching TV Nova's Czech news portal for coverage of a Czech-linked person, incident or location.
selectorsIn:
- name
selectorsOut:
- name
- associate
- geolocation
status: live
pricing: free
costNote: Free ad-supported Czech news portal; no account needed to read or search.
opsec: passive
opsecNote: You are reading a public national news site; the subject is not notified. The site may bot-block or geo-throttle (a 403 on automated fetch is common) — browse manually, ideally from a Czech-locale/VPN session if blocked.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: tn.nova.cz is the news portal of TV Nova, a major established Czech broadcaster — genuine journalism, though commercial and headline-driven.
missingPersonsRelevance: low
coverage:
- cz
auth: none
api: false
localInstall: false
registration: false
aliases:
- tn.nova.cz
- TV Nova news
tags:
- toddington
- curated-directory
- news-journalism
- czech-republic
source: toddington-resources
lastVerified: '2026-07-21'
enrichment: full
---

# Nova (Czech Republic)

> The online news portal of TV Nova, one of the Czech Republic's largest broadcasters — a mainstream Czech-language source to canvass for coverage of a subject.

## When to use
Your subject has a Czech nexus — nationality, residence, an incident in the Czech Republic — and you want to see whether a major national outlet has covered them or a related event. Czech names, places and stories are far better indexed in Czech-language outlets than in Western search engines, so a national source like Nova can surface coverage global tools miss.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open http://tn.nova.cz in a browser (if you hit a 403/bot wall, retry manually, ideally from a Czech-locale or VPN session).
2. Use the site's search box with the subject's `name` (try Czech diacritics and the ASCII-folded form, e.g. Novák / Novak).
3. Read returned articles for named coverage — incidents, court cases, local events.
4. Note co-mentioned people (`associate`) and places (`geolocation`) in the story.
5. Pivot: a dated news mention gives you a location, timeframe, or relatives to chase in Czech public records and social tools.

## Inputs → Outputs
- **In:** `name` (Czech spelling and romanized variants)
- **Out:** Czech-language news coverage, co-mentioned `associate`s, incident `geolocation`
- **Empty/negative result looks like:** the site search returns no articles — meaning Nova hasn't covered the subject, not that no Czech coverage exists (check other Czech outlets and archives).

## Gotchas & OpSec
- Language: content and search are Czech; use a translator on results and search with proper diacritics for best recall.
- It is one outlet, and a commercial/tabloid-leaning one — corroborate any claim against another source before relying on it.
- Automated fetches often 403; treat this as a manual-browse tool.
- OpSec: passive.

## Overlaps ("do both")
- Pairs with other Czech national outlets and news-archive search — Nova is a single broadcaster's portal; cross-outlet search catches stories it didn't run.

## Trust & verifiability
`trust: trusted` — it is the genuine portal of a major Czech broadcaster (TV Nova), so it is real journalism; still, as a commercial outlet, verify specific factual claims against a second source.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | nova-czech-republick |
| category | communities-forums |
| selectorsIn → selectorsOut | name → name, associate, geolocation |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
