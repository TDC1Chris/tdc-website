#!/usr/bin/env python3
"""
Script to add Google Analytics to all HTML files that need it.
"""

import os
import re
from pathlib import Path

# Google Analytics code to insert
GA_CODE = '''  
  <!-- Google Analytics -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'GA_MEASUREMENT_ID');
  </script>'''

def add_analytics_to_file(file_path):
    """Add Google Analytics to a single HTML file if not already present."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if GA already exists
        if 'googletagmanager.com/gtag/js' in content:
            print(f"Analytics already present in {file_path}")
            return False
            
        # Find the closing </head> tag
        head_close = content.find('</head>')
        if head_close == -1:
            print(f"No </head> tag found in {file_path}")
            return False
            
        # Insert GA code before </head>
        new_content = content[:head_close] + GA_CODE + '\n' + content[head_close:]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
            
        print(f"Added analytics to {file_path}")
        return True
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """Add Google Analytics to all HTML files in docs directory."""
    docs_dir = Path("docs")
    html_files = list(docs_dir.glob("*.html"))
    
    updated_count = 0
    for html_file in html_files:
        if add_analytics_to_file(html_file):
            updated_count += 1
    
    print(f"\nSummary: Updated {updated_count} out of {len(html_files)} HTML files")

if __name__ == "__main__":
    main()
