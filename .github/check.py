"""Checks the Broker Sense package before it's published: valid manifests, one version everywhere (the tag's too, on a
release) and in the changelog, every skill named and described, and connectors that are HTTPS with nothing secret in
them (every installer receives .mcp.json), and the icon plugin.json names. Usage: python3 .github/check.py [tag]"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
tag = (sys.argv[1] if len(sys.argv) > 1 else "").lstrip("v")
problems = []
market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text())
changelog = (ROOT / "CHANGELOG.md").read_text()
for entry in market["plugins"]:
    plug = ROOT / entry["source"]
    m = json.loads((plug / ".claude-plugin" / "plugin.json").read_text())
    if (m["name"], m["version"]) != (entry["name"], entry["version"]):
        problems.append(f"{entry['name']}: plugin.json and marketplace.json disagree on its name or version")
    if tag and tag != m["version"]:
        problems.append(f"{m['name']}: the tag says {tag}, the plugin says {m['version']}")
    if not re.search(rf"^## {re.escape(m['version'])}( |$)", changelog, re.M):
        problems.append(f"{m['name']}: CHANGELOG.md has no entry for {m['version']}")
    if m.get("icon") and not (plug / m["icon"]).is_file():
        problems.append(f"{m['name']}: plugin.json's icon {m['icon']} isn't in the plugin")
    if (plug / "bin").exists():
        problems.append(f"{m['name']}: a top-level bin/ blocks install")
    skills = sorted((plug / "skills").glob("*/SKILL.md"))
    if not skills:
        problems.append(f"{m['name']}: no skills")
    for s in skills:
        head = s.read_text().split("\n---\n", 1)[0]
        name = re.search(r"^name: (.+)$", head, re.M)
        if not head.startswith("---\n") or not name or name.group(1).strip() != s.parent.name:
            problems.append(f"{s.relative_to(ROOT)}: frontmatter needs name: {s.parent.name}")
        if not re.search(r"^description: .{20,}$", head, re.M):
            problems.append(f"{s.relative_to(ROOT)}: frontmatter needs a description")
    mcp = plug / ".mcp.json"
    for key, server in (json.loads(mcp.read_text())["mcpServers"] if mcp.exists() else {}).items():
        if server.get("type") != "http" or not str(server.get("url", "")).startswith("https://") or set(server) - {"type", "url"}:
            problems.append(f"{m['name']}: connector {key} must be an https url and nothing else")
print("\n".join(problems) or f"ok: {', '.join(e['name'] + ' ' + e['version'] for e in market['plugins'])}")
sys.exit(1 if problems else 0)
