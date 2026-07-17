---
id: wayback-google-analytics
name: Wayback Google Analytics
description: Use when you have a `domain` and want to link it to other sites via shared current/historical Google Analytics or AdSense IDs — returns related `domain`s.
url: https://github.com/bellingcat/wayback-google-analytics
category: archives-cache
path:
- archives-cache
bestFor: Uncovering ownership links between websites that share the same Google Analytics/GTM/AdSense identifier, including retired IDs recovered from the Wayback Machine.
selectorsIn:
- domain
selectorsOut:
- domain
status: live
pricing: free
costNote: Free and open source (MIT). Uses the public Wayback Machine and each site's own HTML; no API key or payment.
opsec: passive
opsecNote: Historical IDs are pulled from the Internet Archive (no contact with the target). Fetching the CURRENT ID hits the live target site directly — a normal page load, but route it through a sock-puppet IP/VPN if the operator watches their own logs.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: cli
trust: trusted
trustNote: Published and maintained by Bellingcat, a well-known investigative-journalism collective; open source and auditable.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- auto-archiver
- bellingcat-tiktok-hashtag-analysis
- instagram-location-search
- shadow-finder
- telegram-phone-number-checker-github-com
aliases:
- wayback-google-analytics
- bellingcat GA finder
tags:
- Archives
- Tools for working with web archives
source: cyb-detective
lastVerified: '2026-07-17'
enrichment: full
---

# Wayback Google Analytics

> Bellingcat's CLI that harvests current and long-deleted Google Analytics/GTM/AdSense codes from a site and its Wayback snapshots, so you can find every other site that shares them.

## When to use
You have a `domain` (a scam site, a burner blog, a suspect's personal page, a shell-company storefront) and want to know what else the same operator runs. Websites managed by one person often reuse a single Google Analytics (`UA-`/`G-`), Tag Manager (`GTM-`), or AdSense (`pub-`) account, so a shared ID is strong evidence of common ownership. Recovering *retired* IDs from the archive catches links the live page no longer exposes.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `pip install wayback-google-analytics` (Python 3.10+).
2. Run against one or more targets:
   `wayback-google-analytics -u https://targetsite.com https://othersite.com -o xlsx`
   - `-u` accepts URLs directly or `-f urls.txt` for a file list.
   - Optional `-s`/`-e` start/end dates and `-f yearly|monthly|daily` control which snapshots are sampled.
3. Read the output (JSON/CSV/TXT/XLSX). Spreadsheet output builds two indexes: one keyed by website, one keyed by analytics code — scan the code-keyed sheet for any ID appearing under more than one domain.
4. Pivot: an ID shared with an unknown domain is a new lead — run that domain through WHOIS/`[[auto-archiver]]` and repeat.

## Inputs → Outputs
- **In:** `domain` (one or many URLs)
- **Out:** `domain` (other sites sharing a Google Analytics/GTM/AdSense ID), plus the raw ID list and the snapshot dates each was seen.
- **Empty/negative result looks like:** a site with no analytics tags, or a unique ID that appears on only that one domain — no linkage to assert. Absence of a shared ID is not proof of no relationship.

## Gotchas & OpSec
- Human-in-the-loop: the Wayback Machine rate-limits; the authors advise ≤10 URLs and <500 snapshots per run to avoid HTTP 443/429 errors. Batch large jobs.
- A shared modern `G-` ID is strong; a shared legacy `UA-` ID can occasionally be a coincidence of a shared web-design agency — corroborate before asserting single ownership.
- OpSec: reading the live current ID loads the target's page; use a clean IP if the operator monitors visitors.

## Overlaps ("do both")
- Pairs with `[[auto-archiver]]` — archive the evidence pages first, then mine them (and the existing archive) for shared IDs so your linkage is preserved even if the sites vanish.

## Trust & verifiability
`trust: trusted` — a Bellingcat open-source project; the technique (analytics-ID pivoting) is well documented and the output is verifiable against the raw page/archive HTML.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wayback-google-analytics |
| category | archives-cache |
| selectorsIn → selectorsOut | domain → domain |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | cli |
| opsec | passive |
| human-in-loop | yes (rate-limit) |
