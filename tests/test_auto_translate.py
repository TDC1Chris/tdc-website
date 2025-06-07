import os
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
