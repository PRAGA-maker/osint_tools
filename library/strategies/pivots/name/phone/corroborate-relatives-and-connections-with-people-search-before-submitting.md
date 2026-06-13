---
id: corroborate-relatives-and-connections-with-people-search-before-submitting
name: Corroborate relatives and connections with people-search before submitting
description: Use when After identifying candidate relatives/associates from social media, to confirm relationships and pull contact identifiers for flags.
type: technique
summary: Social-media inferences about who is a relative or associate should be confirmed against people-search/public-records databases rather than relying on news articles or assumption. People-search engines validate family relationships, surface additional phone numbers and addresses, and confirm a connection is real. Because record availability is jurisdiction-specific, tool choice must adapt to the subject's country/region. SignalHire-style extensions can also pull phone/email and linked profiles directly off a LinkedIn or social profile.
missingPersonsRelevance: high
phase: enrichment
pivotFrom:
- name
- associate
- social-profile
pivotTo:
- phone
- address
- associate
- email
platforms:
- facebook
- linkedin
steps:
- Take a candidate relative/associate name from the social graph.
- Query a people-search engine appropriate to the subject's country.
- Confirm the relationship and harvest associated phones/addresses.
- On LinkedIn/social profiles, use an extension like SignalHire to extract phone, email, and linked accounts.
- Record the discovery method and source for each fact so it survives judge/LE review.
signals:
- People-search confirms the same household/relationship inferred from social media
- Extracted phone/email links back to another known account
pitfalls:
- Trusting a news article's relationship claim without record confirmation
- Using a US-only people-search for an international subject
- Submitting a relative flag without explaining how the relationship was established
toolsUsed:
- TruePeopleSearch
- SignalHire
- US Phone Book
- country-specific people-search engines
tags:
- people-search
- public-records
- corroboration
- relatives
- enrichment
evidence:
- type: writeup
  url: https://jack.bio/blog/tracelabs
  note: TruePeopleSearch used to verify family connections rather than relying solely on news
- type: writeup
  url: https://medium.com/@cyberbychase/osint-methodology-and-tradecraft-tips-for-winning-the-trace-labs-black-badge-from-team-federal-ebe737d70c6a
  note: SignalHire extension to extract phone/email/linked profiles; TruePeopleSearch and US Phone Book
- type: writeup
  url: https://wondersmithrae.medium.com/finding-missing-people-with-tracelabs-ctf-d5617c7cd659
  note: Country-specific people-search tools needed for international subjects
trust: community
source: searchparty-writeups
---

# Corroborate relatives and connections with people-search before submitting

> Social-media inferences about who is a relative or associate should be confirmed against people-search/public-records databases rather than relying on news articles or assumption. People-search engines validate family relationships, surface additional phone numbers and addresses, and confirm a connection is real. Because record availability is jurisdiction-specific, tool choice must adapt to the subject's country/region. SignalHire-style extensions can also pull phone/email and linked profiles directly off a LinkedIn or social profile.

**When to use:** After identifying candidate relatives/associates from social media, to confirm relationships and pull contact identifiers for flags.

## Steps
- Take a candidate relative/associate name from the social graph.
- Query a people-search engine appropriate to the subject's country.
- Confirm the relationship and harvest associated phones/addresses.
- On LinkedIn/social profiles, use an extension like SignalHire to extract phone, email, and linked accounts.
- Record the discovery method and source for each fact so it survives judge/LE review.

## Signals it's working
- People-search confirms the same household/relationship inferred from social media
- Extracted phone/email links back to another known account

## Pitfalls
- Trusting a news article's relationship claim without record confirmation
- Using a US-only people-search for an international subject
- Submitting a relative flag without explaining how the relationship was established

**Tools:** TruePeopleSearch, SignalHire, US Phone Book, country-specific people-search engines

_Harvested from `searchparty-writeups` — methodology only, no case PII. Promote/curate as needed._
