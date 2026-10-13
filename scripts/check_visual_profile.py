#!/usr/bin/env python3
"""Offline structural checks for the portable R1 visual profile (stdlib only)."""
from html.parser import HTMLParser
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / '.agents/skills/conversation-native-ui'

class Markup(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links = [], []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs: self.ids.append(attrs['id'])
        for name in ('href', 'src'):
            if name in attrs: self.links.append(attrs[name])

class VisualProfileChecks(unittest.TestCase):
    def test_portable_resources(self):
        for name in ('SKILL.md', 'references/claude-ui-design.md', 'assets/claude-inspired.css', 'agents/openai.yaml'):
            self.assertTrue((SKILL / name).is_file(), name)
    def test_visual_sources(self):
        guide = (SKILL / 'references/claude-ui-design.md').read_text(encoding='utf-8')
        for term in ('design-guidelines', 'transparent-theming', 'documented', 'adapted', '#FAF9F5', '#30302E'):
            self.assertIn(term, guide)
    def test_swatch_values_and_scope(self):
        css = (SKILL / 'assets/claude-inspired.css').read_text(encoding='utf-8')
        for term in ('.cnui {', '#FAF9F5', '#F5F4ED', '#30302E', '#262624', '#141413', '--cn-reading-width: 720px', '--cn-radius-md: var(--border-radius-md, 8px)', '--cn-rule: var(--border-width-regular, .5px)'):
            self.assertIn(term, css)
        self.assertNotIn('@font-face', css)
        self.assertNotIn('url(http', css)
    def test_theme_and_accessibility_hooks(self):
        css = (SKILL / 'assets/claude-inspired.css').read_text(encoding='utf-8')
        for term in ('prefers-color-scheme: dark', 'prefers-reduced-motion: reduce', 'focus-visible', 'min-height: 44px'):
            self.assertIn(term, css)
    def test_html_local_resources_and_ids(self):
        for directory in ('claude-inspired', 'evidence-workbench'):
            path = ROOT / 'examples' / directory / 'index.html'
            parsed = Markup(); parsed.feed(path.read_text(encoding='utf-8'))
            self.assertEqual(len(parsed.ids), len(set(parsed.ids)))
            for target in parsed.links:
                if target.startswith(('#', 'http:', 'https:', 'data:', 'mailto:')): continue
                target = target.split('#')[0].split('?')[0]
                self.assertTrue((path.parent / target).exists(), target)
    def test_js_dom_targets(self):
        for directory, pattern in (('claude-inspired', r'byId\("([\w-]+)"\)'), ('evidence-workbench', r'\$\("([\w-]+)"\)')):
            folder = ROOT / 'examples' / directory
            parsed = Markup(); parsed.feed((folder / 'index.html').read_text(encoding='utf-8'))
            for name in re.findall(pattern, (folder / 'app.js').read_text(encoding='utf-8')):
                self.assertIn(name, parsed.ids)
    def test_skill_links_are_self_contained(self):
        text = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
        for target in re.findall(r'\]\(([^)]+)\)', text):
            if not target.startswith(('http:', 'https:', '#')):
                self.assertTrue((SKILL / target).exists(), target)
    def test_sample_labels_and_safe_text_rendering(self):
        app = (ROOT / 'examples/claude-inspired/app.js').read_text(encoding='utf-8')
        self.assertIn('textContent', app)
        self.assertNotIn('innerHTML', app)
        self.assertIn('No AI model analyzed', app)
        self.assertIn('Clipboard access is unavailable', app)
    def test_pattern_gallery_components(self):
        gallery = ROOT / 'examples/pattern-gallery'
        parsed = Markup()
        parsed.feed((gallery / 'index.html').read_text(encoding='utf-8'))
        self.assertEqual(len(parsed.ids), len(set(parsed.ids)))
        for target in parsed.links:
            if target.startswith(('#','http:','https:','data:','mailto:')): continue
            self.assertTrue((gallery / target.split('#')[0]).exists(), target)
        script = (gallery / 'app.js').read_text(encoding='utf-8')
        self.assertIn('initCarousel', script)
        self.assertIn('initWorkspace', script)
        css = (SKILL / 'assets/patterns.css').read_text(encoding='utf-8')
        self.assertIn('scroll-snap-type', css)
        self.assertIn('safe-area-inset', css)
    def test_demo_status_is_truthful(self):
        for path in (
            ROOT / 'examples/claude-inspired/index.html',
            ROOT / 'examples/pattern-gallery/index.html',
            ROOT / 'examples/evidence-workbench/index.html',
        ):
            self.assertTrue(path.is_file())
            self.assertIn('demo', path.read_text(encoding='utf-8').lower())


def run_checks():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(VisualProfileChecks)
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful():
        raise SystemExit(1)

if __name__ == '__main__':
    run_checks()
