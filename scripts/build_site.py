#!/usr/bin/env python3
"""Create an isolated static GitHub Pages site from original browser demos.

No outside assets, package manager, API keys or absolute paths are involved.
Host-specific embedded MCP Apps are NOT created by this builder.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent.parent
REPO = "https://github.com/smallCattyCat/conversation-native-ui-for-codex"

SOURCE_REPLACEMENTS = {
    "../../.agents/skills/conversation-native-ui/assets/claude-inspired.css": "../../assets/claude-inspired.css",
    "../../.agents/skills/conversation-native-ui/assets/patterns.css": "../../assets/patterns.css",
    "../../.agents/skills/conversation-native-ui/assets/patterns.js": "../../assets/patterns.js",
    "../../docs/claude-ui-reference.md": REPO + "/blob/main/docs/claude-ui-reference.md",
    "../../NOTICE.md": REPO + "/blob/main/NOTICE.md",
}

def build(output: Path) -> Path:
    output = output.expanduser().resolve()
    if output == ROOT or ROOT not in output.parents:
        raise ValueError("Output must be a subdirectory of the project")
    if output.is_symlink():
        raise ValueError("Output path must not be a symbolic link")
    if output.exists():
        if not output.is_dir():
            raise ValueError("Output already exists and is not a directory")
        shutil.rmtree(output)
    output.mkdir(parents=True)
    (output / ".nojekyll").touch()
    for fname in ("index.html", "styles.css"):
        shutil.copy2(ROOT / "site" / fname, output / fname)

    assets = ROOT / ".agents" / "skills" / "conversation-native-ui" / "assets"
    destination = output / "assets"
    destination.mkdir()
    for fname in ("claude-inspired.css", "patterns.css", "patterns.js"):
        shutil.copy2(assets / fname, destination / fname)

    for example in ("claude-inspired", "pattern-gallery", "evidence-workbench"):
        source = ROOT / "examples" / example
        target = output / "examples" / example
        target.mkdir(parents=True, exist_ok=True)
        for filename in ("index.html", "styles.css", "app.js"):
            contents = (source / filename).read_text(encoding="utf-8")
            for old, new in SOURCE_REPLACEMENTS.items():
                contents = contents.replace(old, new)
            (target / filename).write_text(contents, encoding="utf-8")
        optional = source / "claude-profile.css"
        if optional.is_file():
            shutil.copy2(optional, target / "claude-profile.css")

    return output

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "site-dist")
    args = parser.parse_args()
    path = build(args.output)
    print(f"Built static site in {path}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
