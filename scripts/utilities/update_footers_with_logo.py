#!/usr/bin/env python3

import os
import re

# List of files that need footer updates with logo
files_to_update = [
    "docs/index.html",
    "docs/portfolio.html", 
    "docs/contact.html",
    "docs/testimonials.html",
    "docs/about-me.html",
    "docs/cybersecurity-consulting.html",
    "docs/network-infrastructure.html",
    "docs/industrial-automation.html",
    "docs/safety-compliance.html",
    "docs/translation-technology.html",
    "docs/sitemap.html"
]

# Enhanced footer template with logo
enhanced_footer_template = """  <footer class="tdc-footer text-white py-3 mt-auto">
    <div class="container">
      <div class="row">
        <div class="col-12">
          <div class="d-flex flex-wrap justify-content-center justify-content-md-between align-items-center">
            <div class="d-flex align-items-center mb-2 mb-md-0">
              <img src="assets/images/green-logo-full-regal.png" alt="Total Design Consulting" height="32" class="me-3">
              <span class="text-white">&copy; 2025 Total Design Consulting LLC</span>
            </div>
            <div class="d-flex flex-wrap gap-3">
              <a href="mailto:support@totaldesignconsulting.com?subject={email_subject}&body={email_body}" class="text-white-50 text-decoration-none">Email</a>
              <a href="https://linkedin.com/company/total-design-consulting" class="text-white-50 text-decoration-none">LinkedIn</a>
              <a href="contact.html" class="text-white-50 text-decoration-none">Contact</a>
              <a href="legal-terms-conditions.html" class="text-white-50 text-decoration-none">Legal</a>
              <a href="sitemap.html" class="text-white-50 text-decoration-none">Site Map</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </footer>"""

# Page-specific email subjects and bodies
email_configs = {
    "index.html": {
        "subject": "Free%20Consultation%20Request%20-%20Total%20Design%20Consulting",
        "body": "Hello%20Total%20Design%20Consulting%20Team%2C%0A%0AI%20would%20like%20to%20schedule%20a%20free%20consultation%20to%20discuss%20my%20project%20needs.%0A%0ACompany%2FOrganization%3A%20%5BYour%20Company%20Name%5D%0AProject%20Type%3A%20%5BPlease%20select%3A%20Cybersecurity%2C%20Network%20Infrastructure%2C%20Industrial%20Automation%2C%20Safety%20%26%20Compliance%2C%20or%20Other%5D%0A%0AProject%20Description%3A%0A%5BPlease%20provide%20a%20brief%20overview%20of%20your%20requirements%5D%0A%0APreferred%20Contact%20Method%3A%20%5BEmail%2FPhone%2FVideo%20Call%5D%0APhone%20Number%3A%20%5BYour%20phone%20number%5D%0ABest%20Time%20to%20Contact%3A%20%5BYour%20preferred%20time%5D%0A%0AThank%20you%20for%20your%20time.%20I%20look%20forward%20to%20hearing%20from%20you.%0A%0ABest%20regards%2C%0A%5BYour%20Name%5D"
    },
    "portfolio.html": {
        "subject": "Portfolio%20and%20Project%20Inquiry",
        "body": "Hello%20Total%20Design%20Consulting%20Team%2C%0A%0AI%20reviewed%20your%20portfolio%20and%20would%20like%20to%20discuss%3A%0A%0ACompany%2FOrganization%3A%20%5BYour%20Company%20Name%5D%0A%0AProject%20Interest%3A%0A%5B%5D%20Similar%20to%20your%20Cybersecurity%20Assessment%20project%0A%5B%5D%20Similar%20to%20your%20Network%20Infrastructure%20project%0A%5B%5D%20Similar%20to%20your%20Industrial%20Automation%20project%0A%5B%5D%20Something%20different%3A%20%5BPlease%20describe%5D%0A%0AProject%20Description%3A%0A%5BPlease%20provide%20details%20about%20your%20project%20needs%5D%0A%0ATimeline%3A%20%5BWhen%20would%20you%20like%20to%20start%3F%5D%0ABudget%20Range%3A%20%5BOptional%5D%0A%0AContact%20Information%3A%0APhone%3A%20%5BYour%20phone%20number%5D%0APreferred%20Contact%20Method%3A%20%5BEmail%2FPhone%2FVideo%20Call%5D%0A%0AThank%20you%21%0A%0ABest%20regards%2C%0A%5BYour%20Name%5D"
    },
    "contact.html": {
        "subject": "Contact%20Page%20Inquiry",
        "body": "Hello%20Total%20Design%20Consulting%20Team%2C%0A%0AI%20visited%20your%20contact%20page%20and%20would%20like%20to%20get%20in%20touch%20regarding%3A%0A%0ACompany%2FOrganization%3A%20%5BYour%20Company%20Name%5D%0AInquiry%20Type%3A%20%5BGeneral%20Question%2FProject%20Inquiry%2FSupport%20Request%5D%0A%0A%5BPlease%20describe%20your%20question%20or%20needs%5D%0A%0AContact%20Information%3A%0APhone%3A%20%5BYour%20phone%20number%5D%0APreferred%20Contact%20Method%3A%20%5BEmail%2FPhone%2FVideo%20Call%5D%0A%0AThank%20you%21%0A%0ABest%20regards%2C%0A%5BYour%20Name%5D"
    },
    "testimonials.html": {
        "subject": "Testimonials%20and%20Client%20Feedback%20Inquiry",
        "body": "Hello%20Total%20Design%20Consulting%20Team%2C%0A%0AI%20visited%20your%20testimonials%20page%20and%20would%20like%20to%20connect%20regarding%3A%0A%0ACompany%2FOrganization%3A%20%5BYour%20Company%20Name%5D%0AInquiry%20Type%3A%0A%5B%5D%20I%27m%20interested%20in%20similar%20services%0A%5B%5D%20I%27d%20like%20to%20discuss%20a%20project%0A%5B%5D%20I%27m%20a%20previous%20client%20with%20feedback%0A%5B%5D%20Other%3A%20%5BPlease%20specify%5D%0A%0A%5BPlease%20describe%20your%20question%20or%20project%20needs%5D%0A%0AContact%20Information%3A%0APhone%3A%20%5BYour%20phone%20number%5D%0APreferred%20Contact%20Method%3A%20%5BEmail%2FPhone%2FVideo%20Call%5D%0A%0AThank%20you%21%0A%0ABest%20regards%2C%0A%5BYour%20Name%5D"
    },
    "about-me.html": {
        "subject": "About%20Page%20Inquiry%20-%20Total%20Design%20Consulting",
        "body": "Hello%20Christopher%2C%0A%0AI%20visited%20your%20About%20page%20and%20would%20like%20to%20connect%20regarding%3A%0A%0ACompany%2FOrganization%3A%20%5BYour%20Company%20Name%5D%0AInquiry%20Type%3A%0A%5B%5D%20Professional%20background%20question%0A%5B%5D%20Project%20collaboration%0A%5B%5D%20Consulting%20opportunity%0A%5B%5D%20Other%3A%20%5BPlease%20specify%5D%0A%0A%5BPlease%20describe%20your%20question%20or%20project%20needs%5D%0A%0AContact%20Information%3A%0APhone%3A%20%5BYour%20phone%20number%5D%0APreferred%20Contact%20Method%3A%20%5BEmail%2FPhone%2FVideo%20Call%5D%0A%0AThank%20you%21%0A%0ABest%20regards%2C%0A%5BYour%20Name%5D"
    },
    "cybersecurity-consulting.html": {
        "subject": "Cybersecurity%20Consulting%20Inquiry",
        "body": "Hello%20Total%20Design%20Consulting%20Team%2C%0A%0AI%20am%20interested%20in%20your%20cybersecurity%20consulting%20services.%0A%0ACompany%2FOrganization%3A%20%5BYour%20Company%20Name%5D%0AIndustry%3A%20%5BYour%20Industry%5D%0ALocation%3A%20%5BCity%2C%20State%2FCountry%5D%0A%0ACybersecurity%20Needs%3A%0A%5B%5D%20Security%20Assessment%0A%5B%5D%20Vulnerability%20Testing%0A%5B%5D%20Compliance%20Support%0A%5B%5D%20Incident%20Response%0A%5B%5D%20Security%20Training%0A%5B%5D%20Other%3A%20%5BPlease%20specify%5D%0A%0AProject%20Description%3A%0A%5BPlease%20provide%20details%20about%20your%20cybersecurity%20requirements%5D%0A%0ATimeline%3A%20%5BWhen%20would%20you%20like%20to%20start%3F%5D%0ABudget%20Range%3A%20%5BOptional%5D%0A%0AContact%20Information%3A%0APhone%3A%20%5BYour%20phone%20number%5D%0APreferred%20Contact%20Method%3A%20%5BEmail%2FPhone%2FVideo%20Call%5D%0A%0AThank%20you%20for%20your%20time.%0A%0ABest%20regards%2C%0A%5BYour%20Name%5D"
    },
    "network-infrastructure.html": {
        "subject": "Network%20Infrastructure%20Consulting%20Inquiry",
        "body": "Hello%20Total%20Design%20Consulting%20Team%2C%0A%0AI%20am%20interested%20in%20your%20network%20infrastructure%20consulting%20services.%0A%0ACompany%2FOrganization%3A%20%5BYour%20Company%20Name%5D%0AIndustry%3A%20%5BYour%20Industry%5D%0ALocation%3A%20%5BCity%2C%20State%2FCountry%5D%0A%0ANetwork%20Infrastructure%20Needs%3A%0A%5B%5D%20Network%20Design%0A%5B%5D%20Infrastructure%20Assessment%0A%5B%5D%20Performance%20Optimization%0A%5B%5D%20Security%20Integration%0A%5B%5D%20Migration%20Support%0A%5B%5D%20Other%3A%20%5BPlease%20specify%5D%0A%0AProject%20Description%3A%0A%5BPlease%20provide%20details%20about%20your%20network%20requirements%5D%0A%0ATimeline%3A%20%5BWhen%20would%20you%20like%20to%20start%3F%5D%0ABudget%20Range%3A%20%5BOptional%5D%0A%0AContact%20Information%3A%0APhone%3A%20%5BYour%20phone%20number%5D%0APreferred%20Contact%20Method%3A%20%5BEmail%2FPhone%2FVideo%20Call%5D%0A%0AThank%20you%20for%20your%20time.%0A%0ABest%20regards%2C%0A%5BYour%20Name%5D"
    },
    "industrial-automation.html": {
        "subject": "Industrial%20Automation%20Consulting%20Inquiry",
        "body": "Hello%20Total%20Design%20Consulting%20Team%2C%0A%0AI%20am%20interested%20in%20your%20industrial%20automation%20consulting%20services.%0A%0ACompany%2FOrganization%3A%20%5BYour%20Company%20Name%5D%0AIndustry%3A%20%5BYour%20Industry%5D%0ALocation%3A%20%5BCity%2C%20State%2FCountry%5D%0A%0AAutomation%20Needs%3A%0A%5B%5D%20Process%20Automation%0A%5B%5D%20PLC%20Programming%0A%5B%5D%20SCADA%20Systems%0A%5B%5D%20System%20Integration%0A%5B%5D%20Modernization%0A%5B%5D%20Other%3A%20%5BPlease%20specify%5D%0A%0AProject%20Description%3A%0A%5BPlease%20provide%20details%20about%20your%20automation%20requirements%5D%0A%0ATimeline%3A%20%5BWhen%20would%20you%20like%20to%20start%3F%5D%0ABudget%20Range%3A%20%5BOptional%5D%0A%0AContact%20Information%3A%0APhone%3A%20%5BYour%20phone%20number%5D%0APreferred%20Contact%20Method%3A%20%5BEmail%2FPhone%2FVideo%20Call%5D%0A%0AThank%20you%20for%20your%20time.%0A%0ABest%20regards%2C%0A%5BYour%20Name%5D"
    },
    "safety-compliance.html": {
        "subject": "Safety%20%26%20Compliance%20Consulting%20Inquiry",
        "body": "Hello%20Total%20Design%20Consulting%20Team%2C%0A%0AI%20am%20interested%20in%20your%20safety%20and%20compliance%20consulting%20services.%0A%0ACompany%2FOrganization%3A%20%5BYour%20Company%20Name%5D%0AIndustry%3A%20%5BYour%20Industry%5D%0ALocation%3A%20%5BCity%2C%20State%2FCountry%5D%0A%0ASafety%20%26%20Compliance%20Needs%3A%0A%5B%5D%20Safety%20Assessments%0A%5B%5D%20Regulatory%20Compliance%0A%5B%5D%20Risk%20Management%0A%5B%5D%20Training%20Programs%0A%5B%5D%20Documentation%0A%5B%5D%20Other%3A%20%5BPlease%20specify%5D%0A%0AProject%20Description%3A%0A%5BPlease%20provide%20details%20about%20your%20safety%20and%20compliance%20requirements%5D%0A%0ATimeline%3A%20%5BWhen%20would%20you%20like%20to%20start%3F%5D%0ABudget%20Range%3A%20%5BOptional%5D%0A%0AContact%20Information%3A%0APhone%3A%20%5BYour%20phone%20number%5D%0APreferred%20Contact%20Method%3A%20%5BEmail%2FPhone%2FVideo%20Call%5D%0A%0AThank%20you%20for%20your%20time.%0A%0ABest%20regards%2C%0A%5BYour%20Name%5D"
    },
    "translation-technology.html": {
        "subject": "Translation%20Technology%20Inquiry",
        "body": "Hello%20Total%20Design%20Consulting%20Team%2C%0A%0AI%20am%20interested%20in%20your%20translation%20technology%20solutions.%0A%0ACompany%2FOrganization%3A%20%5BYour%20Company%20Name%5D%0AIndustry%3A%20%5BYour%20Industry%5D%0ALocation%3A%20%5BCity%2C%20State%2FCountry%5D%0A%0ATranslation%20Technology%20Interest%3A%0A%5B%5D%20NATO%20Translation%20System%0A%5B%5D%20Custom%20translation%20solutions%0A%5B%5D%20API%20integration%0A%5B%5D%20Licensing%20opportunities%0A%5B%5D%20Other%3A%20%5BPlease%20specify%5D%0A%0AProject%20Description%3A%0A%5BPlease%20provide%20details%20about%20your%20translation%20technology%20needs%5D%0A%0ATimeline%3A%20%5BWhen%20would%20you%20like%20to%20start%3F%5D%0ABudget%20Range%3A%20%5BOptional%5D%0A%0AContact%20Information%3A%0APhone%3A%20%5BYour%20phone%20number%5D%0APreferred%20Contact%20Method%3A%20%5BEmail%2FPhone%2FVideo%20Call%5D%0A%0AThank%20you%20for%20your%20time.%0A%0ABest%20regards%2C%0A%5BYour%20Name%5D"
    },
    "sitemap.html": {
        "subject": "Site%20Map%20Navigation%20Inquiry",
        "body": "Hello%20Total%20Design%20Consulting%20Team%2C%0A%0AI%20visited%20your%20site%20map%20and%20would%20like%20to%20get%20in%20touch%20regarding%3A%0A%0ACompany%2FOrganization%3A%20%5BYour%20Company%20Name%5D%0AInquiry%20Type%3A%20%5BGeneral%20Question%2FProject%20Inquiry%2FSupport%20Request%5D%0A%0A%5BPlease%20describe%20your%20question%20or%20needs%5D%0A%0AContact%20Information%3A%0APhone%3A%20%5BYour%20phone%20number%5D%0APreferred%20Contact%20Method%3A%20%5BEmail%2FPhone%2FVideo%20Call%5D%0A%0AThank%20you%21%0A%0ABest%20regards%2C%0A%5BYour%20Name%5D"
    }
}

def update_footer_with_logo(file_path):
    """Update footer in a single file with logo"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Get filename for email config
        filename = os.path.basename(file_path)
        
        # Get email config or use default
        if filename in email_configs:
            email_config = email_configs[filename]
        else:
            email_config = {
                "subject": "General%20Inquiry%20-%20Total%20Design%20Consulting",
                "body": "Hello%20Total%20Design%20Consulting%20Team%2C%0A%0AI%20would%20like%20to%20get%20in%20touch%20regarding%3A%0A%0ACompany%2FOrganization%3A%20%5BYour%20Company%20Name%5D%0AInquiry%20Type%3A%20%5BGeneral%20Question%2FProject%20Inquiry%2FSupport%20Request%5D%0A%0A%5BPlease%20describe%20your%20question%20or%20needs%5D%0A%0AContact%20Information%3A%0APhone%3A%20%5BYour%20phone%20number%5D%0APreferred%20Contact%20Method%3A%20%5BEmail%2FPhone%2FVideo%20Call%5D%0A%0AThank%20you%21%0A%0ABest%20regards%2C%0A%5BYour%20Name%5D"
            }
        
        # Replace placeholder in footer template
        footer_content = enhanced_footer_template.format(
            email_subject=email_config["subject"],
            email_body=email_config["body"]
        )
        
        # Find the existing footer and replace it
        # Pattern to match from footer opening tag to closing tag
        footer_pattern = r'<footer class="tdc-footer[^>]*>.*?</footer>'
        
        # Replace the footer
        new_content = re.sub(footer_pattern, footer_content, content, flags=re.DOTALL)
        
        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        
        print(f"✅ Updated footer with logo in {file_path}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating {file_path}: {str(e)}")
        return False

def main():
    """Main function to update all footers with logo"""
    print("🔄 Starting footer enhancement with logo...")
    success_count = 0
    
    for file_path in files_to_update:
        if os.path.exists(file_path):
            if update_footer_with_logo(file_path):
                success_count += 1
        else:
            print(f"⚠️  File not found: {file_path}")
    
    print(f"\n✨ Footer enhancement complete!")
    print(f"📊 Successfully updated {success_count}/{len(files_to_update)} files")

if __name__ == "__main__":
    main()
