---
id: line-message-analyzer
name: LINE Message Analyzer
description: Use when you already hold an exported LINE chat log and want to profile behaviour from it — returns message-frequency, active-hours and top-word analytics per participant.
url: https://github.com/chonyy/line-message-analyzer
category: messaging
path:
- messaging
- wechat-line
bestFor: Turning a LINE chat export into behavioural analytics — who talks most, when they're active, and what they talk about.
selectorsIn: []
selectorsOut:
- associate
status: live
pricing: free
costNote: Free, open-source Python tool; no account or key. You must supply your own exported LINE chat file.
opsec: passive
opsecNote: Runs entirely locally on a chat log you already possess and makes no network query to LINE or the participants, so it is passive and leaves no trace. The prerequisite is lawful possession of the export — you must be a party to the chat or have proper authority; analysing others' private messages without that is the real risk here.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: A community open-source project (chonyy); the analysis logic is transparent and auditable, and its output is only as good as the export you feed it.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
aliases:
- chonyy line-message-analyzer
tags:
- line
- chat-analysis
source: arf-seed
lastVerified: '2026-07-11'
enrichment: full
---

# LINE Message Analyzer

> A local Python tool that mines an exported LINE conversation for behavioural patterns — activity rhythm, message volume, and recurring topics per person.

## When to use
You lawfully hold an exported LINE chat log (from a device you're examining, a cooperating party's export, or your own conversation with the subject) and want to extract behavioural intelligence rather than read line-by-line. The analyzer quantifies who messages most, the hours/days each participant is active (a proxy for time zone and daily routine), and the words/topics that dominate — useful for building a subject's pattern-of-life or corroborating a relationship's intensity. Reach for it when the raw log is too large to eyeball.

## How to use it (`bestInteractionPattern`: cli)
1. In LINE, export the target conversation's chat history to a text file.
2. Clone https://github.com/chonyy/line-message-analyzer and install its Python requirements.
3. Run the analyzer against the exported file.
4. Review the outputs: per-participant message counts, active-hour/day distributions, and top-word/topic summaries.
5. Pivot: active-hours suggest a time zone/routine to corroborate elsewhere; heavy interlocutors are close `associate`s; recurring names/places become new leads.

## Inputs → Outputs
- **In:** an exported LINE chat-history file (you must already have it)
- **Out:** behavioural analytics — message frequency, active-hours pattern, top words, and the `associate`s a subject converses with most
- **Empty/negative result looks like:** thin/uninformative charts — a short or sparse export yields little signal; the tool can only analyse what the log contains.

## Gotchas & OpSec
- Prerequisite data: this analyses an export you supply — it does not obtain LINE data for you (LINE messages are otherwise not remotely accessible).
- **Legal gate**: only analyse chats you are a party to or have lawful authority over; processing others' private messages without that can be unlawful.
- Format drift: LINE's export format changes; a parser may need tweaks for newer exports.
- OpSec: passive — fully local, no network calls.

## Overlaps ("do both")
- Pairs with device-forensics workflows — forensics recovers the export, this analyses it.
- Pairs with `[[signal-org]]`-style expectation-setting — both underline that messenger content lives on devices/exports, not on remotely-queryable servers.

## Trust & verifiability
`trust: community` — an auditable open-source analyzer; its conclusions are only as reliable as the completeness of the export you feed it, so note any gaps in the log before drawing pattern-of-life inferences.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | line-message-analyzer |
