---
name: platforms-index
description: Per-platform technique notes — what's publicly enumerable, the high-value pivots, the gotchas, and the platform-specific opsec leaks.
kind: group-index
---

# Platforms

Each note covers one platform: what you can enumerate publicly, the best pivots, the gotchas, and — critically — the platform-specific opsec leaks (because what tips off a target differs sharply between platforms). Social media is where most missing-persons cases break, so these notes carry a lot of the practical weight.

## Children
- **[[platform-instagram]]** (high) — face, location, dense associate graph; login-gated; story/profile views leak you.
- **[[platform-tiktok]]** (high) — video leaks face, voice, recurring locations, routine; frame-by-frame analysis is the key technique.
- **[[platform-reddit]]** (high) — pseudonymous but extremely leaky; the full public comment history is the pivot.
- **[[platform-facebook]]** (high) — best for real names and family graphs; pivot to relatives when the subject is locked down.
- **[[platform-x-twitter]]** (high) — public, real-time, searchable timeline; strong for last-known-activity; good deleted-post recovery.
- **[[platform-snapchat]]** (medium) — ephemeral; Snap Map can give near-real-time location; mostly confirmation + location.
- **[[platform-telegram]]** (medium) — username/phone bridge, public groups; adding a contact can notify the target.
- **[[platform-discord]]** (medium) — username/ID resolution, snowflake creation-date, linked accounts; content gated, joining exposes you.
- **[[platform-linkedin]]** (medium) — adult real name/employer/education; profile views are NOTIFIED by default — an opsec minefield.

## How to read these
Match the platform to the case (a runaway teen → Instagram/TikTok/Snapchat/Discord; an adult → Facebook/LinkedIn/X). Use the note's pivots as the *how*, but treat the **opsec** section as a hard constraint — the leaks (story views, profile-view notifications, contact-upload matching, server joins) are exactly the `[[antipattern-contaminating-the-subject]]` traps, and they differ per platform. The cross-cutting rules live in `[[phase-opsec]]`.
