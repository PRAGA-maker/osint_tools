---
id: osint-tools-mcp-server
name: osint-tools-mcp-server
description: Use when you have a `username`, `email`, `domain`, `ip-address`, or `phone` and want an LLM agent to run Sherlock/Holehe/Maigret/GHunt/SpiderFoot/theHarvester/Blackbird directly via MCP — returns `social-profile`, `email`, `domain`, and `ip-address` intelligence.
url: https://github.com/frishtik/osint-tools-mcp-server
category: ai-analysis-automation
path:
- ai-analysis-automation
bestFor: Giving an LLM agent native MCP access to a bundle of classic username/email/domain recon tools.
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
status: live
pricing: free
costNote: Open-source (self-hosted); free to run. Some bundled tools (GHunt, SpiderFoot, Blackbird) require their own separate install and, in GHunt's case, valid Google auth cookies.
opsec: active
opsecNote: The bundled tools reach out to third-party infrastructure on the target's selectors — Holehe pings ~120 platforms' password-reset/registration endpoints, GHunt queries Google with your cookies, SpiderFoot actively probes IPs/domains. Run from a sock-puppet network and use throwaway Google cookies for GHunt; several of these leave lookups that could be logged by the queried providers.
humanInLoop: true
humanInLoopReason:
- account-login
- rate-limit
bestInteractionPattern: api
trust: community
trustNote: Community GitHub project (~200 stars) that wraps well-known open-source OSINT tools behind MCP; the wrapper is only as trustworthy as the upstream tools and your own install. Purpose-built for Claude/AI-assistant integration.
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
lastVerified: '2026-07-15'
enrichment: full
---

# osint-tools-mcp-server

> An MCP server that exposes a bundle of classic OSINT recon tools (Sherlock, Holehe, Maigret, GHunt, SpiderFoot, theHarvester, Blackbird) so an LLM agent can invoke them natively.

## When to use
You are running an agent-driven investigation and want to pivot a `username`, `email`, `domain`, `ip-address`, or `phone` without leaving the agent loop. Because the consuming agent here is itself Claude, wiring this in as a native MCP server lets you fan a single selector across ~seven proven recon tools — username enumeration across thousands of sites (Sherlock/Maigret/Blackbird), email-to-platform mapping (Holehe), Google-account extraction (GHunt), and domain/subdomain/IP recon (theHarvester/SpiderFoot) — and reason over the results in place.

## How to use it (`bestInteractionPattern`: api)
1. Clone the repo and `pip install -r requirements.txt`; install the tools that ship separately (SpiderFoot, GHunt, Blackbird) and, for GHunt, provide valid Google auth cookies.
2. Add the server to your MCP client config (e.g. `claude_desktop_config.json`) pointing at the Python entrypoint.
3. From the agent, call the exposed tool for your selector:
   - `username` → Sherlock (399+ sites), Maigret (3000+ sites, false-positive scoring), Blackbird (581 sites)
   - `email` → Holehe (120+ platforms), GHunt (Google account)
   - `domain` / `ip-address` → theHarvester, SpiderFoot (5–30 min deep scans)
4. Read the structured results (platform lists, registration confirmations, confidence scores) and pivot the confirmed accounts into profile-level tools.

## Inputs → Outputs
- **In:** `username`, `email`, `domain`, `ip-address`, `phone`
- **Out:** `social-profile` lists, confirmed `email` registrations, `domain`/subdomain and `ip-address` intelligence, confidence-scored reports
- **Empty/negative result looks like:** a tool returns zero hits (e.g. Holehe finds no registrations, Sherlock finds no accounts) — treat as "not found on the sites checked," not proof of absence; false negatives are common when a tool's site list is stale.

## Gotchas & OpSec
- Human-in-the-loop: GHunt needs live Google auth cookies (account-login); SpiderFoot scans are slow and can trip rate limits — budget time and expect to babysit long runs.
- OpSec: **active** — these tools query third-party infrastructure on the target's selectors and can leave logged lookups. Isolate the host network and use throwaway credentials.
- Wrapper is community-maintained; verify the upstream tool versions it installs, since Sherlock/Holehe/Maigret site lists rot over time.

## Overlaps ("do both")
- Overlaps heavily with running `[[sherlock]]`, `[[holehe]]`, and `[[maigret]]` standalone — use this when you want them orchestrated from inside the agent, and the standalone tools when you need finer control or the latest release.

## Trust & verifiability
`trust: community` — an independent GitHub wrapper around reputable open-source tools; the intelligence quality comes from those upstream tools, and you should confirm each finding rather than trust the aggregated report blindly.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | osint-tools-mcp-server |
| category | ai-analysis-automation |
| selectorsIn → selectorsOut | username, email, domain, ip-address, phone → social-profile, email, domain, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | high |
| interaction | api |
| opsec | active |
| human-in-loop | yes (account-login, rate-limit) |
</content>
