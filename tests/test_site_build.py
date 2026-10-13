#!/usr/bin/env python3
"""Offline tests for the staged GitHub Pages artifact; Python stdlib only."""
from pathlib import Path
import tempfile
import unittest
import sys
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from build_site import build

class Resources(HTMLParser):
    def __init__(self):
        super().__init__()
        self.paths = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "script" and attrs.get("src"): self.paths.append(attrs["src"])
        if tag == "link" and attrs.get("rel") == "stylesheet": self.paths.append(attrs.get("href",""))

class StaticSiteTest(unittest.TestCase):
    def test_full_static_site_and_asset_paths(self):
        with tempfile.TemporaryDirectory(dir=ROOT) as tmp:
            dest = Path(tmp) / "website"
            build(dest)
            self.assertTrue((dest/".nojekyll").exists())
            for page in ["index.html", "examples/claude-inspired/index.html",
                         "examples/pattern-gallery/index.html",
                         "examples/evidence-workbench/index.html"]:
                file = dest / page
                self.assertTrue(file.is_file(), page)
                html = file.read_text(encoding="utf-8")
                self.assertNotIn("../../.agents/", html)
                parser = Resources()
                parser.feed(html)
                for url in parser.paths:
                    if url.startswith(("https:","data:")): continue
                    self.assertTrue((file.parent/url).resolve().is_file(), f"{page}: {url}")
            gallery = (dest/"examples/pattern-gallery/app.js").read_text(encoding="utf-8")
            self.assertIn('from "../../assets/patterns.js"',gallery)
            for f in ("claude-inspired.css","patterns.css","patterns.js"):
                self.assertTrue((dest/"assets"/f).is_file())
            self.assertFalse((dest/".agents").exists())

    def test_output_cannot_overwrite_project(self):
        with self.assertRaises(ValueError):
            build(ROOT)

if __name__ == "__main__":
    unittest.main()
