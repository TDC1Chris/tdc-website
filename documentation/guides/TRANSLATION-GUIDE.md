# NATO Language Translation Tool Documentation

## Overview

The enhanced `auto_translate_site.py` script now supports all 30 NATO member countries' languages and provides comprehensive translation capabilities for the Total Design Consulting website.

## Supported Languages

### All 30 NATO Languages Supported ✅

| Language Code | Language Name | Country Flag | NATO Member |
|---------------|---------------|--------------|-------------|
| `de` | German | 🇩🇪 | Germany |
| `es` | Spanish | 🇪🇸 | Spain |
| `fr` | French | 🇫🇷 | France |
| `it` | Italian | 🇮🇹 | Italy |
| `pt` | Portuguese | 🇵🇹 | Portugal |
| `nl` | Dutch | 🇳🇱 | Netherlands |
| `no` | Norwegian | 🇳🇴 | Norway |
| `da` | Danish | 🇩🇰 | Denmark |
| `sv` | Swedish | 🇸🇪 | Sweden |
| `fi` | Finnish | 🇫🇮 | Finland |
| `pl` | Polish | 🇵🇱 | Poland |
| `cs` | Czech | 🇨🇿 | Czech Republic |
| `sk` | Slovak | 🇸🇰 | Slovakia |
| `hu` | Hungarian | 🇭🇺 | Hungary |
| `ro` | Romanian | 🇷🇴 | Romania |
| `bg` | Bulgarian | 🇧🇬 | Bulgaria |
| `hr` | Croatian | 🇭🇷 | Croatia |
| `sl` | Slovenian | 🇸🇮 | Slovenia |
| `et` | Estonian | 🇪🇪 | Estonia |
| `lv` | Latvian | 🇱🇻 | Latvia |
| `lt` | Lithuanian | 🇱🇹 | Lithuania |
| `el` | Greek | 🇬🇷 | Greece |
| `tr` | Turkish | 🇹🇷 | Turkey |
| `is` | Icelandic | 🇮🇸 | Iceland |
| `sq` | Albanian | 🇦🇱 | Albania |
| `mk` | Macedonian | 🇲🇰 | North Macedonia |
| `me` | Montenegrin | 🇲🇪 | Montenegro |

**Note:** Countries with shared languages are covered:
- 🇨🇦 Canada: English (base) + French (`fr`)
- 🇧🇪 Belgium: Dutch (`nl`) + French (`fr`)
- 🇱🇺 Luxembourg: French (`fr`) + German (`de`)
- 🇬🇧 United Kingdom: English (base language)
- 🇺🇸 United States: English (base language)

## Installation

### 1. Install Required Packages
```bash
pip install -r requirements.txt
```

### 2. Set Up OpenAI API Key
Create a `.env` file in the project root:
```bash
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

### Basic Commands

#### Translate All Languages
```bash
python auto_translate_site.py
```
Translates all HTML files to all 30 NATO languages and creates a language selection page.

#### Translate Specific Languages
```bash
python auto_translate_site.py de es fr it
```
Translates only to German, Spanish, French, and Italian.

#### Create Language Selection Page Only
```bash
python auto_translate_site.py --create-index
```
Creates `languages.html` with links to all language versions.

#### List All Supported Languages
```bash
python auto_translate_site.py --list-languages
```

#### Show Help
```bash
python auto_translate_site.py --help
```

## Features

### Enhanced Translation Quality
- **Business Context**: Specialized prompts for cybersecurity and industrial automation
- **Technical Accuracy**: Preserves technical terms, certifications, and company names
- **Cultural Adaptation**: Uses appropriate formality levels for each language
- **Brand Protection**: Keeps brand names and certifications in English

### Smart Content Handling
- **Skip Technical Elements**: Avoids translating URLs, email addresses, file paths
- **Preserve Formatting**: Maintains HTML structure and Bootstrap classes
- **Quality Control**: Filters out single characters and meaningless text
- **Rate Limiting**: Prevents API abuse with intelligent delays

### File Coverage
All website pages are translated:
- `index.html` - Homepage with company overview
- `services.html` - Service offerings and capabilities
- `portfolio.html` - Professional experience and client showcase
- `contact.html` - Contact information and templates
- `testimonials.html` - Client testimonials
- `legal-terms-conditions.html` - Legal framework
- `404.html` - Error page

### Directory Structure
```
docs/
├── index.html                    # English (original)
├── services.html
├── portfolio.html
├── contact.html
├── testimonials.html
├── legal-terms-conditions.html
├── 404.html
├── languages.html               # Language selection page
├── assets/                      # Shared assets
├── de/                         # German versions
│   ├── index.html
│   ├── services.html
│   └── ...
├── es/                         # Spanish versions
├── fr/                         # French versions
└── [other language codes]/
```

## Translation Quality Guidelines

### What Gets Translated
✅ Page titles and headings  
✅ Body text and paragraphs  
✅ Navigation labels  
✅ Button text  
✅ Service descriptions  
✅ Professional experience content  

### What's Preserved
🔒 Company names (General Motors, John Deere, ABB, etc.)  
🔒 Technical certifications (CompTIA Security+, TIA Portal)  
🔒 Brand names (Siemens, Motorola, etc.)  
🔒 Email addresses and URLs  
🔒 File paths and technical identifiers  
🔒 CSS classes and IDs  

### Technical Specifications
- **Model**: OpenAI GPT-4o-mini (cost-effective, accurate)
- **Temperature**: 0.2 (consistent translations)
- **Rate Limiting**: 0.5 seconds between requests
- **Error Handling**: Graceful fallback to original text
- **Encoding**: UTF-8 for all languages

## Cost Estimation

### OpenAI API Usage
For translating all 7 HTML files to all 27 languages:
- **Estimated tokens**: ~500,000 tokens total
- **Estimated cost**: $15-25 USD (GPT-4o-mini pricing)
- **Time required**: 2-4 hours (with rate limiting)

### Recommended Approach
1. **Test with 2-3 languages first**: `python auto_translate_site.py de es fr`
2. **Review quality and adjust prompts if needed**
3. **Run full translation**: `python auto_translate_site.py`

## Quality Assurance

### Automated Checks
- Preserves HTML structure
- Maintains Bootstrap classes
- Keeps technical terminology intact
- Validates UTF-8 encoding

### Manual Review Recommended
- Check cultural appropriateness
- Verify technical accuracy
- Test navigation functionality
- Validate contact information

## Troubleshooting

### Common Issues

**ImportError for openai/beautifulsoup4**
```bash
pip install -r requirements.txt
```

**API Key Not Found**
```bash
echo "OPENAI_API_KEY=your_key" > .env
```

**Translation Quality Issues**
- Adjust temperature in `translate_text()` function
- Modify the translation prompt for specific requirements
- Add more skip patterns for technical content

**File Not Found Errors**
- Ensure all HTML files exist in `docs/` directory
- Check file permissions for writing to language subdirectories

## Future Enhancements

### Planned Features
- [ ] Translation memory for consistency
- [ ] Batch processing optimization
- [ ] Quality scoring and validation
- [ ] Integration with translation services beyond OpenAI
- [ ] Automated testing for translation accuracy

### Configuration Options
- [ ] Custom translation prompts per language
- [ ] Selective file translation
- [ ] Translation exclusion patterns
- [ ] Output format options

## Support

For issues or improvements:
1. Check the troubleshooting section
2. Review translation quality guidelines
3. Submit issues through GitHub repository
4. Test with single language first before full deployment

---

**Ready for Production**: This enhanced script supports all NATO languages with professional-quality translation suitable for international business use.
