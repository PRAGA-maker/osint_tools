---
id: sourcecon-com
name: sourcecon.com
description: Use when you have a GitHub username and want to recover the person's email — a how-to article on extracting emails from GitHub commit metadata.
url: https://www.sourcecon.com/how-to-find-almost-any-github-users-email-address/
category: email
path:
- email
bestFor: Learning the technique for pulling a GitHub user's email from their public commit history.
selectorsIn:
- username
- domain
selectorsOut:
- email
- name
status: live
pricing: free
costNote: Free article (technique/methodology reference, not a tool).
opsec: passive
opsecNote: Reading the article and applying the GitHub commit/patch technique is passive — you only read public GitHub data and never contact the subject.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: community
trustNote: A SourceCon (sourcing/recruiting community) how-to article describing a real, well-known GitHub email-extraction technique; it is a guide, not software.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
aliases: []
tags:
- email
- github
- technique
- Email Related Sites
source: uk-osint
lastVerified: ''
enrichment: full
---

# sourcecon.com

> A how-to article (not a tool) explaining how to recover almost any GitHub user's email from their public commits.

## When to use
You have a `username` that is (or might be) a GitHub account and want to derive the associated `email`. The article documents the technique; you apply it manually against GitHub. Useful for pivoting from a developer/technical persona to a real email identity.

## How to use it (`bestInteractionPattern`: web-manual)
1. Read the article at the URL to understand the method (emails are exposed in commit/patch metadata).
2. Apply it: open the target GitHub profile, find a repo with their commits, and view a commit as a `.patch` (append `.patch` to the commit URL) to reveal the author email; or check `events/public` API output.
3. Read the result: the commit author line contains the `email` and committer `name`.
4. Pivot: feed the recovered `email` into breach search, `[[skymem]]`, and `[[snov-io]]` verification.

## Inputs → Outputs
- **In:** `username` (GitHub handle), optionally `domain`
- **Out:** `email`, committer `name`
- **Empty/negative result looks like:** the user has no public commits, or set GitHub's "keep my email private"/noreply address — then no real email is exposed.

## Gotchas & OpSec
- Technique only works if the user committed with a real email and did not enable GitHub's email privacy (commits then show `username@users.noreply.github.com`).
- It is an article, so verify the steps still match current GitHub behavior.
- OpSec: passive; only public GitHub data is read.

## Overlaps ("do both")
- Pairs with username-correlation tools to first confirm the GitHub handle, then `[[snov-io]]` to verify the recovered address is live.

## Trust & verifiability
`trust: community` — reputable sourcing-community article describing a genuine, widely-used technique; it is guidance rather than a maintained tool.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | sourcecon-com |
| category | email |
| selectorsIn → selectorsOut | username, domain → email, name |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
