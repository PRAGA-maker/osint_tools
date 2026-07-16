---
id: bellingcat-com
name: bellingcat.com
description: Use when you have a `name` or keyword and want verbatim quotes from UK & Ireland local-council meetings — returns transcript hits naming who said what in which council (`name`/`employer-org` in local-government context).
url: https://council-search.bellingcat.com/
category: public-records
path:
- public-records
bestFor: Searching auto-generated transcripts of UK & Ireland council meetings for a name or phrase.
selectorsIn:
- name
selectorsOut:
- name
- employer-org
- associate
status: live
pricing: free
costNote: Free and open-source (Bellingcat). No account or payment.
opsec: passive
opsecNote: You search public meeting transcripts; nothing reaches any subject. Fully passive.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: web-manual
trust: trusted
trustNote: Built and maintained by Bellingcat (open source). Transcripts are auto-generated from council AV (via the Public I provider), so quotes can contain transcription errors — verify wording against the source recording before quoting.
missingPersonsRelevance: high
coverage:
- uk
auth: none
api: false
localInstall: false
registration: false
relatedTools:
- tellmescotland-gov-uk
- companies-house
- bellingcat
- bellingcat-openstreetmap-search
- these-are-the-tools-open-source-researchers-say-they-need
- xblog-bellingcat-a-beginner-s-guide-to-flight-tracking-bellingcat
aliases:
- Bellingcat Council Meeting Transcript Search
- CouncilSearcher
- council-search.bellingcat.com
tags:
- propertysites
- Property Related Sites
- local-government
- transcripts
source: uk-osint
lastVerified: '2026-07-11'
enrichment: full
---

# bellingcat.com

> Bellingcat's Council Meeting Transcript Search — search verbatim quotes from local-council meetings across the UK and Ireland by name or phrase, instead of watching hours of recordings.

## When to use
You have a `name` (a councillor, official, applicant, or member of the public) or a keyword/topic and want to find where it was spoken about in UK/Ireland local-government meetings. The tool indexes auto-generated transcripts of council meetings, so you can surface a person's public statements, mentions of a business/development, or discussion of an address/planning matter — mapping a subject to local-government activity and to the officials/`associate`s around them.

## How to use it (`bestInteractionPattern`: web-manual)
1. Open https://council-search.bellingcat.com/.
2. Enter a `name`, organisation, or phrase and search.
3. Read the transcript hits: the verbatim quote, the council/meeting it came from, and (where available) the speaker.
4. Follow a hit back to the source meeting/recording to confirm exact wording and context.
5. Pivot: a named councillor/official feeds `employer-org` and associate mapping; a discussed business/address feeds property and company records (`[[companies-house]]`); for Scotland-specific notices pair with `[[tellmescotland-gov-uk]]`.

## Inputs → Outputs
- **In:** `name` or keyword/phrase
- **Out:** verbatim transcript quotes → speaker `name`, council/`employer-org` context, related `associate`s (other participants)
- **Empty/negative result looks like:** no hits — the council may not use the supported AV provider (Public I), the meeting isn't transcribed/indexed, or the term wasn't said. Coverage is partial, so absence isn't conclusive.

## Gotchas & OpSec
- Human-in-the-loop: none; a public transcript search.
- OpSec: **passive** — public records; no subject is contacted.
- Transcripts are machine-generated and can mis-hear names/words; always verify a quote against the source recording before relying on or attributing it. Coverage is limited to councils on the supported provider.

## Overlaps ("do both")
- Complements `[[tellmescotland-gov-uk]]` (Scottish statutory notices) and `[[companies-house]]` (company/officer records) — the transcript tool captures what was *said* in local government, the others capture the formal records; together they connect a person's words to their official footprint.

## Trust & verifiability
`trust: trusted` — a Bellingcat open-source tool over genuine public-meeting audio. The data is legitimate, but auto-transcription introduces errors, so treat quotes as leads to confirm against the original recording, and remember coverage is provider-limited.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | bellingcat-com |
| category | public-records |
| selectorsIn → selectorsOut | name → name, employer-org, associate |
| pricing / cost | free |
| trust | trusted |
| MP relevance | high |
| interaction | web-manual |
| opsec | passive |
| human-in-loop | no |
