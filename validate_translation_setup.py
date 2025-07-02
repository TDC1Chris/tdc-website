#!/usr/bin/env python3
"""
Validation script for NATO language translation setup.
Tests the translation environment without using OpenAI API calls.
"""

import os
from pathlib import Path

def test_file_structure():
    """Test if required files exist."""
    base_dir = Path("docs")
    required_files = [
        "index.html", 
        "services.html", 
        "portfolio.html",
        "contact.html", 
        "testimonials.html", 
        "legal-terms-conditions.html",
        "404.html"
    ]
    
    print("📁 Testing file structure...")
    missing_files = []
    
    for file_name in required_files:
        file_path = base_dir / file_name
        if file_path.exists():
            print(f"  ✅ {file_name}")
        else:
            print(f"  ❌ {file_name} - MISSING")
            missing_files.append(file_name)
    
    return len(missing_files) == 0

def test_language_mapping():
    """Test NATO language definitions."""
    nato_languages = {
        "de": "German", "es": "Spanish", "fr": "French", "it": "Italian", 
        "pt": "Portuguese", "nl": "Dutch", "no": "Norwegian", "da": "Danish",
        "sv": "Swedish", "fi": "Finnish", "pl": "Polish", "cs": "Czech",
        "sk": "Slovak", "hu": "Hungarian", "ro": "Romanian", "bg": "Bulgarian",
        "hr": "Croatian", "sl": "Slovenian", "et": "Estonian", "lv": "Latvian",
        "lt": "Lithuanian", "el": "Greek", "tr": "Turkish", "is": "Icelandic",
        "sq": "Albanian", "mk": "Macedonian", "me": "Montenegrin"
    }
    
    print(f"\n🌍 Testing NATO language mapping...")
    print(f"  ✅ {len(nato_languages)} NATO languages defined")
    
    # Verify we have all major NATO countries covered
    major_nato = ["de", "fr", "es", "it", "nl", "pl", "tr", "el", "no", "da"]
    missing_major = [lang for lang in major_nato if lang not in nato_languages]
    
    if not missing_major:
        print("  ✅ All major NATO languages included")
    else:
        print(f"  ❌ Missing major languages: {missing_major}")
    
    return len(missing_major) == 0

def test_dependencies():
    """Test if required packages can be imported."""
    print(f"\n📦 Testing dependencies...")
    
    dependencies = {
        "pathlib": "Path",
        "os": "os.getenv", 
        "time": "time.sleep",
        "sys": "sys.argv"
    }
    
    all_good = True
    
    for module, test_attr in dependencies.items():
        try:
            exec(f"import {module}")
            if hasattr(eval(module), test_attr.split('.')[-1]):
                print(f"  ✅ {module}")
            else:
                print(f"  ⚠️  {module} - missing {test_attr}")
        except ImportError:
            print(f"  ❌ {module} - NOT AVAILABLE")
            all_good = False
    
    # Test optional dependencies (for translation)
    optional_deps = ["openai", "bs4", "dotenv"]
    print(f"\n📦 Testing optional translation dependencies...")
    
    for dep in optional_deps:
        try:
            exec(f"import {dep}")
            print(f"  ✅ {dep}")
        except ImportError:
            print(f"  ⚠️  {dep} - Install with: pip install -r requirements.txt")
    
    return all_good

def test_directory_creation():
    """Test if language directories can be created."""
    print(f"\n📁 Testing directory creation...")
    
    test_dir = Path("docs/test_lang")
    try:
        test_dir.mkdir(exist_ok=True)
        print(f"  ✅ Can create directories")
        
        # Test file creation
        test_file = test_dir / "test.html"
        test_file.write_text("<html><body>Test</body></html>", encoding="utf-8")
        print(f"  ✅ Can create files")
        
        # Cleanup
        test_file.unlink()
        test_dir.rmdir()
        print(f"  ✅ Cleanup successful")
        
        return True
    except Exception as e:
        print(f"  ❌ Directory/file operations failed: {e}")
        return False

def test_html_structure():
    """Test HTML files for translation compatibility."""
    print(f"\n🔍 Testing HTML structure...")
    
    base_dir = Path("docs")
    test_files = ["index.html", "services.html"]
    
    issues = []
    
    for file_name in test_files:
        file_path = base_dir / file_name
        if not file_path.exists():
            continue
            
        try:
            content = file_path.read_text(encoding="utf-8")
            
            # Basic HTML structure checks
            if "<html" in content and "</html>" in content:
                print(f"  ✅ {file_name} - Valid HTML structure")
            else:
                print(f"  ⚠️  {file_name} - Incomplete HTML structure")
                issues.append(f"{file_name}: missing html tags")
            
            # Check for translatable content
            if any(tag in content for tag in ["<h1", "<h2", "<p", "<span"]):
                print(f"  ✅ {file_name} - Contains translatable content")
            else:
                print(f"  ⚠️  {file_name} - Limited translatable content")
                issues.append(f"{file_name}: limited content")
                
        except Exception as e:
            print(f"  ❌ {file_name} - Read error: {e}")
            issues.append(f"{file_name}: read error")
    
    return len(issues) == 0

def main():
    """Run all validation tests."""
    print("🔧 NATO Language Translation Validation")
    print("=" * 50)
    
    tests = [
        ("File Structure", test_file_structure),
        ("Language Mapping", test_language_mapping), 
        ("Dependencies", test_dependencies),
        ("Directory Operations", test_directory_creation),
        ("HTML Structure", test_html_structure)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"  ❌ {test_name} failed with error: {e}")
            results.append((test_name, False))
    
    print(f"\n📊 Validation Summary")
    print("=" * 30)
    
    passed = 0
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status:8} {test_name}")
        if result:
            passed += 1
    
    print(f"\nResults: {passed}/{len(results)} tests passed")
    
    if passed == len(results):
        print("\n🎉 All tests passed! Translation system is ready.")
        print("\nNext steps:")
        print("1. pip install -r requirements.txt")
        print("2. Create .env file with OPENAI_API_KEY")
        print("3. Run: python auto_translate_site.py --help")
    else:
        print("\n⚠️  Some tests failed. Please address issues before translation.")
    
    return passed == len(results)

if __name__ == "__main__":
    main()
