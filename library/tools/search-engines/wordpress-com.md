---
id: wordpress-com
name: WordPress.com
description: Use when you have a `name` or `username` and want to find blogs and posts they authored on WordPress.com — returns social-profile, username and domain.
url: https://en.search.wordpress.com/
category: search-engines
path:
- search-engines
bestFor: Keyword/name search across WordPress.com-hosted blogs and their posts.
selectorsIn:
- name
- username
selectorsOut:
- social-profile
- username
- domain
status: live
pricing: freemium
costNote: Free to search. Reader-based search may prompt for a free WordPress.com account; the classic public search endpoint and Google `site:wordpress.com` need no login.
opsec: passive
opsecNote: Searching is read-only against WordPress.com's public content; it does not notify the blog owner. If you sign into a WordPress.com account to use Reader, that ties the session to your identity — use a sock-puppet account.
humanInLoop: true
humanInLoopReason:
- account-login
bestInteractionPattern: web-manual
trust: trusted
trustNote: Operated by Automattic (WordPress.com); results are first-party blog content, not a third-party scraper.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- wordpress
- linkedinsider-deutschland-blog-von-stephan-ko
aliases:
- WordPress.com blog search
- en.search.wordpress.com
tags:
- blogs
- specialty-search
source: osint4all
lastVerified: '2026-07-18'
enrichment: full
---

# WordPress.com

> Keyword search across the millions of blogs hosted on WordPress.com — a way to surface a subject's personal blog and the posts they wrote.

## When to use
You have a `name`, `username`, or a distinctive phrase and want to know whether the subject keeps (or kept) a blog on WordPress.com. Personal blogs often leak biographical detail — location, employer, family, hobbies, and links to other profiles — that never appears on locked-down social media. A hit returns the blog's `domain` (e.g. `subject.wordpress.com`), the author `username`, and the post as a pivotable `social-profile`.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://en.search.wordpress.com/ in a clean/sock-puppet browser session.
2. Enter the subject's `name`, handle, or a unique phrase they use and submit.
3. Read the results — post titles and blog names matching the term. Click through to read the post and note the blog subdomain and author.
4. If the site redirects you into the WordPress.com Reader and demands a login, either sign in with a throwaway account or fall back to a search engine: `site:wordpress.com "Jane Doe"`.
5. Pivot: the blog subdomain is a `domain` for infrastructure lookups; the "About" page and blogroll feed `name`/`associate`; embedded images feed `[[wordpress]]` and EXIF tooling.

## Inputs → Outputs
- **In:** `name` or `username` (or a distinctive keyword)
- **Out:** `social-profile` (the post/blog), `username` (author), `domain` (blog subdomain)
- **Empty/negative result looks like:** no matching posts, or only generic unrelated blogs — meaning the subject either has no WordPress.com blog or uses a self-hosted WordPress install (try `[[wordpress]]`-style fingerprinting on their own domain instead).

## Gotchas & OpSec
- Human-in-the-loop: the modern search flow can bounce you into the Reader, which is login-gated — use a sock-puppet WordPress.com account or a `site:` engine query.
- This only covers blogs hosted **on** WordPress.com. Self-hosted sites that merely run the WordPress software are not indexed here.
- OpSec: passive read; safe. Just don't comment or follow from a real account.

## Overlaps ("do both")
- Pairs with `[[wordpress]]` — that fingerprints self-hosted WordPress sites and enumerates users, while this searches the WordPress.com hosted network for authored content.

## Trust & verifiability
`trust: trusted` — it is Automattic's first-party search over their own hosting platform, so the blog attribution is authoritative.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wordpress-com |
| category | search-engines |
| selectorsIn → selectorsOut | name, username → social-profile, username, domain |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | yes (account-login) |
