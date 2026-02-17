import os
import xml.etree.ElementTree as ET
from datetime import datetime
import glob

def update_sitemap():
    sitemap_path = 'sitemap.xml'
    # Use the correct namespace handling
    ET.register_namespace('', "http://www.sitemaps.org/schemas/sitemap/0.9")
    
    try:
        tree = ET.parse(sitemap_path)
        root = tree.getroot()
    except Exception as e:
        print(f"Error parsing sitemap: {e}")
        return

    # Base URL for the site
    base_url = 'https://www.impactorthocenter.com/'
    
    # Get today's date
    today = datetime.now().strftime('%Y-%m-%d')
    
    # Store existing URLs to check against
    existing_urls = set()
    for url in root.findall('{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
        loc_element = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
        if loc_element is not None:
            existing_urls.add(loc_element.text)
            
    print(f"Found {len(existing_urls)} existing URLs in sitemap.")
    
    # Find all generated PHP files
    files_to_add = glob.glob('orthopedic-doctor-in-*.php')
    print(f"Found {len(files_to_add)} files to potentially add.")
    
    added_count = 0
    
    for filename in files_to_add:
        loc = base_url + filename
        
        if loc not in existing_urls:
            # Create new url element
            url_element = ET.SubElement(root, 'url')
            
            # Add loc
            loc_element = ET.SubElement(url_element, 'loc')
            loc_element.text = loc
            
            # Add lastmod
            lastmod_element = ET.SubElement(url_element, 'lastmod')
            lastmod_element.text = today
            
            # Add changefreq
            changefreq_element = ET.SubElement(url_element, 'changefreq')
            changefreq_element.text = 'weekly'
            
            # Add priority
            priority_element = ET.SubElement(url_element, 'priority')
            priority_element.text = '0.8'
            
            added_count += 1
            existing_urls.add(loc) # Add to set to prevent duplicates if file found twice (unlikely but safe)

    print(f"Added {added_count} new URLs to sitemap.")
    
    if added_count > 0:
        # Write back to file
        tree.write(sitemap_path, encoding='UTF-8', xml_declaration=True)
        print("Sitemap updated successfully!")
    else:
        print("No new URLs needed to be added.")

if __name__ == "__main__":
    update_sitemap()
