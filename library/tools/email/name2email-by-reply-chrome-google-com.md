---
id: name2email-by-reply-chrome-google-com
name: name2email by reply (chrome.google.com)
description: Use when composing in Gmail and you have a person's name plus their company domain — the extension suggests their likely email address inline so you can pick the right format.
url: https://chrome.google.com/webstore/detail/name2email-by-reply/mnbdclgaeiapdnhfpbfalfjfcjddfaii?hl=en
category: email
path:
- email
bestFor: In-Gmail email-address guessing from a name and a domain.
selectorsIn:
- name
- domain
selectorsOut:
- email
status: unknown
pricing: free
costNote: Free Chrome extension by Reply (reply.io); availability on the Web Store may change.
opsec: passive
opsecNote: Generating a candidate address is passive. But it runs inside Gmail and is published by a sales-engagement vendor (Reply.io), so assume it can see your compose context — use a sock-puppet Google account, not your real one.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: browser-extension
trust: unverified
trustNote: Chrome extension by Reply.io that suggests likely email formats in Gmail. Listed by uk-osint under "Email - Covert IP Trackers," which appears mis-categorized — its actual function is email-address guessing, not IP tracking. Vendor data handling not verified.
missingPersonsRelevance: medium
coverage: []
auth: account
api: false
localInstall: true
registration: false
relatedTools:
- metric-sparrow-email-permulator
- mailtester
aliases:
- name2email
tags:
- emailtrackers
- Email - Covert IP Trackers
source: uk-osint
lastVerified: ''
enrichment: full
---

# name2email by reply (chrome.google.com)

> A Gmail Chrome extension by Reply.io that suggests a person's likely email address as you type their name — an in-compose email guesser, not an IP tracker.

## When to use
You are working inside Gmail (sock-puppet account) and have a subject's `name` plus a probable company `domain`. As you compose, the extension proposes the most likely address format, saving a separate permutation step. Use it to get a single best-guess `email` to then verify.

## How to use it (`bestInteractionPattern`: browser-extension)
1. Install the extension from the Chrome Web Store into a sock-puppet Chrome profile.
2. In Gmail, start a new message and type the person's name into the To field; the extension surfaces a suggested address (and/or you append the domain).
3. Capture the suggested `email`.
4. Pivot: verify it with `[[mailtester]]` before relying on it; for a full permutation list use `[[metric-sparrow-email-permulator]]`.

## Inputs → Outputs
- **In:** `name`, `domain`
- **Out:** `email` (a single best-guess address; not contact data lookup)
- **Empty/negative result looks like:** no suggestion or an obviously wrong format — fall back to a permutation generator + verifier.

## Gotchas & OpSec
- Despite the uk-osint "Covert IP Trackers" tag, it does NOT track IPs; it guesses address formats. Don't expect tracking output.
- It's vendor (Reply.io) software running in your mailbox — keep it off any real/personal Google account.
- A suggested address is a guess; always verify deliverability before acting.

## Trust & verifiability
`trust: unverified` — third-party sales-tool extension; function inferred from the name and Reply.io's known "name2email" feature, with the source list's category appearing wrong. Not independently tested; data handling unknown.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | name2email-by-reply-chrome-google-com |
| category | email |
| selectorsIn → selectorsOut | name, domain → email |
| pricing / cost | free |
| trust | unverified |
| MP relevance | medium |
| interaction | browser-extension |
| opsec | passive |
| human-in-loop | yes |
