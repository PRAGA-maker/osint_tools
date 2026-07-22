---
id: wordpress
name: WordPress
description: Use when you have a `domain` or `username` and want to enumerate a WordPress site's authors — returns usernames, display names and linked social-profiles.
url: https://wordpress.com
category: domains-ip-infrastructure
path:
- domains-ip-infrastructure
bestFor: Enumerating author usernames/display names behind a WordPress site (or finding a subject's WordPress.com blog).
selectorsIn:
- domain
- username
selectorsOut:
- username
- name
- social-profile
status: live
pricing: free
costNote: WordPress.com blogs are free to read; the REST-API author-enumeration technique works on any WordPress install (self-hosted or .com) with no account or payment.
opsec: passive
opsecNote: Reading a public blog and its REST API is ordinary web traffic to the target's own server — the site owner could see your IP in their logs. Use a VPN/sock-puppet IP. Do not log in or comment, which would tie an identity to the visit.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: WordPress is the dominant CMS (Automattic / open-source); the author-enumeration behaviour is a well-documented property of the WordPress REST API, not a third-party claim.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: true
localInstall: false
registration: false
relatedTools:
- linkedinsider-deutschland-blog-von-stephan-ko
- wordpress-com
aliases:
- WordPress.com
- WordPress REST API author enumeration
tags:
- cms
- author-enumeration
- domains-ip-infrastructure
source: toddington-resources
lastVerified: '2026-07-22'
enrichment: full
---

# WordPress

> The web's most common CMS — and its default REST API happily lists a site's author usernames and display names, turning any WordPress blog into a small identity leak.

## When to use
You have a `domain` that runs WordPress (very common for personal blogs, small businesses, activists, portfolios) and want to know who writes for it, or you have a `username` you suspect maps to a WordPress.com blog. WordPress exposes registered authors through predictable URLs, so you can often recover the login `username`, the public display `name`, and links to profiles the author added — useful for connecting a site back to a real person.

## How to use it (`bestInteractionPattern`: web-manual)
1. Confirm the target `domain` runs WordPress (page source references `/wp-content/`, `/wp-includes/`, or a `generator` meta tag).
2. Query the REST API: `https://<domain>/wp-json/wp/v2/users` — this returns a JSON list of authors with `slug` (often the login username), display `name`, and `description`/URL fields.
3. If the REST endpoint is blocked, try the legacy redirect trick: `https://<domain>/?author=1`, `?author=2`, … — each often 301-redirects to `/author/<username>/`, leaking the username.
4. For WordPress.com specifically, check `https://<username>.wordpress.com` and the reader/profile at `https://wordpress.com/read` for the subject's blog.
5. Pivot: run recovered usernames through cross-platform username tools; follow any author bio links to other `social-profile`s.

## Inputs → Outputs
- **In:** `domain` (a WordPress site) or `username` (a suspected WordPress.com handle)
- **Out:** author `username`(s)/slugs, display `name`(s), bio links / `social-profile`s
- **Empty/negative result looks like:** `/wp-json/wp/v2/users` returns `[]`, a 401/403, or a 404 (enumeration disabled by a security plugin, or the site isn't WordPress), and `?author=N` does not redirect — treat as "hardened or not WordPress," not as "no authors."

## Gotchas & OpSec
- Many sites now disable REST user enumeration (Wordfence, iThemes, etc.); a blocked endpoint is common and not a dead end — try the `?author=N` redirect and the sitemap.
- The `slug` is usually the login username but can be a customised nicename — treat it as a strong lead, not a guaranteed login.
- OpSec: **passive but direct** — you are hitting the target's own server, which logs your IP. Use a VPN/sock-puppet and never authenticate.

## Overlaps ("do both")
- Pair with `[[wordpress-com]]` for the hosted-blog angle, and with WHOIS/reverse-IP on the `domain` — enumeration gives you the people, WHOIS gives you the registrant/infrastructure; together they connect the site to an owner.

## Trust & verifiability
`trust: trusted` — WordPress is first-party/open-source and the author-enumeration behaviour is a documented, reproducible property of its REST API and permalink handling, not a scraped or brokered dataset.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | wordpress |
| category | domains-ip-infrastructure |
| selectorsIn → selectorsOut | domain, username → username, name, social-profile |
| pricing / cost | free |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
