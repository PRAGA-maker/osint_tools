"""Shared helpers for the OSINT skill library scripts."""
import os
import re
import yaml

LIB = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # .../library
ROOT = os.path.dirname(LIB)                                        # repo root
TOOLS_DIR = os.path.join(LIB, "tools")
STRATEGIES_DIR = os.path.join(LIB, "strategies")
INDEX_DIR = os.path.join(LIB, "index")
LEDGER_DIR = os.path.join(LIB, "ledger")

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", re.S)


def slugify(s: str) -> str:
    s = (s or "").lower().strip()
    s = re.sub(r"\([tdrm]\)", " ", s)        # strip (T)(D)(R)(M) markers
    s = s.replace("&", " and ").replace("+", " plus ")
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s or "item"


def parse_skill(path: str):
    """Return (frontmatter_dict, body_str). frontmatter is None if no YAML block."""
    with open(path, encoding="utf-8") as f:
        text = f.read()
    m = FM_RE.match(text)
    if not m:
        return None, text
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return None, text
    return fm, m.group(2)


def dump_frontmatter(fm: dict) -> str:
    return yaml.safe_dump(fm, sort_keys=False, allow_unicode=True, width=4096).strip()


def write_skill(path: str, fm: dict, body: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(dump_frontmatter(fm))
        f.write("\n---\n\n")
        f.write(body.lstrip("\n"))


def registered_domain(url: str) -> str:
    m = re.search(r"https?://([^/]+)", url or "")
    if not m:
        return ""
    host = m.group(1).lower().split(":")[0]
    if host.startswith("www."):
        host = host[4:]
    parts = host.split(".")
    return ".".join(parts[-2:]) if len(parts) >= 2 else host


def iter_skills(base_dir: str):
    """Yield (path, fm, body) for every non-index skill .md under base_dir."""
    for dirpath, _dirs, files in os.walk(base_dir):
        for fn in files:
            if not fn.endswith(".md") or fn == "_index.md":
                continue
            p = os.path.join(dirpath, fn)
            fm, body = parse_skill(p)
            if fm is None:
                continue
            if str(fm.get("kind", "")) == "group-index":
                continue
            yield p, fm, body


def oneline(s: str, limit: int = 240) -> str:
    s = re.sub(r"\s+", " ", str(s or "")).strip()
    return s[:limit]
