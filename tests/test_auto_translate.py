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

