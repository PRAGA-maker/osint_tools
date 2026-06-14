---
id: snov-io-2
name: Snov.io
description: Use when you want to pull and verify emails directly from a webpage/LinkedIn profile via Snov.io's Chrome extension — returns verified emails for the people on the page.
url: https://snov.io | https://chrome.google.com/webstore/detail/email- finder/einnffiilpmgldkapbikhkeicohlaapj
category: email
path:
- email
bestFor: Extracting verified email addresses in-browser from a profile or company page while you browse.
selectorsIn:
- name
- domain
- social-profile
- employer-org
selectorsOut:
- email
- phone
status: live
pricing: freemium
costNote: Extension uses your Snov.io account credits; free tier has a small monthly allowance.
opsec: passive
opsecNote: The extension scrapes the page you are viewing and verifies via Snov.io; it does not message the subject. Activity ties to your logged-in Snov.io account, and viewing some profiles (e.g. LinkedIn) may register a profile view under whatever account you are logged into.
humanInLoop: true
humanInLoopReason:
- account-login
- api-key
bestInteractionPattern: browser-extension
trust: community
trustNote: Browser-extension front-end for the same established Snov.io email service; reliability matches the core product, with the usual professional-address coverage bias.
missingPersonsRelevance: high
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases: []
tags:
- email
source: metaosint
lastVerified: ''
enrichment: full
---

# Snov.io

> Snov.io's Chrome extension — find and verify emails for people directly from the webpage you are viewing.

## When to use
You are looking at a `social-profile` (e.g. LinkedIn), a company team page, or any site listing people connected to a missing-persons case, and want their `email` without re-typing names into the web app. Best when you are actively browsing a lead's online footprint.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the Snov.io Email Finder extension from the Chrome Web Store and sign in to your Snov.io account.
2. Browse to the target's profile or a company page.
3. Click the extension; it scrapes visible people and returns verified `email` (and sometimes `phone`) per person, charged against your credits.
4. Pivot: export found addresses into breach/username searches; a verified address confirms an identity link.

## Inputs → Outputs
- **In:** the page in view (`social-profile`, `name`, `domain`, `employer-org`)
- **Out:** `email` (verified) and occasionally `phone`
- **Empty/negative result looks like:** the extension finds no addresses for the page, or returns only unverified/invalid guesses.

## Gotchas & OpSec
- Skews to professional/corporate addresses; weak on personal accounts.
- Human-in-the-loop: requires account login and consumes credits; the extension effectively uses your account's API.
- OpSec: passive to the subject, but use a dedicated sock-puppet browser profile — viewing some platforms while logged in (e.g. LinkedIn) can leave a visible "profile view" trail.

## Overlaps ("do both")
- Same underlying service as `[[snov-io]]` (web Email Finder) — use the extension while browsing, the web app for bulk domain searches.

## Trust & verifiability
`trust: community` — extension for a well-known commercial tool; same reliability and coverage caveats as the core service.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | snov-io-2 |
| category | email |
| selectorsIn → selectorsOut | name, domain, social-profile, employer-org → email, phone |
| pricing / cost | freemium |
| trust | community |
| MP relevance | high |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | yes (account-login, api-key) |
