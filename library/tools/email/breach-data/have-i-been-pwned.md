---
id: have-i-been-pwned
name: Have I been pwned?
description: Use when you have an email and want an authoritative list of which data breaches exposed it.
url: https://haveibeenpwned.com/
category: email
path:
- email
- breach-data
bestFor: Confirming whether an email appears in known breaches and which datasets exposed it.
selectorsIn:
- email
selectorsOut:
- email
- metadata-exif
status: live
pricing: freemium
costNote: Web lookup of an email is free. The API (needed for bulk/programmatic queries) requires a paid key; "Pwned Passwords" k-anonymity API is free.
opsec: passive
opsecNote: Queries a breach index; the target is never notified. Web search of your own/target's email is anonymous to the target.
humanInLoop: true
humanInLoopReason:
- api-key
bestInteractionPattern: web-manual
trust: trusted
trustNote: Run by Troy Hunt; the de-facto standard breach-notification service, used by browsers, governments, and 1Password.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
invitationOnly: false
deprecated: false
relatedTools:
- h8mail
- holehe
- hudson-rock
aliases:
- HIBP
tags: []
source: arf-seed
lastVerified: ''
enrichment: full
---

# Have I been pwned?

> The authoritative breach index: tells you which known data breaches an email (or phone) appears in, and what data classes were exposed.

## When to use
You have an `email` (or `phone`) for a missing person or associate and want to know which breaches exposed it. The breach list itself is a lead generator — a breach name reveals which services the person used (a forum, a dating site, a gaming platform), which is a pivot to other tools.

## How to use it (`bestInteractionPattern`: web-manual)
1. Go to https://haveibeenpwned.com/.
2. Enter the `email` in the search box and submit.
3. Read the breach list: each entry gives the breached service, date, and exposed data classes (passwords, names, DOBs, IPs, etc.).
4. For bulk or automated checks, register a paid API key and call the `breachedaccount` endpoint.
5. Pivot: every breached service name is a candidate account to look for via username/email enumeration tools.

## Inputs → Outputs
- **In:** `email` (also supports `phone` via the search)
- **Out:** list of breach names + dates + exposed data classes (`metadata-exif`-style attributes: passwords, IPs, DOB, etc.)
- **Empty/negative result looks like:** "Good news — no pwnage found!"; the email isn't in any indexed breach (does not prove the person has no accounts).

## Gotchas & OpSec
- Human-in-the-loop: free web lookup is one-at-a-time; bulk/programmatic needs a paid **API key**.
- HIBP shows *which* breaches and *what classes* leaked — it does NOT return plaintext passwords (use `[[h8mail]]` / leak-search tools for contents, within legal bounds).
- OpSec: fully passive; the target is never alerted.

## Overlaps ("do both")
- Pairs with `[[holehe]]` (which services an email is registered on, breach or not) and `[[h8mail]]` / `[[hudson-rock]]` (credential contents and infostealer hits).

## Trust & verifiability
`trust: trusted` — long-running, transparently operated by Troy Hunt; widely integrated by major vendors and a standard OSINT reference.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | have-i-been-pwned |
| category | email |
| selectorsIn → selectorsOut | email → email, metadata-exif |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (api-key) |
