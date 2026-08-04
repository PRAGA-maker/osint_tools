---
id: owasp-d4n155
name: OWASP D4N155
description: Use when you have a subject's `domain` or website and want to build a target-specific password/wordlist from its own content — returns a ranked wordlist of terms, names and phrases for credential-guessing or keyword pivots.
url: https://github.com/OWASP/D4N155
category: ai-analysis-automation
path:
- ai-analysis-automation
- wordlist
bestFor: Generating an intelligent, content-derived wordlist from a target website for password auditing or keyword extraction.
selectorsIn:
- domain
selectorsOut:
- password
- name
status: live
pricing: free
costNote: Free and open-source (GPL-3.0).
opsec: active
opsecNote: This is active reconnaissance — it crawls the target website (aggressive mode drives a headless browser), so the target's server logs your crawler's IP and user-agent. Only run it against sites you are authorised to audit, from a controlled IP; wordlists it produces are for legitimate password auditing, not unauthorised access.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: trusted
trustNote: An OWASP-hosted project; open-source and community-reviewed under the OWASP umbrella.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- owasp-amass
aliases:
- d4n155
tags:
- wordlist
- password-audit
- owasp
source: arf-seed
lastVerified: '2026-08-04'
enrichment: full
---

# OWASP D4N155

> An OWASP audit tool that reads a target website and builds a smart, weighted wordlist from its actual content — the words the target is most likely to have used in passwords.

## When to use
You have a subject's or organisation's `domain`/website and, for an authorised security audit, need a bespoke wordlist grounded in that site's vocabulary (names, product terms, local phrases) rather than a generic dictionary. Secondarily useful as a keyword-extraction pass over a target's web presence.

## How to use it (`bestInteractionPattern`: cli)
1. Requirements: Python 3.6+, Bash and Go. `git clone https://github.com/OWASP/D4N155 && cd D4N155 && pip3 install -r requirements.txt`.
2. Point it at a target and generate a wordlist: `bash main -w -t targets.txt -o output.txt` (targets can be domains, URLs, IPs or raw text files).
3. Tune crawl depth/aggressiveness via the documented options; aggressive mode uses a headless browser for JS-heavy sites.
4. Review the ranked `output.txt` — terms are weighted by frequency/relevance across the crawled content.
5. Feed the wordlist into an authorised password-audit workflow, or mine it for `name`/keyword pivots.

## Inputs → Outputs
- **In:** `domain`, URL, IP, or a text corpus for the target.
- **Out:** a ranked wordlist (`password` candidates) plus surfaced `name`s/keywords drawn from the site's content.
- **Empty/negative result looks like:** a tiny or empty wordlist — a thin/JS-only site not crawled properly (try aggressive mode) or a blocked crawler.

## Gotchas & OpSec
- **Active & authorisation-gated:** crawling a target you don't own may be unlawful — only run against sanctioned engagements.
- Requires a Go + Bash + Python toolchain; the README notes an occasional Google-crawler bug.
- Output quality tracks the site's text richness; a brochure site yields a weak list.

## Overlaps ("do both")
- Pairs with mapping/recon of the same target — e.g. `[[owasp-amass]]` enumerates the attack surface while D4N155 mines the content of the sites it finds.

## Trust & verifiability
`trust: trusted` — an OWASP project, so it's community-governed and open to review; note it's an offensive-audit tool, so use is bounded by authorisation rather than data-quality concerns.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | owasp-d4n155 |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | domain → password, name |
| pricing / cost | free |
| trust | trusted |
| MP relevance | low |
| interaction | cli |
| opsec | active |
| human-in-loop | no |
