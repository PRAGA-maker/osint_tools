---
id: metagoofil
name: metagoofil
description: Use when you have a `domain` and want the public documents it has published plus the `metadata-exif` inside them — returns usernames, emails, software and paths harvested from those files' metadata.
url: https://github.com/opsdisk/metagoofil
category: search-engines
path:
- search-engines
bestFor: Harvesting public documents (PDF/DOC/XLS) from a target domain and extracting author/username/software metadata from them.
selectorsIn:
- domain
selectorsOut:
- username
- email
- metadata-exif
status: live
pricing: free
costNote: Free and open-source (Python CLI). No cost; you run it yourself. Google/Bing may rate-limit or CAPTCHA the automated searches it performs.
opsec: active
opsecNote: The document search phase queries a search engine (footprint on that engine, not the target). Downloading files pulls them from the target's own server, so their web logs will show your IP fetching the documents — use a VPN/proxy if you don't want the target to see the retrieval.
humanInLoop: true
humanInLoopReason:
- rate-limit
bestInteractionPattern: cli
trust: community
trustNote: Open-source tool (opsdisk Python3 rewrite of the classic metagoofil). Its output is only as good as the metadata authors left in their files, but that metadata is genuine.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- pagodo-passive-google-dork
- yagooglesearch
aliases:
- metagoofil
- opsdisk metagoofil
tags:
- metadata
- document-harvesting
- cli
- recon
source: osint4all
lastVerified: '2026-07-17'
enrichment: full
---

# metagoofil

> A document-metadata harvester: point it at a domain, and it finds that domain's public files and rips the authors, usernames, software and file paths out of their metadata.

## When to use
Your target is (or is associated with) a `domain` — a company, organisation, or personal site — and you want to mine the documents it has published. Office files and PDFs routinely embed the author's name/`username`, the `email` or account that created them, software versions, and internal file paths (which can leak usernames and network structure). metagoofil automates finding those files and extracting that `metadata-exif`, turning an org's published documents into a list of employee usernames and system details.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `git clone https://github.com/opsdisk/metagoofil && pip install -r requirements.txt` (Python 3).
2. Run against a domain, e.g. `python3 metagoofil.py -d targetdomain.com -t pdf,doc,docx,xls -l 100 -w -o output/`.
   - `-d` target domain, `-t` file types, `-l` search limit, `-w` download the files, `-o` output dir.
3. Let it search (Google/Bing) for indexed files on that domain, download them, and extract metadata.
4. Read the harvested metadata: author names, usernames, creating software, and embedded paths.
5. Pivot: harvested `username`s/`email`s feed username-search, breach-lookup and email tools; software/path leaks feed the technical side of an engagement.

## Inputs → Outputs
- **In:** `domain` (target to harvest documents from)
- **Out:** `username`, `email`, and `metadata-exif` (author, software, paths) extracted from the domain's public files
- **Empty/negative result looks like:** few/no files found, or files with metadata stripped — many orgs sanitise documents, so a clean result means "no leaked metadata found," not "no documents exist."

## Gotchas & OpSec
- Search engines rate-limit and CAPTCHA automated queries; you may need to throttle, add delays, or rerun — hence human-in-the-loop.
- OpSec: **active** on the download phase — fetching the files hits the target's web server and appears in their logs. Use a VPN/proxy if attribution matters. The search phase leaks to Google/Bing, not the target.
- Metadata quality is entirely dependent on what authors left in; sanitised files yield nothing.

## Overlaps ("do both")
- Pairs with `[[pagodo-passive-google-dork]]` and `[[yagooglesearch]]` — those dork for the documents/pages more flexibly; metagoofil specialises in downloading them and extracting embedded metadata. Use dorking to find files, metagoofil to strip them.

## Trust & verifiability
`trust: community` — a maintained open-source tool. The metadata it extracts is genuine (straight from the files), but its usefulness depends on authors not having sanitised their documents; verify extracted names/usernames against other sources before relying on them.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | metagoofil |
| category | search-engines |
| selectorsIn → selectorsOut | domain → username, email, metadata-exif |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (rate-limit) |
