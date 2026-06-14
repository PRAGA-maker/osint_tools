---
id: digify-com
name: digify.com
description: Use when you want to share a document and track who opens it, when, and from where — a document-DRM/tracking product (the harvested URL is its blog on PDF tracking); it returns open/view analytics, not identity lookups.
url: https://digify.com/blog/pdf-document-tracking/
category: email
path:
- email
bestFor: Tracking views/opens and access analytics on documents you distribute.
selectorsIn:
- email
- document-id
selectorsOut:
- ip-address
- geolocation
- metadata-exif
status: live
pricing: freemium
costNote: Commercial document-security/DRM SaaS with tiered paid plans and a limited free tier.
opsec: active
opsecNote: ACTIVE technique — you distribute a tracked document to a target; opening it logs the viewer. It engages the subject and may raise legal/consent and evidentiary issues. Not passive collection.
humanInLoop: true
humanInLoopReason:
- account-login
- payment-wall-partial
- legal-gate
bestInteractionPattern: web-manual
trust: unverified
trustNote: Legitimate commercial document-tracking/DRM vendor; harvested via its marketing blog. Investigative use is an active, consent-sensitive technique with narrow lawful application, so trust for OSINT purposes is unverified.
missingPersonsRelevance: low
coverage:
- global
auth: account
api: true
localInstall: false
registration: true
aliases:
- Digify
tags:
- emailtrackers
- document-tracking
- drm
source: uk-osint
lastVerified: ''
enrichment: full
---

# digify.com

> Digify is a document-security/DRM SaaS that tracks who opens a shared file, when, and from where — the harvested link is its blog page about PDF tracking.

## When to use
Only when you are lawfully distributing a document to a subject and want open/view analytics (who opened it, timestamps, approximate location). It does not resolve a person from an `email`; it tracks engagement with a `document-id` you control. For missing-persons work this is a niche, high-risk engagement technique.

## How to use it (`bestInteractionPattern`: web-manual)
1. Create an account and upload the document; Digify wraps it with tracking/DRM controls.
2. Share the tracked link (often tied to a recipient `email`) with the target.
3. When opened, the dashboard logs viewer activity — time, duration, page-level views, and `ip-address`/approximate `geolocation`.
4. Pivot: a captured IP/location can corroborate a subject's region — only if lawfully obtained and usable.

## Inputs → Outputs
- **In:** recipient `email` + a `document-id` (the tracked file you share)
- **Out:** open/view analytics — `ip-address`, approximate `geolocation`, access timestamps (`metadata-exif`-style)
- **Empty/negative result looks like:** no opens logged — the target never opened it, opened via a proxy/VPN, or access was blocked.

## Gotchas & OpSec
- **Active and consent-sensitive:** distributing a tracked document contacts the subject and can violate consent/privacy law and evidentiary norms. Authorise first.
- It is a *product*, not an OSINT lookup — there is no field to search a person; you must orchestrate the share.
- Human-in-the-loop: account login plus paid tiers for meaningful features.

## Trust & verifiability
`trust: unverified` — reputable vendor, but for investigative use the technique is active and narrowly lawful, and captured IP/location is spoofable. Do not treat it as conclusive.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | digify-com |
| category | email |
| selectorsIn → selectorsOut | email, document-id → ip-address, geolocation, metadata-exif |
| pricing / cost | freemium |
| trust | unverified |
| MP relevance | low |
| interaction | web-manual |
| opsec | active |
| human-in-loop | yes |
