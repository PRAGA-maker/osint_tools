---
id: baike-baidu-chinese-language
name: Baike Baidu (Chinese language)
description: Use when you have a Chinese name, company, or place and want the Chinese-language encyclopedia entry — returns biographical detail, associates, and employer-org from Baidu's crowd encyclopedia.
url: http://baike.baidu.com
category: search-engines
path:
- search-engines
bestFor: Reading Baidu's Chinese-language crowdsourced encyclopedia for people, companies, places, and events under-covered by English Wikipedia.
selectorsIn:
- name
- employer-org
selectorsOut:
- employer-org
- associate
- dob
status: live
pricing: free
costNote: Free to read; no account needed to view entries.
opsec: passive
opsecNote: Passive reading of a public Chinese encyclopedia, but it is Baidu (PRC jurisdiction) — assume queries and IPs are logged. Use a sock-puppet browser for China-sensitive subjects; do not log in.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Baidu's crowd-edited encyclopedia; entries can be authoritative for mainstream Chinese topics but are user-edited and subject to PRC censorship, so verify claims.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools:
- baidu
- baidu-china
- baidu-com
- baidu-image-search
- baidu-image-search-2
- baidu-images
- baidu-maps
- baidu-translate
- baiduknows-search-engine-china
aliases:
- 百度百科
- Baidu Baike
- baike.baidu.com
tags:
- search-engines
- china
- encyclopedia
- chinese-language
source: toddington-resources
lastVerified: '2026-07-18'
enrichment: full
---

# Baike Baidu (Chinese language)

> Baidu Baike (百度百科) — China's dominant crowdsourced encyclopedia, the Chinese-web equivalent of Wikipedia and often the richest single entry on a Chinese person, company, or place.

## When to use
Your subject is a notable Chinese person, business, institution, or place, and English sources are thin. Given a Hanzi/Pinyin `name` or `employer-org`, Baidu Baike frequently has a structured entry with biography, birth date (`dob`), education and career (`employer-org`), family and collaborators (`associate`), and links to related entries — a fast way to build a profile from the Chinese-language record.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to http://baike.baidu.com and search the subject in Hanzi where possible (far more precise than Pinyin).
2. Open the entry; read the infobox and body for birth date/place, education, positions held, affiliated organizations, and named associates.
3. Follow internal links to related people/companies to expand the network, and note the cited references.
4. Pivot: translate with `[[baidu-translate]]`, corroborate on `[[baidu]]` web search and independent sources, and treat the entry as a lead map rather than proof.

## Inputs → Outputs
- **In:** `name` (Hanzi/Pinyin) or `employer-org`
- **Out:** `employer-org` (career/affiliations), `associate` (family, colleagues, linked entities), `dob` (birth date where listed)
- **Empty/negative result looks like:** no entry, or a thin stub — Baike skews toward notable/public figures and companies, so ordinary private individuals usually have nothing.

## Gotchas & OpSec
- Human-in-the-loop: none to read.
- OpSec: passive but PRC-jurisdiction — assume logging; use a sock puppet for sensitive China topics and never log in.
- Reliability: entries are user-edited and censored on sensitive topics; verify dates, roles, and relationships against independent sources before relying on them.

## Overlaps ("do both")
- Pairs with its Baidu siblings — `[[baidu]]` (web), `[[baidu-image-search]]`, `[[baidu-translate]]` — and with English Wikipedia; Baike gives the Chinese-language profile, the others verify and enrich it.

## Trust & verifiability
`trust: community` — it is a genuine, widely-used encyclopedia, but crowd-edited and subject to censorship; corroborate specific facts at their cited sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | baike-baidu-chinese-language |
| category | search-engines |
| selectorsIn → selectorsOut | name, employer-org → employer-org, associate, dob |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
