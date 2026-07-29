---
id: ollama
name: Ollama
description: Use when you have collected OSINT text/documents and want to run an LLM over them entirely offline — returns local model output with no data leaving your machine.
url: https://ollama.com/
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Private, offline LLM analysis of sensitive collected material (summaries, entity extraction, translation) without cloud exposure.
selectorsIn: []
selectorsOut: []
status: live
pricing: freemium
costNote: The local engine and open models are free and open-source (MIT). An optional Ollama Cloud/Pro tier (~$20/mo) runs larger models on their servers — avoid it for sensitive data, defeating the local-only benefit.
opsec: passive
opsecNote: Passive and self-contained when run locally — prompts and documents never leave your hardware, which is the whole point for confidential missing-persons material. Only the initial model download touches the network; verify you are pulling from official model sources. Do NOT route sensitive data through the paid Cloud tier.
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: cli
trust: community
trustNote: Widely adopted open-source project (github.com/ollama/ollama) with a large community; model quality varies by which open model you pull.
missingPersonsRelevance: low
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
invitationOnly: false
deprecated: false
relatedTools: []
aliases:
- ollama.com
tags:
- llm
- local-ai
- offline
- analysis
source: arf-seed
lastVerified: '2026-07-29'
enrichment: full
---

# Ollama

> A local LLM runtime that lets you analyse sensitive OSINT material with open models entirely offline — no cloud, no data egress.

## When to use
You have already collected material (documents, chat exports, scraped text, transcripts) and want an LLM to summarise, translate, extract names/dates/locations, or draft a timeline — but the data is too sensitive to paste into a hosted AI service. Ollama runs open models on your own CPU/GPU so nothing leaves the machine. It is an analysis/enrichment layer, not a data source: it produces no OSINT selectors on its own.

## How to use it (`bestInteractionPattern`: cli)
1. Install: `curl -fsSL https://ollama.com/install.sh | sh` (Linux/macOS; Windows installer on the site).
2. Pull a model once (needs network): e.g. `ollama pull llama3.1` or a small model for a laptop.
3. Run interactively: `ollama run llama3.1` and paste your prompt + material — or feed a file: `ollama run llama3.1 < notes.txt`.
4. For automation, hit the local REST API at `http://localhost:11434/api/generate` from a script/pipeline (e.g. batch-extract entities from many documents).
5. Pivot: the extracted names/usernames/locations feed back into the rest of the library's people-/domain-search tools.

## Inputs → Outputs
- **In:** free-text prompts + your own collected documents (no OSINT selector required)
- **Out:** LLM-generated text — summaries, translations, extracted entities, drafted analysis
- **Empty/negative result looks like:** hallucinated or hedged output. Local open models are smaller than frontier cloud models — treat any extracted "fact" as a lead to verify, never ground truth.

## Gotchas & OpSec
- Human-in-the-loop: none for operation, but you must judge the output — small local models hallucinate more than hosted ones.
- OpSec: passive and offline once the model is downloaded; ideal for confidential casework. The paid Cloud tier sends prompts to Ollama's servers — never use it for sensitive data.
- Hardware: larger/more capable models need a GPU or lots of RAM; pick a quantised/small model on modest machines.

## Overlaps ("do both")
- Complements every collection tool in the library — Ollama is the private "make sense of what you gathered" step. Use it instead of a hosted chatbot whenever the material must not leave your control.

## Trust & verifiability
`trust: community` — the runtime is popular, open-source and inspectable, but answer quality depends entirely on the open model you load and its known tendency to fabricate; always corroborate model claims against primary sources.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | ollama |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | — → — |
| pricing / cost | freemium |
| trust | community |
| MP relevance | low |
| interaction | cli |
| opsec | passive |
| human-in-loop | no |
