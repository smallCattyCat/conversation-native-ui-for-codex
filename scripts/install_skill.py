#!/usr/bin/env python3
"""Portable project-local Codex skill installer. Stdlib-only, non-destructive by default."""
from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import tempfile
from datetime import datetime, timezone
from uuid import uuid4

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / ".agents" / "skills" / "conversation-native-ui"

def install(target: Path, *, dry_run: bool = False, force: bool = False) -> str:
    target = target.expanduser().resolve()
    if not target.is_dir():
        raise ValueError(f"Project directory does not exist: {target}")
    if not (SOURCE / "SKILL.md").is_file():
        raise RuntimeError("Skill source missing; use the full project checkout")
    destination = target / ".agents" / "skills" / SOURCE.name
    if destination.exists() and not force:
        raise FileExistsError(f"Skill already exists: {destination} (use --force to back it up and replace)")
    if dry_run:
        return f"DRY RUN: would copy {SOURCE} -> {destination}" + (" (backup existing)" if destination.exists() else "")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".cnui-install-", dir=destination.parent) as scratch:
        staged = Path(scratch) / SOURCE.name
        shutil.copytree(SOURCE, staged)
        backup = None
        if destination.exists():
            suffix = datetime.now(timezone.utc).strftime("%Y%m%d-%H%M%S") + "-" + uuid4().hex[:6]
            backup = destination.with_name(destination.name + "-backup-" + suffix)
            destination.rename(backup)
        try:
            staged.rename(destination)
        except Exception:
            if backup is not None and not destination.exists():
                backup.rename(destination)
            raise
    return f"INSTALLED: {destination}" + (f"\nPrevious version backed up: {backup}" if backup else "")

def main() -> int:
    parser = argparse.ArgumentParser(description="Install conversation-native-ui into an existing Codex project.")
    parser.add_argument("--target", required=True, type=Path, help="Existing target project's root directory")
    parser.add_argument("--dry-run", action="store_true", help="Show intended changes without writing")
    parser.add_argument("--force", action="store_true", help="Back up and replace an existing copy")
    args = parser.parse_args()
    try:
        print(install(args.target, dry_run=args.dry_run, force=args.force))
    except (OSError, ValueError, RuntimeError) as exc:
        parser.exit(2, f"ERROR: {exc}\n")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
