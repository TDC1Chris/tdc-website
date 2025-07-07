#!/usr/bin/env python3
"""
NATO Language Translation System
Copyright (c) 2025 Total Design Consulting LLC. All Rights Reserved.

PROPRIETARY AND CONFIDENTIAL SOFTWARE
=====================================

This software is the proprietary and confidential property of Total Design Consulting LLC.
All rights reserved. No part of this software may be reproduced, distributed, or 
transmitted in any form or by any means, including photocopying, recording, or other 
electronic or mechanical methods, without the prior written permission of Total Design 
Consulting LLC, except in the case of brief quotations embodied in critical reviews 
and certain other noncommercial uses permitted by copyright law.

LICENSING NOTICE:
- This software is licensed for use by authorized clients of Total Design Consulting LLC only
- Unauthorized copying, modification, distribution, or use is strictly prohibited
- Reverse engineering, decompilation, or disassembly is prohibited
- This software is provided "as is" without warranty of any kind

For licensing inquiries and permissions, contact:
Total Design Consulting LLC
Email: licensing@totaldesignconsulting.com
Website: https://totaldesignconsulting.com

NATO Language Translation System v1.0.0
Developed by: Christopher Clubb, Multilingual Cyber-OT Engineer
Technical Specifications: 27 Languages, 30 NATO Countries, AI-Powered with Human Verification
Security Features: Cost controls, API validation, rate limiting, error handling
"""

import os
import time
from openai import OpenAI
from bs4 import BeautifulSoup
from pathlib import Path
from dotenv import load_dotenv

# Proprietary software identification
SOFTWARE_NAME = "NATO Language Translation System"
SOFTWARE_VERSION = "1.0.0"
COPYRIGHT_NOTICE = "Copyright (c) 2025 Total Design Consulting LLC. All Rights Reserved."
LICENSE_TYPE = "Proprietary - Licensed Software"

load_dotenv()

# Security and cost protection measures
API_KEY = os.getenv("OPENAI_API_KEY")
MAX_TRANSLATIONS_PER_RUN = int(os.getenv("MAX_TRANSLATIONS_PER_RUN", "1000"))  # Safety limit
REQUIRE_CONFIRMATION = os.getenv("REQUIRE_CONFIRMATION", "true").lower() == "true"

# Cost estimation constants
ESTIMATED_TOKENS_PER_TRANSLATION = 200
ESTIMATED_COST_PER_1K_TOKENS = 0.00015  # GPT-4o-mini pricing

def check_api_key_security():
    """Verify API key is properly secured."""
    if not API_KEY:
        print("❌ SECURITY: No OpenAI API key found!")
        print("   Please create a .env file with: OPENAI_API_KEY=your_key_here")
        print("   ⚠️  NEVER commit your .env file to git!")
        return False
    
    if len(API_KEY) < 20:
        print("❌ SECURITY: API key appears invalid (too short)")
        return False
    
    # Check if this looks like a placeholder
    if API_KEY.lower() in ["your_key_here", "replace_me", "api_key", "openai_key"]:
        print("❌ SECURITY: API key appears to be a placeholder!")
        print("   Please set a real OpenAI API key in your .env file")
        return False
    
    print("✅ SECURITY: API key found and appears valid")
    return True

def check_software_license():
    """
    Proprietary Software License Verification
    Total Design Consulting LLC - All Rights Reserved
    """
    print("=" * 70)
    print(f"🏢 {SOFTWARE_NAME} v{SOFTWARE_VERSION}")
    print(f"📋 {COPYRIGHT_NOTICE}")
    print(f"🔐 License Type: {LICENSE_TYPE}")
    print("=" * 70)
    print("⚠️  PROPRIETARY SOFTWARE NOTICE:")
    print("   This software is licensed for authorized use only.")
    print("   Unauthorized copying, distribution, or modification is prohibited.")
    print("   For licensing inquiries: licensing@totaldesignconsulting.com")
    print("=" * 70)
    
    # License compliance check
    license_file = Path(".tdc_license")
    if not license_file.exists():
        print("❌ LICENSE: No valid license file found!")
        print("   Contact Total Design Consulting LLC for licensing.")
        print("   This software requires a valid license to operate.")
        return False
    
    return True

def estimate_translation_cost(num_languages, num_files=7):
    """
    Estimate OpenAI API costs for translation operation.
    
    PROPRIETARY ALGORITHM - Total Design Consulting LLC
    Cost estimation methodology is proprietary and confidential.
    """
    # Rough estimation based on average content
    translations_per_file = 50  # Average translatable elements per page
    total_translations = num_languages * num_files * translations_per_file
    total_tokens = total_translations * ESTIMATED_TOKENS_PER_TRANSLATION
    estimated_cost = (total_tokens / 1000) * ESTIMATED_COST_PER_1K_TOKENS
    
    return {
        'total_translations': total_translations,
        'total_tokens': total_tokens,
        'estimated_cost': estimated_cost
    }

def get_user_confirmation(cost_info):
    """Get user confirmation before proceeding with translations."""
    if not REQUIRE_CONFIRMATION:
        return True
    
    print("\n💰 COST ESTIMATION:")
    print("=" * 40)
    print(f"Estimated translations: {cost_info['total_translations']:,}")
    print(f"Estimated tokens: {cost_info['total_tokens']:,}")
    print(f"Estimated cost: ${cost_info['estimated_cost']:.2f} USD")
    print("=" * 40)
    
    print("\n⚠️  WARNING: This will charge your OpenAI account!")
    print("💡 TIP: Start with 1-2 languages first to test: python auto_translate_site.py de es")
    
    while True:
        response = input("\nDo you want to proceed? (yes/no): ").lower().strip()
        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            print("Translation cancelled by user.")
            return False
        else:
            print("Please enter 'yes' or 'no'")

# Initialize client only after security checks
client = None

def initialize_openai_client():
    """Initialize OpenAI client with security checks."""
    global client
    
    if not check_api_key_security():
        return False
    
    try:
        client = OpenAI(api_key=API_KEY)
        # Test the connection with a minimal request
        test_response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": "test"}],
            max_tokens=1
        )
        print("✅ SECURITY: OpenAI connection verified")
        return True
    except Exception as e:
        print(f"❌ SECURITY: OpenAI connection failed: {e}")
        print("   Please check your API key and internet connection")
        return False

BASE_DIR = Path("docs")
EN_DIR = BASE_DIR  # English files are in the root docs directory

# All 30 NATO member countries with their language codes and names
NATO_LANGUAGES = {
    # Major NATO languages (already supported in portfolio)
    "de": "German",           # 🇩🇪 Germany
    "es": "Spanish",          # 🇪🇸 Spain
    "fr": "French",           # 🇫🇷 France
    "it": "Italian",          # 🇮🇹 Italy
    "pt": "Portuguese",       # 🇵🇹 Portugal
    "nl": "Dutch",            # 🇳🇱 Netherlands
    "no": "Norwegian",        # 🇳🇴 Norway
    "da": "Danish",           # 🇩🇰 Denmark
    "sv": "Swedish",          # 🇸🇪 Sweden
    "fi": "Finnish",          # 🇫🇮 Finland
    "pl": "Polish",           # 🇵🇱 Poland
    "cs": "Czech",            # 🇨🇿 Czech Republic
    "sk": "Slovak",           # 🇸🇰 Slovakia
    "hu": "Hungarian",        # 🇭🇺 Hungary
    "ro": "Romanian",         # 🇷🇴 Romania
    "bg": "Bulgarian",        # 🇧🇬 Bulgaria
    "hr": "Croatian",         # 🇭🇷 Croatia
    "sl": "Slovenian",        # 🇸🇮 Slovenia
    "et": "Estonian",         # 🇪🇪 Estonia
    "lv": "Latvian",          # 🇱🇻 Latvia
    "lt": "Lithuanian",       # 🇱🇹 Lithuania
    "el": "Greek",            # 🇬🇷 Greece
    "tr": "Turkish",          # 🇹🇷 Turkey
    "is": "Icelandic",        # 🇮🇸 Iceland
    "sq": "Albanian",         # 🇦🇱 Albania
    "mk": "Macedonian",       # 🇲🇰 North Macedonia
    "me": "Montenegrin",      # 🇲🇪 Montenegro
    
    # NATO countries with shared languages
    # Canada (English/French) - French already included
    # Belgium (Dutch/French) - Both already included  
    # Luxembourg (French/German) - Both already included
    # United Kingdom (English) - Base language
    # United States (English) - Base language
}

HTML_FILES = [
    "index.html", 
    "services.html", 
    "portfolio.html",
    "contact.html", 
    "testimonials.html", 
    "legal-terms-conditions.html",
    "404.html"
]

VISIBLE_TAGS = ["h1", "h2", "h3", "h4", "h5", "h6", "p", "li", "span", "a", "button", "label", "title"]

# Skip translation for these classes/ids to preserve functionality
SKIP_CLASSES = ["nav-link", "navbar-brand", "btn", "badge", "bi", "flag-icon"]
SKIP_IDS = ["navbarNav"]

def ensure_all_directories_exist():
    """Create language directories and copy English files if they don't exist."""
    for lang_code in NATO_LANGUAGES.keys():
        target_dir = BASE_DIR / lang_code
        target_dir.mkdir(exist_ok=True)
        
        # Copy English files as templates if they don't exist
        for fname in HTML_FILES:
            src_file = EN_DIR / fname
            dst_file = target_dir / fname
            if src_file.exists() and not dst_file.exists():
                dst_file.write_text(src_file.read_text(encoding="utf-8"), encoding="utf-8")
                print(f"  📄 Created template: {lang_code}/{fname}")

def should_skip_element(element):
    """Check if an element should be skipped based on classes or IDs."""
    if element.get('class'):
        for class_name in element.get('class'):
            if any(skip_class in class_name for skip_class in SKIP_CLASSES):
                return True
    
    if element.get('id') and element.get('id') in SKIP_IDS:
        return True
    
    # Skip elements that are likely technical (contain URLs, emails, etc.)
    text = element.get_text(strip=True) if element else ""
    if any(indicator in text.lower() for indicator in ['@', 'http', '.com', '.pdf', 'mailto:']):
        return True
        
    return False

def extract_translatable_text(soup):
    """Extract text nodes that should be translated."""
    text_nodes = []
    for tag in soup.find_all(VISIBLE_TAGS):
        if (tag.string and tag.string.strip() and 
            not should_skip_element(tag) and
            len(tag.string.strip()) > 1):  # Skip single characters
            text_nodes.append(tag)
    return text_nodes

def translate_text(text, target_language, lang_code, translation_count=0):
    """Translate text using OpenAI with context-aware prompts and safety limits."""
    
    # Safety check: prevent runaway translations
    if translation_count > MAX_TRANSLATIONS_PER_RUN:
        print(f"⚠️  SAFETY: Translation limit reached ({MAX_TRANSLATIONS_PER_RUN}). Stopping to prevent excessive costs.")
        return text
    
    # Skip very short or potentially non-translatable content
    if len(text.strip()) < 3:
        return text
    
    # Enhanced prompt with business context
    prompt = f"""Translate the following text into {target_language} for a professional cybersecurity and industrial automation consulting website. 

Guidelines:
- Use formal, professional business language appropriate for {target_language}
- Maintain technical terminology accuracy for cybersecurity, PLC programming, and industrial automation
- Keep brand names, company names, and technical certifications in English (e.g., "CompTIA Security+", "General Motors", "TIA Portal")
- Preserve any numeric values, percentages, or measurements exactly
- Use appropriate business formality for the target culture
- Return ONLY the translated text, no explanations

Text to translate: {text}"""

    try:
        if not client:
            print("❌ ERROR: OpenAI client not initialized. Run initialization first.")
            return text
            
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # More cost-effective and still accurate
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,  # Lower temperature for more consistent translations
            max_tokens=500
        )
        translated = response.choices[0].message.content.strip()
        
        # Remove any quotes that might be added by the AI
        if translated.startswith('"') and translated.endswith('"'):
            translated = translated[1:-1]
        if translated.startswith("'") and translated.endswith("'"):
            translated = translated[1:-1]
            
        return translated
    except Exception as e:
        print(f"  ❌ Translation failed for '{text[:50]}...': {e}")
        return text  # Return original text if translation fails

def translate_file(file_path, language_name, lang_code, translation_count_ref):
    """Translate a single HTML file to the target language."""
    print(f"    🔄 Translating {file_path.name}...")
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            soup = BeautifulSoup(f, "html.parser")

        # Update the language attribute
        if soup.html:
            soup.html['lang'] = lang_code

        # Update page title if it exists
        if soup.title:
            original_title = soup.title.string
            if original_title and "Total Design Consulting" in original_title:
                translated_title = translate_text(original_title, language_name, lang_code, translation_count_ref[0])
                soup.title.string = translated_title
                translation_count_ref[0] += 1

        # Extract and translate text nodes
        text_nodes = extract_translatable_text(soup)
        file_translations = 0
        
        for node in text_nodes:
            # Safety check: stop if we've hit the translation limit
            if translation_count_ref[0] >= MAX_TRANSLATIONS_PER_RUN:
                print(f"    ⚠️  Hit translation safety limit. Stopping at {MAX_TRANSLATIONS_PER_RUN} translations.")
                break
                
            original = node.string.strip()
            if len(original) > 2:  # Only translate meaningful text
                translated = translate_text(original, language_name, lang_code, translation_count_ref[0])
                if translated != original:
                    node.string.replace_with(translated)
                    file_translations += 1
                    translation_count_ref[0] += 1
                
                # Rate limiting to avoid API limits and reduce costs
                time.sleep(0.5)

        # Save the translated file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(str(soup))
            
        print(f"    ✅ Completed {file_path.name} ({file_translations} translations)")
        
    except Exception as e:
        print(f"    ❌ Error translating {file_path.name}: {e}")

def update_language_links(soup, current_lang_code):
    """Update language switcher links for the current page."""
    # This would be where you'd update navigation language links
    # For now, we'll skip this as the current site doesn't have a language switcher
    pass

def run_translation(specific_languages=None, specific_files=None):
    """Run translation for specified languages and files."""
    print("🌍 NATO Language Translation Tool for Total Design Consulting")
    print("=" * 60)
    
    # Ensure all language directories exist
    print("\n📁 Setting up language directories...")
    ensure_all_directories_exist()
    
    # Filter languages if specified
    languages_to_process = specific_languages if specific_languages else NATO_LANGUAGES.keys()
    files_to_process = specific_files if specific_files else HTML_FILES
    
    print(f"\n🎯 Processing {len(languages_to_process)} languages and {len(files_to_process)} files...")
    
    for lang_code in languages_to_process:
        if lang_code not in NATO_LANGUAGES:
            print(f"⚠️  Skipping unknown language code: {lang_code}")
            continue
            
        language_name = NATO_LANGUAGES[lang_code]
        folder = BASE_DIR / lang_code
        
        print(f"\n🇺� Translating to {language_name} ({lang_code})...")
        
        for file_name in files_to_process:
            file_path = folder / file_name
            if file_path.exists():
                translate_file(file_path, language_name, lang_code, [0])  # Pass translation counter
            else:
                print(f"    ⚠️  File not found: {file_name}")
        
        print(f"✅ Completed {language_name} translation")

def create_language_index():
    """Create an index page showing all available languages."""
    index_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Total Design Consulting - Language Selection</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet"/>
    <link href="assets/css/style.css" rel="stylesheet"/>
</head>
<body>
    <div class="container mt-5">
        <h1 class="text-center text-success mb-4">Total Design Consulting</h1>
        <h2 class="text-center mb-5">Select Your Language / Choisissez votre langue / Wählen Sie Ihre Sprache</h2>
        <div class="row g-3">
"""
    
    # Add language cards
    for lang_code, language_name in NATO_LANGUAGES.items():
        flag_map = {
            "de": "🇩🇪", "es": "🇪🇸", "fr": "🇫🇷", "it": "🇮🇹", "pt": "🇵🇹",
            "nl": "🇳🇱", "no": "🇳🇴", "da": "🇩🇰", "sv": "🇸🇪", "fi": "🇫🇮",
            "pl": "🇵🇱", "cs": "🇨🇿", "sk": "🇸🇰", "hu": "🇭🇺", "ro": "🇷🇴",
            "bg": "🇧🇬", "hr": "🇭🇷", "sl": "🇸🇮", "et": "🇪🇪", "lv": "🇱🇻",
            "lt": "🇱🇹", "el": "🇬🇷", "tr": "🇹🇷", "is": "🇮🇸", "sq": "🇦🇱",
            "mk": "🇲🇰", "me": "🇲🇪"
        }
        
        flag = flag_map.get(lang_code, "🌍")
        index_content += f"""
            <div class="col-md-4 col-lg-3">
                <a href="{lang_code}/index.html" class="text-decoration-none">
                    <div class="card h-100 text-center hover-shadow">
                        <div class="card-body">
                            <div style="font-size: 2rem;">{flag}</div>
                            <h5 class="card-title mt-2">{language_name}</h5>
                        </div>
                    </div>
                </a>
            </div>"""
    
    # Add English option
    index_content += """
            <div class="col-md-4 col-lg-3">
                <a href="index.html" class="text-decoration-none">
                    <div class="card h-100 text-center hover-shadow border-success">
                        <div class="card-body">
                            <div style="font-size: 2rem;">🇺🇸</div>
                            <h5 class="card-title mt-2">English</h5>
                            <small class="text-success">Original</small>
                        </div>
                    </div>
                </a>
            </div>
        </div>
    </div>
</body>
</html>"""
    
    # Write the language index
    with open(BASE_DIR / "languages.html", "w", encoding="utf-8") as f:
        f.write(index_content)
    
    print("📄 Created language selection page: languages.html")

if __name__ == "__main__":
    import sys
    
    # Proprietary Software License Check
    if not check_software_license():
        print("\n❌ SOFTWARE LICENSE REQUIRED")
        print("   This is proprietary software owned by Total Design Consulting LLC.")
        print("   Contact licensing@totaldesignconsulting.com for authorization.")
        sys.exit(1)
    
    # Parse command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == "--help":
            print(f"""
{SOFTWARE_NAME} v{SOFTWARE_VERSION}
{COPYRIGHT_NOTICE}

PROPRIETARY SOFTWARE - AUTHORIZED USE ONLY

Usage:
    python auto_translate_site.py                    # Translate all languages
    python auto_translate_site.py de es fr          # Translate specific languages
    python auto_translate_site.py --create-index    # Create language selection page
    python auto_translate_site.py --list-languages  # List all supported languages
    
Supported NATO Languages:
""")
            for code, name in NATO_LANGUAGES.items():
                print(f"    {code}: {name}")
            print(f"\nTotal Design Consulting LLC - Proprietary Software")
            print(f"For licensing: licensing@totaldesignconsulting.com")
            sys.exit(0)
            
        elif sys.argv[1] == "--create-index":
            create_language_index()
            sys.exit(0)
            
        elif sys.argv[1] == "--list-languages":
            print("Supported NATO Languages:")
            for code, name in NATO_LANGUAGES.items():
                print(f"  {code}: {name}")
            sys.exit(0)
            
        else:
            # Translate specific languages
            specific_langs = sys.argv[1:]
            run_translation(specific_languages=specific_langs)
    else:
        # Translate all languages
        run_translation()
        create_language_index()
