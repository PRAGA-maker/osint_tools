---
id: osint-tools-mcp-server
name: osint-tools-mcp-server
description: MCP server exposing multiple OSINT tools to AI assistants like Claude.
url: https://github.com/frishtik/osint-tools-mcp-server
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Giving an LLM agent direct tool access to OSINT lookups via the Model Context Protocol
selectorsIn:
- username
- email
- domain
- ip-address
- phone
selectorsOut:
- social-profile
- email
- domain
- ip-address
status: unknown
pricing: free
opsec: passive
opsecNote: ''
humanInLoop: false
humanInLoopReason: []
bestInteractionPattern: api
trust: community
trustNote: 207 stars; directly designed for Claude/AI-assistant integration, highly relevant to an agent-driven workflow.
missingPersonsRelevance: high
coverage:
- global
auth: none
api: true
localInstall: true
registration: false
aliases:
- osint-mcp
tags:
- mcp
- ai-agent
- claude
- integration
source: gh-topic-intelligence-gathering
lastVerified: ''
enrichment: full
---

# osint-tools-mcp-server

> MCP server exposing multiple OSINT tools to AI assistants like Claude.

- **URL:** https://github.com/frishtik/osint-tools-mcp-server
- **Best for:** Giving an LLM agent direct tool access to OSINT lookups via the Model Context Protocol
- **Source:** harvested from `gh-topic-intelligence-gathering`

Purpose-built to expose OSINT tools to an LLM via MCP. Highly relevant for this skill library since the consuming agent is itself Claude; can be wired in as a native MCP server to run username/email/domain lookups.

_Enrichment: full. If stub, complete per `schema/templates/tool.template.md`._
