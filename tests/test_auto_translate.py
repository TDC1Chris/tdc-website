import os
from pathlib import Path
import sys
import types
import re

sys.path.append(str(Path(__file__).resolve().parents[1]))

# Provide a minimal stub for the openai package required by auto_translate_site
sys.modules.setdefault("openai", types.SimpleNamespace(OpenAI=lambda api_key: None))

class _Tag:
    def __init__(self, name, string):
        self.name = name
        self.string = string

class _SimpleSoup:
    def __init__(self, html, parser="html.parser"):
        self.tags = [
            _Tag(m.group(1), m.group(2))
            for m in re.finditer(r"<(\w+)>([^<]+)</\1>", html)
        ]

    def find_all(self, names):
        return [t for t in self.tags if t.name in names]

FakeBS4 = types.SimpleNamespace(BeautifulSoup=_SimpleSoup)
sys.modules.setdefault("bs4", FakeBS4)
sys.modules.setdefault("dotenv", types.SimpleNamespace(load_dotenv=lambda: None))

import auto_translate_site as ats
from bs4 import BeautifulSoup


def test_extract_translatable_text():
    html = "<h1>Hello</h1><p>World</p><div>Ignore</div>"
    soup = BeautifulSoup(html, "html.parser")
    tags = ats.extract_translatable_text(soup)
    assert [t.name for t in tags] == ["h1", "p"]


def test_ensure_all_files_present(tmp_path, monkeypatch):
    docs = tmp_path / "docs"
    en = docs / "en"
    es = docs / "es"
    en.mkdir(parents=True)
    es.mkdir(parents=True)

    (en / "index.html").write_text("EN index")
    (en / "services.html").write_text("EN services")
    (es / "index.html").write_text("existing")

    monkeypatch.setattr(ats, "BASE_DIR", docs)
    monkeypatch.setattr(ats, "EN_DIR", en)
    monkeypatch.setattr(ats, "LANG_CODES", ["es"])
    monkeypatch.setattr(ats, "HTML_FILES", ["index.html", "services.html"])

    ats.ensure_all_files_present()

    assert (es / "services.html").read_text() == "EN services"
    assert (es / "index.html").read_text() == "existing"

import sys
import types
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

# Stub out external dependencies if they are not available
bs4_module = types.ModuleType('bs4')
class _Tag:
    def __init__(self, elem):
        self._elem = elem
    @property
    def name(self):
        return self._elem.tag
    @property
    def string(self):
        return self._elem.text
class BeautifulSoup:
    def __init__(self, markup, parser):
        self._root = ET.fromstring(markup)
    def find_all(self, tags):
        return [_Tag(e) for e in self._root.iter() if e.tag in tags]
bs4_module.BeautifulSoup = BeautifulSoup
sys.modules.setdefault('bs4', bs4_module)

dotenv_module = types.ModuleType('dotenv')
dotenv_module.load_dotenv = lambda *args, **kwargs: None
sys.modules.setdefault('dotenv', dotenv_module)

openai_module = types.ModuleType('openai')
class DummyOpenAI:
    def __init__(self, api_key=None):
        self.api_key = api_key
openai_module.OpenAI = DummyOpenAI
sys.modules.setdefault('openai', openai_module)

os.environ.setdefault('OPENAI_API_KEY', 'dummy')

import auto_translate_site

from pathlib import Path
import tempfile


def test_extract_translatable_text():
    html = """
    <html><body>
        <h1>Hello</h1>
        <p>World</p>
        <div><span>Span Text</span></div>
    </body></html>
    """
    soup = BeautifulSoup(html, "html.parser")
    nodes = auto_translate_site.extract_translatable_text(soup)
    assert [n.name for n in nodes] == ["h1", "p", "span"]
    assert [n.string.strip() for n in nodes] == ["Hello", "World", "Span Text"]


def test_ensure_all_files_present(monkeypatch, tmp_path):
    base = tmp_path / "docs"
    en = base / "en"
    fr = base / "fr"
    en.mkdir(parents=True)
    fr.mkdir()

    html_files = ["index.html", "services.html"]
    for name in html_files:
        (en / name).write_text(f"EN {name}")
    (fr / "index.html").write_text("FR index")

    monkeypatch.setattr(auto_translate_site, "BASE_DIR", base)
    monkeypatch.setattr(auto_translate_site, "EN_DIR", en)
    monkeypatch.setattr(auto_translate_site, "HTML_FILES", html_files)
    monkeypatch.setattr(auto_translate_site, "LANG_CODES", ["fr"])

    auto_translate_site.ensure_all_files_present()

    assert (fr / "index.html").read_text() == "FR index"
    assert (fr / "services.html").read_text() == (en / "services.html").read_text()