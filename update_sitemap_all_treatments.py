#!/usr/bin/env python3
"""
Script to update sitemap.xml with all treatment location pages
"""

import xml.etree.ElementTree as ET
from datetime import date

base_url = "https://www.impactorthocenter.com/"

# All Indian States and Union Territories
states = [
    "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", 
    "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", 
    "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", 
    "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", 
    "Uttarakhand", "West Bengal", "Delhi", "Jammu and Kashmir", "Ladakh", "Chandigarh", 
    "Puducherry", "Lakshadweep", "Andaman and Nicobar Islands", "Dadra and Nagar Haveli and Daman and Diu"
]

# Treatment slugs
treatment_slugs = [
    "knee-replacement",
    "total-knee-replacement",
    "total-hip-replacement",
    "shoulder-replacement",
    "knee-pain",
    "back-pain",
    "shoulder-pain",
    "elbow-pain",
    "neck-pain",
    "foot-ankle-pain",
    "hand-wrist-pain",
    "arthritis",
    "osteoporosis",
    "avascular-necrosis",
    "meniscus-tear",
    "rotator-cuff-tear",
    "tennis-elbow",
    "shoulder-impingement",
    "arthroscopy",
    "trauma-surgery",
    "physiotherapy-rehabilitation",
]

def create_slug(text):
    return text.lower().replace(" ", "-").replace("&", "and")

def update_sitemap():
    """Update sitemap.xml with all treatment location pages"""
    
    # Parse existing sitemap
    tree = ET.parse('sitemap.xml')
    root = tree.getroot()
    
    # Get namespace
    ns = {'sm': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
    
    # Get today's date
    today = date.today().isoformat()
    
    # Check existing URLs to avoid duplicates
    existing_urls = set()
    for url_elem in root.findall('sm:url', ns):
        loc = url_elem.find('sm:loc', ns)
        if loc is not None:
            existing_urls.add(loc.text)
    
    # Add new treatment location pages
    added_count = 0
    skipped_count = 0
    
    print("=" * 80)
    print("UPDATING SITEMAP WITH TREATMENT LOCATION PAGES")
    print("=" * 80)
    
    for treatment_slug in treatment_slugs:
        print(f"\n📄 Processing: {treatment_slug}")
        treatment_added = 0
        
        for state in states:
            state_slug = create_slug(state)
            url = f"{base_url}{treatment_slug}-in-{state_slug}.php"
            
            # Skip if already exists
            if url in existing_urls:
                skipped_count += 1
                continue
            
            # Create new URL element
            url_elem = ET.SubElement(root, 'url')
            
            loc = ET.SubElement(url_elem, 'loc')
            loc.text = url
            
            lastmod = ET.SubElement(url_elem, 'lastmod')
            lastmod.text = today
            
            changefreq = ET.SubElement(url_elem, 'changefreq')
            changefreq.text = 'weekly'
            
            priority = ET.SubElement(url_elem, 'priority')
            priority.text = '0.8'
            
            added_count += 1
            treatment_added += 1
        
        print(f"   ✓ Added {treatment_added} location pages")
    
    # Write updated sitemap
    tree.write('sitemap.xml', encoding='UTF-8', xml_declaration=True)
    
    print("\n" + "=" * 80)
    print(f"✅ SITEMAP UPDATE COMPLETE!")
    print(f"   New URLs Added: {added_count}")
    print(f"   Skipped (already exist): {skipped_count}")
    print(f"   Total Treatments: {len(treatment_slugs)}")
    print("=" * 80)

if __name__ == "__main__":
    update_sitemap()
