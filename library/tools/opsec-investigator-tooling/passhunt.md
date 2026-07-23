---
id: passhunt
name: PassHunt
description: Use when you have identified a `domain`/device vendor and model and want its factory default credentials — a CLI that searches ~2000 default passwords across ~500 vendors.
url: https://github.com/Viralmaniar/Passhunt
category: opsec-investigator-tooling
path:
- opsec-investigator-tooling
bestFor: Looking up factory default usernames/passwords for a known network device or application vendor/model.
selectorsIn: []
selectorsOut:
- password
status: live
pricing: free
costNote: Free and open source (GPL-3.0); a local Python CLI, no account or payment.
opsec: passive
opsecNote: The tool itself is a passive, offline lookup of a static credential database (from cirt.net) — running it touches no target. ACTUALLY USING a default credential to log into a device you don't own is active and likely illegal; only do so against systems you are authorised to test.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source tool (Viralmaniar/Passhunt) with a static default-credential dataset sourced from cirt.net; the data is dated (last release 2018) so newer devices may be missing.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- i-see-you-iseeyou
- xposedornot
aliases:
- Passhunt
- Viralmaniar/Passhunt
tags:
- Passwords
- default-credentials
source: cyb-detective
lastVerified: '2026-07-23'
enrichment: full
---

# PassHunt

> A small offline CLI that searches a database of factory default credentials — ~2,000 passwords across ~500 vendors — so you can look up a device's out-of-the-box login.

## When to use
You've fingerprinted a network device, appliance, or application (from a banner, a screenshot, a service scan) and want to know its documented default username/password. Reach for PassHunt to search its bundled credential list by vendor. This is context for authorised security testing — knowing a device *ships* with a default credential. Actually attempting the login is a separate, active step that requires authorisation.

## How to use it (`bestInteractionPattern`: cli)
1. Clone the repo and install: `pip3 install -r requirements.txt` (needs Python 3).
2. Run `python3 Passhunt.py` for the interactive menu.
3. Choose to list supported vendors or search a specific vendor for its default credentials.
4. Read the returned username/password pairs for that vendor/model.
5. Pivot: use the result only against systems you're authorised to test; for real-world devices, verify defaults against the vendor's current documentation, since this dataset is dated.

## Inputs → Outputs
- **In:** a device/application vendor (and model) — identified out-of-band
- **Out:** documented default `password`/username pairs for that vendor
- **Empty/negative result looks like:** vendor not in the dataset, or only old models covered — the 2018-era database misses newer devices; absence isn't proof there's no default.

## Gotchas & OpSec
- Data is static and dated (cirt.net, ~2018) — cross-check against the vendor's current docs.
- The lookup is passive; **using** a credential is active and legally gated — authorised engagements only.
- It's a convenience over manually searching cirt.net, not a novel data source.

## Overlaps ("do both")
- Complements service-fingerprinting tools (which identify the device) and vulnerability lookups like `[[cve-details]]` — fingerprint the device, check its CVEs, and check its default creds together when scoping an authorised test.

## Trust & verifiability
`trust: community` — a widely-used open-source tool wrapping a public credential list; the data is reliable but dated, so confirm any default against the vendor's current documentation before relying on it.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | passhunt |
| category | opsec-investigator-tooling |
| selectorsIn → selectorsOut |  → password |
| pricing / cost | free |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
