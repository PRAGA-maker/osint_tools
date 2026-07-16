---
id: company-or-organisation
name: Facebook "works at" Google dork
description: Use when you have an `employer-org` (or a person `name`) and want to find Facebook profiles that list working there — returns social-profile and associate leads via a Google site-search dork.
url: https://www.google.com/search?client=firefox-b-d&q=site%3Afacebook.com+%22works+at%22+%22Search+Term%22+
category: social-networks
path:
- social-networks
bestFor: Enumerating Facebook profiles tied to a company or organisation via a Google dork.
selectorsIn:
- employer-org
- name
selectorsOut:
- social-profile
- name
- associate
status: live
pricing: free
costNote: Uses Google's free web search; no account or payment needed.
opsec: passive
opsecNote: You query Google, never Facebook or the target, so nobody is alerted. Heavy dorking from one IP can trigger a Google CAPTCHA; space queries out or use a sock-puppet browser. Any profile you then open on Facebook is a separate, active step.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A community OSINT technique (a Google site: dork), not a hosted product; effectiveness depends on what Facebook has left publicly indexable.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools: []
aliases:
- Facebook works-at dork
- site:facebook.com works at
tags:
- facebook
- google-dork
source: uk-osint
lastVerified: '2026-07-16'
enrichment: full
---

# Facebook "works at" Google dork

> A prebuilt Google site-search that surfaces public Facebook profiles listing a given employer, turning a company name into a list of associated people.

## When to use
You have an `employer-org` (a company/organisation) or a person `name` and want to find the Facebook profiles connected to it — colleagues, a specific employee, or the subject's own profile where they've listed their workplace. This dork leans on Google's index of public Facebook pages, so it reaches profiles that Facebook's own search buries.

## How to use it (`bestInteractionPattern`: web-manual)
1. In Google, run `site:facebook.com "works at" "COMPANY NAME"` (replace COMPANY NAME; the stub URL is a template — swap the `Search Term` token).
2. To target a person, add their `name` in quotes: `site:facebook.com "works at" "ACME Corp" "Jane Doe"`.
3. Read the results: each hit is a public Facebook profile/snippet mentioning the employer — note the profile URLs (`social-profile`) and names.
4. Pivot: open promising profiles (from a sock-puppet), and treat co-listed colleagues as `associate` leads. Vary the phrasing (`"worked at"`, `"CEO at"`, job titles) to widen coverage.

## Inputs → Outputs
- **In:** `employer-org` (company name), optionally a person `name`
- **Out:** `social-profile` (Facebook profile URLs), `name`, `associate` (co-workers)
- **Empty/negative result looks like:** zero or irrelevant hits — means Facebook hasn't left matching text publicly indexed, or the employer string doesn't match how people wrote it; retry with synonyms and quotes.

## Gotchas & OpSec
- This surfaces only what Google has indexed from public Facebook pages; privacy-locked profiles won't appear.
- Exact-match quoting matters — try the trade name, abbreviations, and alternate verbs.
- OpSec: passive (you query Google); repeated dorking may trigger a Google CAPTCHA. Opening the profiles on Facebook is the active follow-up — use a sock-puppet account.

## Overlaps ("do both")
- Pairs with `[[facebook-directory-users-by-name]]` and `[[facebook-email-reverse-lookup]]` — the dork finds people by employer, those pivot a found name/email into the specific profile.

## Trust & verifiability
`trust: community` — a well-known dorking technique, not a maintained service; its yield rises and falls with Google's index and Facebook's public-visibility settings, so absence of results is never proof of absence.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | company-or-organisation |
| category | social-networks |
| selectorsIn → selectorsOut | employer-org, name → social-profile, name, associate |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
