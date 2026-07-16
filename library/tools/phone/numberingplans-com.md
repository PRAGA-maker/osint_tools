---
id: numberingplans-com
name: numberingplans.com
description: Use when you have a `phone` number, IMEI or IMSI and want to decode its country, operator/number-type or device make — returns carrier/geolocation and device metadata.
url: https://www.numberingplans.com/?page=home
category: phone
path:
- phone
bestFor: Decoding what a phone number, IMEI, IMSI or SIM identifies — country, network/operator, number type or handset make/model.
selectorsIn:
- phone
- device-id
selectorsOut:
- geolocation
- metadata-exif
status: live
pricing: freemium
costNote: Most analysis is free for personal/limited use; professional/business volume needs a paid subscription. The number-analysis, IMEI and IMSI tools are usable free.
opsec: passive
opsecNote: You query numberingplans.com's own reference databases, not the subscriber's carrier, so the number holder is not contacted or alerted. It reveals no personal identity — only technical metadata about the number/device.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: International Numbering Plans is a long-established reference for global telephone numbering, IMEI (TAC) and IMSI/MCC-MNC data; the technical decoding is authoritative, though it does not identify people.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- freephonenum-com
- international-numbering-plans-database
- numbering-plans
aliases:
- International Numbering Plans
- numberingplans
tags:
- mobilephone
- phone-analysis
- imei
- imsi
source: uk-osint
lastVerified: '2026-07-10'
enrichment: full
---

# numberingplans.com

> A reference decoder for the world's numbering plans: feed it a phone number, IMEI or IMSI and it tells you the country, operator, number type or handset make — technical metadata, not a subscriber name.

## When to use
You have a `phone` number and want to know what it *is* before you spend effort on it: which country and operator issued it, whether it's mobile/fixed/VoIP/premium, and how it should be formatted. It also decodes hardware identifiers — an **IMEI** (via its TAC prefix → manufacturer and model) and an **IMSI** (via MCC/MNC → home country and network). Correct classification stops you wasting time (e.g. realising a "mobile" is actually a VoIP or premium-rate line).

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://www.numberingplans.com/ and pick the relevant analyser: **Number analysis**, **IMEI analysis**, or **IMSI analysis**.
2. Enter the identifier — full international `phone` number, 15-digit IMEI, or IMSI.
3. Read the decoded output: country, operator/network, number type/range for phones; manufacturer + model for IMEI; home country + carrier for IMSI.
4. Pivot: a confirmed country/operator narrows which regional lookup or messaging-app check to run next; a mobile classification greenlights `[[freephonenum-com]]` and app-registration checks.

## Inputs → Outputs
- **In:** `phone` number, or a `device-id` (IMEI/IMSI/SIM)
- **Out:** `geolocation` (country of issue), `metadata-exif`-style technical facts (operator, number type, handset make/model)
- **Empty/negative result looks like:** "number range not found" / unallocated range, or a TAC not in the database — meaning the identifier is invalid, spoofed, or too new to be catalogued, not that the person doesn't exist.

## Gotchas & OpSec
- It returns **network/technical** data, never a subscriber's name or address — don't expect identity here.
- Number portability means the *original* operator may not be the *current* one; treat operator as issuing-network, not present carrier.
- OpSec: fully passive — it's a reference lookup, invisible to the number's owner.

## Overlaps ("do both")
- Pairs with `[[freephonenum-com]]` and app-registration checks — use numberingplans first to classify country/type, then those tools to attach activity/identity once you know the number is a real mobile line.

## Trust & verifiability
`trust: trusted` — authoritative numbering/TAC/MCC-MNC reference data; the caveat is portability and database freshness, so verify current carrier separately if it matters.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | numberingplans-com |
| category | phone |
| selectorsIn → selectorsOut | phone, device-id → geolocation, metadata-exif |
| pricing / cost | freemium |
| trust | trusted |
| MP relevance | medium |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
</content>
