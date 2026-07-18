---
id: i-see-you-iseeyou
name: I-See-You (ISeeYou)
description: Use when you can get a target to click a link in an AUTHORIZED engagement and want their precise `geolocation` — returns HTML5 GPS coordinates plus `ip-address`.
url: https://github.com/Viralmaniar/I-See-You
category: geolocation
path:
- geolocation
bestFor: Capturing a target's exact GPS location via a crafted link during an authorized social-engineering/phishing test.
selectorsIn:
- social-profile
selectorsOut:
- geolocation
- ip-address
status: live
pricing: free
costNote: Free, open-source (Bash + JavaScript). Uses free Serveo/ngrok tunnels; no account required to run.
opsec: active
opsecNote: This is intrusive and legally sensitive — it tricks the target's browser into surrendering GPS location, which requires their consent to the browser prompt and requires YOUR legal authorization (engagement scope / written consent). It interacts directly with the target and can be logged by the tunnel provider. Never use it without documented authorization; unsanctioned use is likely illegal.
humanInLoop: true
humanInLoopReason:
- legal-gate
bestInteractionPattern: cli
trust: community
trustNote: Popular open-source red-team tool (~1.2k stars); does what it says, but it is offensive tooling — audit the script and only deploy within an authorized engagement.
missingPersonsRelevance: medium
coverage:
- global
auth: none
api: false
localInstall: true
registration: false
relatedTools:
- seeker
- passhunt
- xposedornot
aliases:
- ISeeYou
- Viralmaniar/I-See-You
tags:
- geolocation
- phishing
- social-engineering
- red-team
source: gh-topic-reconnaissance
lastVerified: '2026-07-17'
enrichment: full
---

# I-See-You (ISeeYou)

> A red-team geolocation tool: host a link that, when a target opens it and accepts the browser prompt, hands you their exact GPS coordinates — for authorized engagements only.

## When to use
You are running an **authorized** social-engineering or phishing assessment (or a consented locate) and need a target's precise position, not just a coarse IP geolocation. ISeeYou stands up a small web server, tunnels it publicly via Serveo, and uses the browser's HTML5 Geolocation API so that a target who opens the link and grants location permission leaks latitude/longitude to your terminal. This is an active, intrusive capability with a hard legal gate — it belongs in sanctioned pentests, not open investigation of a stranger.

## How to use it (`bestInteractionPattern`: cli)
1. **Confirm authorization first** — engagement scope or written consent covering location capture of this target. Without it, stop.
2. Clone and run: `git clone https://github.com/Viralmaniar/I-See-You && cd I-See-You && bash ISeeYou.sh`.
3. The script starts a local listener and opens a Serveo tunnel, printing a public URL on a random subdomain.
4. Deliver that URL to the target through your authorized pretext; when they open it and accept the browser's location prompt, their `geolocation` (and `ip-address`) print to your terminal.
5. Convert the lat/long via Google Maps to a place; record it as evidence with a timestamp.
6. Pivot: coordinates corroborate an address; the leaked IP feeds IP-intel.

## Inputs → Outputs
- **In:** a target willing/tricked into clicking your link (delivered via a `social-profile`/message) **within scope**
- **Out:** precise `geolocation` (lat/long) and the target's `ip-address`
- **Empty/negative result looks like:** the target opens the link but **denies** the location prompt (or has it blocked) — you then get only the coarse IP, not GPS. No click at all means no data.

## Gotchas & OpSec
- **Legal gate:** capturing someone's location this way without authorization is illegal in most jurisdictions. Documented consent/scope is mandatory.
- Requires the target to actively grant the browser location permission — many will decline, especially on desktop; success rates are higher on mobile.
- Traffic transits a third-party tunnel (Serveo/ngrok) that can log it; use disposable infrastructure and clean up after.
- Active and target-facing: assume the interaction may be noticed and attributed.

## Overlaps ("do both")
- Same family as `[[seeker]]` — both use the HTML5 geolocation trick with a hosted link; keep one as a fallback if the other's tunnelling breaks. Choose based on which template/pretext fits the engagement.

## Trust & verifiability
`trust: community` — a well-known, widely-forked open-source offensive tool. It reliably does what it claims, but it is attacker tooling: read the script before running, and only operate it inside a lawful, authorized engagement.

---
## Metadata
<!-- generated from frontmatter by scripts/build_index.py; do not edit by hand -->
| field | value |
|---|---|
| id | i-see-you-iseeyou |
| category | geolocation |
| selectorsIn → selectorsOut | social-profile → geolocation, ip-address |
| pricing / cost | free |
| trust | community |
| MP relevance | medium |
| interaction | cli |
| opsec | active |
| human-in-loop | yes (legal-gate) |
