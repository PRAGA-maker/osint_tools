"""Shared policy for same-domain "do both" tool groups.

Both validate.py (warn on un-wired overlaps) and wire_related.py (populate the
links) import this so the validator's expectations exactly match what the wirer
produces — a group is either link-worthy (and should be cross-linked) or it isn't.
"""
import re

import _common as C

# Hosts where one domain serves many independent tools; key on host+first-path-seg
# so distinct repos/users aren't treated as one group.
MULTITENANT = {"github.com", "gitlab.com", "sourceforge.net", "bitbucket.org",
               "medium.com", "wordpress.com", "blogspot.com", "gitbook.io",
               "herokuapp.com", "netlify.app", "pages.dev", "web.app",
               "firebaseapp.com", "glitch.me", "replit.app", "readthedocs.io"}

# Generic platforms where sharing a domain does NOT make tools siblings — linking
# them would be noise, so neither wire nor warn for these.
GENERIC_DENYLIST = {"google.com", "youtube.com", "js.org", "gstatic.com",
                    "googleapis.com", "cloudflare.com", "amazonaws.com",
                    "apple.com", "microsoft.com", "wikipedia.org"}

# Multi-part public suffixes (eTLD): registered_domain() naively takes the last
# two labels, so core.ac.uk and jisc.ac.uk both collapse to 'ac.uk' — that groups
# unrelated institutions. Treat any key that IS one of these as generic (skip),
# so we don't cross-link unrelated sites that merely share a country/sector eTLD.
PUBLIC_SUFFIXES = {
    "co.uk", "ac.uk", "gov.uk", "org.uk", "me.uk", "net.uk", "sch.uk", "nhs.uk",
    "police.uk", "mod.uk", "ltd.uk", "plc.uk",
    "com.au", "net.au", "org.au", "gov.au", "edu.au", "id.au", "asn.au",
    "co.nz", "net.nz", "org.nz", "govt.nz", "ac.nz",
    "co.jp", "or.jp", "ne.jp", "ac.jp", "go.jp", "gr.jp",
    "com.br", "net.br", "org.br", "gov.br",
    "com.cn", "net.cn", "org.cn", "gov.cn",
    "co.za", "org.za", "gov.za", "co.in", "net.in", "org.in", "gov.in",
    "co.kr", "or.kr", "com.mx", "gob.mx", "com.ar", "com.tr", "com.ua",
    "com.pl", "com.sg", "com.hk", "com.tw", "com.my", "com.ph", "com.vn",
    "co.il", "co.id", "or.id", "co.th",
}

# Above this many tools a shared domain is almost certainly a generic host, not a
# curated suite; don't auto-link (keeps links meaningful and diffs bounded).
GROUP_CAP = 12


def dedup_key(url):
    dom = C.registered_domain(url)
    if not dom:
        return ""
    m = re.search(r"https?://([^/]+)(/[^/?#]*)?", url or "")
    host = (m.group(1).lower() if m else dom)
    if host.endswith(".github.io") or host.endswith(".gitlab.io"):
        return host  # user.github.io is already per-tool
    if dom in MULTITENANT:
        seg = (m.group(2) or "").strip("/") if m else ""
        return f"{dom}/{seg}" if seg else dom
    return dom


def should_link_group(key, ids):
    """Return (ok, reason). ok=True means this same-domain group is a genuine
    suite that should be cross-linked; reason explains a False."""
    dom = key.split("/")[0]
    if dom in GENERIC_DENYLIST or dom in PUBLIC_SUFFIXES:
        return False, "generic"
    if len([i for i in ids if i]) > GROUP_CAP:
        return False, "oversized"
    return True, ""


def is_cross_linked(ids, related_of):
    """True if every member lists every other member in its relatedTools."""
    idset = {i for i in ids if i}
    for i in idset:
        rel = set(related_of.get(i, ()))
        if (idset - {i}) - rel:
            return False
    return True
