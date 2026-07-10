---
id: commit-stream
name: commit-stream
description: Use when you have a GitHub `username` or org and want the real name and email behind commits — returns committer names and emails harvested from the live GitHub event stream.
url: https://github.com/x1sec/commit-stream
category: username
path:
- username
bestFor: Extracting the real name and email tied to a GitHub account/organisation by reading commit author metadata from GitHub's public event firehose.
selectorsIn:
- username
- employer-org
selectorsOut:
- name
- email
status: live
pricing: free
costNote: Free and open-source (Go). A GitHub API token raises rate limits; the public event stream is otherwise free.
opsec: passive
opsecNote: You read GitHub's public events/commit metadata, not the target's account directly, so the user is not notified. The name/email are self-published in commits. Use a dedicated GitHub token, not your primary account, if you supply one.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A known open-source tool (x1sec); it simply surfaces the author name/email that developers themselves put in their commits — reliable data, but a global @users.noreply.github.com address means the user hid their email.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
relatedTools:
- keybase
aliases:
- x1sec/commit-stream
tags:
- github
- commits
- email-harvest
source: osintambition-social
lastVerified: '2026-07-10'
enrichment: full
---

# commit-stream

> A Go CLI that taps GitHub's public commit event stream to pull the **real name and email** developers embed in their commits — a fast route from a GitHub identity to a personal email.

## When to use
You have a GitHub `username` or an organisation and want the name/email behind the account. Git commits carry an `author name <email>` that developers often set to their real name and personal or work email — data not shown on the GitHub profile page. commit-stream harvests this from the live events firehose (or you can target a specific org/user), turning a code identity into a contactable email and real name.

## How to use it (`bestInteractionPattern`: cli)
1. Build/install from https://github.com/x1sec/commit-stream (Go).
2. Run it against the live stream, or filter by `-user <username>` / `-org <employer-org>` to focus on a target.
3. Optionally supply a GitHub token (`-t`) to raise rate limits — use a burner token, not your main account.
4. Read the output: committer `name` and `email` pairs tied to the account/org.
5. Pivot: a harvested `email` feeds email-OSINT and breach checks; the `name` feeds people-search; cross-check the identity via `[[keybase]]`.

## Inputs → Outputs
- **In:** `username` (GitHub account) or `employer-org` (GitHub org)
- **Out:** committer `name` and `email` addresses
- **Empty/negative result looks like:** only `<id>+<user>@users.noreply.github.com` addresses, or no commits during the capture window — meaning the user enabled email privacy or wasn't active; you get no personal email.

## Gotchas & OpSec
- Only works if the developer left a real email in their commits — privacy-enabled users show a GitHub noreply address.
- Live-stream capture is time-bounded; targeting a specific org/user is more reliable than waiting for them to appear.
- OpSec: passive (public commit metadata); use a burner API token if you add one.

## Overlaps ("do both")
- Pairs with `[[keybase]]` — commit-stream gives name/email from commits; Keybase can cryptographically confirm the same person's other accounts. Do both to corroborate a technical subject's identity.

## Trust & verifiability
`trust: community` — an open tool surfacing self-published commit metadata, so the data is authentic; just remember a noreply address means the email is hidden, and verify a harvested email is current before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | commit-stream |
| category | username |
| selectorsIn → selectorsOut | username, employer-org → name, email |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
</content>
