#!/usr/bin/env python3
"""Non-destructive install / reinstall / backup regression tests."""
import subprocess
import sys
import tempfile
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent.parent
INSTALLER = ROOT / "scripts/install_skill.py"

class InstallSkillTest(unittest.TestCase):
    def run_installer(self, target, *args):
        return subprocess.run(
            [sys.executable, str(INSTALLER), "--target", str(target), *args],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
    def test_portable_install_and_safe_replace(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            skill = root / ".agents/skills/conversation-native-ui"
            preview = self.run_installer(root, "--dry-run")
            self.assertEqual(preview.returncode, 0, preview.stderr)
            self.assertFalse(skill.exists())
            created = self.run_installer(root)
            self.assertEqual(created.returncode, 0, created.stderr)
            self.assertTrue((skill/"SKILL.md").is_file())
            self.assertTrue((skill/"assets/patterns.css").is_file())
            self.assertTrue((skill/"assets/patterns.js").is_file())
            self.assertTrue((skill/"references/claude-ui-design.md").is_file())
            # Existing content must not be overwritten by default.
            (skill/"user-note.txt").write_text("keep this prior version")
            duplicate = self.run_installer(root)
            self.assertEqual(duplicate.returncode, 2)
            self.assertEqual((skill/"user-note.txt").read_text(), "keep this prior version")
            replaced = self.run_installer(root, "--force")
            self.assertEqual(replaced.returncode, 0, replaced.stderr)
            self.assertFalse((skill/"user-note.txt").exists())
            backups = list(skill.parent.glob("conversation-native-ui-backup-*"))
            self.assertEqual(len(backups), 1)
            self.assertEqual((backups[0]/"user-note.txt").read_text(), "keep this prior version")
    def test_missing_project_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            result = self.run_installer(Path(folder)/"missing")
            self.assertEqual(result.returncode, 2)
            self.assertIn("does not exist", result.stderr)

if __name__ == "__main__":
    unittest.main()
