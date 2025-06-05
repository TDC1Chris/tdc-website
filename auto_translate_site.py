import os
import time
from openai import OpenAI
from bs4 import BeautifulSoup
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

BASE_DIR = Path("docs")
EN_DIR = BASE_DIR / "en"
LANG_CODES = [d.name for d in BASE_DIR.iterdir() if d.is_dir() and d.name not in ["en", "assets"]]

HTML_FILES = ["index.html", "services.html", "contact.html", "testimonials.html", "404.html"]
VISIBLE_TAGS = ["h1", "h2", "h3", "p", "li", "span", "a", "button", "label"]

def ensure_all_files_present():
    for lang in LANG_CODES:
        target_dir = BASE_DIR / lang
        for fname in HTML_FILES:
            src_file = EN_DIR / fname
            dst_file = target_dir / fname
            if not dst_file.exists():
                dst_file.write_text(src_file.read_text(encoding="utf-8"), encoding="utf-8")

def extract_translatable_text(soup):
    text_nodes = []
    for tag in soup.find_all(VISIBLE_TAGS):
        if tag.string and tag.string.strip():
            text_nodes.append(tag)
    return text_nodes

def translate_text(text, target_language):
    prompt = f"Translate the following into {target_language} using professional, localized business terminology. Only return the translated version.\n\n{text}"
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Translation failed: {e}")
        return text

def translate_file(path, language_name):
    with open(path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    text_nodes = extract_translatable_text(soup)

    for node in text_nodes:
        original = node.string.strip()
        translated = translate_text(original, language_name)
        node.string.replace_with(translated)
        time.sleep(1.5)

    with open(path, "w", encoding="utf-8") as f:
        f.write(str(soup))

def run_translation():
    ensure_all_files_present()

    for lang_code in LANG_CODES:
        folder = BASE_DIR / lang_code
        print(f"\n🌍 Translating files in '{lang_code}'...")
        for file in HTML_FILES:
            path = folder / file
            if path.exists():
                print(f"  - Translating: {file}")
                translate_file(path, lang_code)

if __name__ == "__main__":
    run_translation()
