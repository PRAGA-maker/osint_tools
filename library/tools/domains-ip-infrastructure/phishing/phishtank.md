---
id: phishtank
name: PhishTank
description: Use when you have a `domain`/URL and want to know whether it's a known, community-verified phishing site — returns phishing status and verification detail.
url: https://www.phishtank.com/
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
- phishing
bestFor: Checking whether a URL/domain is a known, community-verified phishing site.
selectorsIn:
- domain
selectorsOut: []
status: live
pricing: free
costNote: Free; a free API key (registration) is available for automated/bulk lookups.
opsec: passive
opsecNote: A lookup queries PhishTank's database, not the phishing site itself, so it's passive. Never open the live phishing URL from your real environment — verify via the database and, if you must view it, use an isolated sandbox.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: Operated by Cisco (formerly OpenDNS); entries are community-submitted and confirmed by verification votes, so reliable in aggregate but only as fresh as recent submissions.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- PhishTank
tags:
- phishing
- url-reputation
- threat-intel
source: arf-seed
lastVerified: '2026-07-28'
enrichment: full
---

# PhishTank

> A community-verified database of phishing URLs — look up whether a suspicious link is a confirmed phish without touching it.

## When to use
You have a `domain` or full URL — from a message, a lure, or a scam tied to your investigation — and want to know if it's a known phishing site and, if so, what brand it impersonates. Useful for triaging suspicious links and for corroborating that a domain is malicious infrastructure rather than a subject's legitimate site.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://www.phishtank.com/ and search the suspect URL/`domain`.
2. Read the entry: whether it's **verified phishing**, the target brand, submission and verification timestamps, and community votes.
3. For automation, register a free API key and query the API (or download the hourly database dump) for bulk checks.
4. Pivot: a confirmed phishing domain feeds WHOIS/passive-DNS/hosting lookups to map who stood it up; the impersonated brand tells you the campaign's target.

## Inputs → Outputs
- **In:** `domain` / URL
- **Out:** phishing status (verified / unverified / not in database), impersonated brand, submission & verification metadata
- **Empty/negative result looks like:** "not in the database" — PhishTank only knows what's been submitted, so absence is NOT proof the URL is safe; check other reputation sources too.

## Gotchas & OpSec
- Coverage is submission-driven — brand-new or low-volume phishing may not be listed yet.
- Do not browse the live phishing URL from your real machine; PhishTank exists precisely so you don't have to.
- OpSec: passive database lookup; nothing reaches the phishing host.

## Overlaps ("do both")
- Pair with other URL-reputation feeds (e.g. Google Safe Browsing, URLhaus) — each has different coverage, so a URL missing from one may be flagged by another.

## Trust & verifiability
`trust: community` — Cisco-operated but community-sourced; a "verified" entry has passed community voting, which is reliable, while "unverified"/absent entries need corroboration.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | phishtank |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain →  |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
